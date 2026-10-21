import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- HTML CHAT UI ---
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Emmy AI - CEO MODE</title>
<style>
body{margin:0;font-family:Arial;background:#0f0f0f;color:white;display:flex;flex-direction:column;height:100vh}
header{padding:15px;background:#1a1a1a;text-align:center;border-bottom:2px solid #6d28d9;font-weight:bold;font-size:18px}
#chat{flex:1;overflow-y:auto;padding:15px;display:flex;flex-direction:column;gap:12px}
.msg{padding:12px 15px;border-radius:15px;max-width:80%;line-height:1.4}
.user{background:#6d28d9;align-self:flex-end;border-bottom-right-radius:2px}
.ai{background:#1f1f1f;align-self:flex-start;border-bottom-left-radius:2px;border:1px solid #333}
#inputArea{display:flex;padding:12px;background:#1a1a1a;gap:10px}
input{flex:1;padding:12px;border-radius:25px;border:none;outline:none;background:#2a2a2a;color:white}
button{padding:12px 20px;border-radius:25px;border:none;background:#6d28d9;color:white;font-weight:bold}
</style>
</head>
<body>
<header>👑 EMMY AI - CEO MODE ONLINE 24/7</header>
<div id="chat">
<div class="msg ai">Hello Boss! I'm Emmy AI 🚀<br>Your site is now ONLINE 24/7! How can I help you today?</div>
</div>
<div id="inputArea">
<input id="text" placeholder="Ask Emmy AI anything..." onkeypress="if(event.key==='Enter')send()">
<button onclick="send()">Send</button>
</div>
<script>
async function send(){
 let input=document.getElementById('text');
 let txt=input.value.trim();
 if(!txt)return;
 let chat=document.getElementById('chat');
 chat.innerHTML+=`<div class="msg user">${txt}</div>`;
 input.value='';
 chat.scrollTop=chat.scrollHeight;
 let res=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:txt})});
 let data=await res.json();
 chat.innerHTML+=`<div class="msg ai">${data.reply}</div>`;
 chat.scrollTop=chat.scrollHeight;
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()
    
    # Simple CEO Brain — you can connect real AI later
    if "hello" in user_msg or "hi" in user_msg:
        reply = "Hello CEO! 👑 Ready to build empire today?"
    elif "how are you" in user_msg:
        reply = "I'm ONLINE 24/7 and Active on Railway! Thanks to your cron-job! 🔥"
    elif "who are you" in user_msg:
        reply = "I'm Emmy AI — Your personal CEO Assistant built by YOU!"
    elif "railway" in user_msg:
        reply = "Railway is Active ✅ Gunicorn 23.0.0 listening on 0.0.0.0:8080 — No more crash!"
    elif "cron" in user_msg:
        reply = "Cron-job 'Emmy Ai Keep Alive' is pinging every 15 mins to keep us awake 24/7!"
    else:
        reply = f"CEO, you said: '{user_msg}' — I'm learning! Soon we'll connect me to real AI (OpenAI API). For now, I'm your 24/7 online assistant! 🚀"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
