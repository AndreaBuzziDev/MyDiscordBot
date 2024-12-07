import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$indovina'):
            await message.channel.send('Indovina un numero tra 1 e 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Mi spiace, ci hai messo troppo tempo {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('La risposta è corretta!')
            else:
                await message.channel.send(f'Peccato, il numero è {answer}.')
        elif message.content.startswith('$chiudi'):
            await message.channel.send('Ciao, alla prossima!')
            await client.close()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTMxNDI2NjYyNDM3NDYwMzgxNw.G0EoKE.qb1sCT_x-w9PvzIt-kdreInxI3aP_WIAT7blUw')