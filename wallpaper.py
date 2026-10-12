# make_green_wallpapers.py
import io
from rembg import remove
from PIL import Image

# --- CONFIG ---
INPUT_FILE = "input.jpg"          # your uploaded snake image
OUTPUT_HOME = "wallpaper_home.png"
OUTPUT_LOCK = "wallpaper_lock.png"

# Default sizes (change as needed)
SIZE_HOME = (1170, 2532)          # e.g. iPhone 12/13/14
SIZE_LOCK = (1284, 2778)          # e.g. larger iPhone models

# Chroma green color (R,G,B)
CHROMA_GREEN = (0, 255, 0)        # bright key green (#00FF00)
# --- END CONFIG ---

def remove_background(pil_img):
    with io.BytesIO() as inp:
        pil_img.save(inp, format="PNG")
        input_bytes = inp.getvalue()
    output_bytes = remove(input_bytes)   # rembg removes background
    return Image.open(io.BytesIO(output_bytes)).convert("RGBA")

def place_subject_on_canvas(fg, canvas_size, vertical_mode="center"):
    canvas_w, canvas_h = canvas_size
    # Get bounding box of non-transparent pixels
    bbox = fg.split()[-1].getbbox()
    if bbox:
        subject = fg.crop(bbox)
    else:
        subject = fg

    # Scale to fit within canvas with margin
    max_w = int(canvas_w * 0.9)
    max_h = int(canvas_h * 0.9)
    w, h = subject.size
    scale = min(max_w / w, max_h / h, 1.0)
    new_w = int(w * scale)
    new_h = int(h * scale)
    subject = subject.resize((new_w, new_h), Image.LANCZOS)

    # Compose onto green canvas
    canvas = Image.new("RGBA", canvas_size, CHROMA_GREEN + (255,))
    x = (canvas_w - new_w) // 2
    if vertical_mode == "lock":
        # place slightly higher so subject is visible behind clock/widgets
        y = int((canvas_h - new_h) * 0.30)
    else:
        # center
        y = (canvas_h - new_h) // 2

    canvas.paste(subject, (x, y), subject)
    return canvas

def main():
    src = Image.open(INPUT_FILE).convert("RGBA")
    fg = remove_background(src)

    home = place_subject_on_canvas(fg, SIZE_HOME, vertical_mode="center")
    lock = place_subject_on_canvas(fg, SIZE_LOCK, vertical_mode="lock")

    home.save(OUTPUT_HOME, format="PNG")
    lock.save(OUTPUT_LOCK, format="PNG")
    print(f"Saved: {OUTPUT_HOME}, {OUTPUT_LOCK}")

if __name__ == "__main__":
    main()
