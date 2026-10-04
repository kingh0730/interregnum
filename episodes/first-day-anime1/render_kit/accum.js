// Final compositor: renders N sub-frames of SCENE, averages them in LINEAR light in a half-float
// buffer (true motion blur, 180-degree shutter by default), then encodes sRGB with triangular dither
// (prevents banding in sky gradients) into the visible #out canvas.
(() => {
  'use strict';
  const VS = `#version 300 es
  in vec2 p; out vec2 uv;
  void main(){ uv = p * 0.5 + 0.5; gl_Position = vec4(p, 0.0, 1.0); }`;

  const FS_ADD = `#version 300 es
  precision highp float; in vec2 uv; uniform sampler2D src; uniform float w; out vec4 o;
  vec3 s2l(vec3 c){ return mix(c / 12.92, pow((c + 0.055) / 1.055, vec3(2.4)), step(0.04045, c)); }
  void main(){ vec3 c = texture(src, uv).rgb; o = vec4(s2l(c) * w, w); }`;

  const FS_RESOLVE = `#version 300 es
  precision highp float; in vec2 uv; uniform sampler2D acc; uniform float frame; out vec4 o;
  vec3 l2s(vec3 c){ return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c)); }
  float h(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
  void main(){
    vec3 c = l2s(clamp(texture(acc, uv).rgb, 0.0, 1.0));
    float n = h(gl_FragCoord.xy + frame * 17.0) + h(gl_FragCoord.xy * 1.37 + frame * 31.0) - 1.0; // triangular PDF
    float luma=dot(c,vec3(.2126,.7152,.0722));
    bool bars=frame<358. && (uv.y<.12808 || uv.y>.87192);
    float grain=bars?0.:(h(gl_FragCoord.xy*2.31+frame*43.)-.5)*.02*clamp(luma,.15,1.);
    if(frame>=358. && frame<360.)o=vec4(1.);
    else o = vec4(c + vec3(grain) + n / 255.0, 1.0);
  }`;

  function sh(gl, type, src) {
    const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error('shader: ' + gl.getShaderInfoLog(s));
    return s;
  }
  function prog(gl, fs) {
    const p = gl.createProgram();
    gl.attachShader(p, sh(gl, gl.VERTEX_SHADER, VS)); gl.attachShader(p, sh(gl, gl.FRAGMENT_SHADER, fs));
    gl.bindAttribLocation(p, 0, 'p'); gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error('link: ' + gl.getProgramInfoLog(p));
    return p;
  }

  window.__initAccum = (canvas) => {
    const gl = canvas.getContext('webgl2', { antialias: false, alpha: false, preserveDrawingBuffer: true, premultipliedAlpha: false });
    if (!gl) throw new Error('WebGL2 unavailable: fix Chromium GL flags; do NOT fall back to 2D/CSS.');
    if (!gl.getExtension('EXT_color_buffer_float') && !gl.getExtension('EXT_color_buffer_half_float'))
      throw new Error('Half-float render targets unavailable: motion blur accumulation impossible.');
    window.__glInfo = (() => {
      const e = gl.getExtension('WEBGL_debug_renderer_info');
      return e ? gl.getParameter(e.UNMASKED_RENDERER_WEBGL) : 'unknown';
    })();

    const W = canvas.width, H = canvas.height;
    const pAdd = prog(gl, FS_ADD), pRes = prog(gl, FS_RESOLVE);
    const vao = gl.createVertexArray(); gl.bindVertexArray(vao);
    const vb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, vb);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

    const srcTex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, srcTex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

    const accTex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, accTex);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA16F, W, H, 0, gl.RGBA, gl.HALF_FLOAT, null);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    const fbo = gl.createFramebuffer();
    gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, accTex, 0);
    if (gl.checkFramebufferStatus(gl.FRAMEBUFFER) !== gl.FRAMEBUFFER_COMPLETE) throw new Error('accum FBO incomplete');

    window.__renderFrame = async (frame, subframes) => {
      const S = window.SCENE;
      const total = RT.FPS * 43.70;
      const n = Math.max(1, subframes ?? (S.subframesFor ? S.subframesFor(frame) : 8));
      const shutter = S.shutter ?? 0.5; // 180 degrees
      const t0 = frame / RT.FPS;
      if(S.prepareFrame)await S.prepareFrame(t0,frame);
      const [a, b] = S.shotRange ? S.shotRange(t0) : [0, 1e9]; // blur must never straddle a hard cut

      gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
      gl.viewport(0, 0, W, H);
      gl.disable(gl.BLEND);
      gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);

      for (let k = 0; k < n; k++) {
        let t = n === 1 ? t0 : t0 - (shutter / RT.FPS) / 2 + ((shutter / RT.FPS) * (k + 0.5)) / n;
        t = RT.clamp(t, Math.max(0, a), Math.min(total / RT.FPS, b - 1e-4));
        RT.setTime(t, frame * 64 + k);
        await S.render(t, frame, k);

        gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
        gl.viewport(0, 0, W, H);
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, srcTex);
        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
        gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, S.canvas);
        gl.bindVertexArray(vao);
        gl.useProgram(pAdd);
        gl.uniform1i(gl.getUniformLocation(pAdd, 'src'), 0);
        gl.uniform1f(gl.getUniformLocation(pAdd, 'w'), 1 / n);
        gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      }

      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      gl.viewport(0, 0, W, H);
      gl.disable(gl.BLEND);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, accTex);
      gl.useProgram(pRes);
      gl.uniform1i(gl.getUniformLocation(pRes, 'acc'), 0);
      gl.uniform1f(gl.getUniformLocation(pRes, 'frame'), frame);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      gl.finish();
      return true;
    };
  };
})();
