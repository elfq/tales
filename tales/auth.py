from requests import get

class api:
  """
  Used to store the API key.
  """

  def key(api_key):
    get(f"https://api.hypixel.net/player?key={api_key}")

  def watchdog(api_key):
    get(f"https://api.hypixel.net/watchdogstats?key={api_key}")

    
    