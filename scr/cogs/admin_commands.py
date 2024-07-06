import discord.ext.commands
from discord.ext import commands
from discord import Member

from main import db
from scr import phrases_func

from scr.cfg import phrases, permissions
from scr.command_author_check import command_author_check
from scr import error_replies


class AdminCommands(commands.Cog):
    """Хранит набор команд администратора"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @command_author_check(permissions_level=permissions.root)
    async def editper(self, ctx, member: Member, level: int):
        """Изменяет уровень прав юзера"""
        user = db.get_user(member)
        db.edit_user_permission_level(user, level)
        await ctx.reply(phrases_func.random_phrase(phrases.successfully_answer_phrases))

    @editper.error
    async def editper_error(self, ctx, error: discord.ext.commands.CommandError):
        await ctx.send(phrases.invalid_command_args + "$editper <Пинг пользователя> <Новый уровень прав>")

    @commands.command()
    @command_author_check(permissions_level=permissions.root)
    async def editmoney(self, ctx, member: Member, value: float):
        """Изменяет количество денег у юзера"""
        user = db.get_user(member)
        db.edit_user_money(user, value)
        await ctx.reply(phrases_func.random_phrase(phrases.successfully_answer_phrases))

    @editmoney.error
    async def editmoney_error(self, ctx, error: discord.ext.commands.CommandError):
        await ctx.send(phrases.invalid_command_args + "$editmoney <Пинг пользователя> <Новое число денег>")


async def setup(bot: commands.Bot):
    """Служебная функция. Добавляет данный класса с командами в объект бота"""
    await bot.add_cog(AdminCommands(bot))
