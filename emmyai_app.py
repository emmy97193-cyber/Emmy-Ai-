from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('face_hud.html')

@app.route('/face')
def face():
    return render_template('face_hud.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
