from flask import Flask, redirect, render_template
from replit import db
burl = "kewurl";
try:
  db["n"]
except:
  db["n"] = 0

try:
  db["posts"]
except:
  db["posts"] = []
import rickroller_forum

app = Flask('app', template_folder = "t")
@app.route("/<l>") 
def re(l):
  try:
    db[str(l)]
    return render_template("redir.html", lol = db[str(l)])
  except:
    return render_template("404.html")

@app.route("/new/<link>")
def n(link):
  db["n"] += 1;
  db[str(db["n"])] = "https://"+link.replace("_", "/");
  return render_template("success.html", url = f"https://{burl}.amoghthecool.repl.co/{db['n']}")

@app.route("/")
def h():
  return render_template("render.html")

@app.route("/post/<post_content>")
def post(post_content):
  rickroller_forum.send_message(post_content)
  return redirect("/forum")

@app.route("/get_posts")
def get():
  return render_template("all_posts.html", posts = rickroller_forum.get_posts())

@app.route("/docs")
def docs():
  return render_template("docs/docs.html")

@app.route("/forum")
def forum():
  return render_template("forum.html")

app.run(host='0.0.0.0', port=8080)
