from flask import Flask, render_template_string, session, redirect, request
import os
app = Flask(__name__)
app.secret_key = "emmy-lion-v4-secret"
CEO_PASSWORD = "EMMY2026"

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EMMY AI LION V4</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
body{background:#050505;color:#fff;text-align:center}
header{padding:20px;background:#0a0a0a;border-bottom:2px solid #FFD700}
h1{color:#FFD700;font-size:30px}
.sub{color:#00FF66;font-size:13px;margin-top:5px}
.main-lion{width:330px;height:330px;object-fit:cover;border-radius:25px;margin:20px auto 10px;border:3px solid #FFD700;box-shadow:0 0 40px #FFD700;display:block}
.main-lion.fire{border-color:#FF3300;box-shadow:0 0 50px #FF3300}
.main-lion.royal{border-color:#FFD700;box-shadow:0 0 50px #FFD700}
.core-dot{width:28px;height:28px;background:#00FF66;border-radius:50%;margin:-45px auto 15px;box-shadow:0 0 20px #00FF66,0 0 50px #00FF66;animation:pulse 1.2s infinite;position:relative;z-index:2}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.6)}}
.btn{padding:16px 28px;margin:8px;border:none;border-radius:50px;font-size:18px;font-weight:900;cursor:pointer}
.roar{background:linear-gradient(45deg,#FFD700,#FF6600);color:#000}
.fire{background:#FF2200;color:#fff}
.royal{background:#FFD700;color:#000}
.normal{background:#00FF66;color:#000}
.grid{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;padding:15px}
.card{background:#111;border:2px solid #333;border-radius:20px;padding:10px;width:155px;cursor:pointer}
.card img{width:100%;height:110px;object-fit:cover;border-radius:12px}
.card h3{color:#FFD700;margin:8px 0;font-size:14px}
.card p{font-size:11px;color:#aaa}
.dash{background:#111;margin:15px;border-radius:20px;padding:20px;text-align:left;border:1px solid #222}
.dash h2{color:#FFD700}
input{padding:15px;width:85%;border-radius:12px;border:1px solid #333;background:#111;color:#fff;font-size:18px;text-align:center;margin:10px}
.login-btn{background:#FFD700;padding:15px 40px;border:none;border-radius:50px;font-weight:900;font-size:18px}
.fire-bg{background:radial-gradient(circle,#4a0f00,#050505)!important}
</style></head>
<body id="body">
<header><h1>EMMY AI LION V4</h1><div class="sub">REAL LIONS - GOLDEN ROBOT - GREEN CORE</div></header>
{% if not logged %}
<div style="padding:40px 15px"><h2 style="color:#FFD700">CEO LOGIN</h2><p style="color:#aaa;margin:10px">Password: <b style="color:#00FF66">EMMY2026</b></p>
<form method="POST"><input type="password" name="pw" placeholder="Enter CEO Password" required><br><button class="login-btn">ENTER</button></form>
{% if err %}<p style="color:red;margin-top:10px">Wrong password Boss</p>{% endif %}</div>
{% else %}
<img id="mainLion" class="main-lion" src="/static/lion-official.jpg" onerror="this.src='https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=600'">
<div class="core-dot"></div>
<h2 id="status" style="color:#00FF66">ONLINE - READY TO ROAR</h2>
<p style="color:#aaa;font-size:13px;margin:8px">Tap a card below to change lion</p>
<button class="btn roar" onclick="roar()">ROAR !!!</button><br>
<button class="btn fire" onclick="setMode('fire')">FIRE MODE</button>
<button class="btn royal" onclick="setMode('royal')">ROYAL MODE</button>
<button class="btn normal" onclick="setMode('normal')">NORMAL MODE</button>
<div class="grid">
<div class="card" onclick="setMode('normal')"><img src="/static/lion-official.jpg" onerror="this.src='https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=400'"><h3>OFFICIAL V2</h3><p>Golden Robot<br>Green Chest Core</p></div>
<div class="card" onclick="setMode('fire')"><img src="/static/lion-fire.jpg" onerror="this.src='https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=400'"><h3>FIRE MODE</h3><p>Roaring In Fire<br>Battle Mode</p></div>
<div class="card" onclick="setMode('royal')"><img src="/static/lion-royal.jpg" onerror="this.src='https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=400'"><h3>ROYAL MODE</h3><p>Calm King<br>Golden Mane</p></div>
</div>
<div class="dash"><h2>EMMY AI Dashboard</h2><p><b>Version:</b> V4 - Real Lions</p><p><b>Project:</b> EMMY-AI-LION-V2-001 to V4 Live</p><p><b>Status:</b> <span style="color:#00FF66">ACTIVE on Railway</span></p><p><b>Lion:</b> Jaw - Head - Legs - Chest Pulse - Camera - Real Roar</p><br><a href="/logout" style="color:#FFD700">Logout</a></div>
{% endif %}
<script>
let roarAudio = new Audio('https://cdn.pixabay.com/audio/2022/03/10/audio_2c8c7b3b1a.mp3');
function roar(){
let img=document.getElementById('mainLion');
img.style.transform='scale(1.08) rotate(-2deg)';
document.getElementById('status').innerText='ROARRRR!!! EMMY IS KING!!!';
document.getElementById('status').style.color='#FF6600';
try{ roarAudio.currentTime=0; roarAudio.play(); }catch(e){}
try{
let ctx=new (window.AudioContext||window.webkitAudioContext)();
let o=ctx.createOscillator();let g=ctx.createGain();
o.type='sawtooth';o.frequency.setValueAtTime(90,ctx.currentTime);
o.frequency.exponentialRampToValueAtTime(40,ctx.currentTime+0.9);
g.gain.setValueAtTime(0.25,ctx.currentTime);
g.gain.exponentialRampToValueAtTime(0.01,ctx.currentTime+0.9);
o.connect(g);g.connect(ctx.destination);o.start();o.stop(ctx.currentTime+0.9);
}catch(e){}
setTimeout(()=>{img.style.transform='scale(1)';document.getElementById('status').innerText='ONLINE - READY TO ROAR';document.getElementById('status').style.color='#00FF66'},1200);
}
function setMode(m){
let b=document.getElementById('body');let img=document.getElementById('mainLion');
if(m=='fire'){b.classList.add('fire-bg');img.src='/static/lion-fire.jpg';img.className='main-lion fire';document.getElementById('status').innerText='FIRE MODE ACTIVE';}
if(m=='royal'){b.classList.remove('fire-bg');img.src='/static/lion-royal.jpg';img.className='main-lion royal';document.getElementById('status').innerText='ROYAL MODE ACTIVE';}
if(m=='normal'){b.classList.remove('fire-bg');img.src='/static/lion-official.jpg';img.className='main-lion';document.getElementById('status').innerText='ONLINE - READY TO ROAR';}
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
