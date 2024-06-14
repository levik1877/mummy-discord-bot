import asyncio
import os
import discord
from discord.ext import commands

from scr.UsersDatabese import UsersDatabase
from scr.SportDatabase import SportDatabase

db = UsersDatabase('database/database.db')
sdb = SportDatabase('database/database.db')

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all(), case_insensitive=True)


@bot.event
async def on_ready():
    """Вызывается когда бот начинает работать"""
    print('К вашим услугам хозяин!')
    await bot.change_presence(activity=discord.Game(name=' $info'))


async def load_extension():
    """Собирает все классы Cogs с командами, добавляя их к объекту бота"""
    for filename in os.listdir("scr/cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"scr.cogs.{filename[:-3]}")


async def main():
    """Подготавливает всё к запуску бота"""
    from scr.cfg.TOKEN import token
    async with bot:
        await load_extension()
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())

