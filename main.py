import os, glob
from flask import Flask, send_from_directory

app = Flask(__name__)

def get_wallpapers():
    files = []
    for ext in ["jpg","jpeg","png","webp","JPG","JPEG","PNG"]:
        files += glob.glob(f"*.{ext}")
        files += glob.glob(f"static/*.{ext}")
        files += glob.glob(f"static/wallpapers/*.{ext}")
    return sorted(set(files), reverse=True)

@app.route('/')
def home():
    wallpapers = get_wallpapers()
    cards = ""
    for img in wallpapers:
        cards += f"""
        <div style="background:#111;border-radius:15px;overflow:hidden;">
            <img src="/file/{img}" style="width:100%;height:350px;object-fit:cover;" onerror="this.style.display='none'">
            <div style="padding:10px;"><a href="/file/{img}" download style="display:block;background:#0f0;color:#000;text-align:center;padding:12px;border-radius:10px;font-weight:bold;text-decoration:none;">↓ Download</a><p style="color:#555;font-size:10px;text-align:center;margin:5px 0 0 0;">{img}</p></div>
        </div>
        """
    if not wallpapers:
        cards = "<p style='color:white'>No images found. Check GitHub files.</p>"
    return f"""
    <html><meta name="viewport" content="width=device-width, initial-scale=1">
    <body style="background:black;margin:0;font-family:sans-serif;">
    <div style="background:#0a5c26;padding:20px;text-align:center;color:white;">
    <h1 style="margin:0;">EMMY AI 🐸 $WALLPAPER</h1><p>Meme Coin • AI Wallpaper Bot</p><span style="background:black;padding:5px 15px;border-radius:20px;">BOT ONLINE ✅ emmyai0616#1150</span></div>
    <div style="padding:15px;"><h2 style="color:white;text-align:center;">🔥 Trending Wallpapers - {len(wallpapers)} Found</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">{cards}</div></div></body></html>"""

@app.route('/file/<path:filename>')
def serve_file(filename):
    d = os.path.dirname(filename) or "."
    f = os.path.basename(filename)
    return send_from_directory(d, f)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
