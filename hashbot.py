import asyncio
from email import message
from time import sleep
import discord
import random


client = discord.Client()

# Name combinations 
voice_channel_name_nouns = ["Burgers" ,"King " ,"Ice-cream "]
voice_channel_name_adjectives = ["Nice "]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$change'):
        await message.channel.send('working!')
        await voiceNameChanger()

async def voiceNameChanger(): 
    words = random.randint(0,1)
    print(words)
    if words == 0:
        channel_name = str(random.choice(voice_channel_name_nouns))
    else: channel_name = str(random.choice(voice_channel_name_adjectives)) +  str(random.choice(voice_channel_name_nouns))
    print(channel_name)
    channel = client.get_channel(618860313562972160) # Channel ID hardcoded. Fix in future version.
    await discord.VoiceChannel.edit(channel, name = str(channel_name)) # Edits chosen channel name

client.run('')
    


