import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
 
Client = discord.Client()
bot_prefix= "/"
client = commands.Bot(command_prefix=bot_prefix)
 
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='type /help'))
 
@client.command(pass_context=True)
async def rules(ctx):
    await client.say("""**
========================================
- Do not impersonating People
- Do not spam
- Do not swearing
- Do not say inappropriate words 
- Do not bullying others
========================================**""")
#command1
@client.command(pass_context = True)
async def invite(ctx):
    x = await client.invites_from(ctx.message.server)
    x = ["<" + y.url + ">" for y in x]
    print(x)
    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome To @&s To Server!')
    print('Sent message to ' + member.name)

#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command3
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

#command4
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
 
#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

#command6
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

#command7
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")

    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

@client.event
async def on_message(message):
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('blitz') in message.content:
       await client.delete_message(message)
    if ('dls') in message.content:
       await client.delete_message(message)
    if message.content.startswith('ping'):
        await client.send_message(message.channel,'Pong! @&s'  %(message.author.id))

#command8
@client.command(pass_context = True)
async def listservers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)
async def whomade(ctx):
    await client.say("This bot by NabzGT Aka Blank")
	
#command9
@client.command(pass_context = True)
async def info(ctx):
    await client.say("""**Useful Links:**
Discord Invite: https://discord.gg/vxVNFkF

Invite This Bot: https://discordapp.com/oauth2/authorize?client_id=504655132521398292&permissions=8&scope=bot

@Owner - Developer Of OG Bot
@Co-owners  - Helping Code Bot

Any issues please **PM** @Owners directly.""")

      
client.run("NTA0NjU1MTMyNTIxMzk4Mjky.DrIMWA.-UWGkKteGkf-YqCZSxFP9jLqn6o")
