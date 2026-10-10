from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class AppInfo(BaseModel):
    name: str
    permissions: List[str]

class DeviceData(BaseModel):
    battery: int
    storage_free_percent: int
    apps: List[AppInfo]

@app.get("/")
def home():
    return {"status": "EmmyGuard AI Online"}

@app.post("/analyze")
def analyze(data: DeviceData):
    fitness = int(data.battery * 0.5 + data.storage_free_percent * 0.5)

    risky = []
    for app in data.apps:
        p = " ".join(app.permissions)
        score = 0
        reason = ""
        if "READ_SMS" in p and "SEND_SMS" in p:
            score = 95; reason = "Can read & send SMS - Banking fraud risk"
        elif "ACCESS_FINE_LOCATION" in p and len(app.permissions) > 10:
            score = 75; reason = f"Location + {len(app.permissions)} perms - Over-privileged"
        elif len(app.permissions) > 15:
            score = 60; reason = f"Requests {len(app.permissions)} permissions"

        if score > 0:
            risky.append({"app": app.name, "score": score, "reason": reason})

    status = "Good" if fitness > 75 else "Warning" if fitness > 45 else "Critical"

    return {
        "fitness_score": fitness,
        "status": status,
        "risky_count": len(risky),
        "risky_apps": risky[:10], # top 10
        "advice": f"Your device health is {fitness}/100 ({status}). {len(risky)} apps need attention."
  }
