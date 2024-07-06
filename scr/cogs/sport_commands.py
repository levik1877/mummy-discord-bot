import discord
from discord.ext import commands

from main import db, sdb

from scr import phrases_func
from scr.bot_ui import sport_menu

from scr.cfg import phrases, permissions
from scr.cfg import sport_phrases
from scr.command_author_check import command_author_check


class SportCommands(commands.Cog):
    """Хранит набор команд, связанных со спортом"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @command_author_check()
    async def sport(self, ctx):
        """Вызывает меню спорта"""
        auth = ctx.message.author
        view = sport_menu.SportMenu()
        await auth.send(
            content=phrases_func.random_phrase(sport_phrases.sport_greeting_phrases) + sport_phrases.sport_greeting,
            view=view
        )

    @commands.command()
    @command_author_check(permissions_level=permissions.admin)
    async def add_exersice(self, ctx, new_exersice_name: str, exersice_type: str):
        """Добавляет новое упражнение в базу данных"""
        sdb.add_exersice(new_exersice_name, exersice_type)
        await ctx.reply(phrases_func.random_phrase(phrases.successfully_answer_phrases))

    @add_exersice.error
    async def add_exersice_error(self, ctx, error: discord.ext.commands.CommandError):
        await ctx.send(phrases.invalid_command_args + "$add_exersice <Название упражнения> <Тип упражнения (может принимать значения count и time)>")


async def setup(bot: commands.Bot):
    """Служебная функция. Добавляет данный класса с командами в объект бота"""
    await bot.add_cog(SportCommands(bot))


