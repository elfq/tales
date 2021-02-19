from requests import get
from .auth import api


class watchdog:
  """
  Watchdog endpoint.
  """

  def last_minute():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      return r.json()["watchdog_lastMinute"]

  def staff_bans_daily():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      return r.json()["staff_rollingDaily"]

  def total_bans():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      return r.json()["watchdog_total"]

  def watchdog_bans_daily():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      return r.json()["watchdog_rollingDaily"]

  def staff_total_bans():
      r = get(f"https://api.hypixel.net/watchdogstats?key={api.watchdog}")
      return r.json()["staff_total"]

  