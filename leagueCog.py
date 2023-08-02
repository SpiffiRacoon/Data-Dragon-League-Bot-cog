"""
Discord python bot cog with league of legends commands using the Riots Data dragon api. 
For more info on Data dragon: https://developer.riotgames.com/docs/lol

Author: Spiffi the Raccoon
"""

import discord
from discord.ext import commands
from datetime import datetime
from urllib.request import urlopen
import json
from discord.ui import Select, View

class league(commands.Cog, description="League commands, please keep these to the league channel"):
    def __init__(self, bot, role):
        self.bot = bot
        self.version = json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())[0] # Fetches all patch versions and applies the latest one.
        self.dataDragonStr = f"http://ddragon.leagueoflegends.com/cdn/{self.version}/" # This needs to be updated every patch for new skins and champions to work.
        self.league_role_id = role # This is the role that has access to all commands in this cog.

    @commands.command(brief='Returns a splash art for a champhion', description='Based on champion name given as a argument it returns a list of all skin names from riots data dragon api. ' 
                 'After selecting a skin it returns the splash art for that skin also taken from data dragon.')
    async def splash(self, ctx, champion: str = commands.parameter(default="None", description="name, check $helpList for correct syntax.")):
        print(f"{datetime.now()}: splash art command received from {ctx.author}")
        if  ctx.author.get_role(self.league_role_id) != None:
            if champion == "None":
                fuckup = f'<@{ctx.author.id}>'
                await ctx.reply(f"Alright let met get this straight {fuckup}. You want me to show you splash art for nothing?!? How the FUCK DO YOU EXPECT THAT TO WORK!?!?!?!?!?")
                return
            try:
                dataDragon = urlopen(f"{self.dataDragonStr}data/en_US/champion/{champion}.json")

                dataJson = json.loads(dataDragon.read())
                skins = dataJson['data'][f'{champion}']['skins']
                skin_options = []
                for x in skins:
                    skin_options.append(discord.SelectOption(label=f"{x['name']}", value=f"{x['num']}"))

                select = Select(placeholder=f"Pick a {champion} skin", options=skin_options)

                async def displaySplash(interaction):
                    select.disabled=True
                    await interaction.response.edit_message(view=view)
                    await interaction.followup.send(f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion}_{select.values[0]}.jpg')


                select.callback = displaySplash

                view = View()
                view.add_item(select)
                await ctx.reply(f"Select a skin for {champion}:", view=view)
            except:
                await ctx.reply(f"That isn't a League of legends Champion you dummy!")
        else:
            # This was just something funny i did on my server remove this else state if you find it annoying
            await ctx.send(f'https://tenor.com/view/peter-griffin-victory-dance-cry-about-it-cry-about-it-meme-gif-26283524')

    @commands.command()
    async def champSmall(self, ctx, champion: str = commands.parameter(default="None", description="name, check $helpList for correct syntax.")):
        print(f"{datetime.now()}: champInfo command received from {ctx.author}")
        if ctx.author.get_role(self.league_role_id) != None:
            if champion == "None":
                fuckup = f'<@{ctx.author.id}>'
                await ctx.reply(f"Alright let met get this straight {fuckup}. You want me to show you splash art for nothing?!? How the FUCK DO YOU EXPECT THAT TO WORK!?!?!?!?!?")
                return
            try:
                dataDragon = urlopen(f"{self.dataDragonStr}data/en_US/champion/{champion}.json")
                dataJson = json.loads(dataDragon.read())

                AllyTips = ""
                i = 0
                for x in dataJson['data'][champion]['allytips']:
                    i = i+1
                    AllyTips += f"{i}:{x}\n\n"

                EnemyTips = ""
                i = 0
                for x in dataJson['data'][champion]['enemytips']:
                    i = i+1
                    EnemyTips += f"{i}:{x}\n\n"

                embed=discord.Embed(title=f"{dataJson['data'][champion]['name']}", description=f"{dataJson['data'][champion]['title']}", color=0xFF5733)
                embed.set_thumbnail(url=f"{self.dataDragonStr}img/champion/{champion}.png")
                embed.add_field(name="Lore (Short)", value= f"{dataJson['data'][champion]['blurb']}", inline=False)
                embed.add_field(name="Ally Tips", value=AllyTips, inline=True)
                embed.add_field(name="Enemy Tips", value=EnemyTips, inline=True)
                embed.add_field(name="Roles", value=f"{dataJson['data'][champion]['tags']}", inline=False)
                await ctx.send(embed=embed)
            except:
                await ctx.reply(f"That isn't a League of legends Champion you dummy!")
        else:
            # This was just something funny i did on my server remove this else state if you find it annoying
            await ctx.send(f'https://tenor.com/view/peter-griffin-victory-dance-cry-about-it-cry-about-it-meme-gif-26283524')

    @commands.command()
    async def champBig(self, ctx, champion: str = commands.parameter(default="None", description="name, check $helpList for correct syntax.")):
        print(f"{datetime.now()}: champInfo command received from {ctx.author}")
        if ctx.author.get_role(self.league_role_id) != None:
            if champion == "None":
                fuckup = f'<@{ctx.author.id}>'
                await ctx.reply(f"Alright let met get this straight {fuckup}. You want me to show you splash art for nothing?!? How the FUCK DO YOU EXPECT THAT TO WORK!?!?!?!?!?")
                return
            try:
                dataDragon = urlopen(f"{self.dataDragonStr}data/en_US/champion/{champion}.json")
                dataJson = json.loads(dataDragon.read())

                AllyTips = ""
                i = 0
                for x in dataJson['data'][champion]['allytips']:
                    i = i+1
                    AllyTips += f"{i}:{x}\n\n"

                EnemyTips = ""
                i = 0
                for x in dataJson['data'][champion]['enemytips']:
                    i = i+1
                    EnemyTips += f"{i}:{x}\n\n"

                Info = ""
                for key, value in dataJson['data'][champion]['info'].items():
                    Info += f"{key} : {value}\n\n"

                Stats = ""
                for key, value in dataJson['data'][champion]['stats'].items():
                    Stats += f"{key} : {value}\n"

                embed=discord.Embed(title=f"{dataJson['data'][champion]['name']}", description=f"{dataJson['data'][champion]['title']}", color=0xFF5733)
                embed.set_thumbnail(url=f"{self.dataDragonStr}img/champion/{champion}.png")
                embed.add_field(name="Lore", value= f"{dataJson['data'][champion]['lore']}", inline=False)
                embed.add_field(name="Ally Tips", value=AllyTips, inline=True)
                embed.add_field(name="Enemy Tips", value=EnemyTips, inline=True)
                embed.add_field(name="Roles", value=f"{dataJson['data'][champion]['tags']}", inline=False)
                embed.add_field(name="Info", value=Info, inline=True)
                embed.add_field(name="Stats", value=Stats, inline=True)
                await ctx.send(embed=embed)
            except:
                await ctx.reply(f"That isn't a League of legends Champion you dummy!")
        else:
            # This was just something funny i did on my server remove this else state if you find it annoying
            await ctx.send(f'https://tenor.com/view/peter-griffin-victory-dance-cry-about-it-cry-about-it-meme-gif-26283524')
        
    @commands.command(brief='Based on 1st letter get champion list', description='Champion list Which returns based on starting charachter a list of champions with correct syntax for the splash command.')
    async def champNames(self, ctx):
        print(f"{datetime.now()}: champNames command received from {ctx.author}")
        if ctx.author.get_role(self.league_role_id) != None:

            await ctx.send("Write Starting letter:")

            def letterReply(letter):
                return (letter.author == ctx.author and (letter.content == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z') and letter.channel == ctx.channel)

            msg = await self.bot.wait_for("message", check=letterReply)
            dataDragon = urlopen(f"{self.dataDragonStr}data/en_US/champion.json")
            dataJson = json.loads(dataDragon.read())
            champList = list(dataJson['data'].keys())
            sort = [x for x in champList if x[0] == msg.content.upper()]
            if len(sort) == 0:
                await msg.reply(f'Message input was, "{msg.content}". No champion list printed.')
            else:
                await msg.reply(f"```{sort}```")
            
        else:
            # This was just something funny i did on my server remove this else state if you find it annoying
            await ctx.send(f'https://tenor.com/view/peter-griffin-victory-dance-cry-about-it-cry-about-it-meme-gif-26283524')

    @commands.command(brief='Checks current latest patch version', description='Checks current latest patch version on riots data dragon api and checks if the bot needs to update the version.')
    async def checkPatch(self, ctx):
        print(f"{datetime.now()}: checkPatch command received from {ctx.author}")
        if ctx.author.get_role(self.league_role_id) != None:
            current_patch = json.loads(urlopen("https://ddragon.leagueoflegends.com/api/versions.json").read())[0]
            if self.version != current_patch:
                await ctx.send(f"Bot currently running patch ***{self.version}***. Latest Data Dragon patch ***{current_patch}***, Updating...")
                self.version = current_patch # Done updating string to use latest data dragon patch version.
            else:
                await ctx.send(f"Bot currently running patch ***{self.version}***. Latest Data Dragon patch ***{current_patch}***, no point in updating it you silly goose.")
        else:
            # This was just something funny i did on my server remove this else state if you find it annoying
            await ctx.send(f'https://tenor.com/view/peter-griffin-victory-dance-cry-about-it-cry-about-it-meme-gif-26283524')