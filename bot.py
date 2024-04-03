import discord
from discord.ext import commands

prefix = "!"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user}')

@bot.command()
async def teste(ctx):
    await ctx.send("Este é um comando de teste!")

@bot.command()
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade+1) # Apaga msgs


bot.run('TOKEN DO SEU BOT') # Aqui é pro token
