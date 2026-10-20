from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI</title></head>
<body style="background:#050612;color:white;text-align:center;font-family:Arial;padding:30px">
<h1 style="font-size:3rem;background:linear-gradient(90deg,#f9d76e,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent">EMMY AI ⭐</h1>
<p style="font-size:80px">⭐</p>
<img src="https://raw.githubusercontent.com/emmy9719/Emmy-Ai-/main/IMG-20261020-WA9640.jpg" style="width:90%;max-width:400px;border-radius:20px;border:3px solid #a855f7" />
<p>INTELLIGENCE • INNOVATION • IMPACT</p>
<p>CEO MODE: ACTIVE</p>
</body></html>
"""

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
