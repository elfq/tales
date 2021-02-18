from requests import get
from .errors import InvalidAPIKey

class api:
  """
  Used to store the API key.
  """

  def key(api_key):
    """
    api.key
    """
    r = get(f"https://api.hypixel.net/player?key={api_key}")

    
    