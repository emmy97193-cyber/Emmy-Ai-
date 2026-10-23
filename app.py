from flask import Flask, render_template_string, request, redirect, session, jsonify, Response
import os, sqlite3, csv, io, secrets, datetime
from urllib.parse import urlencode
import requests

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "emmy-secret-123")
DB = "emmy.db"
PASSWORD = os.getenv("DASHBOARD_PASSWORD", "EmmyBoss2026")
TIKTOK_KEY = os.getenv("TIKTOK_CLIENT_KEY")
TIKTOK_SECRET = os.getenv("TIKTOK_CLIENT_SECRET")
PUBLIC_URL = os.getenv("PUBLIC_BASE_URL", "").rstrip("/")

def get_db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    c = get_db()
    c.execute("CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, url TEXT, views INTEGER DEFAULT 0, likes INTEGER DEFAULT 0, comments INTEGER DEFAULT 0, shares INTEGER DEFAULT 0, hook TEXT, caption TEXT, created_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS ideas (id INTEGER PRIMARY KEY AUTOINCREMENT, hook TEXT, caption TEXT, tags TEXT)")
    cur = c.execute("SELECT COUNT(*) FROM ideas")
    if cur.fetchone()[0]==0:
        seeds = [
            ("POV: Built AI CEO from wheelchair at 3AM","Built Emmy AI from phone in Laredo. Day 1 to 10M views.","#LaredoTX #WheelchairCEO #AI"),
            ("My site is ONLINE 24/7 from phone","Railway + GitHub = CEO MODE. Tutorial coming.","#Railway #Python #Laredo"),
            ("I track what makes videos viral","Views, likes, shares, engagement rate - real data.","#TikTokGrowth"),
            ("Fixing my follow ratio LIVE","2888 Following vs 1376 Followers - cleaning up.","#Laredo #Growth"),
            ("Laredo to world - CEO Mode","Webb County to worldwide. Emmy AI online.","#CEOmode #LaredoProud"),
        ]
        for h,cap,tag in seeds:
            c.execute("INSERT INTO ideas (hook,caption,tags) VALUES (?,?,?)",(h,cap,tag))
        c.commit()
    c.close()
init_db()

def need_login(f):
    from functools import wraps
    @wraps(f)
    def w(*a,**kw):
        if not session.get("ok"):
            return redirect("/login")
        return f(*a,**kw)
    return w

LAYOUT = """
<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EMMY AI Growth</title>
<style>
body{margin:0;background:#0a0614;color:#fff;font-family:system-ui;padding:16px}
a{color:#c084fc;text-decoration:none}
.card{background:rgba(255,255,255,0.06);border:1px solid #a855f7;border-radius:18px;padding:16px;margin:12px 0}
input{width:100%;padding:10px;border-radius:10px;border:1px solid #333;background:#151022;color:#fff;margin:6px 0}
button{padding:10px 16px;border-radius:20px;border:0;background:linear-gradient(90deg,#d4af37,#f5d78e);font-weight:700;color:#1a1033}
.btn2{background:transparent;border:1px solid #a855f7;color:#c084fc}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:8px;border-bottom:1px solid #222;text-align:left}
</style>
<div><b>EMMY AI</b> Growth Booster | <a href="/">Dashboard</a> | <a href="/ideas">Ideas</a> | <a href="/settings">Settings</a> | <a href="/export">CSV</a> | <a href="/logout">Logout</a></div><hr>
{{content|safe}}
"""

@app.route("/login", methods=["GET","POST"])
def login():
    m=""
    if request.method=="POST":
        if request.form.get("password")==PASSWORD:
            session["ok"]=True
            return redirect("/")
        m="Wrong password"
    return render_template_string(LAYOUT, content='<div class="card" style="max-width:360px;margin:60px auto"><h3>CEO Login</h3><form method="post"><input type="password" name="password" placeholder="Password"><button>Enter</button></form><p style="color:red">'+m+'</p></div>')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/")
@need_login
def dash():
    c=get_db()
    vids=c.execute("SELECT * FROM videos ORDER BY id DESC").fetchall()
    tv=sum(v["views"] for v in vids)
    tl=sum(v["likes"] for v in vids)
    av=round((tl+sum(v["comments"] for v in vids)+sum(v["shares"] for v in vids))/tv*100,2) if tv else 0
    c.close()
    rows=""
    for v in vids:
        eng=round((v["likes"]+v["comments"]+v["shares"])/v["views"]*100,2) if v["views"] else 0
        rows+="<tr><td>"+v["title"]+"</td><td>"+str(v["views"])+"</td><td>"+str(v["likes"])+"</td><td>"+str(v["comments"])+"</td><td>"+str(v["shares"])+"</td><td>"+str(eng)+"%</td></tr>"
    content=(
    '<div class="card"><b>Views:</b> '+str(tv)+' | <b>Likes:</b> '+str(tl)+' | <b>Avg Eng:</b> '+str(av)+'% | <b>Videos:</b> '+str(len(vids))+'</div>'
    '<div class="card"><h4>Add Performance</h4><form method="post" action="/add">'
    '<input name="title" placeholder="Title - Day1 CEO" required>'
    '<input name="url" placeholder="TikTok URL">'
    '<input name="views" type="number" placeholder="Views">'
    '<input name="likes" type="number" placeholder="Likes">'
    '<input name="comments" type="number" placeholder="Comments">'
    '<input name="shares" type="number" placeholder="Shares">'
    '<input name="hook" placeholder="Hook used">'
    '<input name="caption" placeholder="Caption">'
    '<button>Add</button></form></div>'
    '<div class="card"><table><tr><th>Title</th><th>Views</th><th>Likes</th><th>Com</th><th>Shares</th><th>Eng</th></tr>'+rows+'</table></div>'
    )
    return render_template_string(LAYOUT, content=content)

@app.route("/add", methods=["POST"])
@need_login
def add():
    c=get_db()
    c.execute("INSERT INTO videos (title,url,views,likes,comments,shares,hook,caption,created_at) VALUES (?,?,?,?,?,?,?,?,?)",
    (request.form.get("title"),request.form.get("url"),int(request.form.get("views")or 0),int(request.form.get("likes")or 0),int(request.form.get("comments")or 0),int(request.form.get("shares")or 0),request.form.get("hook"),request.form.get("caption"),datetime.datetime.utcnow().isoformat()))
    c.commit()
    c.close()
    return redirect("/")

@app.route("/ideas")
@need_login
def ideas():
    c=get_db()
    data=c.execute("SELECT * FROM ideas").fetchall()
    c.close()
    rows="".join(["<tr><td>"+i["hook"]+"</td><td>"+i["caption"]+"</td><td>"+i["tags"]+"</td></tr>" for i in data])
    return render_template_string(LAYOUT, content='<div class="card"><h3>Hooks & Captions</h3><table><tr><th>Hook</th><th>Caption</th><th>Tags</th></tr>'+rows+'</table></div>')

@app.route("/export")
@need_login
def export():
    c=get_db()
    vids=c.execute("SELECT * FROM videos").fetchall()
    c.close()
    out=io.StringIO()
    w=csv.writer(out)
    w.writerow(["title","views","likes","comments","shares","hook","caption"])
    for v in vids:
        w.writerow([v["title"],v["views"],v["likes"],v["comments"],v["shares"],v["hook"],v["caption"]])
    return Response(out.getvalue(), mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=emmy.csv"})

@app.route("/settings")
@need_login
def settings():
    stat=session.get("tiktok_user",{}).get("display_name","Not connected")
    base=PUBLIC_URL or request.host_url.rstrip("/")
    return render_template_string(LAYOUT, content='<div class="card"><h3>TikTok Official</h3><p>Display API: user.info.basic, video.list (needs approval)</p><p>Posting API: separate approval - no auto publish</p><p>Status: '+stat+'</p><p>Client Key: '+('Yes' if TIKTOK_KEY else 'No')+'</p><p>Redirect URI: '+base+'/auth/tiktok/callback</p><a href="/auth/tiktok"><button>Connect TikTok</button></a> <a href="/tiktok/profile"><button class="btn2">Profile</button></a> <a href="/tiktok/videos"><button class="btn2">Videos</button></a></div>')

@app.route("/auth/tiktok")
@need_login
def auth_tiktok():
    if not TIKTOK_KEY:
        return "Set TIKTOK_CLIENT_KEY in Railway first",400
    redir=PUBLIC_URL or request.host_url.rstrip("/") + "/auth/tiktok/callback"
    if "/auth" not in redir:
        redir=redir+"/auth/tiktok/callback"
    st=secrets.token_hex(16)
    session["st"]=st
    params={"client_key":TIKTOK_KEY,"scope":"user.info.basic,video.list","response_type":"code","redirect_uri":redir,"state":st}
    url="https://www.tiktok.com/v2/auth/authorize/?"+urlencode(params)
    return redirect(url)

@app.route("/auth/tiktok/callback")
@need_login
def cb():
    code=request.args.get("code")
    state=request.args.get("state")
    if state!=session.get("st"):
        return "Invalid state",400
    redir=PUBLIC_URL or request.host_url.rstrip("/") + "/auth/tiktok/callback"
    if "/auth" not in redir:
        redir=redir+"/auth/tiktok/callback"
    try:
        r=requests.post("https://open.tiktokapis.com/v2/oauth/token/", data={"client_key":TIKTOK_KEY,"client_secret":TIKTOK_SECRET,"code":code,"grant_type":"authorization_code","redirect_uri":redir}, headers={"Content-Type":"application/x-www-form-urlencoded"})
        data=r.json()
        session["tiktok_token"]=data
        tok=data.get("access_token")
        if tok:
            pr=requests.get("https://open.tiktokapis.com/v2/user/info/?fields=open_id,display_name,avatar_url", headers={"Authorization":"Bearer "+tok})
            if pr.ok:
                session["tiktok_user"]=pr.json().get("data",{}).get("user",{})
        return redirect("/settings")
    except Exception as e:
        return str(e),500

@app.route("/tiktok/profile")
@need_login
def tp():
    tok=session.get("tiktok_token",{}).get("access_token")
    if not tok:
        return jsonify(error="Not connected"),400
    r=requests.get("https://open.tiktokapis.com/v2/user/info/?fields=open_id,avatar_url,display_name,follower_count,likes_count,video_count", headers={"Authorization":"Bearer "+tok})
    return jsonify(r.json())

@app.route("/tiktok/videos")
@need_login
def tv():
    tok=session.get("tiktok_token",{}).get("access_token")
    if not tok:
        return jsonify(error="Not connected"),400
    r=requests.post("https://open.tiktokapis.com/v2/video/list/?fields=id,title,view_count,like_count,comment_count,share_count,create_time", headers={"Authorization":"Bearer "+tok,"Content-Type":"application/json"}, json={"max_count":20})
    return jsonify(r.json())

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT",8080)))
