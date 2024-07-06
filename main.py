"""
Здесь происходит инициализация основных объектов, а также сборка и запуск бота.
"""
import asyncio
import logging
import os
import discord
from discord.ext import commands
from sqlite3 import connect

from scr.UsersDatabese import UsersDatabase
from scr.SportDatabase import SportDatabase
from scr.cfg import config, phrases
from scr import phrases_func, error_replies

connection_db = connect(config.database_directory)
db = UsersDatabase(connection_db)
sdb = SportDatabase(connection_db)

bot = commands.Bot(command_prefix=config.prefix, intents=discord.Intents.all(), case_insensitive=True)


@bot.event
async def on_ready():
    """Вызывается когда бот начинает работать"""
    print('К вашим услугам хозяин!')
    logging.info("Bot has been started.")
    await bot.change_presence(activity=discord.Game(name=config.bot_status_description))


@bot.event
async def on_command_error(ctx, error: Exception):
    """Срабатывает если юзер не зарегистрирован или у него недостаточно прав для использования команды"""
    if type(error) is discord.ext.commands.errors.CheckFailure:
        await ctx.send("**ИЛИ**")
        await error_replies.no_reg_reply(ctx)
        await ctx.send("**ИЛИ**")
        await error_replies.invalid_permissions(ctx)
    else:
        print(error)


async def load_extension():
    """Собирает все классы Cogs с командами, добавляя их к объекту бота"""
    for filename in os.listdir(config.cogs_directory):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"{config.cogs_directory.replace('/', '.', 1)}.{filename[:-3]}")


async def main():
    """Подготавливает всё к запуску бота"""
    from scr.cfg.TOKEN import token
    async with bot:
        await load_extension()
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
