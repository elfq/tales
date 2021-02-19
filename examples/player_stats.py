from tales import player, api

api.key = "" # Your API key
username = "Technoblade"

print(f"All coins: {player.overall_coins(username)}\nAll wins: {player.overall_wins(username)}\nAll kills: {player.overall_kills(username)}")