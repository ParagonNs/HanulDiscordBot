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

@bot.command()
async def 주사위(ctx):
    await ctx.send("hello")
    a = random.randrange(1,7)
    embed = discord.Embed(title = "주사위 굴리기 결과", description = None, color = 0xFAFA00)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: ", inline = True)
    embed.set_footer(text="주사위 결과: " + str(a))
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("없거나 잘못된 명령어입니다.")

bot.run('token')
