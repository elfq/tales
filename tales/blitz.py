from requests import get
from .auth import api

class blitz:
  """
  Stat tracking for the Blitz minigame.
  """
  
  def wins(username):
      """
      blitz.wins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_wins"]

  def kills(username):
      """
      blitz.kills
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_kills"]

  def coins(username):
      """
      blitz.coins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_coins"]

  def team_wins(username):
      """
      blitz.team_wins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_wins_teams"]