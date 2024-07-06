import discord
from scr.cfg import phrases
from scr import phrases_func


async def no_reg_reply(ctx):
    await ctx.send(phrases_func.random_phrase(phrases.no_reg_answer_phrase))


async def invalid_permissions(ctx):
    await ctx.send(phrases_func.random_phrase(phrases.rejection_phrases))
