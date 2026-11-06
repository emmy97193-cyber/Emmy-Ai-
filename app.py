import os
import time
import requests
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

ACCESS_TOKEN = os.getenv("THREADS_ACCESS_TOKEN")
USER_ID = os.getenv("THREADS_USER_ID")
GRAPH_URL = "https://graph.threads.net/v1.0"

# Your content bank - add as many as you want
POST_BANK = [
    "Good evening from my world ✨ Stay warm, stay kind, stay focused.",
    "Luxury is not what you wear, it's how you carry yourself.",
    "Cozy nights, good conversations, and a grateful heart. 💛",
    "New chapter. Same values. Bigger vision.",
]

post_index = 0

def create_and_publish_post(text):
    """Create a Threads container, then publish it"""
    # 1. Create container
    create_res = requests.post(
        f"{GRAPH_URL}/{USER_ID}/threads",
        data={
            "media_type": "TEXT",
            "text": text,
            "access_token": ACCESS_TOKEN
        }
    )
    data = create_res.json()
    if "id" not in data:
        print("Create failed:", data)
        return False

    container_id = data["id"]

    # 2. Publish container
    publish_res = requests.post(
        f"{GRAPH_URL}/{USER_ID}/threads_publish",
        data={
            "creation_id": container_id,
            "access_token": ACCESS_TOKEN
        }
    )
    print("Published:", publish_res.json())
    return True

def auto_post_job():
    global post_index
    text = POST_BANK[post_index % len(POST_BANK)]
    print(f"Auto posting: {text}")
    create_and_publish_post(text)
    post_index += 1

def keep_alive_job():
    """Ping Threads to keep account active"""
    res = requests.get(
        f"{GRAPH_URL}/{USER_ID}",
        params={"fields": "id,username", "access_token": ACCESS_TOKEN}
    )
    print("Keep-alive check:", res.status_code, res.json())

scheduler = BackgroundScheduler()
# Post every 6 hours - change this to what you want
scheduler.add_job(auto_post_job, 'interval', hours=6)
# Check account every 30 mins to keep it live
scheduler.add_job(keep_alive_job, 'interval', minutes=30)
scheduler.start()

@app.route("/")
def home():
    return jsonify({"status": "live", "message": "Threads Bot is running on Railway 🚀"})

@app.route("/post-now")
def post_now():
    auto_post_job()
    return jsonify({"status": "posted"})

@app.route("/health")
def health():
    return jsonify({"status": "active"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
