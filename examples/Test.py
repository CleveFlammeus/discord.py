import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')



@client.event
async def on_message(message):
        print(f'Message from {message.author}: {message.content}')

client.run('MTAyNTgyMTk4OTg1Mzc0NTE2Mw.GW6qNM.2PRIgVmyHw5dLv4Xa-OPEQmDHjTk7u1hMPxgEk')