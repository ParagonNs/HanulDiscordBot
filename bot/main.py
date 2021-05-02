# -*_ coding: utf-8 -*-

import asyncio, discord
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
    	await ctx.send("Command not found")
        

bot.run('token')
