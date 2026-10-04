/** Bun + headless Chromium renderer. Every run retains its bundle, frames and hashes. */
import puppeteer from "../../../../tools/web/node_modules/puppeteer-core/lib/puppeteer/puppeteer-core.js";
import { spawn } from "node:child_process";
import { once } from "node:events";
import {
  mkdirSync,
  writeFileSync,
  readFileSync,
  copyFileSync,
  renameSync,
  openSync,
  closeSync,
  unlinkSync,
  existsSync,
  statSync,
} from "node:fs";
import { resolve, join, relative, sep } from "node:path";
import { createHash } from "node:crypto";
const ROOT = resolve(import.meta.dir, "../../../.."),
  SRC = import.meta.dir,
  WORK = join(ROOT, "work/first-day-anime-test/faithful"),
  OUT = join(ROOT, "renders/first-day-anime-test");
const stills = process.argv.includes("--stills"),
  preview = process.argv.includes("--preview"),
  width = preview ? 960 : 1920,
  height = (width * 9) / 16;
const digest = (path: string) =>
  createHash("sha256").update(readFileSync(path)).digest("hex");
mkdirSync(WORK, { recursive: true });
mkdirSync(OUT, { recursive: true });
const lockPath = join(WORK, "render.lock");
if (existsSync(lockPath)) {
  const prior = JSON.parse(readFileSync(lockPath, "utf8"));
  let alive = true;
  try {
    process.kill(prior.pid, 0);
  } catch (e: any) {
    if (e.code === "ESRCH") alive = false;
    else throw e;
  }
  if (alive) throw Error(`Renderer ${prior.pid} is still using this episode`);
  unlinkSync(lockPath);
}
const lock = openSync(lockPath, "wx");
writeFileSync(
  lock,
  JSON.stringify({ pid: process.pid, started: new Date().toISOString() }),
);
process.once("exit", () => {
  try {
    closeSync(lock);
    unlinkSync(lockPath);
  } catch {}
});
const sourceNames = [
  "film.js",
  "effects.js",
  "rigs.js",
  "surfaces.js",
  "common.js",
  "index.html",
  "render.ts",
  "timeline.json",
  "package.json",
  "bun.lock",
];
const sources = sourceNames.map((name) => ({
  path: relative(ROOT, join(SRC, name)),
  sha256: digest(join(SRC, name)),
}));
const sourceHash = createHash("sha256")
  .update(JSON.stringify(sources))
  .digest("hex");
const RUN = join(
  WORK,
  "runs",
  `${Date.now()}-${sourceHash.slice(0, 10)}-${height}`,
);
mkdirSync(join(RUN, "qa"), { recursive: true });
mkdirSync(join(WORK, "qa"), { recursive: true });
copyFileSync(join(SRC, "index.html"), join(RUN, "index.html"));
const built = await Bun.build({
  entrypoints: [join(SRC, "film.js")],
  outdir: join(RUN, "app"),
  target: "browser",
});
if (!built.success) throw Error(JSON.stringify(built.logs));
const requested = new Map<string, { size: number; mtimeMs: number }>(),
  errors: string[] = [];
const server = Bun.serve({
  hostname: "127.0.0.1",
  port: 0,
  async fetch(req) {
    const url = new URL(req.url);
    let path: string | undefined;
    if (url.pathname === "/favicon.ico")
      return new Response(null, { status: 204 });
    if (url.pathname === "/") path = join(RUN, "index.html");
    else if (url.pathname === "/film.js") path = join(RUN, "app/film.js");
    else {
      for (const [prefix, folder] of [
        ["/assets/", join(ROOT, "work/first-day-anime-test/assets")],
        ["/base/", join(ROOT, "work/first-day-anime-test/graphics-v2")],
        ["/faithful/", WORK],
        ["/motion/", join(ROOT, "work/first-day-anime-test/motion")],
      ]) {
        if (url.pathname.startsWith(prefix)) {
          const candidate = resolve(
            folder,
            decodeURIComponent(url.pathname.slice(prefix.length)),
          );
          if (!candidate.startsWith(folder + sep))
            return new Response("Invalid path", { status: 400 });
          path = candidate;
          break;
        }
      }
    }
    if (!path) return new Response("Not found", { status: 404 });
    const file = Bun.file(path);
    if (!(await file.exists()))
      return new Response("Not found " + url.pathname, { status: 404 });
    if (!requested.has(path)) {
      const st = statSync(path);
      requested.set(path, { size: st.size, mtimeMs: st.mtimeMs });
    }
    const range = req.headers.get("range");
    if (range && path.endsWith(".mp4")) {
      const m = range.match(/bytes=(\d+)-(\d*)/);
      if (m) {
        const start = +m[1],
          end = m[2] ? Math.min(+m[2], file.size - 1) : file.size - 1;
        if (start > end)
          return new Response(null, {
            status: 416,
            headers: { "Content-Range": `bytes */${file.size}` },
          });
        return new Response(file.slice(start, end + 1), {
          status: 206,
          headers: {
            "Content-Type": "video/mp4",
            "Accept-Ranges": "bytes",
            "Content-Range": `bytes ${start}-${end}/${file.size}`,
            "Content-Length": String(end - start + 1),
          },
        });
      }
    }
    return new Response(file, { headers: { "Cache-Control": "no-store" } });
  },
});
let browser: any, ff: any, completion: Promise<any> | undefined;
const traces: any[] = [];
const timeline = await Bun.file(join(SRC, "timeline.json")).json();
const defaults = [
  0, 20, 30, 33, 34, 35, 42, 51, 65, 84, 90, 104, 110, 120, 165, 185, 201, 220,
  242, 260, 300, 328, 335, 339, 346, 350, 355, 358, 359, 360, 371, 377, 378,
  379, 383, 386, 387, 388, 390, 402, 409, 437, 528, 550, 559, 560, 570, 581,
  589, 592, 605, 619, 622, 650, 680, 720, 753, 755, 760, 763, 773, 785, 800,
  829, 838, 847, 856, 889, 905, 915, 920, 922, 930, 959, 960, 961, 973, 999,
  1005, 1014, 1020, 1050, 1138, 1183, 1190, 1196, 1197, 1200, 1218, 1230, 1240,
  1284, 1306, 1310,
];
const sampled = [
  ...new Set([
    ...defaults,
    ...timeline.shots.flatMap((s: any) => [
      s.start_frame,
      Math.floor((s.start_frame + s.end_frame - 1) / 2),
      s.end_frame - 1,
    ]),
  ]),
].sort((a, b) => a - b);
const custom = process.argv.find((x) => x.startsWith("--frames="));
const samples = custom ? custom.slice(9).split(",").map(Number) : sampled;
const output = join(OUT, `first-day_opus55_faithful_${height}p30.mp4`),
  runMovie = join(RUN, "film.mp4");
try {
  browser = await puppeteer.launch({
    executablePath:
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: true,
    args: [
      "--hide-scrollbars",
      "--force-color-profile=srgb",
      "--autoplay-policy=no-user-gesture-required",
    ],
  });
  const page = await browser.newPage();
  await page.setViewport({ width, height, deviceScaleFactor: 1 });
  page.on("requestfailed", (r: any) => {
    if (r.failure()?.errorText !== "net::ERR_ABORTED")
      errors.push(`${r.url()} ${r.failure()?.errorText}`);
  });
  page.on("console", (m: any) => {
    if (m.type() === "error") errors.push(m.text());
  });
  page.on("response", (r: any) => {
    if (r.status() >= 400) errors.push(`HTTP ${r.status()} ${r.url()}`);
  });
  page.on("pageerror", (e: any) => errors.push(String(e)));
  await page.goto(`http://127.0.0.1:${server.port}/`, { waitUntil: "load" });
  await page.evaluate(async () => {
    await window.ready;
  });
  if (errors.length) throw Error(errors.join("\n"));
  if (!stills) {
    ff = spawn(
      "ffmpeg",
      [
        "-y",
        "-v",
        "error",
        "-f",
        "image2pipe",
        "-framerate",
        "30",
        "-i",
        "-",
        "-i",
        join(ROOT, "episodes/first-day-anime-test/first-day.mp3"),
        "-map",
        "0:v",
        "-map",
        "1:a",
        "-frames:v",
        "1311",
        "-t",
        "43.7",
        "-c:v",
        "libx264",
        "-preset",
        "fast",
        "-crf",
        "16",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "256k",
        "-movflags",
        "+faststart",
        runMovie,
      ],
      { stdio: ["pipe", "inherit", "inherit"] },
    );
    completion = once(ff, "close");
    ff.stdin.on("error", (e: any) => errors.push("Encoder " + e.message));
  }
  const frames = stills ? samples : Array.from({ length: 1311 }, (_, i) => i);
  for (const i of frames) {
    await page.evaluate(
      async (t: number) => await window.renderFrame(t),
      i / 30,
    );
    if (errors.length) throw Error(errors.join("\n"));
    const bytes = await page.screenshot({ type: "jpeg", quality: 96 });
    traces.push(await page.evaluate(() => window.trace));
    if (samples.includes(i)) {
      const name = `frame-${String(i).padStart(4, "0")}.jpg`;
      writeFileSync(join(RUN, "qa", name), bytes);
      writeFileSync(join(WORK, "qa", name), bytes);
    }
    if (ff && !ff.stdin.write(bytes)) await once(ff.stdin, "drain");
    if (i % 90 === 0 || stills) console.log(`frame ${i}/1311`);
  }
  if (ff) {
    ff.stdin.end();
    const [code] = await completion!;
    if (code !== 0) throw Error("ffmpeg exit " + code);
  }
  const assets = [...requested].map(([path, before]) => {
    const now = statSync(path);
    if (before.size !== now.size || before.mtimeMs !== now.mtimeMs)
      throw Error("Input changed during render: " + path);
    return { path: relative(ROOT, path), size: now.size, sha256: digest(path) };
  });
  for (const s of sources)
    if (digest(join(ROOT, s.path)) !== s.sha256)
      throw Error("Source changed during render: " + s.path);
  const manifest = {
    status: "rendered; visual/playback approval separate",
    mode: stills ? "stills" : "film",
    width,
    height,
    fps: 30,
    frames: frames.length,
    source_sha256: sourceHash,
    sources,
    authority: {
      path: "episodes/first-day-anime-test/director-response.md",
      sha256: digest(
        join(ROOT, "episodes/first-day-anime-test/director-response.md"),
      ),
    },
    audio: {
      path: "episodes/first-day-anime-test/first-day.mp3",
      sha256: digest(join(ROOT, "episodes/first-day-anime-test/first-day.mp3")),
    },
    runtime: { bun: Bun.version, chrome: await browser.version() },
    assets,
    output: stills
      ? null
      : { path: relative(ROOT, output), sha256: digest(runMovie) },
    run: relative(ROOT, RUN),
    errors,
  };
  writeFileSync(
    join(RUN, "camera-trace.json"),
    JSON.stringify(traces, null, 2),
  );
  writeFileSync(join(RUN, "manifest.json"), JSON.stringify(manifest, null, 2));
  writeFileSync(
    join(WORK, "camera-trace.json"),
    JSON.stringify(traces, null, 2),
  );
  if (!stills) {
    copyFileSync(runMovie, output + ".tmp");
    renameSync(output + ".tmp", output);
  }
  writeFileSync(
    join(WORK, stills ? "latest-stills.json" : `latest-${height}.json`),
    JSON.stringify(manifest, null, 2),
  );
  console.log(stills ? "Diagnostic frames ready" : output);
  console.log("Review run " + relative(ROOT, RUN));
} finally {
  if (ff?.exitCode === null) {
    ff.stdin.destroy();
    ff.kill("SIGTERM");
  }
  if (browser) await browser.close();
  server.stop(true);
}
