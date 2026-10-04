"""Lossless PNG re-encoding; pixel values, resolution and frame count are unchanged."""
import io,sys
from PIL import Image
image=Image.open(sys.argv[1] if len(sys.argv)>1 else io.BytesIO(sys.stdin.buffer.read()))
image.save(sys.argv[2] if len(sys.argv)>2 else sys.stdout.buffer,format='PNG',optimize=True,compress_level=9)
