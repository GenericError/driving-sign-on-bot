import discord
import asyncio
import time
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if "Licensed Driver" in message.author.roles:
        if message.content.lower() == ('#signon'):
            await client.delete_message(message)
            await client.send_message(message.channel, 'Driver <@'+message.author.id+'> signing on at '+time.strftime('%H%M')+' hours')
        if message.content.lower() == ('#signoff'):
            await client.delete_message(message)
            await client.send_message(message.channel, 'Driver <@'+message.author.id+'> signing off at '+time.strftime('%H%M')+' hours')

client.run(os.environ.get('BOT_TOKEN'))
