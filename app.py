from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>EMMY-AI - BOSS MODE</title>
    <style>
    body{background:black;color:gold;text-align:center;font-family:sans-serif;padding-top:80px}
    .dragon{font-size:100px;animation:fly 2s infinite}
    @keyframes fly{0%{transform:translateY(0)}50%{transform:translateY(-30px)}100%{transform:translateY(0)}}
    button{background:gold;color:black;padding:15px 30px;font-size:20px;border:none;border-radius:10px}
    </style>
    </head>
    <body>
    <div class="dragon">🌟</div>
    <h1>EMMY-AI</h1>
    <h3>BOSS MODE - ONLINE</h3>
    <p>Hi Boss, I'm EMMY-AI. I'm live on Railway.</p>
    <button onclick="alert('Hi Boss, I am EMMY-AI!')">TALK TO EMMY-AI</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
