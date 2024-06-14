from discord.ext import commands

from main import db


class RegistrationCommands(commands.Cog):
    """Хранит набор команд для регистрации"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def reg(self, ctx):
        """Регистрирует нового пользователя"""
        author = ctx.message.author
        if not db.check_user(author):
            user = db.add_user(author)
            await user.discord.send(content=f"{user.discord.mention}, поздравляю с успешной регистрацией.")
            print(user)
        else:
            await ctx.message.reply(content="Ты уже в зарегистрирован")


async def setup(bot: commands.Bot):
    """Служебная функция. Добавляет данный класса с командами в объект бота"""
    await bot.add_cog(RegistrationCommands(bot))
