import discord
import requests
from discord.ext import commands
from Pymoe import Anilist
import datetime
from json import load
import json
import time
from pathlib import Path
from urllib import parse, request
import re
import ocr
import io
import os
from discord.utils import get
api = ocr.API('api-key')

token=os.environ['token']
ani = Anilist()
bot = commands.Bot(command_prefix='x', description="This is a Karuta Ping Bot")
bot.remove_command('help')


# Events= 
@bot.event
async def on_ready():
  print("am ready")

@bot.command()
async def ping(message):
  await message.send('Pong! {bot.latency} s')
  print ("pong! {bot.latency}")


@bot.group(invoke_without_command=True)
async def help(ctx):
  embed=discord.Embed(title="**XXanaXX HELP MENU**", description="Help Menu Of This Bot ! () are optional and {} are required.", color=0x00ff00)
  embed.set_author(name="XXanaXX")
  embed.add_field(name="BOT HELP", value="help,info,support,invite", inline=False)
  embed.add_field(name="KARUTA HELP", value="ksetup", inline=False)
  embed.add_field(name="GREMORY HELP", value="grsetup", inline=False)
  embed.add_field(name="GACHAPON HELP", value="gasetup", inline=False)
  embed.add_field(name="OTHER", value="uptime,updates,ping", inline=False)
  embed.set_footer(text="Any Problems or Suggestions? DM Me or Join the Support Server ")
  await ctx.send(embed=embed)
@help.command()
async def ksetup(ctx):
  await ctx.send("WILL SHOW YOU HOW TO SETUP !")

@bot.command()
async def servers(ctx):
  if ctx.author.id == 707787324469280799:
    guildname=[]
    users=[]     
    activeservers = bot.guilds
    for guild in activeservers:
      users.append(guild.member)
      guildname.append(guild.name)
    await ctx.send(guildname)
    await ctx.send(users)

@bot.command()
async def addwhitelist(ctx, guildid):
  if ctx.author.id == 707787324469280799:
    whitelist = open("whitelist.txt","r")
    readwl = whitelist.read()
    if str(guildid) in readwl:
      await ctx.send("GUILD ALREADY WHITELISTED!!!")
      whitelist.close()
    else:
      whitelist = open("whitelist.txt","a")
      whitelist.write("\n")
      whitelist.write(guildid)
      whitelist.close()
      await ctx.send("GUILD WHITELISTED!!!")



@bot.command()
async def ksetup(ctx):
  embed=discord.Embed(title="KARUTA SETUP", color=0xff0000)
  embed.add_field(name="PING RROLES", value="To setup Ping Roles Create Roles named as Common,Uncommon,Rare,Exotic,Legendary,Godly !", inline=True)
  embed.add_field(name="NOTE", value="Make Roles with exact same name else it will not work SORRY", inline=False)
  embed.set_footer(text="SORRY FOR INCONVIENCE !")
  await ctx.send(embed=embed)


@bot.command()
async def rarity(message):
  embed=discord.Embed(title="RARITY", color=0x00ffff)
  embed.add_field(name="COMMON", value="0-600", inline=True)
  embed.add_field(name="UNCOMMON", value="600-1000", inline=True)
  embed.add_field(name="RARE", value="1000-2400", inline=True)
  embed.add_field(name="EXOTIC", value="2400-6000", inline=True)
  embed.add_field(name="LEGENDARY", value="6000-10000", inline=True)
  embed.add_field(name="GODLY", value="10000+", inline=True)
  embed.set_footer(text="1000 wl ≈ 300 karuta wl ≈ 50 gacha wl")
  await message.send(embed=embed)

@bot.command()
async def look(message,x):
  dict = ani.search.character(x, page = 1 , perpage = 1)
  a = dict['data']['Page']['characters'][0]['favourites']
  f = "favourites : " + str(a)
  await message.reply(f)

    
@bot.listen()
async def on_message(message): 
  if "dropping" in message.content:
    if message.author.id == 603446902393929728 or 646937666251915264 or 815289915557675118 or 707787324469280799:
      if "3 cards" in message.content:
        n = 4 
      elif "4 cards" in message.content:
        n = 5
      elif "2 cards" in message.content:
        n=3
       
      attachment = message.attachments[0]
      a = attachment.url
        
      r = api.ocr_url(a)
      buf = io.StringIO(r)
      char = []
      for i in range(1,n):
        try:
          x = buf.readline()
          dict = ani.search.character(x, page = 1 , perpage = 1)
          a = dict['data']['Page']['characters'][0]['favourites']
          b = dict['data']['Page']['characters'][0]['name']['full']
          if a < 601:
            rarity = "Common"
          elif 600<a<1001:
            rarity = "Uncommon"
          elif 1000<a<2401:
            rarity = "Rare"
          elif 2400<a<6001:
            rarity = "Exotic"
          elif 6000<a<10001:
            rarity = "Legendary"
          elif 10000<a:
            rarity = "Godly"
          try:
            ping =get(message.guild.roles, name=str(rarity))
            pm = ping.mention
          except :
            pm == "NO-PING"
            pass
          print (pm)
        except:
            
          pass
        try:
          c = str(i) + ". "+"**Character:** "+str(b)+" **Rarity:** " + str(rarity) + " <a:r_heart:858231323209498634>" + "**Ping:** "+ pm
          
          char.append(c)
          ch = '\n'.join(char)
        
        except:
          pass
      await message.reply(ch)
      print ("dropped")
bot.run(token)
