import discord
from discord.ext import discord

intents = discord.Intents.default()
intents.message_content = true

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


bot.run('MTIyMzA0MDYzODEwNzI1ODk3MQ.GLjrxB.7EK8BGQYrfgNJqcpodw_yvNyzYw8xlMA4Pypkk')
