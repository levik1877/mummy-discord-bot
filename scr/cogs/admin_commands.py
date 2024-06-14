from discord.ext import commands
from discord import Member

from main import db
import scr.phrases_func as str_func

import scr.cfg.phrases as phrases


class AdminCommands(commands.Cog):

    def __init__(self, bot: commands.Bot): # Тут просто ебейшая путаница с переменной bot, я ваще хз как это работает, но менять имя никак нельзя!
        self.bot = bot

    @commands.command()
    async def editper(self, ctx, member: Member, level: int):
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


async def setup(bot: commands.Bot): # Тутпросто ебейшая путаница с переменной bot, я ваще хз как это работает, но менять имя никак нельзя!
    await bot.add_cog(AdminCommands(bot))
