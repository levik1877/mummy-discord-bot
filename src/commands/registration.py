import discord
from time import sleep

from main import bot, db
from src.database_src.database import User


@bot.command()
async def reg(ctx):
    author = ctx.message.author
    user = db.get_user(author.id)
    if user is None:
        db.add_user(author.id)
        await ctx.message.reply("Вы успешно зерегистрированы!")
    else:
        await ctx.message.reply("Вы уже зарегистрированы.")



