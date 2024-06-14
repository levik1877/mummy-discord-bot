from discord.ext import commands

from main import db

from scr.phrases_func import dict_to_str
import scr.cfg.phrases as phrases


class GeneralCommands(commands.Cog):
    """Хранит набор основных команд"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        """Выводит список команд"""
        auth = ctx.message.author
        if db.check_user(auth):
            if db.get_user(auth).permissions_level >= 20:
                await auth.send(ctx.message.author.mention + phrases.master_greeting + dict_to_str(phrases.master_commands))
            else:
                await auth.send(ctx.message.author.mention + phrases.slaves_greeting + dict_to_str(phrases.slaves_commands))
        else:
            await auth.send(ctx.message.author.mention + phrases.general_greeting + dict_to_str(phrases.slaves_commands))


async def setup(bot: commands.Bot):
    """Служебная функция. Добавляет данный класса с командами в объект бота"""
    await bot.add_cog(GeneralCommands(bot))
