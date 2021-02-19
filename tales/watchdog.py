from requests import get
from .auth import api


class watchdog:
  """
  Watchdog endpoint.
  """

  def last_minute():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      if r.json()["success"] == "true":
       return r.json()["watchdog_lastMinute"]
      else: 
        raise FalseSuccessError(r.json()["cause"])

  def staff_bans_daily():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      if r.json()["success"] == "true":
       return r.json()["staff_rollingDaily"]
      else: 
        raise FalseSuccessError(r.json()["cause"])

  def total_bans():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      if r.json()["success"] == "true":
       return r.json()["watchdog_total"]
      else: 
        raise FalseSuccessError(r.json()["cause"])

  def watchdog_bans_daily():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      if r.json()["success"] == "true":
       return r.json()["watchdog_rollingDaily"]
      else: 
        raise FalseSuccessError(r.json()["cause"])

  def staff_total_bans():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      if r.json()["success"] == "true":
       return r.json()["staff_total"]
      else: 
        raise FalseSuccessError(r.json()["cause"])

  