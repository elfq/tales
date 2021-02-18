import requests
from .auth import api

class blitz:
  """
  Stat tracking for the Blitz minigame.
  """

  def wins(username):
      """
      :blitz.wins: Track wins amounts.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_wins"]

  def kills(username):
      """
      :blitz.kills: Track kill amount.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_kills"]

  def coins(username):
      """
      :blitz.coins: Track coins amounts.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_coins"]