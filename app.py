# EMMY AI LION V3 - EMMY★..★
# FILE: app.py - Replace old app.py completely

from flask import Flask, render_template_string, session, redirect, request
import os

app = Flask(__name__)
app.secret_key = "emmy-lion-v3-secret"

# YOUR NEW PASSWORD - Change this to what you want
CEO_PASSWORD = "EMMY2026"

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EMMY AI LION V3</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
body{background:#050505;color:#fff;text-align:center;overflow-x:hidden}
header{padding:20px;background:#0a0a0a;border-bottom:2px solid #FFD700}
h1{color:#FFD700;font-size:32px;letter-spacing:2px}
.sub{color:#00FF66;font-size:14px;margin-top:5px}
.lion-wrap{position:relative;width:320px;height:320px;margin:25px auto}
.lion{font-size:230px;line-height:320px;filter:drop-shadow(0 0 30px #FFD700);transition:0.3s}
.lion.roaring{transform:scale(1.15) rotate(-3deg);filter:drop-shadow(0 0 50px #FF6600)}
.core{position:absolute;bottom:95px;left:50%;transform:translateX(-50%);width:28px;height:28px;background:#00FF66;border-radius:50%;box-shadow:0 0 20px #00FF66,0 0 50px #00FF66;animation:pulse 1.2s infinite}
@keyframes pulse{0%,100%{transform:translateX(-50%) scale(1)}50%{transform:translateX(-50%) scale(1.6)}}
.eyes{position:absolute;top:95px;left:50%;transform:translateX(-50%);display:flex;gap:45px}
.eye{width:16px;height:16px;background:#00FF66;border-radius:50%;box-shadow:0 0 15px #00FF66;animation:blink 3s infinite}
@keyframes blink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(0.1)}}
.btn{padding:16px 30px;margin:8px;border:none;border-radius:50px;font-size:18px;font-weight:900;cursor:pointer}
.roar{background:linear-gradient(45deg,#FFD700,#FF6600);color:#000}
.fire{background:#FF2200;color:#fff}
.royal{background:#FFD700;color:#000}
.normal{background:#00FF66;color:#000}
.grid{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;padding:15px}
.card{background:#111;border:2px solid #333;border-radius:20px;padding:15px;width:150px}
.card.fire-mode{border-color:#FF6600;background:#2a0a00}
.card.royal-mode{border-color:#FFD700;background:#1a1500}
.card h3{color:#FFD700;margin:8px 0}
.card p{font-size:12px;color:#aaa}
.dash{background:#111;margin:15px;border-radius:20px;padding:20px;text-align:left;border:1px solid #222}
.dash h2{color:#FFD700}
.dash p{margin:10px 0;color:#ccc}
input{padding:15px;width:85%;border-radius:12px;border:1px solid #333;background:#111;color:#fff;font-size:18px;text-align:center;margin:10px}
.login-btn{background:#FFD700;padding:15px 40px;border:none;border-radius:50px;font-weight:900;font-size:18px}
.fire-bg{background:radial-gradient(circle,#4a0f00,#050505)!important}
</style></head>
<body id="body">
<header><h1>🦁 EMMY★..★ AI LION V3</h1><div class="sub">GOLDEN ROBOT • GREEN CORE • CEO MODE</div></header>

{% if not logged %}
<div style="padding:40px 15px"><h2 style="color:#FFD700">CEO LOGIN</h2><p style="color:#aaa;margin:10px">Your new password is: <b style="color:#00FF66">EMMY2026</b></p>
<form method="POST"><input type="password" name="pw" placeholder="Enter CEO Password" required><br><button class="login-btn">ENTER 🦁</button></form>
{% if err %}<p style="color:red;margin-top:10px">Wrong password Boss, try again</p>{% endif %}</div>
{% else %}

<div class="lion-wrap"><div class="lion" id="lion">🦁</div><div class="eyes"><div class="eye"></div><div class="eye"></div></div><div class="core"></div></div>
<h2 id="status" style="color:#00FF66">● ONLINE • READY TO ROAR</h2>
<p style="color:#aaa;margin:8px">Top-Left = Official • Top-Right = Fire • Bottom-Right = Royal</p>

<button class="btn roar" onclick="roar()">🦁 ROAR !!!</button><br>
<button class="btn fire" onclick="setMode('fire')">🔥 FIRE MODE</button>
<button class="btn royal" onclick="setMode('royal')">👑 ROYAL MODE</button>
<button class="btn normal" onclick="setMode('normal')">💚 NORMAL MODE</button>

<div class="grid">
<div class="card" id="c1"><div style="font-size:60px">🤖🦁</div><h3>OFFICIAL V2</h3><p>Golden Robot<br>Green Chest Core<br>Dark Mane</p></div>
<div class="card" id="c2"><div style="font-size:60px">🔥🦁</div><h3>FIRE MODE</h3><p>Roaring In Fire<br>Orange Glow<br>Battle Mode</p></div>
<div class="card" id="c3"><div style="font-size:60px">👑🦁</div><h3>ROYAL MODE</h3><p>Calm King<br>Golden Mane<br>Logo / Dashboard</p></div>
</div>

<div class="dash"><h2>📊 EMMY AI Dashboard</h2><p><b>Project:</b> EMMY-AI-LION-V2-001 → V3 Live</p><p><b>Status:</b> <span style="color:#00FF66">● ACTIVE on Railway</span></p><p><b>Lion:</b> Jaw • Head • Legs • Chest Pulse • Camera</p><p><b>Next:</b> V4 = Real 3D + Voice Roar</p><br><a href="/logout" style="color:#FFD700">Logout</a></div>
{% endif %}

<script>
let audioCtx;
function roar(){
  let l=document.getElementById('lion');
  l.classList.add('roaring');
  document.getElementById('status').innerText='🔥 ROARRRR!!! EMMY IS KING!!!';
  document.getElementById('status').style.color='#FF6600';
  try{
    audioCtx=new (window.AudioContext||window.webkitAudioContext)();
    let o=audioCtx.createOscillator(); let g=audioCtx.createGain();
    o.type='sawtooth'; o.frequency.setValueAtTime(80,audioCtx.currentTime);
    o.frequency.exponentialRampToValueAtTime(40,audioCtx.currentTime+0.8);
    g.gain.setValueAtTime(0.3,audioCtx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.01,audioCtx.currentTime+0.8);
    o.connect(g); g.connect(audioCtx.destination); o.start(); o.stop(audioCtx.currentTime+0.8);
  }catch(e){}
  setTimeout(()=>{l.classList.remove('roaring');document.getElementById('status').innerText='● ONLINE • READY TO ROAR';document.getElementById('status').style.color='#00FF66'},1200);
}
function setMode(m){
  let b=document.getElementById('body');
  if(m=='fire'){b.classList.add('fire-bg');document.getElementById('status').innerText='🔥 FIRE MODE ACTIVE';}
  if(m=='royal'){b.classList.remove('fire-bg');document.getElementById('status').innerText='👑 ROYAL MODE ACTIVE';}
  if(m=='normal'){b.classList.remove('fire-bg');document.getElementById('status').innerText='● ONLINE • READY TO ROAR';}
}
</script></body></html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    err=False
    if request.method=="POST":
        if request.form.get("pw")==CEO_PASSWORD:
            session["logged"]=True
            return redirect("/")
        err=True
    return render_template_string(HTML, logged=session.get("logged"), err=err)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    port=int(os.environ.get("PORT",8080))
    app.run(host="0.0.0.0", port=port)
"""

Paste > Commit > Wait 1 min > Open your Railway link again.

**Your NEW password is now:**
