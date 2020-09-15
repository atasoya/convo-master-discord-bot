# Dependencies
import discord, random, datetime
from discord import Embed
from discord.ext import commands, tasks
from googletrans import Translator, constants  

# Import Strings
from strings import *

# Variables
translator = Translator()

#Accent Color
r = 82
g = 181
b = 238

# Bot Prefix
client = commands.Bot(command_prefix="c.")
client.remove_command('help')
# Start bot
@client.event
async def on_ready() :
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="c.help"))

# General Command
@client.command()
async def general(message,lang = "en") :
    channel = message.channel
    context = random.choice(generaltopic)
    context = translator.translate(context,dest=lang)
    title = translator.translate("Lets talk about",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)


# Translate
@client.command()
async def translate(message,lang, *,word) :
    channel = message.channel
    context = word
    context = translator.translate(word,dest=lang)
    title = f"{context.origin} ({context.src}) --> {context.text} ({context.dest})"
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name="Translated", value=title)
    await channel.send(embed=embed)

# Question
@client.command()
async def question(message,lang = "en") :
    channel = message.channel
    context = random.choice(questiontopic)
    context = translator.translate(context,dest=lang)
    title = translator.translate("Your question is",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)

# This or That
@client.command()
async def thisorthat(message,lang = "en") :
    channel = message.channel
    context = random.choice(thisorthattopic)
    context = context.lower()
    context = translator.translate(context,dest=lang)
    title = translator.translate("This or that",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)

# Personal Question
@client.command()
async def personal(message,lang = "en") :
    channel = message.channel
    context = random.choice(personaltopic)
    context = translator.translate(context,dest=lang)
    title = translator.translate("Let's get to know you",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)

# Would you rather
@client.command()
async def wouldyourather(message,lang = "en") :
    channel = message.channel
    context = random.choice(wouldyourathertopic)
    context = translator.translate(context,dest=lang)
    title = translator.translate("Would you rather",dest=lang)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title.text, value=context.text)
    await channel.send(embed=embed)

# Languages List
@client.command()
async def languages(message) :
    channel = message.channel
    title = "Supported Languages"
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title, value='[Click here.](https://cloud.google.com/translate/docs/languages)')
    await channel.send(embed=embed)
    
# Invite Link
@client.command()
async def add(message) :
    channel = message.channel
    title = "Add me to your server "
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title, value='[Click here.](https://discord.com/api/oauth2/authorize?client_id=744956642214543362&permissions=84992&scope=bot)')
    await channel.send(embed=embed)

# Help
@client.command()
async def help(message) :
    channel = message.channel
    title = "All Commands"
    xxx = "`c.general [language]` , to get general topics"+"\n"+"`c.question [language]` , to get interesting questions"+"\n"+"`c.thisorthat [language]` , to get this or that questions"+"\n"+"`c.personal [language]` , to get personal questions"+"\n"+"`c.wouldyourather [language]` , to get would you rather questions"+"\n"+"`c.add` , to add me"+"\n"+"`c.translate [language] [sentence]` , to translate sentences"+"\n"+"`c.languages` , to see supported languages"
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.from_rgb(r,g,b))
    embed.add_field(name=title, value=xxx)
    await channel.send(embed=embed)

# Debug
@client.command()
async def botservers(ctx):
    if ctx.author.id == OWNER_ID :
        await ctx.send("I'm in " + str(len(client.guilds)) + " servers")
# Init
client.run("TOKEN")
