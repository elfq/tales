import requests

class api:
  """
  Used to store the API key.

  """

  def key(api_key):
    """
    ":api.key: Used to access the API."
    """
    r = requests.get(f"https://api.hypixel.net/player?key={api_key}")
    