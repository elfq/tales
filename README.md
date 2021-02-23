![Logo](https://static1.textcraft.net/data1/1/2/123e6b700e7371a68846bc668a61c4c85efab325da39a3ee5e6b4b0d3255bfef95601890afd80709da39a3ee5e6b4b0d3255bfef95601890afd8070905ead434cfff4e79270d97f5509e0324.png)

- **Docs**

https://elf.is-a.dev/docs

### What is Tales?

Tales is a new, easy to use hypixel API wrapper designed with python.

### Installation
**Installing from Github**
```
python -m pip install -U git+https://github.com/elfq/tales
```
**Installing from PyPi**
 ```
 pip install tales
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
More examples can be found in [the examples folder.](/examples)
