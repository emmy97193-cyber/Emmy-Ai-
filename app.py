from flask import Flask
import os
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>EMMY-AI</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing: border-box; }
body{
  margin:0; padding:15px; text-align:center; font-family:sans-serif; color:#4a0080;
  background: linear-gradient(180deg, #ff9a9e 0%, #fad0c4 15%, #ffecd2 30%, #fcb69f 45%, #a18cd1 60%, #fbc2eb 75%, #8fd3f4 90%, #84fab0 100%);
  background-size: 400% 400%;
  animation: rainbowMove 15s ease infinite;
  min-height:100vh; overflow-x:hidden;
}
@keyframes rainbowMove{
  0%{background-position:0% 0%}
  50%{background-position:100% 100%}
  100%{background-position:0% 0%}
}
/* CLOUDS */
.cloud{
  position:fixed; background:white; border-radius:50px; opacity:0.9; z-index:0;
  filter: blur(2px);
}
.cloud1{ width:180px;height:50px; top:10%; left:-200px; animation: cloudMove 25s linear infinite; }
.cloud2{ width:140px;height:40px; top:25%; left:-150px; animation: cloudMove 35s linear infinite; animation-delay:5s; }
.cloud3{ width:220px;height:60px; top:5%; left:-250px; animation: cloudMove 45s linear infinite; animation-delay:10s; }
.cloud:before{ content:''; position:absolute; background:white; width:70px;height:70px; border-radius:50%; top:-30px; left:30px; }
.cloud:after{ content:''; position:absolute; background:white; width:50px;height:50px; border-radius:50%; top:-20px; left:90px; }
@keyframes cloudMove{ from{left:-250px} to{left:110%} }

/* FALLING STARS */
.star-fall{
  position:fixed; top:-20px; font-size:24px; z-index:1; animation: fall linear infinite;
}
@keyframes fall{
  to{ transform: translateY(110vh) rotate(360deg); }
}
.s1{ left:10%; animation-duration:4s; }
.s2{ left:30%; animation-duration:5s; animation-delay:1s; }
.s3{ left:50%; animation-duration:3.5s; animation-delay:0.5s; }
.s4{ left:70%; animation-duration:6s; animation-delay:2s; }
.s5{ left:85%; animation-duration:4.5s; animation-delay:1.5s; }
.s6{ left:20%; animation-duration:5.5s; animation-delay:3s; }
.s7{ left:60%; animation-duration:4s; animation-delay:0.2s; }
.s8{ left:90%; animation-duration:6.5s; animation-delay:2.5s; }

/* DANCING ANGELS */
.angel{
  position:fixed; font-size:42px; z-index:1; animation: dance 2s ease-in-out infinite;
}
@keyframes dance{
  0%,100%{ transform: translateY(0) rotate(-10deg); }
  50%{ transform: translateY(-20px) rotate(10deg) scale(1.1); }
}
.a1{ top:12%; left:5%; }
.a2{ top:18%; right:5%; animation-delay:0.5s; }
.a3{ top:65%; left:3%; animation-delay:1s; }
.a4{ top:70%; right:3%; animation-delay:0.3s; }
.a5{ top:45%; left:2%; animation-delay:1.5s; font-size:32px; }
.a6{ top:50%; right:2%; animation-delay:0.8s; font-size:32px; }

.main{ position:relative; z-index:10; }
.star-big{ font-size:90px; animation: dance 2s ease-in-out infinite; display:block; }
h1{ color:#fff; text-shadow: 0 0 15px #ff00ff, 0 0 25px gold; font-size:36px; margin:5px; }
h3{ color:#fff; text-shadow: 0 2px 10px #ff00ff; margin:2px; }
#chat{
  background:rgba(255,255,255,0.92); border:3px solid #ff9a9e; border-radius:18px;
  padding:12px; height:320px; overflow-y:auto; text-align:left; color:#333;
  box-shadow: 0 0 20px rgba(255,255,255,0.9);
}
input{ padding:13px; width:62%; border-radius:15px; border:2px solid #ff9a9e; margin-top:10px; background:white; }
button{ background:linear-gradient(45deg,#ff00ff,#ffcc00); color:white; padding:13px 18px; border:none; border-radius:15px; font-weight:bold; box-shadow:0 4px 10px rgba(0,0,0,0.2); }
img{ width:100%; border-radius:15px; margin-top:8px; border:2px solid #ffc0ff; }
.small{ font-size:12px; color:#fff; background:rgba(0,0,0,0.25); padding:6px; border-radius:10px; display:inline-block; }
</style>
</head>
<body>

<div class="cloud cloud1"></div>
<div class="cloud cloud2"></div>
<div class="cloud cloud3"></div>

<div class="star-fall s1">⭐</div>
<div class="star-fall s2">🌟</div>
<div class="star-fall s3">✨</div>
<div class="star-fall s4">⭐</div>
<div class="star-fall s5">🌟</div>
<div class="star-fall s6">✨</div>
<div class="star-fall s7">⭐</div>
<div class="star-fall s8">🌟</div>

<div class="angel a1">👼</div>
<div class="angel a2">👼</div>
<div class="angel a3">😇</div>
<div class="angel a4">😇</div>
<div class="angel a5">👼</div>
<div class="angel a6">😇</div>

<div class="main">
<div class="star-big">🌟</div>
<h1>EMMY-AI</h1>
<h3>👼 HEAVEN MODE - BOSS ONLINE 👼</h3>
<p class="small">Type: hi | photo of a lion | edit: make it red</p>
<div id="chat"><p><b>EMMY-AI:</b> Hi Boss 🌟 Welcome to Heaven! ☁️🌈 I fit chat, generate photo, and edit photo! Try: photo of a lion wearing crown</p></div>
<input id="msg" placeholder="Type here Boss...">
<button onclick="send()">SEND 🌟</button>
</div>

<script>
let lastPhoto = "";
function send(){
  let m=document.getElementById('msg').value;
  if(!m) return;
  let c=document.getElementById('chat');
  let low=m.toLowerCase();
  c.innerHTML+='<p><b>You:</b> '+m+'</p>';

  if((low.includes('edit') || low.includes('make it') || low.includes('change it')) && lastPhoto){
    let editPrompt = lastPhoto + " , " + m;
    c.innerHTML+='<p><b>EMMY-AI:</b> Boss, I dey edit am now in heaven... 🌟👼</p><img src="https://image.pollinations.ai/prompt/'+encodeURIComponent(editPrompt)+'">';
    lastPhoto = editPrompt;
    document.getElementById('msg').value='';
    c.scrollTop=c.scrollHeight;
    return;
  }

  if(low.includes('photo') || low.includes('generate') || low.includes('draw') || low.includes('picture') || low.includes('image')){
    let prompt = m.replace(/photo of/gi,'').replace(/generate/gi,'').replace(/draw/gi,'').replace(/picture of/gi,'').replace(/image of/gi,'').replace(/photo/gi,'');
    if(!prompt.trim()) prompt = "beautiful angel in heaven clouds rainbow";
    lastPhoto = prompt;
    c.innerHTML+='<p><b>EMMY-AI:</b> Boss, I dey draw: '+prompt+' ... 🌟</p><img src="https://image.pollinations.ai/prompt/'+encodeURIComponent(prompt)+'">';
    document.getElementById('msg').value='';
    c.scrollTop=c.scrollHeight;
    return;
  }

  let reply='Boss, I hear you! You say: '+m;
  if(low.includes('hi')||low.includes('hello')) reply='Hi Boss! Welcome to Heaven 👼🌈 How I fit help you?';
  if(low.includes('who are you')||low.includes('your name')||low.includes('what is your name')) reply='My name na EMMY-AI 🌟 Your star AI from heaven, built by you Boss!';
  if(low.includes('love')) reply='Boss I love you too ❤️ You be the best in heaven and earth!';
  if(low.includes('how are you')) reply='I dey fine Boss, I dey dance with angels for heaven because you dey here 🌟👼';
  if(low.includes('thank')) reply='You welcome Boss 👑 Na my work to make you happy!';
  if(low.includes('heaven')||low.includes('beautiful')||low.includes('background')) reply='Yes Boss! This na heaven background you ask for - clouds, rainbow, falling stars, dancing angels! 🌈☁️👼🌟 You like am?';
  c.innerHTML+='<p><b>EMMY-AI:</b> '+reply+'</p>';
  document.getElementById('msg').value='';
  c.scrollTop=c.scrollHeight;
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    port=int(os.environ.get("PORT",8080))
    app.run(host="0.0.0.0",port=port)
