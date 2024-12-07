import discord
import gen_password

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$close'):
        await message.channel.send("Bye bye!")
        await client.close()
    elif message.content.startswith('$genpassword'):
        await message.channel.send("Ecco la tua password:")
        await message.channel.send(gen_password.gen_new_password(8))
    elif message.content.startwith('$dammi un meme'):
        f = open('images/meme01.png', 'rb', encoding='utf-8')
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
        f.close()
        # Possiamo quindi inviare questo file come parametro!
        await message.channel.send(file=picture)
    # else:
    #     await message.channel.send(message.content)


client.run("MTMxNDI2NjYyNDM3NDYwMzgxNw.G0EoKE.qb1sCT_x-w9PvzIt-kdreInxI3aP_WIAT7blUw")