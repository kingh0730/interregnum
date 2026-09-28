"""Shot 11 THE ORDER: J06 per-line typed layers + seal, homography onto k06's blank paper (aspect kept), 0.6 px blur.
Each becomes a full-frame (k06 cover-fit) RGBA still; 11.json reveals them with multiply blend + fade_in."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
S = W / 1672
# paper flat area in k06 (source px): x 450-1240, y 358-562. Keep the J06 canvas aspect (1600x460).
# crop the canvas to x 0-1560, y 25-425 (aspect 3.9 = the paper's), so the type fills the strip
CX0, CY0, CX1, CY1 = 0, 25, 1560, 425
ph = 198; pw = ph * (CX1 - CX0) / (CY1 - CY0)
x0, y0 = 458, 362
dst = np.float32([[x0, y0], [x0 + pw, y0 - 3], [x0 + pw, y0 + ph - 5], [x0 + 2, y0 + ph]]) * S
M = cv2.getPerspectiveTransform(np.float32([[CX0, CY0], [CX1, CY0], [CX1, CY1], [CX0, CY1]]), dst)
for name in ["line1", "line2", "line3", "line4", "line5", "seal"]:
    im = rd(ROOT / f"work/pilot/js/s11_order_j06/{name}.png").astype(np.float32)
    im[..., :3] *= im[..., 3:4] / 255
    w = cv2.warpPerspective(im, M, (W, H), flags=cv2.INTER_AREA)
    w = cv2.GaussianBlur(w, (0, 0), 0.6)
    a = w[..., 3:4] / 255
    rgb = np.where(a > 1e-3, w[..., :3] / np.maximum(a, 1e-3), 0)
    cv2.imwrite(str(C / f"11_{name}.png"), np.clip(np.dstack([rgb, w[..., 3]]), 0, 255).astype(np.uint8))
