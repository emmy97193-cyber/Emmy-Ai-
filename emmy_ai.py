import openai
import requests
from datetime import datetime

# CONFIG - put your keys here
OPENAI_KEY = "sk-..."
IG_ACCESS_TOKEN = "YOUR_IG_LONG_LIVED_TOKEN"
IG_USER_ID = "YOUR_IG_USER_ID"
BUFFER_TOKEN = "YOUR_BUFFER_TOKEN"

client = openai.OpenAI(api_key=OPENAI_KEY)

EMMY_PROMPT = """
You are emmy Ai ⭐️. Voice: calm, confident, mystical, Naija boss energy.
Closed smile, no teeth. Never loud. Short sentences.
Write Instagram caption: 2-3 lines max + 5 hashtags for this idea: {idea}
Include 'emmy Ai ⭐️' vibe.
"""

def generate_caption(idea):
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": EMMY_PROMPT.format(idea=idea)}]
    )
    return res.choices[0].message.content

def queue_to_buffer(caption, image_url):
    url = "https://api.bufferapp.com/1/updates/create.json"
    data = {
        "access_token": BUFFER_TOKEN,
        "profile_ids[]": "YOUR_IG_PROFILE_ID",
        "text": caption,
        "media[photo]": image_url
    }
    r = requests.post(url, data=data)
    print("Queued for approval:", r.json())
    return r.json()

# EXAMPLE USE
if __name__ == "__main__":
    idea = "The forest eye is watching, AI is not coming, it's already here"
    caption = generate_caption(idea)
    print(caption)
