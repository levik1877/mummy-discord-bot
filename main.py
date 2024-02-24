import discord
from discord.ext import commands
from src.database_src.database import Database, User

db = Database('database.db')
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all(), case_insensitive=True)


@bot.event
async def on_ready():
    print('К вашим услугам хозяин!')
    await bot.change_presence(activity=discord.Game(name=' $info'))


@bot.command()
async def leg(ctx):
    await ctx.send('net')


if __name__ == "__main__":
    from src.commands.registration import bot
    from src.TOKEN import token
    bot.run(token)
