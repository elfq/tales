from requests import get
from .auth import api

class player:
  """
  General stat tracking.
  """
  
  def overall_coins(username):
      """
      player.overall_coins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["general_coins"]

  def overall_wins(username):
      """
      player.overall_wins
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["general_wins"]

  def quests_finished(username):
      """
      player.quests_finished
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["general_quest_master"]

  