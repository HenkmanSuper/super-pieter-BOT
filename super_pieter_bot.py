import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()  
client = commands.Bot(command_prefix = "!") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") 

@client.event
async def on_message(message):
    if message.content == "hoi":
        await client.send_message(message.channel,":wave: HALLO!! :wave:") 

        
        
        
@client.event
async def on_message(test):
    if test.content == ":pk:":
        await client.send_message(test.channel,":pk: = SUPER COOL!! ")               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
client.run("NDg4Mjc1OTQ3NjkxNDQyMTg3.DnfxXQ.Ear2_QUHygAA02wTXzIMEVMcK4s")


