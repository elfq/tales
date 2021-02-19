from requests import get
from .auth import api

class player:
  """
  Player endpoint.
  """
  
  def overall_coins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["general_coins"]

  def overall_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["general_wins"]

  def quests_finished(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["general_quest_master"]

  def blitz_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_wins"]

  def blitz_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_kills"]

  def blitz_coins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_coins"]

  def blitz_team_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_wins_teams"]
  
  def combat(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_combat"]

  def minion_lover(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_minion_lover"]

  def skyblock_excavator(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock.excavator"]

  def skyblock_gatherer(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_gatherer"]

  def skyblock_angler(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_angler"]

  def skyblock_harvester(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_harvester"]

  def skyblock_treasury(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_treasury"]

  def skyblock_concoctor(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_concoctor"]

  def skyblock_augmentation(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_augmentation"]

  def skyblock_gifts(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_unique_gifts"]

  def skyblock_domesticator(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_domesticator"]

  def skyblock_slayer(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_slayer"]
  
  def skywars_team_kits(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kits_team"]
  
  def skywars_solo_kits(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kits_solo"]
  
  def skywars_mega_kits(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kits_mega"]

  def skywars_solo_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kills_solo"]

  def skywars_team_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kills_team"]

  def skywars_mega_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_kills_mega"]

  def skywars_team_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_wins_team"]

  def skywars_solo_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_wins_solo"]
  
  def skywars_mega_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_wins_mega"]

  def skywars_skywars_cages(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_cages"]

  def skywars_heads(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skywars_heads"]

  def bedwars_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_wins"]

  def bedwars_beds(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_beds"]

  def bedwars_level(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_level"]

  def bedwars_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["bedwars_bedwars_killer"]

  