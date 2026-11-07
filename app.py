from flask import Flask
import os
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html>
<head><title>EMMY-AI</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:black;color:gold;text-align:center;font-family:sans-serif;padding:15px}
.star{font-size:90px}
#chat{background:#111;border:1px solid gold;border-radius:12px;padding:10px;height:280px;overflow-y:auto;text-align:left}
input{padding:13px;width:62%;border-radius:10px;border:none;margin-top:10px}
button{background:gold;color:black;padding:13px 18px;border:none;border-radius:10px;font-weight:bold}
</style>
</head>
<body>
<div class="star">🌟.🪄</div>
<h1>EMMY-AI</h1>
<h3>BOSS MODE - ONLINE</h3>
<div id="chat"><p><b>EMMY-AI:</b> Hi Boss, I be star now 🌟 Ask me anything!</p></div>
<input id="msg" placeholder="Type here Boss...">
<button onclick="send()">SEND</button>
<script>
function send(){
  let m=document.getElementById('msg').value;
  if(!m) return;
  let c=document.getElementById('chat');
  c.innerHTML+='<p><b>You:</b> '+m+'</p>';
  let low=m.toLowerCase();
  let reply='Boss, I hear you! You say: '+m;
  if(low.includes('hi')||low.includes('hello')) reply='Hi Boss! Welcome back 👑 How I fit help you?';
  if(low.includes('who are you')) reply='I be EMMY-AI, your star AI 🌟 Built by you Boss!';
  if(low.includes('love')) reply='Boss I love you too ❤️ You be the best!';
  if(low.includes('how are you')) reply='I dey fine Boss, because you dey here 🌟';
  c.innerHTML+='<p><b>EMMY-AI:</b> '+reply+'</p>';
  document.getElementById('msg').value='';
  c.scrollTop=c.scrollHeight;
}
</script>
</body>
</html>
</magic>
"""
@app.route("/")
def home((..)):
    return HTML
if __name__ == "__main__":
    port=int(os.environ.get("PORT",8080))
    app.run(host="0.0.0.0",port=port)
