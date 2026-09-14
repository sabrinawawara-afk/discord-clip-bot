
import os
import discord

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")

bot.run(os.environ["DISCORD_TOKEN"])
