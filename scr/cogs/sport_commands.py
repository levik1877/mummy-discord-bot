import discord
from discord.ext import commands

from main import db, sdb

import scr.phrases_func as str_func
from scr.bot_ui import sport_menu

import scr.cfg.phrases as phrases
import scr.cfg.sport_phrases as sport_phrases


class SportCommands(commands.Cog):
    """Хранит набор команд, связанных со спортом"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def sport(self, ctx):
        """Вызывает меню спорта"""
        auth = ctx.message.author
        if db.check_user(auth):
            view = sport_menu.SportMenu()
            await auth.send(
                content=str_func.random_phrase(sport_phrases.sport_greeting_phrases) + sport_phrases.sport_greeting,
                view=view
            )
        else:
            await ctx.reply(phrases.no_reg_answer + str_func.random_phrase(phrases.no_reg_answer_phrase))

    # сделать команду для добавления нового упражнения


async def setup(bot: commands.Bot):
    """Служебная функция. Добавляет данный класса с командами в объект бота"""
    await bot.add_cog(SportCommands(bot))


