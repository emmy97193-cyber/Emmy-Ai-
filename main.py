@app.get("/")
def root():
    return {"status": "Emmy-AI is live"}
