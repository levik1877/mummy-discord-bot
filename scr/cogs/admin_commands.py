from discord.ext import commands
from discord import Member

from main import db
import scr.phrases_func as str_func

import scr.cfg.phrases as phrases


class AdminCommands(commands.Cog):
    """Хранит набор команд администратора"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def editper(self, ctx, member: Member, level: int):
        """Изменяет уровень прав юзера"""
        auth = ctx.message.author
        if db.check_user(auth):
            if db.get_user(auth).permissions_level == 1488:
                user = db.get_user(member)
                db.edit_user_permission_level(user, level)
                await ctx.reply(str_func.random_phrase(phrases.successfully_answer_phrases))
            else:
                await ctx.reply(str_func.random_phrase(phrases.rejection_phrases))
        else:
            await ctx.reply(str_func.random_phrase(phrases.no_reg_answer_phrase) + phrases.no_reg_answer)

    @commands.command()
    async def editmoney(self, ctx, member: Member, value: float):
        """Изменяет количество денег у юзера"""
        auth = ctx.message.author
        if db.check_user(auth):
            if db.get_user(auth).permissions_level == 1488:
                user = db.get_user(member)
                db.edit_user_money(user, value)
                await ctx.reply(str_func.random_phrase(phrases.successfully_answer_phrases))
            else:
                await ctx.reply(str_func.random_phrase(phrases.rejection_phrases))
        else:
            await ctx.reply(str_func.random_phrase(phrases.no_reg_answer_phrase) + phrases.no_reg_answer)


async def setup(bot: commands.Bot):
    """Служебная функция. Добавляет данный класса с командами в объект бота"""
    await bot.add_cog(AdminCommands(bot))
