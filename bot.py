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
    await bot.say("GROWTOPIA 2.983 OPCODES BY NABZGT|\nGrowtopia.exe+228C2 - Punch place|\nGrowtopia.exe+6262D - Antirespawn 2|\nGrowtopia.exe+6E434 - Disconnect|\nGrowtopia.exe+6E5EC - Ghost v2|\nGrowtopia.exe+CBBC9 - Water Ring|\nGrowtopia.exe+1F2819 - Legen Name|\nGrowtopia.exe+24F3E1 - Growsz|\nHope You Enjoy for theese code|")

bot.run ("NTA0NjA5MDg2MzE5NDkzMTIx.DrHh4Q.mNWyisOC6MI5pKQUEzZ-W3m0EKQ")
