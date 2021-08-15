from replit import db
def send_message(mContent):
  db["posts"].append(mContent.replace("_", "/"))

def get_posts():
  return db["posts"]