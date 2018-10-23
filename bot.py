#discord bot made by NabzGT
#NabzGT - youtube
#@NabzGT#9028 - discord
 
import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time

bot = commands.Bot(command_prefix='<')
 
@bot.event
async def on_ready():
    print("Bot Is Starting Up... Please Wait")
    print("Name: " + bot.user.name)
    print("ID: " + bot.user.id)
    print("Bot Is Online! And Ready To Spam")
    print("Made By NabzGT")

@bot.command(pass_context=True)
async def madeby(ctx):
    await bot.say("Made By   #9028 (aka NabzGT)")
	
@bot.command(pass_context=True)
async def auto(ctx):
    await bot.say("Enabling Auto Messager!")
    time.sleep(10000)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        await bot.say("Make Sure To Check Our Website: https://growtopiaprivate.000webhostapp.com/ dont have growtopia 2.982? : gg.gg/growtopiainstaller")

bot.run ("Token")