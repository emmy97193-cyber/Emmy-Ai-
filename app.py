from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>EMMY AI | Star Trek Activated</title>
        <style>
            :root {
                --bg-1: #050612;
                --bg-2: #140b2a;
                --purple: #a855f7;
                --violet: #7c3aed;
                --cyan: #72f1ff;
                --gold: #f9d76e;
                --gold-2: #ffef9a;
                --white: #f8f8ff;
            }
            * { box-sizing: border-box; }
            html, body {
                margin: 0;
                min-height: 100%;
                font-family: Arial, sans-serif;
                background: radial-gradient(circle at top, rgba(168,85,247,0.25), transparent 40%), 
                            radial-gradient(circle at bottom, rgba(124,58,237,0.3), #050612);
                color: var(--white);
                text-align: center;
            }
            .hero {
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .logo {
                font-size: 3.5rem;
                font-weight: 900;
                background: linear-gradient(90deg, var(--gold), var(--purple));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: 2px;
                text-shadow: 0 0 30px rgba(249,215,110,0.5);
            }
            .star {
                font-size: 4rem;
                animation: pulse 2s infinite;
                filter: drop-shadow(0 0 20px var(--gold));
            }
            @keyframes pulse {
                0%,100% { transform: scale(1); }
                50% { transform: scale(1.2); }
            }
            .ceo-img {
                width: 90%;
                max-width: 420px;
                border-radius: 24px;
                border: 3px solid var(--purple);
                box-shadow: 0 0 40px rgba(168,85,247,0.6), 0 0 80px rgba(249,215,110,0.3);
                margin: 25px 0;
            }
            .tagline {
                font-size: 1.1rem;
                letter-spacing: 3px;
                color: var(--gold);
                margin: 10px 0 30px 0;
                font-weight: bold;
            }
            .btns {
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
                justify-content: center;
            }
            .btn {
                padding: 14px 28px;
                border-radius: 50px;
                border: 2px solid var(--purple);
                background: linear-gradient(90deg, var(--violet), var(--purple));
                color: white;
                font-weight: 800;
                text-decoration: none;
                box-shadow: 0 0 20px rgba(168,85,247,0.5);
                transition: 0.3s;
            }
            .btn:hover {
                transform: scale(1.05);
                box-shadow: 0 0 40px var(--gold);
            }
            .btn-gold {
                background: linear-gradient(90deg, #ffcc33, #ffef9a);
                color: #140b2a;
                border-color: var(--gold);
            }
        </style>
    </head>
    <body>
        <div class="hero">
            <div class="logo">EMMY AI ⭐</div>
            <div class="star">⭐</div>
            
            <!-- YOUR NEW GLASSES CEO IMAGE -->
            <img src="/static/emmy_ceo.png" class="ceo-img" alt="EMMY AI CEO" />
            
            <div class="tagline">INTELLIGENCE • INNOVATION • IMPACT</div>
            
            <div class="btns">
                <a href="/static/emmy_ceo.png" download class="btn btn-gold">📥 Download Home Wallpaper</a>
                <a href="/static/emmy_ceo.png" download class="btn">📱 Download Lock Screen</a>
            </div>
            <p style="margin-top:30px; opacity:0.6;">CEO MODE: ACTIVE | GLASSES: FUTURE VISION | STAR: ⭐ ACTIVATED</p>
        </div>
    </body>
    </html>
    """

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
