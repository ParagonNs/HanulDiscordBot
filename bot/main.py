# -*_ coding: utf-8 -*-
#main

import asyncio, discord
from user.py import *
from discord.ext import commands

bot = commands.Bot(command_prefix="&")
bot_token = open("token.txt", "r").readline()

bot_language = "한국어"

@bot.event
async def on_ready():
	print("봇 {0}이 실행되었습니다.".format(bot))

@bot.command()
async def 도움말(ctx):
    await ctx.send("도움말")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("없거나 잘못된 명령어입니다. 봇의 명령어는 ( &도움말 )을 사용해서 확인할 수 있습니다.")
	
@bot.command()
async def 회원가입(ctx):
    if Check_user(ctx.author.name, ctx.author.id):
	await ctx.send("{0}님은 이미 가입되었습니다.".format(ctx.author.name))
    else:
	Signup(ctx.author.name, ctx.author.id)
	await ctx.send("{0}님의 회원 가입이 완료되었습니다.".format(ctx.author.name))
	
bot.run(bot_token)
print("봇이 성공적으로 실행되었습니다!")
