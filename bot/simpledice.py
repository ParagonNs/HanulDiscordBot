#simpledice.py
import random

def simpledice():
    a = random.randrange(1,7)
    embed = discord.Embed(title = "주사위 굴리기 결과", description = None, color = 0xFAFA00)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: ", inline = True)
    embed.set_footer(text="주사위 결과: " + str(a))
    await ctx.send(embed=embed)
