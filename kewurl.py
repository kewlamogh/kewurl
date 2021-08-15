from flask import Flask, redirect, render_template
from replit import db
burl = "kewurl";
try:
  db["n"]
except:
  db["n"] = 0
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

@app.route("/docs")
def docs():
  return render_template("docs/docs.html")
app.run(host='0.0.0.0', port=8080)
