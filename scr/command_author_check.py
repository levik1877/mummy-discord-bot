"""
Здесь хранится декоратор, в котором происходит проверка пользователя, использовавшего команду, на то зарегистрирован
он или нет, а также на уровень прав.
Также происходит логирование.
"""
from discord.ext import commands

from main import db
from scr.cfg import permissions, config


def command_author_check(permissions_level: int = permissions.slave):
    def check_permissions_and_verify(ctx):
        auth = ctx.message.author
        return db.check_user(auth) and (db.get_user(auth).permissions_level >= permissions_level)
    return commands.check(check_permissions_and_verify)
