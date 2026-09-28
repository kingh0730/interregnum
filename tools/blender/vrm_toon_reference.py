"""Blender head-turn shot from the sample VRM.

Run: blender -b --factory-startup --python scene.py -- lookdev|render
"""
import math
import sys
from pathlib import Path

import bpy
from mathutils import Euler, Quaternion, Vector

HERE = Path(__file__).parent
MODE = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "lookdev"
FPS = 24
FRAMES = 78

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.preferences.addon_enable(module="bl_ext.user_default.vrm")
bpy.ops.import_scene.vrm(filepath=str(HERE / "models" / "sample.vrm"))
scene = bpy.context.scene
arm = next(o for o in bpy.data.objects if o.type == "ARMATURE")
face = bpy.data.objects["Face"]
hb = arm.data.vrm_addon_extension.vrm1.humanoid.human_bones
B = lambda k: arm.pose.bones[getattr(hb, k).node.bone_name]

# ---------------------------------------------------------------- look: silver hair
for mat_name in ("Hair_00_HAIR", "HairBack_00_HAIR"):
    mat = bpy.data.materials.get(mat_name)
    if not mat:
        continue
    for node in mat.node_tree.nodes:
        img = getattr(node, "image", None)
        if img is None or img.get("silvered"):
            continue
        px = list(img.pixels)
        for i in range(0, len(px), 4):
            l = 0.3 * px[i] + 0.59 * px[i + 1] + 0.11 * px[i + 2]
            v = min(1.0, 0.30 + 0.95 * l)
            px[i], px[i + 1], px[i + 2] = v * 0.93, v * 0.93, v * 0.98
        img.pixels = px
        img["silvered"] = True

# ---------------------------------------------------------------- look: anime toon shading (MToon)
SHADE = {"HAIR": (0.40, 0.38, 0.58), "SKIN": (0.80, 0.50, 0.50), "CLOTH": (0.44, 0.43, 0.62)}
for m in bpy.data.materials:
    e = m.vrm_addon_extension.mtoon1
    if not e.enabled:
        continue
    kind = next((k for k in SHADE if m.name.endswith(k) or f"_{k}" in m.name), None)
    x = e.extensions.vrmc_materials_mtoon
    x.gi_equalization_factor = 0.3              # less flat ambient
    if kind is None:                            # eyes, brows, mouth: leave as authored
        continue
    x.shade_color_factor = SHADE[kind]
    x.shading_toony_factor = 0.97               # hard cel shadow edge
    x.shading_shift_factor = 0.30               # sun behind her: mostly shadow side, lit rim
    x.parametric_rim_color_factor = (1.0, 0.55, 0.28)
    x.parametric_rim_fresnel_power_factor = 5.0
    x.parametric_rim_lift_factor = 0.0
    x.rim_lighting_mix_factor = 0.6
    if x.outline_width_mode != "none":
        x.outline_width_factor = 0.0011
        x.outline_color_factor = (0.20, 0.09, 0.09)
        x.outline_lighting_mix_factor = 1.0
    if kind == "CLOTH":                         # white tee -> warm off-white so it does not glow
        e.pbr_metallic_roughness.base_color_factor = (0.90, 0.86, 0.84, 1.0)


# ---------------------------------------------------------------- pose helpers (rotations in world axes)
def world_rot(pb, q_world):
    """Set a pose bone's rotation from a rotation expressed in armature space."""
    rest = pb.bone.matrix_local.to_quaternion()
    pb.rotation_mode = "QUATERNION"
    pb.rotation_quaternion = rest.inverted() @ q_world @ rest


def yaw_pitch_roll(yaw, pitch=0.0, roll=0.0):
    # armature space: character faces -Y, +Z up. yaw>0 turns her toward screen-right.
    return (Quaternion((0, 0, 1), math.radians(yaw)) @ Quaternion((1, 0, 0), math.radians(pitch))
            @ Quaternion((0, 1, 0), math.radians(roll)))


for side, sgn in (("left", 1), ("right", -1)):
    world_rot(B(f"{side}_upper_arm"), Quaternion((0, 1, 0), math.radians(70 * sgn)))
    world_rot(B(f"{side}_lower_arm"), Quaternion((0, 0, 1), math.radians(-12 * sgn)))


# ---------------------------------------------------------------- animation curves
def smooth(a, b, x):
    u = min(max((x - a) / (b - a), 0.0), 1.0)
    return u * u * (3 - 2 * u)


def track(keys, f):
    """Piecewise eased interpolation through (frame, value) keys."""
    if f <= keys[0][0]:
        return keys[0][1]
    for (f0, v0), (f1, v1) in zip(keys, keys[1:]):
        if f <= f1:
            return v0 + (v1 - v0) * smooth(f0, f1, f)
    return keys[-1][1]


# frame numbers below are the timing sheet
HIPS = [(1, 30), (24, 30), (40, 20), (78, 20)]
CHEST = [(1, 12), (17, 14), (23, 14), (37, 3), (41, 2), (78, 2)]          # starts last (drag)
NECK = [(1, 28), (17, 31), (21, 31), (34, -9), (38, -7), (78, -7)]
HEAD = [(1, 30), (15, 35), (20, 35), (32, -18), (35, -21), (39, -17), (78, -17)]  # antic, overshoot
PITCH = [(1, 2), (16, 5), (26, 9), (34, 1), (40, 0), (78, 0)]              # dip through the turn
ROLL = [(1, 0), (32, 0), (42, 7), (78, 6)]                                 # head tilt at the end
EYES = [(1, 20), (16, 22), (19, -22), (30, -8), (36, 0), (78, 0)]          # eyes lead the head
BLINK = [(1, 0), (23, 0), (25, 1), (28, 1), (30, 0), (60, 0), (62, 1), (64, 1), (66, 0), (78, 0)]
JOY = [(1, 0), (30, 0), (42, 0.75), (78, 0.8)]
BREATH = lambda f: 0.8 * math.sin(2 * math.pi * f / (3.4 * FPS))

keyblocks = face.data.shape_keys.key_blocks
blink_key = keyblocks["Face_Blendshape.Fcl_EYE_Close"]
joy_keys = [keyblocks["Face_Blendshape.Fcl_MTH_Joy"], keyblocks["Face_Blendshape.Fcl_EYE_Joy"]]


def pose_at(f):
    world_rot(B("hips"), yaw_pitch_roll(track(HIPS, f)))
    world_rot(B("upper_chest"), yaw_pitch_roll(track(CHEST, f), BREATH(f)))
    world_rot(B("neck"), yaw_pitch_roll(track(NECK, f) * 0.5, track(PITCH, f) * 0.4))
    world_rot(B("head"), yaw_pitch_roll(track(HEAD, f) * 0.6, track(PITCH, f) * 0.6, track(ROLL, f)))
    for e in ("left_eye", "right_eye"):
        world_rot(B(e), yaw_pitch_roll(track(EYES, f) * 0.5))
    blink_key.value = track(BLINK, f)
    joy_keys[0].value = track(JOY, f) * 0.6
    joy_keys[1].value = track(JOY, f) * (1 - track(BLINK, f)) * 0.35


for f in range(1, FRAMES + 1):
    pose_at(f)
    for pb in (B("hips"), B("upper_chest"), B("neck"), B("head"), B("left_eye"), B("right_eye")):
        pb.keyframe_insert("rotation_quaternion", frame=f)
    for kb in [blink_key] + joy_keys:
        kb.keyframe_insert("value", frame=f)

# hair / cloth physics from the model's spring bones
arm.data.vrm_addon_extension.spring_bone1.enable_animation = True

# ---------------------------------------------------------------- camera: close-up at eye height
head_z = (arm.matrix_world @ arm.data.bones[B("head").name].head_local).z
cam_data = bpy.data.cameras.new("Cam")
cam_data.lens = 60
cam = bpy.data.objects.new("Cam", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.location = Vector((0.20, -1.25, head_z + 0.06))
target = Vector((0.07, 0, head_z + 0.0))
cam.rotation_euler = (target - cam.location).to_track_quat("-Z", "Y").to_euler()


# ---------------------------------------------------------------- lights: warm sunset rim from back-right, cool fill
def light(name, energy, color, rot):
    d = bpy.data.lights.new(name, "SUN")
    d.energy = energy
    d.color = color
    o = bpy.data.objects.new(name, d)
    o.rotation_euler = Euler([math.radians(a) for a in rot])
    scene.collection.objects.link(o)


light("Sun", 3.2, (1.0, 0.68, 0.42), (68, 0, -75))
# MToon counts each light near-fully regardless of energy, so no fill light: ambient only
# light("Fill", 0.5, (0.70, 0.68, 0.95), (55, 0, -25))
world = bpy.data.worlds.new("W")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.4, 0.28, 0.3, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.15

# ---------------------------------------------------------------- render settings
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x, scene.render.resolution_y = 1920, 1080
scene.render.film_transparent = True
scene.render.fps = FPS
scene.frame_start, scene.frame_end = 1, FRAMES
scene.view_settings.view_transform = "Standard"
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"

if MODE == "lookdev":
    for f in (1, 45):
        scene.frame_set(f)
        scene.render.filepath = str(HERE / "render" / f"lookdev_{f:03d}.png")
        bpy.ops.render.render(write_still=True)
elif MODE == "render":
    for f in range(1, FRAMES + 1):   # step every frame so the spring bones simulate continuously
        scene.frame_set(f)
        scene.render.filepath = str(HERE / "render" / "frames" / f"{f:03d}.png")
        bpy.ops.render.render(write_still=True)
