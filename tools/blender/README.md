# Blender

Blender 5.2.2 LTS at `/Applications/Blender.app/Contents/MacOS/Blender`, run headless:
`Blender -b --factory-startup --python script.py -- <args>`.

**Use for:** 3D set pieces (ships, mechs, megastructures, space, crowds, destruction), exact camera moves,
previs and layout, depth, mask and normal passes for compositing, and rigged VRM characters when exact motion
matters more than a drawn look.

**VRM characters:** add-on `vrm` 4.7.2 (from extensions.blender.org, enabled as `bl_ext.user_default.vrm`).
`vrm_toon_reference.py` is the v4 head-turn test: VRM import, posing through world-space rotations,
eased keyframes, spring-bone hair, MToon settings and lighting.

**Lessons from v4:**
- MToon counts each light's color almost fully, whatever its energy: use one key light and low world ambient. A fill light flattens everything.
- The sun's direction is easy to get backwards. Verify with two opposite test renders.
- Spring bones only simulate correctly when every frame is stepped in order. Pre-roll a few frames before the shot so cloth settles.
- Faces need normal editing for clean anime shadow shapes; default normals give blotchy shadows mid-turn.
- Don't name a script `inspect.py`: it shadows the Python standard-library module.
