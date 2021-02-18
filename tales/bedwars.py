import requests
from .auth import api

class bedwars:
  """
  Stat tracking for the Bedwars Minigame.
  """

  def wins(username):
      """
      bedwars.wins
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_wins"]

  def beds(username):
      """
      bedwars.beds
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_beds"]

  def level(username):
      """
      bedwars.level
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_level"]

  def kills(username):
      """
      blitz.kills
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_bedwars_killer"]
