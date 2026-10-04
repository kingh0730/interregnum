import * as T from "three";
import { quad, calendarTexture } from "./surfaces.js";
import { Reflector } from "three/addons/objects/Reflector.js";
import { SVGLoader } from "three/addons/loaders/SVGLoader.js";
import {
  W,
  H,
  C,
  clamp,
  ease,
  lerp,
  rng,
  canvas,
  labelTexture,
  musicTexture,
  lanternTexture,
  image,
} from "./common.js";
const V = (x = 0, y = 0, z = 0) => new T.Vector3(x, y, z);
const DEGREES = Math.PI / 180;
export class Rigs {
  constructor(node, data) {
    this.timeline = data.shots;
    this.renderer = new T.WebGLRenderer({
      canvas: node,
      alpha: true,
      antialias: true,
      preserveDrawingBuffer: true,
    });
    this.renderer.setSize(W, H, false);
    this.renderer.setClearColor(0, 0);
    this.renderer.outputColorSpace = T.SRGBColorSpace;
    this.renderer.toneMapping = T.NoToneMapping;
    this.scenes = {};
    this.textures = {};
    this.loader = new T.TextureLoader();
    this.trace = {};
  }
  async tex(path) {
    if (this.textures[path]) return this.textures[path];
    const tx = await this.loader.loadAsync(path);
    tx.colorSpace = T.SRGBColorSpace;
    return (this.textures[path] = tx);
  }
  texture(c) {
    const tx = new T.CanvasTexture(c);
    tx.colorSpace = T.SRGBColorSpace;
    return tx;
  }
  plane(w, h, map, { opacity = 1, depthWrite = true, color = 0xffffff } = {}) {
    return new T.Mesh(
      new T.PlaneGeometry(w, h),
      new T.MeshBasicMaterial({
        map,
        transparent: true,
        alphaTest: 0.015,
        opacity,
        depthWrite,
        color,
        side: T.DoubleSide,
      }),
    );
  }
  scene(name, fov = 45) {
    const scene = new T.Scene(),
      camera = new T.PerspectiveCamera(fov, W / H, 0.01, 1800);
    camera.position.set(0, 1, 6);
    camera.lookAt(0, 1, 0);
    const state = { scene, camera, objects: [] };
    this.scenes[name] = state;
    return state;
  }
  async init() {
    this.marks = await (await fetch("/faithful/marks.json")).json();
    this.markSpark = await image("/assets/claude-spark.svg");
    this.markA = await image("/assets/anthropic-a.svg");
    this.markDarkSpark = canvas(256, 256);
    const ds = this.markDarkSpark.getContext("2d");
    ds.drawImage(this.markSpark, 0, 0, 256, 256);
    ds.globalCompositeOperation = "source-in";
    ds.fillStyle = C.ink;
    ds.fillRect(0, 0, 256, 256);
    const svg = await new SVGLoader().loadAsync("/assets/claude-spark.svg");
    this.sparkShapes = svg.paths.flatMap((p) => SVGLoader.createShapes(p));
    this.sky = await this.tex("/assets/sky.png");
    this.cloudSprite = await this.tex("/faithful/cloud-element.png");
    this.meadow = await this.tex("/faithful/meadow-empty.png");
    this.closedEye = await this.tex("/faithful/eye-closed.png");
    this.panorama = await this.tex("/faithful/room-panorama.png");
    this.facades = await this.tex("/faithful/facades.png");
    this.room = await this.tex("/faithful/birth-room-clean.png");
    for (const [key, points] of [
      [
        "room",
        [
          [111, 104],
          [185, 129],
          [181, 291],
          [109, 268],
        ],
      ],
      [
        "panorama",
        [
          [234, 283],
          [291, 296],
          [291, 383],
          [234, 375],
        ],
      ],
    ]) {
      const im = this[key].image,
        c = canvas(im.width, im.height),
        g = c.getContext("2d");
      g.drawImage(im, 0, 0);
      quad(g, calendarTexture(true), points);
      this[key] = this.texture(c);
    }
    this.ceilingSpec = await (
      await fetch("/faithful/ceiling-registration.json")
    ).json();
    const ceiling = await this.tex("/faithful/birth-room-overscan.png"),
      cc = canvas(ceiling.image.width, ceiling.image.height),
      cg = cc.getContext("2d");
    cg.drawImage(ceiling.image, 0, 0);
    quad(cg, calendarTexture(true), [
      [111, 304],
      [185, 329],
      [181, 491],
      [109, 468],
    ]);
    this.roomOverscan = this.texture(cc);

    this.flight = await this.tex("/faithful/flight-clean-actor.png");
    this.float = await this.tex("/faithful/float-clean-actor.png");
    for (const name of ["flight", "float"]) {
      const im = this[name].image,
        c = canvas(im.width, im.height),
        g = c.getContext("2d");
      g.drawImage(im, 0, 0);
      const points =
        name === "flight"
          ? [
              [548 / 983, 125 / 562],
              [584 / 983, 136 / 562],
              [626 / 983, 119 / 562],
              [568 / 983, 207 / 562],
            ]
          : [
              [849 / 1672, 271 / 941],
              [876 / 1672, 260 / 941],
              [917 / 1672, 231 / 941],
              [907 / 1672, 333 / 941],
            ];
      this.marks["static-" + name] = { frames: [{ points }] };
      this.decorate(g, "static-" + name, 0);
      this[name] = this.texture(c);
    }
    this.bareFeet = await this.tex("/faithful/leap-bare-registered.png");
    this.footMask = await this.tex("/faithful/leap-foot-regions.png");
    const sc = canvas(64, 64),
      sg = sc.getContext("2d");
    const shine = sg.createRadialGradient(32, 32, 1, 32, 32, 31);
    shine.addColorStop(0, "#FFFDF7");
    shine.addColorStop(0.22, "#FFD9A8");
    shine.addColorStop(1, "#D9775700");
    sg.fillStyle = shine;
    sg.fillRect(0, 0, 64, 64);
    sg.fillStyle = "#FAF9F5";
    sg.beginPath();
    for (const [i, p] of [
      [32, 3],
      [36, 27],
      [61, 32],
      [36, 37],
      [32, 61],
      [27, 37],
      [3, 32],
      [27, 27],
    ].entries()) {
      if (!i) sg.moveTo(...p);
      else sg.lineTo(...p);
    }
    sg.closePath();
    sg.fill();
    this.smallSpark = this.texture(sc);
    this.lanternPaper = this.texture(lanternTexture());
    this.music = this.texture(musicTexture());
    this.halo = this.texture(
      labelTexture("OPUS 5.5 · OPUS 5.5 · OPUS 5.5 ·", {
        width: 3072,
        height: 160,
        size: 103,
        color: C.gold,
        family: "FDLora",
      }),
    );

    this.views = {};
    for (const [name, folder] of [
      ["hand-clean", "hand-camera-reverse"],
      ["leap-clean", "leap-camera"],
      ["helix-clean", "helix-camera"],
    ]) {
      const d = await (
        await fetch("/faithful/" + folder + "/layers/index.json")
      ).json();
      this.views[name] = await Promise.all(
        d.indices.map((i) =>
          this.tex(
            "/faithful/" +
              folder +
              "/layers/" +
              String(i).padStart(4, "0") +
              ".png",
          ),
        ),
      );
    }
    this.views["helix-clean"][0] = await this.tex(
      "/faithful/helix-front-registered.png",
    );
    const un = await (
      await fetch("/faithful/unfurl-clean/layers/index.json")
    ).json();
    this.unfurl = await Promise.all(
      un.indices
        .filter((i) => i <= 45)
        .map((i) =>
          this.tex(
            "/faithful/unfurl-clean/layers/" +
              String(i).padStart(4, "0") +
              ".png",
          ),
        ),
    );
    this.observer = await this.tex("/faithful/birth-xiaoman.png");
    this.setupHelix();
    this.setupOrbit("hand", 270);
    this.setupOrbit("leap", 360);
    this.setupFlight();
    this.setupVertigo();
    this.setupFloat();
    this.setupClimb();
    await this.setupOutro();
    await this.setupPaper();
    this.setupOrigami();
  }
  skyWorld(state) {
    state.scene.background = new T.Color(C.sky);
    const dome = new T.Mesh(
      new T.SphereGeometry(600, 64, 48),
      new T.ShaderMaterial({
        side: T.BackSide,
        uniforms: {
          art: { value: this.sky },
          top: { value: new T.Color(C.sky) },
          bottom: { value: new T.Color(C.kraft) },
        },
        vertexShader:
          "varying vec3 p;void main(){p=position;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",
        fragmentShader: `varying vec3 p;uniform sampler2D art;uniform vec3 top;uniform vec3 bottom;void main(){vec3 d=normalize(p);float a=atan(d.x,d.z);float u=.5+.46*sin(a);float v=.5+.48*tanh(d.y);vec3 painted=texture2D(art,vec2(u,v)).rgb;gl_FragColor=vec4(painted,1.);
#include <colorspace_fragment>
}`,
      }),
    );
    state.scene.add(dome);
    state.clouds = [];
  }
  spark(size) {
    const group = new T.Group();
    for (const shape of this.sparkShapes) {
      const mesh = new T.Mesh(
        new T.ShapeGeometry(shape, 16),
        new T.MeshBasicMaterial({
          color: C.coral,
          side: T.DoubleSide,
          transparent: true,
        }),
      );
      mesh.geometry.translate(-62.5, -62.5, 0);
      mesh.geometry.scale(size / 125, -size / 125, 1);
      group.add(mesh);
    }
    return group;
  }
  ring(radius, y) {
    const height = (2 * Math.PI * radius * 160) / 3072,
      geometry = new T.CylinderGeometry(radius, radius, height, 192, 1, true),
      mat = new T.MeshBasicMaterial({
        map: this.halo,
        transparent: true,
        side: T.FrontSide,
        depthWrite: false,
        opacity: 0.85,
      });
    const obj = new T.Mesh(geometry, mat);
    obj.position.y = y;
    const inward = this.halo.clone();
    inward.repeat.x = -1;
    inward.offset.x = 1;
    inward.needsUpdate = true;
    const inner = new T.Mesh(
      geometry,
      new T.MeshBasicMaterial({
        map: inward,
        transparent: true,
        side: T.BackSide,
        depthWrite: false,
        opacity: 0.52,
      }),
    );
    inner.userData.opacityFactor = 0.62;
    obj.add(inner);
    const rim = new T.Mesh(
      new T.TorusGeometry(radius, 0.008, 8, 192),
      new T.MeshBasicMaterial({
        color: C.gold,
        transparent: true,
        opacity: 0.65,
        depthWrite: false,
      }),
    );
    rim.rotation.x = Math.PI / 2;
    rim.position.y = -height * 0.48;
    rim.userData.opacityFactor = 0.76;
    obj.add(rim);
    return obj;
  }
  decorate(g, name, frame) {
    const row = this.marks[name];
    if (!row || frame >= row.frames.length) return;
    const points = row.frames[frame].points,
      w = g.canvas.width,
      h = g.canvas.height,
      sizes =
        name === "unfurl"
          ? [10, 10, 64, 22]
          : name === "hand"
            ? [7, 7, 38, 20]
            : name.startsWith("static-")
              ? [6, 6, 32, 13]
              : [0, 0, 29, 8.5];
    for (let i = 0; i < 4; i++) {
      if (!sizes[i]) continue;
      if (name === "hand") {
        if (i === 2 && frame > 42) continue;
        if (i === 3 && frame > 34 && frame < 60) continue;
        if (i === 0 && ((frame > 37 && frame < 54) || frame > 65)) continue;
        if (i === 1 && (frame < 21 || (frame > 43 && frame < 60) || frame > 65))
          continue;
      }
      const [x, y] = points[i],
        sz = (sizes[i] / 983) * w;
      g.save();
      g.translate(x * w, y * h);
      if (i < 2) {
        g.globalAlpha = 0.8;
        g.drawImage(this.markDarkSpark, -sz / 2, -sz / 2, sz, sz);
        g.fillStyle = C.ivory;
        g.beginPath();
        g.moveTo(-sz * 0.16, -sz * 0.45);
        g.lineTo(-sz * 0.1, -sz * 0.22);
        g.lineTo(sz * 0.12, -sz * 0.16);
        g.lineTo(-sz * 0.1, -sz * 0.1);
        g.lineTo(-sz * 0.16, sz * 0.1);
        g.lineTo(-sz * 0.22, -sz * 0.1);
        g.lineTo(-sz * 0.42, -sz * 0.16);
        g.lineTo(-sz * 0.22, -sz * 0.22);
        g.closePath();
        g.fill();
      } else if (i === 2) {
        g.drawImage(this.markSpark, -sz / 2, -sz / 2, sz, sz);
      } else {
        g.fillStyle = "#141413";
        g.beginPath();
        g.ellipse(0, 0, sz * 0.85, sz * 0.8, 0, 0, Math.PI * 2);
        g.fill();
        if (!this.markWhiteA) {
          this.markWhiteA = canvas(256, 256);
          const a = this.markWhiteA.getContext("2d");
          a.drawImage(this.markA, 0, 0, 256, 256);
          a.globalCompositeOperation = "source-in";
          a.fillStyle = "#FAF9F5";
          a.fillRect(0, 0, 256, 256);
        }
        g.drawImage(this.markWhiteA, -sz / 2, -sz / 2, sz, sz);
      }
      g.restore();
    }
  }
  view(state, name, p, height = 2.7) {
    const a = this.views[name],
      index = Math.min(a.length - 1, Math.floor(clamp(p) * (a.length - 1))),
      im = a[index].image;
    if (!state.actor) {
      state.actorCanvas = canvas(im.width, im.height);
      state.actorMap = this.texture(state.actorCanvas);
      state.actor = this.plane(
        (height * im.width) / im.height,
        height,
        state.actorMap,
      );
      if (name === "helix-clean") {
        state.actor.geometry = new T.PlaneGeometry(
          (height * im.width) / im.height,
          height,
          96,
          54,
        );
        state.rest = new Float32Array(
          state.actor.geometry.attributes.position.array,
        );
      }
      state.scene.add(state.actor);
    }
    if (state.actorIndex !== index) {
      state.actorIndex = index;
      const g = state.actorCanvas.getContext("2d");
      g.clearRect(0, 0, state.actorCanvas.width, state.actorCanvas.height);
      g.drawImage(im, 0, 0, state.actorCanvas.width, state.actorCanvas.height);
      if (name === "helix-clean") this.decorate(g, "helix", index * 3);
      if (name === "hand-clean") this.decorate(g, "hand", index * 3);
      state.actorMap.needsUpdate = true;
    }
    state.actor.position.set(0, height * 0.5, 0);
    state.actor.rotation.set(
      0,
      Math.atan2(state.camera.position.x, state.camera.position.z),
      0,
    );
    if (name === "hand-clean" || name === "leap-clean") {
      const keys =
        name === "hand-clean"
          ? [
              [0, 365 / 540, 30 / 810],
              [30, 321 / 540, 70 / 810],
              [60, 219 / 540, 95 / 810],
              [90, 150 / 540, 90 / 810],
              [111, 163 / 540, 35 / 810],
            ]
          : [
              [0, 295 / 640, 12 / 360],
              [24, 254 / 640, 2 / 360],
              [48, 309 / 640, 17 / 360],
              [72, 310 / 640, 35 / 360],
              [96, 288 / 640, 10 / 360],
              [123, 315 / 640, 13 / 360],
            ];
      const f = index * 3;
      let k = 0;
      while (k < keys.length - 2 && f > keys[k + 1][0]) k++;
      const a = keys[k],
        b = keys[k + 1],
        q = clamp((f - a[0]) / (b[0] - a[0]));
      if (!state.headHalo) {
        state.headHalo = this.ring(name === "hand-clean" ? 0.26 : 0.34, 0);
        state.headHalo.rotation.x = 0.22;
        state.actor.add(state.headHalo);
      }
      state.headHalo.position.set(
        ((lerp(a[1], b[1], q) - 0.5) * height * im.width) / im.height,
        (0.5 - lerp(a[2], b[2], q)) * height +
          (name === "hand-clean" ? 0.4 : 0),
        0.04,
      );
      state.headHalo.rotation.y = p * 2;
    }
    this.trace.view_index = index;
    return state.actor;
  }
  lyric(state, content, factor = 1.35) {
    if (!state.lyric || state.lyric.userData.text !== content) {
      if (state.lyric) {
        state.scene.remove(state.lyric);
        state.lyric.material.map.dispose();
      }
      state.lyric = this.plane(
        1,
        0.11,
        this.texture(labelTexture(content, { highlights: true })),
        { depthWrite: true },
      );
      state.lyric.userData.text = content;
      state.lyric.layers.set(1);
      state.camera.layers.enable(1);
      state.scene.add(state.lyric);
    }
    state.lyric.material.opacity = this.lyricOpacity ?? 1;
    state.lyric.visible = state.lyric.material.opacity > 0;
    const cam = state.camera,
      dir = cam.getWorldDirection(V()),
      right = V(1, 0, 0).applyQuaternion(cam.quaternion),
      up = V(0, 1, 0).applyQuaternion(cam.quaternion);
    const depth = cam.position.distanceTo(V(0, 1.5, 0)) + 0.4;
    const span = 2 * depth * Math.tan((cam.fov * DEGREES) / 2);
    state.lyric.position
      .copy(cam.position)
      .addScaledVector(dir, depth)
      .addScaledVector(up, -span * 0.34);
    state.lyric.scale.set(span * factor, span * factor, 1);
    state.lyric.lookAt(cam.position);
    this.trace.lyric_depth = depth;
  }
  openArms(s, p) {
    if (!s.rest) return;
    const pos = s.actor.geometry.attributes.position,
      uv = s.actor.geometry.attributes.uv,
      span =
        3.1 *
        (this.views["helix-clean"][0].image.width /
          this.views["helix-clean"][0].image.height),
      fold = 0.33 * (1 - ease(p / 0.19)),
      follow =
        p > 0.19
          ? 0.035 * Math.sin((p - 0.19) * 48) * Math.exp(-(p - 0.19) * 24)
          : 0;
    for (let i = 0; i < pos.count; i++) {
      let x = s.rest[i * 3],
        y = s.rest[i * 3 + 1];
      const u = uv.getX(i),
        v = 1 - uv.getY(i);
      for (const [sx, sy, sign, weight] of [
        [
          0.525,
          0.285,
          -1,
          ease((0.525 - u) / 0.075) *
            (1 - ease((v - 0.37) / 0.05)) *
            ease((v - 0.22) / 0.05),
        ],
        [
          0.645,
          0.34,
          1,
          ease((u - 0.645) / 0.075) *
            ease((v - 0.32) / 0.06) *
            (1 - ease((v - 0.5) / 0.07)),
        ],
      ]) {
        const w = clamp(weight),
          a = (fold + follow) * sign * w,
          cx = (sx - 0.5) * span,
          cy = (0.5 - sy) * 3.1,
          dx = x - cx,
          dy = y - cy;
        x = cx + dx * Math.cos(a) + dy * Math.sin(a);
        y = cy - dx * Math.sin(a) + dy * Math.cos(a);
      }
      pos.setXYZ(i, x, y, s.rest[i * 3 + 2]);
    }
    pos.needsUpdate = true;
    this.trace.arm_open_fraction = ease(p / 0.19);
  }
  setupHelix() {
    const s = this.scene("helix", 44);
    this.skyWorld(s);
    s.halo = this.ring(4, 3.0);
    s.scene.add(s.halo);
    s.spark = this.spark(25);
    s.spark.position.set(-7, 4, 0);
    s.spark.rotation.y = Math.PI / 2;
    s.scene.add(s.spark);
    s.spark.visible = false;
    const glowCanvas = canvas(512, 512),
      gg = glowCanvas.getContext("2d"),
      gr = gg.createRadialGradient(256, 256, 12, 256, 256, 256);
    gr.addColorStop(0, "#FFD9A8E0");
    gr.addColorStop(0.45, "#FFD9A876");
    gr.addColorStop(1, "#FFD9A800");
    gg.fillStyle = gr;
    gg.fillRect(0, 0, 512, 512);
    s.sunGlow = this.plane(37, 37, this.texture(glowCanvas), {
      opacity: 0,
      depthWrite: false,
    });
    s.sunGlow.position.set(-7.15, 4, 0);
    s.sunGlow.rotation.y = Math.PI / 2;
    s.scene.add(s.sunGlow);
    s.ribbons = [];
    for (let k = 0; k < 2; k++) {
      const geo = new T.BufferGeometry(),
        positions = new Float32Array(241 * 2 * 3),
        uv = new Float32Array(241 * 2 * 2),
        idx = [];
      for (let i = 0; i <= 240; i++) {
        uv.set([i / 240, 0, i / 240, 1], i * 4);
        if (i < 240) {
          let a = i * 2;
          idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2);
        }
      }
      geo.setAttribute("position", new T.BufferAttribute(positions, 3));
      geo.setAttribute("uv", new T.BufferAttribute(uv, 2));
      geo.setIndex(idx);
      const mat = new T.ShaderMaterial({
        side: T.DoubleSide,
        transparent: true,
        depthWrite: true,
        uniforms: {
          time: { value: 0 },
          clay: { value: new T.Color(C.coral) },
          which: { value: k },
        },
        vertexShader:
          "varying vec2 v;varying vec3 world;void main(){v=uv;world=(modelMatrix*vec4(position,1.)).xyz;gl_Position=projectionMatrix*viewMatrix*vec4(world,1.);}",
        fragmentShader:
          "varying vec2 v;varying vec3 world;uniform float time;uniform vec3 clay;uniform float which;void main(){vec3 prism=.55+.4*cos(6.283*(v.x+vec3(0.,.34,.67)));vec3 col=mix(clay,prism,smoothstep(.2,.7,v.x)*.78);float edge=pow(sin(3.14159*v.y),.4);float staff=1.-.24*step(.82,fract(v.y*7.));float sheen=.7+.3*sin(v.y*3.14159);gl_FragColor=vec4(col*staff*sheen+vec3(.08)*pow(edge,8.),.9*edge);\n#include <colorspace_fragment>\n}",
      });
      const mesh = new T.Mesh(geo, mat);
      s.scene.add(mesh);
      s.ribbons.push(mesh);
    }
    const r = rng(334),
      p = new Float32Array(1200 * 3),
      col = new Float32Array(1200 * 3);
    for (let i = 0; i < 1200; i++) {
      p.set([(r() - 0.5) * 60, r() * 24 - 4, (r() - 0.5) * 60], i * 3);
      const cc = new T.Color().setHSL(r(), 0.65, 0.75);
      col.set([cc.r, cc.g, cc.b], i * 3);
    }
    const pg = new T.BufferGeometry();
    pg.setAttribute("position", new T.BufferAttribute(p, 3));
    pg.setAttribute("color", new T.BufferAttribute(col, 3));
    s.particles = new T.Points(
      pg,
      new T.PointsMaterial({
        size: 0.035,
        vertexColors: true,
        transparent: true,
        opacity: 0.65,
        depthWrite: false,
      }),
    );
    s.scene.add(s.particles);
  }
  helix(t, p, words = "第一天的纯真色彩它总是") {
    const s = this.scenes.helix,
      theta = 450 * DEGREES * ease(p),
      radius = 0.65 + 3.8 * ease(p / 0.5) + 34 * ease((p - 0.45) / 0.55),
      cross =
        (32 * 30 - this.timeline[33].start_frame) /
        (this.timeline[33].end_frame - this.timeline[33].start_frame - 1),
      complete =
        (Math.round(33.5 * 30) - this.timeline[33].start_frame) /
        (this.timeline[33].end_frame - this.timeline[33].start_frame - 1);
    const y =
      p <= cross
        ? lerp(2.63, 3.0, p / cross)
        : 3.0 + 5 * ease((p - cross) / (1 - cross));
    const target = V(
      lerp(0.43, 0, ease(p / 0.28)),
      p <= cross
        ? lerp(2.63, 2.0, ease(p / cross))
        : lerp(2.0, 1.4, ease((p - cross) / 0.24)),
      0,
    );
    s.camera.position.set(
      target.x + radius * Math.sin(theta),
      y,
      radius * Math.cos(theta),
    );
    s.camera.lookAt(target);
    s.camera.rotateZ(20 * DEGREES * ease(p));
    this.view(s, "helix-clean", ease(p), 3.1);
    this.openArms(s, p);
    s.halo.rotation.y = p * Math.PI * 2;
    const haloRadius = lerp(0.75, 4, ease(p / cross));
    s.halo.scale.setScalar(haloRadius / 4);
    s.halo.material.opacity = 0.75 * (1 - ease((p - cross) / 0.19));
    for (const child of s.halo.children)
      child.material.opacity =
        s.halo.material.opacity * (child.userData.opacityFactor || 1);
    s.spark.visible = p > 0.68;
    s.sunGlow.material.opacity = ease((p - 0.62) / 0.2);
    s.spark.children.forEach(
      (m) => (m.material.opacity = ease((p - 0.68) / 0.2)),
    );
    for (let k = 0; k < 2; k++) {
      const a = s.ribbons[k].geometry.attributes.position,
        arr = a.array;
      for (let i = 0; i <= 240; i++) {
        const u = i / 240,
          angle = k * Math.PI + u * Math.PI * 3.6 + p * 2,
          rad = 0.2 + u * (2 + 20 * ease(p)),
          x = 0.4 + Math.cos(angle) * rad,
          y0 = 2.45 + u * 6 + Math.sin(u * 9 + k) * 1.7,
          z = Math.sin(angle) * rad;
        const ray = Math.min(5, Math.floor(u * 6)),
          local = (u * 6) % 1,
          rr = Math.pow(Math.sin(local * Math.PI), 2) * 12.5,
          aa = ((ray * 2 + k) * Math.PI) / 6;
        const target = V(-7, 4 + Math.sin(aa) * rr, Math.cos(aa) * rr),
          m = ease((p - 0.52) / (complete - 0.52));
        const center = V(x, y0, z).lerp(target, m),
          width =
            (0.12 + 0.95 * u) *
            Math.sin(Math.PI * u * 0.95) *
            lerp(1, Math.sin(local * Math.PI), m);
        for (let side = 0; side < 2; side++) {
          const sign = side ? 1 : -1;
          arr.set(
            [
              center.x + sign * width * (1 - m),
              center.y + sign * width * lerp(1, Math.cos(aa), m),
              center.z - sign * width * Math.sin(aa) * m,
            ],
            (i * 2 + side) * 3,
          );
        }
      }
      a.needsUpdate = true;
      s.ribbons[k].geometry.computeVertexNormals();
      s.ribbons[k].material.uniforms.time.value = t;
      s.ribbons[k].material.opacity = 1;
    }
    this.lyric(s, words, lerp(2.5, 1.65, ease(p / 0.32)));
    this.trace = {
      ...this.trace,
      shot: "S34",
      orbit_degrees: 450 * ease(p),
      roll_degrees: 20 * ease(p),
      camera: s.camera.position.toArray(),
      halo_plane_distance: y - 3.0,
      halo_radius: haloRadius,
      continuous: true,
      spark_complete: p >= complete,
    };
    this.renderer.render(s.scene, s.camera);
  }
  roomWorld(s) {
    s.scene.background = new T.Color(C.ink);
    const material = new T.ShaderMaterial({
      side: T.BackSide,
      uniforms: { map: { value: this.panorama }, progress: { value: 0 } },
      vertexShader:
        "varying vec2 v;void main(){v=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",
      fragmentShader: `varying vec2 v;uniform sampler2D map;uniform float progress;void main(){vec3 c=texture2D(map,v).rgb;float l=dot(c,vec3(.299,.587,.114));float d=distance(v,vec2(.46,.48));float warm=smoothstep(d-.05,d+.05,progress);gl_FragColor=vec4(mix(vec3(l)*vec3(1.,1.,.97),c,warm),1.);
#include <colorspace_fragment>
}`,
    });
    const sphere = new T.Mesh(new T.SphereGeometry(7, 96, 64), material);
    sphere.position.y = 1.7;
    sphere.rotation.y = -Math.PI * 0.15;
    s.scene.add(sphere);
    s.environment = sphere;
  }
  balconyWorld(s) {
    this.skyWorld(s);
    s.scene.fog = new T.FogExp2("#D8B69B", 0.015);
    const facade = canvas(1024, 512),
      g = facade.getContext("2d"),
      im = this.facades.image;
    g.drawImage(
      im,
      im.width / 2 + 4,
      4,
      im.width / 2 - 8,
      im.height / 2 - 8,
      0,
      0,
      1024,
      512,
    );
    const tx = this.texture(facade);
    tx.wrapS = T.RepeatWrapping;
    tx.wrapT = T.RepeatWrapping;
    tx.repeat.set(1, 4);
    const wall = this.plane(30, 60, tx);
    wall.position.set(0, 5, -6);
    s.scene.add(wall);
    const floor = new T.Mesh(
      new T.BoxGeometry(12, 0.15, 3),
      new T.MeshBasicMaterial({ color: "#716859" }),
    );
    floor.position.set(0, -0.45, -4.4);
    s.scene.add(floor);
    const metal = new T.MeshBasicMaterial({ color: "#2B3030" });
    for (let i = 0; i < 30; i++) {
      const bar = new T.Mesh(new T.BoxGeometry(0.035, 1.03, 0.035), metal);
      bar.position.set(-6 + (i * 12) / 29, 0.1, -2.9);
      s.scene.add(bar);
    }
    const rail = new T.Mesh(new T.BoxGeometry(12, 0.05, 0.05), metal);
    rail.position.set(0, 0.63, -2.9);
    s.scene.add(rail);
  }
  setupOrbit(name, degrees) {
    const s = this.scene(name, name === "hand" ? 53.13 : 58);
    if (name === "hand") {
      s.camera.filmGauge = 36;
      s.camera.setFocalLength(24);
      this.roomWorld(s);
    } else this.balconyWorld(s);
    s.degrees = degrees;
    const r = rng(525);
    s.frozen = new T.Group();
    for (let i = 0; i < 65; i++) {
      const paperWidth = 0.06 + r() * 0.15,
        mesh = this.plane(paperWidth, (paperWidth * 4) / 3, this.music, {
          opacity: 0.85,
        });
      mesh.position.set((r() - 0.5) * 6, r() * 4, (r() - 0.5) * 5);
      mesh.rotation.set(r(), r(), r());
      s.frozen.add(mesh);
    }
    s.scene.add(s.frozen);
    if (name === "leap") {
      const rr = rng(2525);
      for (let j = 0; j < 90; j++) {
        const drop = new T.Sprite(
          new T.SpriteMaterial({
            map: this.smallSpark,
            color: C.gold,
            transparent: true,
            opacity: 0.65,
            depthWrite: false,
          }),
        );
        drop.position.set((rr() - 0.5) * 7, 0.1 + rr() * 4.5, (rr() - 0.5) * 6);
        drop.scale.setScalar(0.015 + rr() * 0.035);
        s.frozen.add(drop);
      }
      for (let j = 0; j < 18; j++) {
        const size = 0.035 + rr() * 0.1,
          geo = new T.BufferGeometry();
        geo.setAttribute(
          "position",
          new T.Float32BufferAttribute(
            [0, 0, 0, size, 0.15 * size, 0, 0.3 * size, 1.6 * size, 0],
            3,
          ),
        );
        const shard = new T.Mesh(
          geo,
          new T.MeshBasicMaterial({
            color: C.sky,
            side: T.DoubleSide,
            transparent: true,
            opacity: 0.3,
            depthWrite: false,
          }),
        );
        shard.add(
          new T.LineSegments(
            new T.EdgesGeometry(geo),
            new T.LineBasicMaterial({
              color: C.ivory,
              transparent: true,
              opacity: 0.65,
            }),
          ),
        );
        shard.position.set((rr() - 0.5) * 6, rr() * 4, (rr() - 0.5) * 5);
        shard.rotation.set(rr() * 3, rr() * 3, rr() * 3);
        s.frozen.add(shard);
      }
      const r = rng(2515),
        points = new Float32Array(400 * 3),
        origins = [
          [-1.25, 1.11, 0],
          [-1.08, 0.64, 0],
          [0.45, 0.5, 0],
          [0.67, 0.87, 0],
        ];
      s.footOrigins = [];
      s.footVelocity = [];
      for (let i = 0; i < 400; i++) {
        const o = origins[i % 4];
        s.footOrigins.push(o);
        s.footVelocity.push([
          (r() - 0.5) * 2,
          (r() - 0.25) * 2,
          (r() - 0.5) * 2,
        ]);
        points.set(o, i * 3);
      }
      const geo = new T.BufferGeometry();
      geo.setAttribute("position", new T.BufferAttribute(points, 3));
      s.footDust = new T.Points(
        geo,
        new T.PointsMaterial({
          color: C.coral,
          size: 0.075,
          map: this.smallSpark,
          alphaTest: 0.015,
          transparent: true,
          opacity: 0,
          depthWrite: false,
        }),
      );
      s.scene.add(s.footDust);
    }
  }
  orbit(name, t, p) {
    const s = this.scenes[name];
    let angle, view;
    if (name === "leap") {
      const q = clamp((t - 24) / 1.1);
      angle = 360 * ease(q);
      view = q;
      this.trace.performance_time = t < 24 ? t : t < 25.15 ? 24 : t;
      s.frozen.rotation.y =
        t < 24 ? (t - 23.75) * 0.2 : t < 25.15 ? 0.05 : 0.05 + (t - 25.15) * 2;
    } else {
      angle = -270 * ease(p);
      view = Math.min(ease(p), 111 / 123);
    }
    const rack = ease((p - 0.82) / 0.18),
      radius =
        name === "hand"
          ? lerp(lerp(1.3, 1.9, ease(p / 0.45)), 1.25, rack)
          : 4.4;
    s.camera.position.set(
      Math.sin(angle * DEGREES) * radius,
      name === "hand" ? lerp(2.0, 2.25, rack) : 1.5,
      Math.cos(angle * DEGREES) * radius,
    );
    s.camera.lookAt(
      0,
      name === "hand" ? lerp(1.95, 2.268, rack) : 1.3,
      name === "hand" ? -0.108 * rack : 0,
    );
    this.view(
      s,
      name === "hand" ? "hand-clean" : "leap-clean",
      view,
      name === "hand" ? 2.7 : 3.2,
    );
    if (name === "hand") {
      s.environment.material.uniforms.progress.value = ease(p / 0.5);
      if (!s.reveal) {
        s.reveal = new T.ShaderMaterial({
          transparent: true,
          side: T.DoubleSide,
          depthWrite: true,
          uniforms: {
            map: { value: s.actorMap },
            progress: { value: 0 },
            paper: { value: new T.Color(C.cream) },
            ink: { value: new T.Color(C.ink) },
          },
          vertexShader:
            "varying vec2 v;void main(){v=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",
          fragmentShader: `varying vec2 v;uniform sampler2D map;uniform float progress;uniform vec3 paper,ink;void main(){vec4 c=texture2D(map,v);if(c.a<.015)discard;float lum=dot(c.rgb,vec3(.299,.587,.114));vec3 sketch=mix(ink,paper,smoothstep(.08,.50,lum));float heroine=smoothstep(.465,.50,v.x);float d=length((v-vec2(.49,.76))*vec2(1.,1.4));float fill=smoothstep(d-.06,d+.06,progress*1.5);c.rgb=mix(c.rgb,sketch,heroine*(1.-fill));gl_FragColor=c;
#include <colorspace_fragment>
}`,
        });
        s.actor.material = s.reveal;
      }
      s.reveal.uniforms.progress.value = clamp(p / 0.34);
      this.trace.colour_spread = clamp(p / 0.34);
    }
    if (name === "leap") {
      if (!s.dissolve) {
        s.dissolve = new T.ShaderMaterial({
          transparent: true,
          side: T.DoubleSide,
          depthWrite: true,
          uniforms: {
            oldMap: { value: s.actorMap },
            newMap: { value: this.bareFeet },
            region: { value: this.footMask },
            progress: { value: 0 },
            clay: { value: new T.Color(C.coral) },
          },
          vertexShader:
            "varying vec2 v;void main(){v=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",
          fragmentShader: `varying vec2 v;uniform sampler2D oldMap,newMap,region;uniform float progress;uniform vec3 clay;void main(){vec4 a=texture2D(oldMap,v),b=texture2D(newMap,v);float m=texture2D(region,v).r;vec2 p=v*vec2(160.,120.),cell=floor(p),f=fract(p);f=f*f*(3.-2.*f);float aa=fract(sin(dot(cell,vec2(127.1,311.7)))*43758.5453),ab=fract(sin(dot(cell+vec2(1.,0.),vec2(127.1,311.7)))*43758.5453),ac=fract(sin(dot(cell+vec2(0.,1.),vec2(127.1,311.7)))*43758.5453),ad=fract(sin(dot(cell+vec2(1.,1.),vec2(127.1,311.7)))*43758.5453);float noise=mix(mix(aa,ab,f.x),mix(ac,ad,f.x),f.y);float skin=step(a.g+.04,a.r)*step(a.b+.1,a.r)*step(.22,a.g);m*=1.-skin*.98;float q=smoothstep(noise-.03,noise+.03,progress);if(progress<=0.)q=0.;if(progress>=1.)q=1.;vec4 outColor=mix(a,b,q*m);float edge=(1.-smoothstep(.015,.07,abs(noise-progress)))*m*step(.01,progress)*(1.-step(.99,progress));outColor.rgb=mix(outColor.rgb,clay,edge*.85);if(outColor.a<.015)discard;gl_FragColor=outColor;
#include <colorspace_fragment>
}`,
        });
        s.actor.material = s.dissolve;
      }
      const q = clamp((t - 25.15) / 0.25);
      s.dissolve.uniforms.progress.value = q;
      s.actor.position.y +=
        t < 24 ? -0.1 * (1 - ease((t - 23.75) / 0.25)) : q * 0.4;
      s.footDust.material.opacity = q > 0 ? Math.sin(q * Math.PI) * 0.9 : 0;
      const points = s.footDust.geometry.attributes.position;
      for (let i = 0; i < 400; i++) {
        const o = s.footOrigins[i],
          v = s.footVelocity[i];
        points.setXYZ(i, o[0] + v[0] * q, o[1] + v[1] * q, o[2] + v[2] * q);
      }
      points.needsUpdate = true;
      this.trace.shoe_dissolve = q;
    }
    this.trace = {
      ...this.trace,
      rack_focus: name === "hand" ? rack : 0,
      focal_length_mm: name === "hand" ? 24 : null,
      actor_turn_degrees: name === "hand" ? 270 * (ease(p) - view) : 0,
      shot: name === "hand" ? "S23" : "S25",
      orbit_degrees: angle,
      camera: s.camera.position.toArray(),
      frozen: name === "leap" && t >= 24 && t < 25.15,
    };
    this.renderer.render(s.scene, s.camera);
  }
  setupVertigo() {
    const s = this.scene("vertigo", 35);
    const extra =
        this.ceilingSpec.margin_top_px / this.ceilingSpec.original_height,
      bg = this.plane(15.364, 8.642 * (1 + extra), this.roomOverscan);
    bg.position.set(-0.2045, 1.1909 + (8.642 * extra) / 2, -3.6);
    s.scene.add(bg);
    const actorImage = this.unfurl[0].image;
    s.actor = this.plane(
      (3.355 * actorImage.width) / actorImage.height,
      3.355,
      null,
    );
    s.actor.position.set(0.249, 1.83, 0);
    s.actorCanvas = canvas(actorImage.width, actorImage.height);
    s.actorMap = this.texture(s.actorCanvas);
    s.actor.material.map = s.actorMap;
    s.scene.add(s.actor);
    s.observer = this.plane(6.894, 3.878, this.observer);
    s.observer.position.set(-0.00909, 1.5818, -0.16);
    s.scene.add(s.observer);
    s.halo = this.ring(0.65, 3.37);
    s.halo.rotation.x = 0.4;
    s.scene.add(s.halo);
    for (const [i, pos] of [
      [-1.4, 0.5, 0.8],
      [-1.7, 1.8, -0.7],
      [1.7, 0.6, 0.4],
      [2, 2.1, 1],
      [1.6, 3, -1],
      [-1.8, 2.8, -1.3],
    ].entries()) {
      const note = this.plane(0.14, (0.14 * 4) / 3, this.music, {
        opacity: 0.9,
      });
      note.position.set(...pos);
      note.rotation.set(0.2 + i * 0.17, 0.3 + i * 0.6, 0.2 + i * 0.8);
      s.scene.add(note);
    }
  }
  vertigo(p) {
    const s = this.scenes.vertigo;
    const frame = Math.min(
        this.unfurl.length - 1,
        Math.floor(p * (this.unfurl.length - 1)),
      ),
      g = s.actorCanvas.getContext("2d");
    g.clearRect(0, 0, s.actorCanvas.width, s.actorCanvas.height);
    g.drawImage(
      this.unfurl[frame].image,
      0,
      0,
      s.actorCanvas.width,
      s.actorCanvas.height,
    );
    this.decorate(g, "unfurl", frame * 3);
    s.actorMap.needsUpdate = true;
    s.camera.position.set(
      0.15,
      lerp(3.05, 1.9, ease(p)),
      lerp(3, 2.64, ease(p)),
    );
    s.camera.fov = lerp(13, 66, ease(p));
    s.camera.updateProjectionMatrix();
    s.camera.lookAt(0.15, lerp(3.05, 1.9, ease(p)), 0);
    s.halo.rotation.y = p * 2;
    s.actor.rotation.set(0, 0, 0);
    this.trace = {
      shot: "S16",
      dolly_push_fraction: 0.12 * ease(p),
      fov: s.camera.fov,
      camera: s.camera.position.toArray(),
    };
    this.renderer.render(s.scene, s.camera);
  }
  setupFlight() {
    const s = this.scene("flight", 72);
    this.skyWorld(s);
    s.scene.fog = new T.FogExp2("#DDBDA3", 0.012);
    const r = rng(326);
    s.city = new T.Group();
    this.facadeTiles = [];
    for (let k = 0; k < 4; k++) {
      const im = this.facades.image,
        tx = canvas(1024, 512),
        g = tx.getContext("2d"),
        ww = im.width / 2,
        hh = im.height / 2;
      g.drawImage(
        im,
        (k % 2) * ww + 4,
        Math.floor(k / 2) * hh + 4,
        ww - 8,
        hh - 8,
        0,
        0,
        1024,
        512,
      );
      this.facadeTiles.push(tx);
    }
    for (let i = 0; i < 70; i++) {
      const h = 75 + r() * 170,
        w = 8 + r() * 13,
        d = 8 + r() * 15,
        tx = this.texture(this.facadeTiles[i % 4]);
      tx.wrapS = T.RepeatWrapping;
      tx.wrapT = T.RepeatWrapping;
      tx.repeat.set(1, (h / w) * 2);
      tx.offset.y = r();
      const m = new T.Mesh(
        new T.BoxGeometry(w, h, d),
        new T.MeshBasicMaterial({
          map: tx,
          color: i % 3 ? "#DDD5C9" : "#CCD6DF",
        }),
      );
      m.position.set((i % 2 ? 1 : -1) * (14 + r() * 32), h / 2 - 110, -i * 9);
      s.city.add(m);
      const crown = new T.Mesh(
        new T.BoxGeometry(w * 0.72, 0.3, d * 0.72),
        new T.MeshBasicMaterial({ color: "#343E42" }),
      );
      crown.position.copy(m.position);
      crown.position.y += h / 2 + 0.15;
      s.city.add(crown);
    }
    s.scene.add(s.city);
    s.mirrors = [];
    for (const side of [-1, 1]) {
      const body = new T.Mesh(
        new T.BoxGeometry(7, 80, 15),
        new T.MeshBasicMaterial({
          map: this.texture(this.facadeTiles[0]),
          color: "#687C87",
        }),
      );
      body.position.set(side * 7.7, -17, -10);
      s.scene.add(body);
      const mirror = new Reflector(new T.PlaneGeometry(14, 19), {
        color: 0x8798a4,
        textureWidth: 768,
        textureHeight: 768,
      });
      const getReflection = mirror.getReflectionCamera.bind(mirror);
      mirror.getReflectionCamera = (cam) => {
        const reflected = getReflection(cam);
        reflected.layers.disable(1);
        return reflected;
      };
      mirror.rotation.y = side > 0 ? -Math.PI / 2 : Math.PI / 2;
      mirror.position.set(side * 4.1, 2, -10);
      s.scene.add(mirror);
      s.mirrors.push(mirror);
      const metal = new T.MeshBasicMaterial({ color: "#3B4A53" });
      for (let k = 0; k < 11; k++) {
        const bar = new T.Mesh(new T.BoxGeometry(0.065, 19, 0.045), metal);
        bar.position.set(side * 4.08, 2, -17 + k * 1.4);
        s.scene.add(bar);
        s.mirrors.push(bar);
      }
      for (let k = 0; k < 9; k++) {
        const bar = new T.Mesh(new T.BoxGeometry(0.065, 0.055, 14), metal);
        bar.position.set(side * 4.08, -7.5 + (k * 19) / 8, -10);
        s.scene.add(bar);
        s.mirrors.push(bar);
      }
      s.mirrors.push(body);
    }
    s.actor = this.plane(
      7.2,
      (7.2 * this.flight.image.height) / this.flight.image.width,
      this.flight,
    );
    s.actorHalo = this.ring(0.43, 1.72);
    s.actorHalo.position.x = 0.5;
    s.actorHalo.rotation.x = 0.35;
    s.actor.add(s.actorHalo);
    s.scene.add(s.actor);
    s.frame = new T.Group();
    const material = new T.MeshBasicMaterial({ color: C.ink });
    for (const [x, y, w, h] of [
      [0, 5, 13, 0.2],
      [0, -5, 13, 0.2],
      [-6.5, 0, 0.2, 10],
      [6.5, 0, 0.2, 10],
    ]) {
      const bar = new T.Mesh(new T.BoxGeometry(w, h, 0.25), material);
      bar.position.set(x, y, 0);
      s.frame.add(bar);
    }
    s.frame.position.set(0, 2, -24);
    s.scene.add(s.frame);
    s.cloudBanks = new T.Group();
    for (let i = 0; i < 20; i++) {
      const cloud = this.plane(10 + r() * 13, 5 + r() * 5, this.cloudSprite, {
        opacity: 0.97,
        depthWrite: false,
      });
      cloud.position.set(
        (i % 2 ? 1 : -1) * (3 + r() * 5),
        4 + r() * 4,
        -35 - i * 5,
      );
      s.cloudBanks.add(cloud);
    }
    s.scene.add(s.cloudBanks);
  }
  flightShot(n, t, p) {
    const s = this.scenes.flight;
    let z,
      y,
      roll = 0;
    if (n === 26) {
      z = lerp(8, -12, ease(p));
      y = 2;
    } else if (n === 27) {
      z = lerp(-12, -36, p);
      y = 2;
      roll = 360 * ease(p);
    } else {
      z = lerp(-36, -80, p);
      y = lerp(8, 16, p);
    }
    s.camera.position.set(0, y, z);
    s.camera.lookAt(0, y, -200);
    s.camera.rotateZ(roll * DEGREES);
    s.actor.position.set(0, y - 0.3, z - 8);
    s.actor.lookAt(V(0, y, z));
    s.actor.material.map = n === 28 ? this.float : this.flight;
    s.actorHalo.rotation.y = t * 0.7;
    s.cloudBanks.visible = n === 28;
    s.city.visible = n !== 28;
    for (const m of s.mirrors) m.visible = n !== 28;
    s.frame.visible = n === 27;
    this.lyric(s, n === 28 ? "第一次能飞起来" : "第一次能飞起来");
    this.trace = {
      shot: "S" + n,
      camera: s.camera.position.toArray(),
      roll_degrees: roll,
      billboard_frame_z: -24,
    };
    this.renderer.render(s.scene, s.camera);
  }
  cityRush(p) {
    const s = this.scenes.flight;
    s.actor.visible = false;
    s.frame.visible = false;
    s.cloudBanks.visible = false;
    s.city.visible = true;
    for (const m of s.mirrors) m.visible = false;
    if (s.lyric) s.lyric.visible = false;
    s.camera.fov = 82;
    s.camera.updateProjectionMatrix();
    s.camera.position.set(lerp(-1, 1, p), 3, lerp(-42, -87, p));
    s.camera.lookAt(0, 3, -200);
    s.camera.rotateZ(lerp(-0.04, 0.04, p));
    this.renderer.render(s.scene, s.camera);
    s.actor.visible = true;
    if (s.lyric) s.lyric.visible = true;
    s.camera.fov = 72;
    s.camera.updateProjectionMatrix();
    this.trace = {
      shot: "S38",
      camera: s.camera.position.toArray(),
      city_only: true,
    };
  }
  setupClimb() {
    const s = this.scene("climb", 66);
    this.skyWorld(s);
    s.actor = this.plane(6.0, 3.375, this.float);
    s.scene.add(s.actor);
    for (let i = 0; i < 6; i++) {
      const cloud = this.plane(60, 25, this.cloudSprite, {
        opacity: 0.9,
        depthWrite: false,
      });
      cloud.position.set(((i % 2) - 0.5) * 8, 38 + i * 2, 0);
      cloud.rotation.x = -Math.PI / 2;
      s.scene.add(cloud);
    }
  }
  climb(p, t) {
    const s = this.scenes.climb,
      y = lerp(2, 36, ease(p));
    s.camera.position.set(0, y, 5.2);
    s.camera.lookAt(0, y + 15, -0.5);
    s.camera.rotateZ(360 * DEGREES * ease(p));
    s.actor.position.set(0, y + 9, 0);
    s.actor.lookAt(s.camera.position);
    this.lyric(s, "第一次能飞起来");
    this.trace = {
      shot: "S31",
      vertical_rise: y - 2,
      roll_degrees: 360 * ease(p),
    };
    this.renderer.render(s.scene, s.camera);
  }
  async setupOutro() {
    const s = this.scene("outro", 38);
    s.scene.background = this.meadow;
    const data = await (
      await fetch("/faithful/outro-layers/index.json")
    ).json();
    s.frames = await Promise.all(
      data.indices.map((i) =>
        this.tex(
          "/faithful/outro-layers/" + String(i).padStart(4, "0") + ".png",
        ),
      ),
    );
    s.canvas = canvas(s.frames[0].image.width, s.frames[0].image.height);
    s.map = this.texture(s.canvas);
    s.actor = this.plane(5.333, 3, s.map);
    s.actor.position.set(0, 1.5, 0);
    s.scene.add(s.actor);
  }
  outro(p, t) {
    const s = this.scenes.outro,
      age = t - 39.9,
      q = ease(p),
      index = Math.min(s.frames.length - 1, Math.floor(age * 12)),
      g = s.canvas.getContext("2d");
    g.clearRect(0, 0, s.canvas.width, s.canvas.height);
    g.drawImage(s.frames[index].image, 0, 0, s.canvas.width, s.canvas.height);
    g.globalCompositeOperation = "destination-in";
    const edge = g.createLinearGradient(
      0,
      s.canvas.height * 0.92,
      0,
      s.canvas.height,
    );
    edge.addColorStop(0, "#FFFFFFFF");
    edge.addColorStop(1, "#FFFFFF00");
    g.fillStyle = edge;
    g.fillRect(0, 0, s.canvas.width, s.canvas.height);
    g.globalCompositeOperation = "source-over";
    s.map.needsUpdate = true;
    const z = 1.6 * Math.exp(Math.log(30 / 1.6) * q),
      y = lerp(0.75, 8, q),
      tx = lerp(-1.41, 0, ease(p / 0.45)),
      ty =
        p < 0.45
          ? lerp(0.75, 1.5, ease(p / 0.45))
          : lerp(1.5, 9.5, ease((p - 0.45) / 0.55));
    s.camera.position.set(tx, y, z);
    s.camera.fov = lerp(38, 50, q);
    s.camera.updateProjectionMatrix();
    s.camera.lookAt(tx, ty, 0);
    this.trace = {
      shot: "S44",
      camera: s.camera.position.toArray(),
      crane_height: y - 0.75,
      drift_back: z - 1.6,
      performance_frame: index * 2,
    };
    this.renderer.render(s.scene, s.camera);
  }
  setupFloat() {
    const s = this.scene("float", 52);
    this.skyWorld(s);
    s.actor = this.plane(
      5.2,
      (5.2 * this.float.image.height) / this.float.image.width,
      this.float,
    );
    const halo = this.ring(0.34, 1.03);
    halo.position.x = 0.18;
    halo.rotation.x = 0.3;
    s.actor.add(halo);
    s.actor.position.set(0, 1.2, 0);
    s.scene.add(s.actor);
    s.lanterns = [];
    const r = rng(532);
    for (let i = 0; i < 35; i++) {
      const m = new T.Mesh(
        new T.CylinderGeometry(0.16, 0.2, 0.4, 12, 1, true),
        new T.MeshBasicMaterial({
          map: this.lanternPaper,
          side: T.DoubleSide,
          transparent: true,
          opacity: 0.8,
        }),
      );
      m.position.set((r() - 0.5) * 15, -3 + r() * 5, (r() - 0.5) * 12);
      s.scene.add(m);
      s.lanterns.push({ mesh: m, y: m.position.y });
    }
  }
  floatShot(p, t) {
    const s = this.scenes.float;
    s.camera.position.set(0, 1.4, lerp(5.5, 4.8, ease(p)));
    s.camera.lookAt(0, 1.4, 0);
    s.camera.rotateZ(360 * DEGREES * ease(p));
    s.actor.lookAt(V(0, 1.4, 6));
    for (const l of s.lanterns) l.mesh.position.y = l.y + p * 0.5;
    this.lyric(s, "爱是腾空的魔幻");
    this.trace = {
      shot: "S32",
      roll_degrees: 360 * ease(p),
      push_distance: 0.7 * ease(p),
    };
    this.renderer.render(s.scene, s.camera);
  }
  async setupPaper() {
    const s = this.scene("paper", 40);
    s.scene.background = new T.Color(C.cream);
    s.layers = [];
    const art = await image("/faithful/paper-empty.png");
    const d = await (await fetch("/faithful/paper/index.json")).json();
    s.running = await Promise.all(
      d.indices
        .slice(0, 42)
        .map((i) =>
          this.tex("/faithful/paper/" + String(i).padStart(4, "0") + ".png"),
        ),
    );
    for (let i = 0; i < 5; i++) {
      const z = [-3, -2, -1, 0, 0.6][i],
        c = canvas(1920, 1080),
        g = c.getContext("2d");
      if (i !== 3) {
        if (i > 0) {
          g.beginPath();
          g.moveTo(0, 1080);
          for (let x = 0; x <= 1920; x += 8) {
            const y =
              i === 1
                ? 565 + 38 * Math.sin(x * 0.002)
                : i === 2
                  ? 780 + 55 * Math.sin(x * 0.003 + 0.5)
                  : 1020 + 65 * Math.sin(x * 0.004 + 1);
            g.lineTo(x, y);
          }
          g.lineTo(1920, 1080);
          g.closePath();
          g.clip();
        }
        g.fillStyle = C.cream;
        g.fillRect(0, 0, 1920, 1080);
        g.drawImage(art, 0, 70, 1920, (1920 * art.height) / art.width);
        if (i === 0) {
          for (const side of [-1, 1]) {
            g.save();
            g.translate(side < 0 ? 210 : 1740, 510);
            g.scale(side < 0 ? 0.75 : -0.75, 0.75);
            g.rotate(-0.5);
            g.strokeStyle = "#141413";
            g.globalAlpha = 0.24;
            g.lineWidth = 2.5;
            g.beginPath();
            g.moveTo(-38, 95);
            g.lineTo(-45, 48);
            g.lineTo(-72, 4);
            g.bezierCurveTo(-83, -15, -62, -26, -49, -3);
            g.lineTo(-30, 20);
            g.lineTo(-30, -69);
            g.bezierCurveTo(-30, -93, -7, -90, -8, -69);
            g.lineTo(-6, -17);
            g.lineTo(0, -87);
            g.bezierCurveTo(2, -111, 28, -104, 21, -79);
            g.lineTo(15, -14);
            g.lineTo(28, -69);
            g.bezierCurveTo(35, -94, 58, -77, 47, -54);
            g.lineTo(33, -3);
            g.lineTo(47, -34);
            g.bezierCurveTo(59, -57, 77, -34, 61, -8);
            g.lineTo(43, 40);
            g.quadraticCurveTo(43, 72, 30, 95);
            g.stroke();
            g.restore();
          }
        }
      }
      const scale = (7.4 - z) / 7.4;
      const m =
        i === 3
          ? this.plane(
              (4.7 * s.running[0].image.width) / s.running[0].image.height,
              4.7,
              s.running[0],
            )
          : this.plane(11.8 * scale, 6.6375 * scale, this.texture(c));
      m.position.set(0, i === 3 ? 1.48 : 1.7, z);
      s.scene.add(m);
      s.layers.push(m);
    }
  }
  paper(p) {
    const s = this.scenes.paper,
      frame = Math.min(s.running.length - 1, Math.floor(p * 34));
    s.layers[3].material.map = s.running[frame];
    s.camera.position.set(lerp(-0.55, 0.55, ease(p)), 1.7, 7.4);
    s.camera.lookAt(s.camera.position.x, 1.7, 0);
    this.trace = {
      shot: "S35",
      layers: s.layers.length,
      animation_fps: 12,
      actor_frame: frame,
    };
    this.renderer.render(s.scene, s.camera);
  }
  setupOrigami() {
    const s = this.scene("origami", 38);
    s.scene.background = new T.Color(C.ink);
    const room = this.plane(15, 8.44, this.room);
    room.position.set(0, 1, -3.7);
    s.scene.add(room);
    const observer = this.plane(15, 8.44, this.observer);
    observer.position.set(0, 1, -3.69);
    s.scene.add(observer);
    s.parts = [];
    const ambient = new T.AmbientLight(0xffffff, 1.8),
      key = new T.DirectionalLight(0xffe3bd, 3);
    key.position.set(-3, 5, 6);
    s.scene.add(ambient, key);
    const make = (name, points, pivot, angle) => {
      const group = new T.Group();
      group.position.set(...pivot);
      const center = points
          .reduce((v, p) => v.add(V(p[0], p[1], 0)), V())
          .multiplyScalar(1 / points.length),
        pos = [],
        uv = [],
        norm = [];
      for (let i = 0; i < points.length; i++) {
        const a = points[i],
          b = points[(i + 1) % points.length];
        for (const [x, y, z] of [
          [center.x, center.y, 0.045],
          [a[0], a[1], i % 2 ? 0.008 : 0],
          [b[0], b[1], (i + 1) % 2 ? 0.008 : 0],
        ]) {
          pos.push(x, y, z);
          uv.push(0.5 + (x + pivot[0]) * 0.4, 0.15 + (y + pivot[1]) * 0.32);
        }
      }
      const geo = new T.BufferGeometry();
      geo.setAttribute("position", new T.Float32BufferAttribute(pos, 3));
      geo.setAttribute("uv", new T.Float32BufferAttribute(uv, 2));
      geo.computeVertexNormals();
      const mat = new T.MeshStandardMaterial({
        map: this.music,
        side: T.DoubleSide,
        roughness: 1,
        metalness: 0,
        color: 0xf0eee6,
      });
      group.add(new T.Mesh(geo, mat));
      const edges = new T.LineSegments(
        new T.EdgesGeometry(geo, 4),
        new T.LineBasicMaterial({
          color: "#8A7D66",
          transparent: true,
          opacity: 0.33,
        }),
      );
      group.add(edges);
      s.scene.add(group);
      s.parts.push({ name, group, pivot, angle });
    };
    make(
      "torso",
      [
        [-0.29, 0.43],
        [0.29, 0.43],
        [0.23, 0.08],
        [0.19, -0.36],
        [-0.19, -0.36],
        [-0.23, 0.08],
      ],
      [0, 1.16, 0],
      0,
    );
    make(
      "neck",
      [
        [-0.075, 0.09],
        [0.075, 0.09],
        [0.09, -0.09],
        [-0.09, -0.09],
      ],
      [0, 1.62, 0],
      0,
    );
    make(
      "head",
      [
        [-0.18, 0.15],
        [-0.11, 0.27],
        [0.11, 0.27],
        [0.19, 0.14],
        [0.15, -0.13],
        [0, -0.23],
        [-0.15, -0.13],
      ],
      [0, 1.87, 0.025],
      0,
    );
    make(
      "leftSleeve",
      [
        [0, 0.14],
        [-0.29, 0.19],
        [-0.51, 0.08],
        [-0.43, -0.14],
        [-0.18, -0.11],
        [0, -0.07],
      ],
      [-0.25, 1.53, 0],
      -0.28,
    );
    make(
      "rightSleeve",
      [
        [0, 0.14],
        [0.29, 0.19],
        [0.51, 0.08],
        [0.43, -0.14],
        [0.18, -0.11],
        [0, -0.07],
      ],
      [0.25, 1.53, 0],
      0.28,
    );
    make(
      "leftHand",
      [
        [0, 0.06],
        [-0.13, 0.09],
        [-0.19, 0.03],
        [-0.13, -0.01],
        [-0.2, -0.04],
        [-0.11, -0.065],
        [0, -0.06],
      ],
      [-0.73, 1.47, 0.02],
      -0.28,
    );
    make(
      "rightHand",
      [
        [0, 0.06],
        [0.13, 0.09],
        [0.19, 0.03],
        [0.13, -0.01],
        [0.2, -0.04],
        [0.11, -0.065],
        [0, -0.06],
      ],
      [0.73, 1.47, 0.02],
      0.28,
    );
    for (let i = 0; i < 7; i++) {
      const x = (i - 3) * 0.103;
      make(
        "pleat" + i,
        [
          [x * 0.53 - 0.035, 0.3],
          [x * 0.53 + 0.035, 0.3],
          [x + 0.066, -0.3],
          [x - 0.066, -0.3],
        ],
        [0, 0.64, 0.008 * (i % 2)],
        0,
      );
    }
    make(
      "leftLeg",
      [
        [-0.08, 0.45],
        [0.08, 0.45],
        [0.066, 0.04],
        [0.04, -0.3],
        [-0.12, -0.43],
        [-0.15, -0.39],
        [-0.045, -0.26],
        [-0.065, 0.05],
      ],
      [-0.16, -0.06, 0.01],
      -0.06,
    );
    make(
      "rightLeg",
      [
        [-0.08, 0.45],
        [0.08, 0.45],
        [0.065, 0.05],
        [0.045, -0.26],
        [0.15, -0.39],
        [0.12, -0.43],
        [-0.04, -0.3],
        [-0.066, 0.04],
      ],
      [0.16, -0.06, 0.01],
      0.06,
    );
    const portrait = canvas(1920, 1080),
      pg = portrait.getContext("2d");
    pg.drawImage(this.closedEye.image, 0, 0, 1920, 1080);
    pg.globalCompositeOperation = "destination-in";
    pg.beginPath();
    pg.ellipse(
      1920 * 0.56,
      1080 * 0.4,
      1920 * 0.32,
      1080 * 0.5,
      0,
      0,
      Math.PI * 2,
    );
    pg.fill();
    s.eyeSurface = this.plane(0.815, 0.46, this.texture(portrait), {
      opacity: 0,
    });
    s.eyeSurface.position.set(0, 1.88, 0.051);
    s.scene.add(s.eyeSurface);
    s.page = this.plane(1.42, 2.05, this.music);
    s.page.position.set(0, 1.0, 0.3);
    s.scene.add(s.page);
  }
  origami(p) {
    const s = this.scenes.origami,
      q = ease(p),
      unfold = 1 - Math.exp(-9 * q) * (Math.cos(q * 9) + Math.sin(q * 9));
    for (let i = 0; i < s.parts.length; i++) {
      const o = s.parts[i],
        u = clamp(unfold);
      o.group.position.set(
        o.pivot[0] * (0.22 + 0.78 * u),
        lerp(1, o.pivot[1], u),
        o.pivot[2] + (1 - u) * i * 0.004,
      );
      o.group.rotation.y = (1 - u) * Math.PI * (i % 2 ? 1 : -1);
      o.group.rotation.z = o.angle * u;
      if (o.name === "head") {
        const alpha = 1 - ease((p - 0.66) / 0.18);
        o.group.visible = alpha > 0;
        for (const m of o.group.children) {
          m.material.transparent = true;
          m.material.opacity = alpha;
        }
      }
    }
    s.page.visible = p < 0.18;
    s.page.rotation.y = ease(p / 0.18) * Math.PI * 0.5;
    s.page.scale.x = 1 - ease(p / 0.18) * 0.94;
    s.eyeSurface.material.opacity = ease((p - 0.68) / 0.26);
    const push = ease((q - 0.78) / 0.22);
    s.camera.position.set(
      0.053 * push,
      lerp(0.95, 1.949, push),
      lerp(4.9, 0.341, push),
    );
    s.camera.lookAt(0.053 * push, lerp(0.95, 1.949, push), 0.051);
    this.trace = {
      shot: "S15",
      folded_parts: s.parts.length,
      crease_geometry: true,
      spring_hinges: true,
      unfold_fraction: q,
    };
    this.renderer.render(s.scene, s.camera);
  }
}
