from requests import get
from .auth import api

class skyblock:
  """
  Stat tracking for Skyblock.
  """

  def combat(username):
      """
      skyblock.combat
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_combat"]

  def minion_lover(username):
      """
      skyblock.minion_lover
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_minion_lover"]

  def excavator(username):
      """
      skyblock.excavator
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock.excavator"]

  def gatherer(username):
      """
      skyblock.gatherer
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_gatherer"]

  def angler(username):
      """
      skyblock.angler
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_angler"]

  def harvester(username):
      """
      skyblock.harvester
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_harvester"]

  def treasury(username):
      """
      skyblock.treasury
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_treasury"]

  def concoctor(username):
      """
      skyblock.concoctor
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_concoctor"]

  def augmentation(username):
      """
      skyblock.augmentation
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_augmentation"]

  def gifts(username):
      """
      skyblock.gifts
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_unique_gifts"]

  def domesticator(username):
      """
      skyblock.domesticator
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_domesticator"]

  def slayer(username):
      """
      skyblock.slayer
      """
      r = get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
      return r.json()["player"]["achievements"]["skyblock_slayer"]