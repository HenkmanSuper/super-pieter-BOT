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
        await client.send_message(message.channel,":wave: HALLOoooooo!! :wave:") 

               
                   

       
        
        
        
        
        
        
        
              
        
        
        
client.run("TOKEN")


