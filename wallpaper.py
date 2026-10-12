import io
from rembg import remove
from PIL import Image
HOME = (1170, 2532)
LOCK = (1284, 2778)
GREEN = (0, 255, 0)
def remove_bg(img):
  buf = io.BytesIO()
  img.save(buf, format="PNG")
  out = remove(buf.getvalue())
  res = Image.open(io.BytesIO(out))
  return res.convert("RGBA")
def make_wallpapers(img):
  fg = remove_bg(img)
  out = []
  for size, mode in [(HOME, "c"), (LOCK, "l")]:
    cw, ch = size
    box = fg.split()[-1].getbbox()
    sub = fg.crop(box) if box else fg
    mw = int(cw*0.9)
    mh = int(ch*0.9)
    w, h = sub.size
    sc = min(mw/w, mh/h, 1.0)
    nw = int(w*sc)
    nh = int(h*sc)
    sub = sub.resize((nw, nh), Image.LANCZOS)
    can = Image.new("RGBA", size, GREEN+(255,))
    x = (cw-nw)//2
    if mode == "l":
      y = int((ch-nh)*0.3)
    else:
      y = (ch-nh)//2
    can.paste(sub, (x, y), sub)
    out.append(can)
  return out
