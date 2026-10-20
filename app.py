from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI</title>
<style>
body{background:#050612;color:white;text-align:center;font-family:Arial;padding:30px;margin:0}
h1{font-size:40px;background:linear-gradient(90deg,#f9d76e,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.box{border:3px solid #a855f7;border-radius:20px;padding:20px;max-width:400px;margin:20px auto}
</style>
</head>
<body>
<h1>EMMY AI ⭐</h1>
<p style="font-size:80px">⭐</p>
<div class="box">
<p>CEO MODE: ACTIVE</p>
<p>Site is ONLINE!</p>
<p>Image coming next...</p>
</div>
<p>INTELLIGENCE • INNOVATION • IMPACT</p>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
