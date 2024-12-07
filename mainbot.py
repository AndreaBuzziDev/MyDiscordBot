import discord
from discord.ext import commands
import gen_password

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def buongiorno(ctx):
    await ctx.send(f'Buongiorno a te!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_password.gen_new_password(8))

@bot.command()
async def meme(ctx):
    with open('images/meme01.png', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

@bot.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def arrivederci(ctx):
    await ctx.send("\U0001f642")
    await bot.close()

bot.run("MTMwNjY2NjY4MjgwMjExNDU5MA.Gx9Iw0.XsKcYU8bICfcSmXZ1Zt3Fys7VlRFe0sylYhi7A")