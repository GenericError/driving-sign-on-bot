import discord
import asyncio
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == ('#signon'):
        await client.delete_message(message)
        await client.send_message(message.channel, 'Driver <@'+message.author.id+'> signing on at '+time.strftime('%H%M')+' hours')
    if message.content == ('#signoff'):
        await client.delete_message(message)
        await client.send_message(message.channel, 'Driver <@'+message.author.id+'> signing off at '+time.strftime('%H%M')+' hours')

client.run(process.env.BOT_TOKEN)
