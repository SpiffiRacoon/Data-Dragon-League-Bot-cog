# Data-Dragon-League-Bot-cog
Discord py bot command cog using riots Data Dragon api to get skin splash art and short info on league of legends champions
## Requirements
The python code was written using Discord.py version: 2.2.2, so i recommend using that version or a version very close for the bot you add this cog to.
## How to use
Simple, add the python file to the same directory as your "main" bot python file. Then import all the classes from the file:
```py
from leagueCog import *
```
Then once the bot has started the commands can be added to the bot using:
```py
await bot.add_cog(league(bot, <role-id>)) # The league cog takes role as input. only this role can use the league commands
```
