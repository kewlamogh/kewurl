import os
for i in ["flask", "replit"]:
  os.system(f"pip install {i}")
from flask import Flask, redirect 
from replit import db  
app = Flask('app')
@app.route("/<l>") 
def re(l):
  return redirect(db[str(l)])

@app.route("/new/<link>")
def n(link):
  db["n"] += 1;
  db[str(db["n"])] = "https://"+link;
  return f"Your shortened url is https://t.amoghthecool.repl.co/{db['n']}"

app.run(host='0.0.0.0', port=8080)
