from discord.ext import commands

from main import db


class RegistrationCommands(commands.Cog):

    def __init__(self, bot: commands.Bot): # Тутпросто ебейшая путаница с переменной bot, я ваще хз как это работает, но менять имя никак нельзя!
        self.bot = bot
    @commands.command()
    async def reg(self, ctx):
        author = ctx.message.author
        if not db.check_user(author):
            user = db.add_user(author)
            await user.discord.send(content=f"{user.discord.mention}, поздравляю с успешной регистрацией.")
            print(user)
        else:
            await ctx.message.reply(content="Ты уже в зарегистрирован")


async def setup(bot: commands.Bot): # Тутпросто ебейшая путаница с переменной bot, я ваще хз как это работает, но менять имя никак нельзя!
    await bot.add_cog(RegistrationCommands(bot))
