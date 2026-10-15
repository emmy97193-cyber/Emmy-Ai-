import os, glob
from flask import Flask, send_from_directory

app = Flask(__name__)

def get_wallpapers():
    images = []
    # Check root (where you uploaded)
    images += glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png") + glob.glob("*.webp") + glob.glob("*.JPG") + glob.glob("*.JPEG")
    # Filter only your IMG uploads
    
    # Check other folders too
    for folder in ["static", "static/wallpapers", "wallpapers"]:
        if os.path.exists(folder):
            for ext in ["jpg","jpeg","png","webp","JPG"]:
                images += glob.glob(f"{folder}/*.{ext}")
    return images

@app.route('/')
def home():
    wallpapers = get_wallpapers()
    # Build HTML grid
    cards = ""
    for img in wallpapers:
        cards += f"""
        <div style="background:#111;border-radius:15px;overflow:hidden;margin:10px;">
            <img src="/file/{img}" style="width:100%;height:300px;object-fit:cover;">
            <a href="/file/{img}" download style="display:block;background:#0f0;color:#000;text-align:center;padding:12px;margin:10px;border-radius:10px;font-weight:bold;text-decoration:none;">↓ Download</a>
        </div>
        """
    if not cards:
        cards = "<p style='color:white;text-align:center;'>No wallpapers found yet. Upload IMG files to GitHub root.</p>"

    return f"""
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>EMMY AI WALLPAPER</title>
    </head>
    <body style="background:black;margin:0;font-family:sans-serif;">
        <div style="background:#0a5c26;padding:20px;text-align:center;color:white;">
            <h1 style="margin:0;">EMMY AI 🐸 $WALLPAPER</h1>
            <p>Meme Coin Community • AI Wallpaper Bot</p>
            <span style="background:black;padding:5px 15px;border-radius:20px;font-size:13px;">BOT ONLINE ✅ emmyai0616#1150</span>
        </div>
        <div style="padding:15px;">
            <h2 style="color:white;text-align:center;">🔥 Trending Wallpapers</h2>
            <p style="color:gray;text-align:center;">Download • Set • Share</p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                {cards}
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/file/<path:filename>')
def serve_file(filename):
    # Serve from root or subfolder
    directory = os.path.dirname(filename) or "."
    file = os.path.basename(filename)
    if directory == ".":
        return send_from_directory(".", file)
    else:
        return send_from_directory(directory, file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
