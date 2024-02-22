import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all(), case_insensitive=True)


@bot.event
async def on_ready():
    print('К вашим услугам хозяин!')
    await bot.change_presence(activity=discord.Game(name=' $info'))


if __name__ == "__main__":
    from src.config import token
    bot.run(token)
