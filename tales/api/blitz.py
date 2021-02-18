import requests
from .api_key import api

class blitz:

    def wins(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["blitz_wins"]

    def kills(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["blitz_kills"]

    def coins(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["blitz_coins"]