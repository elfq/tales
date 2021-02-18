from requests import get
from .auth import api

class skywars:
  """
  Stat tracking for the Skywars minigame.
  """

  def team_kits(username):
      """
      skywars.team_kits
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kits_team"]
  
  def solo_kits(username):
      """
      skywars.solo_kits
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kits_solo"]
  
  def mega_kits(username):
      """
      skywars.mega_kits
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kits_mega"]


  def solo_kills(username):
      """
      skywars.kills_solo
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kills_solo"]

  def team_kills(username):
      """
      skywars.team_kills
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kills_team"]

  def mega_kills(username):
      """
      skywars.mega_kills
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kills_mega"]

  def team_wins(username):
      """
      skywars.team_wins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_wins_team"]

  def solo_wins(username):
      """
      skywars.solo_wins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_wins_solo"]
  
  def mega_wins(username):
      """
      skywars.mega_wins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_wins_mega"]

  def cages(username):
      """
      skywars.cages
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_cages"]

  def heads(username):
      """
      skywars.heads
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_heads"]