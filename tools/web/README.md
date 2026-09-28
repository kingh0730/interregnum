# JS rendering

HTML, Canvas and WebGL pages rendered frame by frame in headless Chrome. Use it for anything that is really
*interface* or *graphic*: in-world social feeds, chat threads, AI consoles, propaganda screens, news tickers,
HUDs, maps, data visualizations, title and credit sequences, typography, glitch transitions, generative art,
animatics and review pages.

**Setup (not installed yet, to save disk):** `puppeteer-core` driving the system Chrome at
`/Applications/Google Chrome.app`. Node v22 is at `~/.nvm/versions/node/v22.23.1/bin`; call it by that path
in scripts, because the `node` shell function fails in non-interactive shells.

**Convention:** each piece is one page that exposes `window.renderFrame(t)` (t in seconds). The renderer calls it
for every frame, screenshots at 1920×1080 with transparency where needed, and pipes the frames to ffmpeg. Time is
driven by the renderer, never by the wall clock, so renders are deterministic.
