import requests
from .auth import api

class bedwars:
  """
  Stat tracking for the Bedwars Minigame.
  """

  def wins(username):
      """
      :bedwars.wins: Track wins amounts.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_wins"]

  def beds(username):
      """
      :bedwars.beds: Track amount of beds destroyed.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_beds"]

  def level(username):
      """
      :bedwars.level: Track level.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_level"]

  def kills(username):
      """
      :blitz.kills: Track kills amounts.
      """
      r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_bedwars_killer"]