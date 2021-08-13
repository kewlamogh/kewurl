from flask import Flask, redirect, render_template
from replit import db
try:
  db["n"]
except:
  db["n"] = 0
app = Flask('app', template_folder = "t")
@app.route("/<l>") 
def re(l):
  try:
    db[str(l)]
    return redirect(db[str(l)])
  except:
    return render_template("404.html")

@app.route("/new/<link>")
def n(link):
  db["n"] += 1;
  db[str(db["n"])] = "https://"+link.replace("_", "/");
  return render_template("success.html", url = f"https://q.amoghthecool.repl.co/{db['n']}")

@app.route("/")
def h():
  return render_template("render.html")

app.run(host='0.0.0.0', port=8080)
