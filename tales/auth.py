import requests

class api:
  """
  Used to store the API key.

  """

  def key(api_key):
    """
    api.key
    """
    r = requests.get(f"https://api.hypixel.net/player?key={api_key}")
    