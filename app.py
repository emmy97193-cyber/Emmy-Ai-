import os
import random
import requests
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz

app = Flask(__name__)

ACCESS_TOKEN = os.getenv("THREADS_ACCESS_TOKEN")
USER_ID = os.getenv("THREADS_USER_ID")
GRAPH_URL = "https://graph.threads.net/v1.0"

# --- LUXURY / ROMANTIC CONTENT BANK ---
MORNING_POSTS = [
    "Good morning ☀️ New day, new grace, new opportunities. Walk in luxury, speak with kindness, live with purpose.",
    "Good morning my people ✨ May today be soft, beautiful and full of blessings. Coffee first, then conquer the world.",
    "Rise and shine 💛 A gentleman's day starts with gratitude, good style, and a calm heart.",
    "Good morning 🌹 Life is beautiful when you choose peace over noise. Today, choose peace.",
    "Morning blessings to you. May your day be as warm as candlelight and as elegant as you are. ✨",
]

EVENING_POSTS = [
    "Good night 🌙 Rest well. Tomorrow is another chance to love better, dream bigger, and shine brighter.",
    "Evening vibes 🕯️ Cozy lights, calm heart, grateful soul. Thank you for being part of my journey.",
    "Good night my beautiful people 💛 May your dreams be sweet and your heart be at peace.",
    "As the night falls, I just want to say — you are loved, you are valued, you are enough. Sleep well. ✨",
    "Cozy night, warm heart. Luxury is not things, it's peace of mind. Good night. 🌙",
]

DAY_POSTS = [
    "Luxury is not what you wear, it's how you carry yourself. 👑",
    "A real man protects, provides, and loves with his whole heart. 💎",
    "Cozy nights, good conversations, and a grateful heart. That's true wealth. 🕯️",
    "Elegance never goes out of style. Kindness never goes unnoticed. ✨",
    "Stay calm. Stay classy. Stay focused. Your time is coming. 🙏",
    "Sunset reminds me — even endings can be beautiful. 🌅",
    "I believe in love that is soft, honest, and intentional. ❤️",
    "Good company, good wine, good music, good soul. That's my kind of evening. 🍷",
]

def create_and_publish_post(text):
    try:
        # 1. Create container
        create_res = requests.post(
            f"{GRAPH_URL}/{USER_ID}/threads",
            data={"media_type": "TEXT", "text": text, "access_token": ACCESS_TOKEN},
            timeout=30
        )
        data = create_res.json()
        if "id" not in data:
            print("Create failed:", data)
            return False
        container_id = data["id"]

        # 2. Publish
        publish_res = requests.post(
            f"{GRAPH_URL}/{USER_ID}/threads_publish",
            data={"creation_id": container_id, "access_token": ACCESS_TOKEN},
            timeout=30
        )
        print(f"[{datetime.now()}] Published:", publish_res.json())
        return True
    except Exception as e:
        print("Post error:", e)
        return False

def morning_job():
    text = random.choice(MORNING_POSTS)
    print("Morning post:", text)
    create_and_publish_post(text)

def evening_job():
    text = random.choice(EVENING_POSTS)
    print("Evening post:", text)
    create_and_publish_post(text)

def day_job():
    text = random.choice(DAY_POSTS)
    print("Day post:", text)
    create_and_publish_post(text)

def keep_alive_job():
    try:
        res = requests.get(
            f"{GRAPH_URL}/{USER_ID}",
            params={"fields": "id,username", "access_token": ACCESS_TOKEN},
            timeout=15
        )
        print("Keep-alive:", res.status_code)
    except Exception as e:
        print("Keep-alive error:", e)

# --- SCHEDULER - Nigeria Time (Africa/Lagos) ---
scheduler = BackgroundScheduler(timezone="Africa/Lagos")
scheduler.add_job(morning_job, 'cron', hour=7, minute=0)   # 7:00 AM Good Morning
scheduler.add_job(day_job, 'cron', hour=13, minute=0)      # 1:00 PM Luxury Post
scheduler.add_job(day_job, 'cron', hour=18, minute=0)      # 6:00 PM Luxury Post
scheduler.add_job(evening_job, 'cron', hour=22, minute=0) # 10:00 PM Good Night
scheduler.add_job(keep_alive_job, 'interval', minutes=30)
scheduler.start()

@app.route("/")
def home():
    return jsonify({"status": "live", "message": "Emmy-Ai Luxury Bot is running on Railway 🚀", "mode": "luxury-romantic"})

@app.route("/post-now")
def post_now():
    success = create_and_publish_post(random.choice(DAY_POSTS))
    return jsonify({"status": "posted" if success else "failed"})

@app.route("/morning-now")
def morning_now():
    morning_job()
    return jsonify({"status": "morning posted"})

@app.route("/night-now")
def night_now():
    evening_job()
    return jsonify({"status": "night posted"})

@app.route("/health")
def health():
    return jsonify({"status": "active", "time": str(datetime.now())})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
