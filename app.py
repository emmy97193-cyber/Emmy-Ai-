from flask import Flask
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
                --panel: rgba(20, 26, 48, 0.8);
                --glass: rgba(118, 10, 255, 0.22);
            }

            * { box-sizing: border-box; }

            html, body {
                margin: 0;
                min-height: 100%;
                font-family: Arial, Helvetica, sans-serif;
                background:
                    radial-gradient(circle at top, rgba(168,85,247,0.32), transparent 30%),
                    linear-gradient(180deg, #040510 0%, #12091d 22%, #060813 100%);
                color: var(--white);
            }

            body {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                overflow-x: hidden;
            }

            .poster {
                position: relative;
                width: min(100vw, 980px);
                min-height: 100vh;
                background:
                    linear-gradient(180deg, rgba(5, 6, 18, 0.97), rgba(13, 7, 21, 1));
                overflow: hidden;
                padding: 28px 18px 30px;
            }

            .poster::before {
                content: "";
                position: absolute;
                inset: 0;
                background:
                    linear-gradient(90deg, rgba(255,255,255,0.03) 0 1px, transparent 1px 100%),
                    linear-gradient(180deg, rgba(255,255,255,0.03) 0 1px, transparent 1px 100%);
                background-size: 38px 38px;
                opacity: 0.2;
                pointer-events: none;
            }

            .stars {
                position: absolute;
                inset: 0;
                background-image:
                    radial-gradient(circle, rgba(255, 255, 255, 0.9) 0 1px, transparent 1.5px),
                    radial-gradient(circle, rgba(122, 92, 255, 0.9) 0 1.2px, transparent 1.8px),
                    radial-gradient(circle, rgba(255,255,255,0.8) 0 1px, transparent 1.7px);
                background-size: 220px 220px, 300px 300px, 180px 180px;
                background-position: 40px 40px, 140px 160px, 240px 90px;
                opacity: 0.7;
                pointer-events: none;
            }

            .title {
                position: relative;
                z-index: 2;
                text-align: center;
                margin-top: 12px;
                margin-bottom: 0;
                font-weight: 900;
                font-size: clamp(3.2rem, 10vw, 11rem);
                letter-spacing: 0.04em;
                color: var(--gold);
                text-shadow:
                    0 0 8px rgba(255, 240, 130, 0.8),
                    0 0 20px rgba(255, 220, 90, 0.9),
                    0 0 40px rgba(255, 200, 70, 0.7),
                    0 0 70px rgba(255, 170, 60, 0.8);
            }

            .star-wrap {
                position: relative;
                z-index: 2;
                display: flex;
                justify-content: center;
                margin-top: -2px;
                margin-bottom: 8px;
            }

            .star {
                width: 120px;
                height: 120px;
                background: linear-gradient(135deg, #fff7b0, #ffd857 25%, #f6b200 70%, #fff0a8);
                clip-path: polygon(50% 0%, 61% 35%, 100% 35%, 68% 57%, 80% 100%, 50% 70%, 20% 100%, 32% 57%, 0% 35%, 39% 35%);
                box-shadow: 0 0 18px rgba(255, 216, 87, 0.9), 0 0 42px rgba(255, 192, 76, 0.8);
                transform: rotate(8deg);
                filter: drop-shadow(0 0 10px rgba(255, 223, 112, 0.8));
            }

            .hero {
                position: relative;
                z-index: 2;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 8px;
                padding: 0 24px;
            }

            .avatar-stage {
                position: relative;
                width: min(760px, 88vw);
                height: 760px;
                max-height: 74vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .badge-1, .badge-2 {
                position: absolute;
                width: 170px;
                height: 110px;
                border-radius: 18px;
                border: 2px solid rgba(118, 92, 255, 0.9);
                background: rgba(18, 16, 32, 0.5);
                box-shadow: inset 0 0 18px rgba(112, 46, 255, 0.4), 0 0 18px rgba(133, 96, 255, 0.5);
                backdrop-filter: blur(6px);
            }

            .badge-1 { left: 4%; top: 10%; }
            .badge-2 { right: 4%; top: 18%; }

            .badge-1::before, .badge-2::before {
                content: "";
                position: absolute;
                inset: 10px;
                border-radius: 12px;
                background: linear-gradient(135deg, rgba(117,255,255,0.15), rgba(174,93,255,0.15));
                border: 1px solid rgba(114,241,255,0.5);
            }

            .badge-1::after, .badge-2::after {
                content: "";
                position: absolute;
                left: 20px; right: 20px; top: 50%; height: 40%;
                border-radius: 10px;
                transform: translateY(-50%);
                background: linear-gradient(90deg, rgba(74,255,196,0.2), rgba(117,241,255,0.2), rgba(195,105,255,0.2));
                box-shadow: inset 0 0 10px rgba(225,202,255,0.3);
            }

            .avatar {
                position: relative;
                width: min(430px, 70vw);
                height: min(560px, 60vh);
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .head {
                position: relative;
                width: 300px;
                height: 360px;
                border-radius: 45% 45% 32% 32% / 40% 40% 24% 24%;
                background: linear-gradient(180deg, #2a1b14 0%, #120b0b 20%, #0a0a0d 100%);
                box-shadow: inset 0 0 18px rgba(255,255,255,0.06), 0 0 24px rgba(74, 32, 94, 0.6);
                z-index: 4;
            }

            .head::before {
                content: "";
                position: absolute;
                inset: 0;
                border-radius: inherit;
                background: linear-gradient(90deg, rgba(255,255,255,0.03), transparent 20%, rgba(255,255,255,0.02), transparent 80%);
            }

            .hair {
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 260px;
                height: 150px;
                background: radial-gradient(circle at 50% 30%, rgba(14, 14, 14, 0.75), rgba(0,0,0,0.95) 70%);
                border-radius: 45% 45% 38% 38% / 76% 76% 20% 20%;
                box-shadow: inset 0 0 12px rgba(255,255,255,0.04);
                z-index: 5;
            }

            .shades {
                position: absolute;
                left: 50%;
                top: 150px;
                transform: translateX(-50%);
                width: 240px;
                height: 88px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 14px;
                background: linear-gradient(135deg, rgba(46, 12, 68, 0.96), rgba(25, 12, 38, 0.9));
                border: 2px solid rgba(181, 120, 255, 0.92);
                border-radius: 18px;
                box-shadow: 0 0 16px rgba(177, 100, 255, 0.7), inset 0 0 10px rgba(197, 170, 255, 0.24);
                z-index: 6;
            }

            .lens {
                width: 94px;
                height: 52px;
                border-radius: 16px;
                background: linear-gradient(180deg, rgba(110,255,243,0.18), rgba(165,95,255,0.12));
                border: 2px solid rgba(124, 234, 255, 0.8);
                box-shadow: inset 0 0 10px rgba(100, 230, 255, 0.3), 0 0 12px rgba(134, 74, 255, 0.5);
                position: relative;
            }

            .lens::before {
                content: "";
                position: absolute;
                inset: 11px 16px;
                border-radius: 12px;
                border: 2px solid rgba(202, 218, 255, 0.12);
                background: linear-gradient(135deg, rgba(15,14,28,0.2), rgba(112, 95, 255, 0.2));
            }

            .nose {
                position: absolute;
                width: 32px;
                height: 76px;
                left: 50%;
                top: 212px;
                transform: translateX(-50%);
                border-radius: 16px;
                background: linear-gradient(180deg, rgba(92,65,57,0.65), rgba(38,27,23,0.5));
                z-index: 7;
            }

            .mouth {
                position: absolute;
                width: 125px;
                height: 44px;
                left: 50%;
                top: 285px;
                transform: translateX(-50%);
                border-radius: 0 0 24px 24px;
                border-bottom: 3px solid rgba(255, 255, 255, 0.2);
                z-index: 7;
            }

            .body {
                position: absolute;
                bottom: 24px;
                width: 360px;
                height: 180px;
                border-radius: 28px 28px 18px 18px;
                background: linear-gradient(180deg, #f2d62b 0%, #f9c826 25%, #f0c32d 100%);
                box-shadow: inset 0 0 14px rgba(0,0,0,0.18), 0 0 18px rgba(226,209,62,0.18);
                z-index: 3;
                border: 3px solid rgba(83, 10, 99, 0.8);
            }

            .body::before {
                content: "";
                position: absolute;
                left: 18px; right: 18px; top: 18px; bottom: 18px;
                border-radius: 20px;
                background: linear-gradient(180deg, rgba(66, 10, 97, 0.95), rgba(18, 18, 35, 0.94));
                border: 2px solid rgba(123, 83, 255, 0.9);
            }

            .body::after {
                content: "EMMY AI";
                position: absolute;
                left: 50%;
                bottom: 32px;
                transform: translateX(-50%);
                font-size: clamp(0.9rem, 2vw, 2rem);
                font-weight: 900;
                letter-spacing: 0.1em;
                color: rgba(255, 255, 255, 0.9);
                text-shadow: 0 0 10px rgba(255,255,255,0.8);
                z-index: 2;
            }

            .chip {
                position: absolute;
                left: 50%;
                bottom: 26px;
                width: 124px;
                height: 26px;
                transform: translateX(-50%);
                border-radius: 12px;
                background: rgba(255,255,255,0.18);
                border: 2px solid rgba(161, 130, 255, 0.8);
                z-index: 1;
            }

            .module {
                position: absolute;
                width: 100px;
                height: 60px;
                border-radius: 12px;
                background: rgba(20, 16, 30, 0.55);
                border: 2px solid rgba(130, 88, 255, 0.9);
                box-shadow: inset 0 0 14px rgba(130, 90, 255, 0.26), 0 0 10px rgba(130, 90, 255, 0.26);
            }

            .module.m1 { left: 8%; top: 62%; }
            .module.m2 { right: 8%; top: 68%; }
            .module.m3 { left: 18%; bottom: 8%; }
            .module.m4 { right: 18%; bottom: 8%; }

            .module::before {
                content: "";
                position: absolute;
                inset: 12px;
                border-radius: 8px;
                border: 1px solid rgba(118, 219, 255, 0.8);
                background: linear-gradient(135deg, rgba(88, 255, 203, 0.12), rgba(163, 107, 255, 0.12));
            }

            .cta {
                position: relative;
                z-index: 2;
                display: flex;
                justify-content: center;
                gap: 18px;
                flex-wrap: wrap;
                margin-top: 18px;
            }

            .btn {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 16px 26px;
                min-width: 220px;
                border-radius: 999px;
                font-size: 1.1rem;
                font-weight: 800;
                text-decoration: none;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                box-shadow: 0 0 18px rgba(114, 241, 255, 0.3);
            }

            .btn:hover { transform: translateY(-2px); }

            .btn.primary {
                background: linear-gradient(135deg, #8a5cf6, #67f3ff);
                color: #08111d;
                box-shadow: 0 0 20px rgba(103,243,255,0.6);
            }

            .btn.secondary {
                background: linear-gradient(135deg, #ff39a8, #ff7a00);
                color: white;
                box-shadow: 0 0 20px rgba(255,59,168,0.45);
            }

            .footer-tag {
                position: relative;
                z-index: 2;
                margin-top: 24px;
                text-align: center;
                font-weight: 900;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                font-size: clamp(1.2rem, 2.3vw, 2.5rem);
                color: var(--gold);
                text-shadow: 0 0 16px rgba(255, 224, 103, 0.8), 0 0 26px rgba(255, 176, 76, 0.8);
            }

            @media (max-width: 700px) {
                .avatar-stage {
                    height: 600px;
                }

                .body {
                    width: 280px;
                    height: 150px;
                }

                .head {
                    width: 230px;
                    height: 300px;
                }

                .shades {
                    width: 180px;
                    top: 130px;
                }

                .btn {
                    min-width: 180px;
                    padding: 14px 20px;
                }
            }
        </style>
    </head>
    <body>
        <div class="poster">
            <div class="stars"></div>

            <h1 class="title">EMMY AI</h1>

            <div class="star-wrap">
                <div class="star" aria-label="star"></div>
            </div>

            <div class="hero">
                <div class="avatar-stage">
                    <div class="badge-1"></div>
                    <div class="badge-2"></div>

                    <div class="avatar">
                        <div class="head">
                            <div class="hair"></div>
                            <div class="shades">
                                <div class="lens"></div>
                                <div class="lens"></div>
                            </div>
                            <div class="nose"></div>
                            <div class="mouth"></div>
                        </div>
                        <div class="body"></div>
                        <div class="chip"></div>
                        <div class="module m1"></div>
                        <div class="module m2"></div>
                        <div class="module m3"></div>
                        <div class="module m4"></div>
                    </div>
                </div>
            </div>

            <div class="cta">
                <a class="btn primary" href="https://wa.me/2349115131319?text=Hi%20Emmy%20AI%20I%20saw%20your%20live%20site">💬 Chat Emmy</a>
                <a class="btn secondary" href="https://wa.me/2349115131319?text=Hello%20Lady%20T%20I%20want%20to%20buy%20hair">🛍️ Shop Lady T Hairs</a>
            </div>

            <div class="footer-tag">Intelligence • Innovation • Impact</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)































































































































