# -*_ coding: utf-8 -*-
#main

import asyncio, discord
from user.py import *
from discord.ext import commands

bot = commands.Bot( command_prefix = "&" )
bot_token = open( "token.txt", "r" ).readline()
color_list = [ 0x62D0F6 ]

bot_language = "한국어"

@bot.event
async def on_ready():
	print( "봇 {0}이 실행되었습니다.".format( bot ))

@bot.command()
async def 도움말( ctx ):
    await ctx.send("도움말")

@bot.event
async def on_command_error( ctx, error ):
    if isinstance( error, commands.CommandNotFound ):
    	await ctx.send("없거나, 잘못된 명령어입니다. 봇의 명령어는 ( &도움말 )을 사용해서 확인할 수 있습니다.")
	
@bot.command()
async def 회원가입( ctx ):
    if Check_user( ctx.author.name, ctx.author.id ):
	await ctx.send( "{0}님은 이미 가입되었습니다. ".format(ctx.author.name))
    else:
	Signup( ctx.author.name, ctx.author.id )
	await ctx.send( "{0}님의 회원 가입이 완료되었습니다.".format(ctx.author.name))
	
@bot.command()
async def 내정보( ctx ):
    if Check_user( ctx.author.name, ctx.author.id ):
	_id, _name, _credit, _mainlv, _resource_a, _resource_b, _resource_c, _resource_d, _mininglv, _mining_countlv, _mining_lucklv, _credit_bank, _banklv, _banktax, _usertax = Low_user_data( ctx.author.name, ctx.author.id );
	emebed = discord.Embed( title = "사업자등록증", description = ctx.author.name, color = color_list[0] )
	embed.add_field( name = "등급", value = _mainlv, inline = True )
	embed.add_field( name = "은행 신용 등급", value = _banklv, inline = True )
	embed.add_field( name = "보유 자산", value = _credit, inline = True )
	embed.add_field( name = "은행 위탁 자산", value = _credit_bank, inline = True )
	embed.add_field( name = "채광 등급", value = _mininglv, inline = False )
	embed.add_field( name = "채광 횟수 강화", value = _mining_countlv, inline = True )
	embed.add_field( name = "채광 행운 강화", value = _mining_lucklv, inline = True )
	embed.add_field( name = "자원 B", value = _resource_b, inline = True )
	embed.add_field( name = "자원 A", value = _resource_a, inline = False )
	embed.add_field( name = "자원 B", value = _resource_b, inline = True )
	embed.add_field( name = "자원 C", value = _resource_c, inline = True )
	embed.add_field( name = "자원 D", value = _resource_d, inline = True )
	embed.add_field( name = "은행 수수료 총합", value = _banktax, inline = False )
	embed.add_field( name = "납세량 총합", value = _banktax, inline = True )
	await ctx.send( embed = embed )
    else:
	await ctx.send( "{0}님은 회원 가입이 완료되지 않았습니다.".format(ctx.author.name))
	
bot.run(bot_token)
print("봇이 성공적으로 실행되었습니다!")
