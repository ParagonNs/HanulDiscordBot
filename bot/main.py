# -*_ coding: utf-8 -*-
#main

import asyncio, discord
from simpledice import *
from discord.ext import commands

bot = commands.Bot(command_prefix="&")

@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("없거나 잘못된 명령어입니다.")

bot.run('token')
