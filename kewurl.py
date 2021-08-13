from flask import Flask, redirect 
from replit import db  
try:
  db["n"]
except:
  db["n"] = 0
app = Flask('app')
@app.route("/<l>") 
def re(l):
  return redirect(db[str(l)])

@app.route("/new/<link>")
def n(link):
  db["n"] += 1
  db[str(db["n"])] = "https://"+link
  return f"Your shortened url is https://kewl.amoghthecool.repl.co/{db['n']}"

app.run(host='0.0.0.0', port=8080)
