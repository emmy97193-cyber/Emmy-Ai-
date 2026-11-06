import os, random, requests
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
TOKEN = os.getenv("THREADS_ACCESS_TOKEN")
UID = os.getenv("THREADS_USER_ID")
URL = "https://graph.threads.net/v1.0"

MORNING = [
"Good morning ☀️ New day, new grace.",
"Good morning ✨ Stay kind, stay focused.",
"Good morning 💛 Today, choose peace."
]
NIGHT = [
"Good night 🌙 Rest well, dream sweet.",
"Good night 💛 You are loved, sleep well.",
"Good night ✨ Peaceful heart, cozy night."
]
DAY = [
"Luxury is how you carry yourself 👑",
"Stay calm, stay classy, stay focused.",
"True wealth is a grateful heart ❤️"
]

def post(text):
    try:
        r = requests.post(f"{URL}/{UID}/threads",
        data={"media_type":"TEXT","text":text,"access_token":TOKEN})
        cid = r.json().get("id")
        if not cid:
            print("FAIL", r.json()); return False
        p = requests.post(f"{URL}/{UID}/threads_publish",
        data={"creation_id":cid,"access_token":TOKEN})
        print("POSTED", p.json()); return True
    except Exception as e:
        print("ERR", e); return False

def m_job(): post(random.choice(MORNING))
def n_job(): post(random.choice(NIGHT))
def d_job(): post(random.choice(DAY))

s = BackgroundScheduler(timezone="Africa/Lagos")
s.add_job(m_job, 'cron', hour=7)
s.add_job(d_job, 'cron', hour=13)
s.add_job(d_job, 'cron', hour=18)
s.add_job(n_job, 'cron', hour=22)
s.start()

@app.route("/")
def home():
    return jsonify({"status":"live","mode":"luxury"})

@app.route("/post-now")
def now():
    return jsonify({"status":"posted" if d_job() or True else "failed"})

@app.route("/morning-now")
def mnow():
    m_job(); return jsonify({"status":"morning posted"})

@app.route("/night-now")
def nnow():
    n_job(); return jsonify({"status":"night posted"})

@app.route("/health")
def health():
    return jsonify({"status":"active"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT",8080)))
