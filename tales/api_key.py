import requests

class api:

  def key(api_key):
    r = requests.get(f"https://api.hypixel.net/player?key={api_key}")
    