import requests
import os

def getStatus():
  status_url = "https://api.mozambiquehe.re/servers?"
  authorization = {'auth':os.environ.get("APEX_KEY")}
  r = requests.get(url = status_url, params = authorization)
  return r.json()

#news_url = "https://api.mozambiquehe.re/news?lang=en-us"