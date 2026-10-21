@app.get("/")
def root():
    return {"status": "Emmy-AI is live"}
    gunicorn main:app --bind 0.0.0.0:$PORT
