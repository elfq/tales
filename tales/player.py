from requests import get
from .auth import api
from .errors import FalseSuccessError

class player:
  """
  Player endpoint.
  """
  
  def overall_coins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["general_coins"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def overall_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["general_overall_wins"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def quests_finished(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["general_quest_master"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def blitz_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["blitz_wins"]

  def blitz_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["blitz_kills"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def blitz_coins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["blitz_coins"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def blitz_team_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["blitz_wins_team"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")
  
  def combat(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_combat"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def minion_lover(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_minion_lover"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_excavator(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_excavator"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_gatherer(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_gatherer"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_angler(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_angler"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_harvester(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_harvester"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_treasury(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_treasury"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_concoctor(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_concoctor"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_augmentation(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_augmentation"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_gifts(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_gifts"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_domesticator(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_domesticator"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skyblock_slayer(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skyblock_slayer"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")
  
  def skywars_team_kits(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_kits_team"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")
  
  def skywars_solo_kits(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_kits_solo"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")
  
  def skywars_mega_kits(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_kits_mega"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_solo_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_kills_solo"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_team_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_kills_team"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_mega_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_kills_mega"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_team_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_wins_team"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_solo_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_wins_solo"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")
  
  def skywars_mega_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_wins_mega"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_cages(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_cages"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def skywars_heads(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["skywars_head"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def bedwars_wins(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["bedwars_wins"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def bedwars_beds(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["bedwars_beds"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def bedwars_level(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["bedwars_level"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")

  def bedwars_kills(username):
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      if r.json()["success"] == "true":
       return r.json()["player"]["achievements"]["bedwars_kills"]
      else: 
        raise FalseSuccessError("Oops! An error occured, this is possibly due to an invalid username/API key.")
