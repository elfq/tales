# Tales

### What is Tales?

Tales is a new, easy to use hypixel API wrapper designed with python.

### Installation

```
python -m pip install -U git+https://github.com/elfq/tales
```
### Supported API Minigames

- Blitz
- Bedwars

*more to come*

### Example

```py
from tales import blitz, api

api.key = "Your Hypixel API key"

wins = blitz.wins("Technoblade")
print(wins)
```
