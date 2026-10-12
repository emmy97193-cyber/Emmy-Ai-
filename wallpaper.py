import io
from rembg import remove
from PIL import Image

SIZE_HOME = (1170, 2532)
SIZE_LOCK = (1284, 2778)
CHROMA_GREEN = (0, 255, 0)

def remove_background(pil_img):
    with io.BytesIO() as inp:
        pil_img.save(inp, format="PNG")
        input_bytes = inp.getvalue()
    output_bytes = remove(input_bytes)
    return Image.open(io.BytesIO(output_bytes)).convert("RGBA")

def make_wallpapers(pil_img):
    fg = remove_background(pil_img)

    wallpapers = []
    for size, mode in [(SIZE_HOME, "center"), (SIZE_LOCK, "lock")]:
        canvas_w, canvas_h = size
        bbox = fg.split()[-1].getbbox()
        subject = fg.crop(bbox) if bbox else fg

        max_w, max_h = int(canvas_w * 0.9), int(canvas_h * 0.9)
        w, h = subject.size
        scale = min(max_w / w, max_h / h, 1.0)
        subject = subject.resize((int(w*scale), int(h*scale)), Image.LANCZOS)

        canvas = Image.new("RGBA", size, CHROMA_GREEN + (255,))
        x = (canvas_w - subject.size[0]) // 2
        y = int((canvas_h - subject.size[1]) * 0.30) if mode == "lock" else (canvas_h - subject.size[1]) // 2
        canvas.paste(subject, (x, y), subject)
        wallpapers.append(canvas)
    return wallpapers # [home, lock]
