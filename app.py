
from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

BRAND = "EMMY AI ⭐️"
NICHE = "AI glasses, accessibility, futuristic technology"

def create_plan(topic):
    topic = (topic or "AI glasses")[:180]

    return {
        "brand": BRAND,
        "topic": topic,
        "video_ideas": [
            f"Before and after: {topic}",
            f"3 things people should know about {topic}",
            f"How {topic} can help people in everyday life"
        ],
        "hook": f"Wait! Have you seen what AI can do with {topic}?",
        "caption": (
            f"Welcome to {BRAND}! 🚀 Discover {topic}. "
            "Follow for more AI innovation and accessibility content."
        ),
        "hashtags": [
            "#EmmyAI", "#AIGlasses", "#ArtificialIntelligence",
            "#Accessibility", "#TechTok"
        ],
        "call_to_action": "Follow for more. Share with a friend!",
        "posting_tip": (
            "Use a strong opening in the first 2 seconds. "
            "Add clear subtitles and show the result quickly."
        )
    }

@app.get("/")
def home():
    return jsonify({
        "app": "EMMY AI Growth Booster",
        "status": "online",
        "features": [
            "Video ideas",
            "Captions and hashtags",
            "Content planning"
        ],
        "generate_endpoint": "/ideas?topic=AI%20glasses"
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.get("/ideas")
def ideas():
    topic = request.args.get("topic", "AI glasses")
    return jsonify(create_plan(topic))

@app.get("/plan")
def plan():
    return jsonify({
        "date_utc": datetime.now(timezone.utc).date().isoformat(),
        "morning": create_plan("AI glasses demonstration"),
        "afternoon": create_plan("Accessibility technology"),
        "evening": create_plan("Behind the scenes of EMMY AI")
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
