# Built-in imagegen prompt specifications and provenance

These are the production prompt specifications, condensed for readability; the full tool calls are in the session transcript. All images below were made with the built-in imagegen tool, not the fallback CLI. Workspace copies are retained alongside the Luma-generated scene sources. Exact crop/segmentation operations are recorded in the build scripts.

| Output | Reference | Prompt specification |
|---|---|---|
| `proofs/P1-lead-beauty.png` | none | Four full-body leads in cel and soft-vinyl rows: ChatGPT bone hoodie/emerald cuffs/braid knot, Claude cream hair/terracotta cardigan/sunburst clip, DeepSeek whale hood/headlamp, Grok white streak/stripe jacket/towel. Distinct faces and heights, clean ivory space, no text. |
| `assets/cast-cel.png` | P1 | Six separate transparent front A-pose figures, same identities plus peach-puffer double-bun Doubao and split-indigo/peach Gemini with star lantern. Flat cel shading and clean varied outlines. |
| `assets/cast-toy.png` | cel atlas | Same six identities/outfits as dimensional soft-vinyl figures, separated full bodies, transparent background and no shadows. |
| `assets/cast-cel-v2.png` | original cel atlas | Repair clipped hair and reformat into two rows / three columns, preserve faces and all costume invariants, full hands and shoes. |
| `assets/cast-felt.png` | repaired cel atlas | Recreate all six as actual needle-felt stop-motion puppets, fine wool fibers, embroidery, seams, warm miniature lighting; no smooth plastic. |
| `assets/cast-leap.png` | repaired cel atlas | Six different full-body mid-leap poses with bent knees, flying hair/coat hems and underplayed faces. Preserve costume and identity, transparent background, no floor or shadows. |
| `assets/cast-ensemble-leap.png` | none | Nine separate charming human figures: purple crane-carrying Qwen, midnight scarf Kimi, indigo brush-pin Wenxin, gold-ingot Yuanbao, mint-glasses GLM, coral MiniMax, orange sparkler 星火, cream llama-hood Llama, pale-blue windbreaker Mistral. Distinct leaping poses in 3×3 grid, transparent, no labels. |
| `assets/S29r.png` | Luma S29 | Pull back the exact linked-hand aerial composition until all four central shoes and all six figures fit with sky margin. Preserve faces, costumes, gold ring and dawn cel artwork. |
| `assets/AGI-no-shadow.png` | Luma AGI | Remove only the soft oval shadow below hovering feet; preserve the patchwork costume, face, rim light, footprints and composition. |
| `assets/S13-final.png` | Luma S13 | Keep six identities and proportions, raise all heels in a tiptoe anticipation pose, gold threads converge beneath the first girl. Commit to gongbi mineral pigment, fine lines and gold on ivory silk. |
| `assets/hand-layer.png` | Luma E02-hand | Extract only the right hand, grey cuff and spirit level. Preserve original lower-right placement on the same transparent 16:9 canvas; no recentering or new objects. |
| `assets/S33-pencil.png` | cropped Gemini leap | Graphite animator line test of Gemini, preserved face/coat/star lantern/pose, construction circles and sparse hatching on warm white; remove stray neighboring mitten. |
| `assets/P21-drawn.png` | Luma P21_touch | Registered drawn counterpart: left hand graphite, right hand flat cel with terracotta cuff, same fingertips/camera/scale; used with measured vertical registration and the original photo/video inside the contact ring. |

Authoritative lead designs remain in the planner's cast cards and the repaired cel sheet. Rejected or superseded artwork is not silently promoted to a new identity reference. The primitive `doll.ts` timing figures are not the final character designs.
