![Logo](https://static1.textcraft.net/data1/e/3/e385d7775760dc99966075463c88b0f86167c55cda39a3ee5e6b4b0d3255bfef95601890afd80709da39a3ee5e6b4b0d3255bfef95601890afd80709ad0263e05752f8b663c78a8ec35fef42.png)

- **Docs**

https://elf.is-a.dev/docs

### What is Tales?

Tales is a new, easy to use hypixel API wrapper designed with python.

### Installation

```
python -m pip install -U git+https://github.com/elfq/tales
```
### Coverage

**Minigames**
- Blitz
- Bedwars
- Skywars
- Skyblock

**Network**
- Watchdog Info
- Player Info (all coins, kills, etc)

*more to come*

### Example

```py
from tales import player, api

api.key = "Your Hypixel API key"

wins = player.blitz_wins("Technoblade")
print(wins)
```
