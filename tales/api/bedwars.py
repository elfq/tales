import requests
from .api_key import api

class bedwars:

    def wins(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["bedwars_wins"]

    def beds(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["bedwars_beds"]

    def level(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["bedwars_level"]

    def kills(username):
        r = requests.get(f"https://api.hypixel.net/player?key={api.key}&name={username}")
        return r.json()["player"]["achievements"]["bedwars_bedwars_killer"]