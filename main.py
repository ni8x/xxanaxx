# CONFIG
 # Just google how to get discord token.

import time
# Import the needed libs.
import asyncio
from discord.ext import commands
import os
import discord
import random
from random import randint
import re
from json import load
from pathlib import Path
from keep_alive import keep_alive
print("Loading..")
token=os.environ['token']

bot = commands.Bot(command_prefix="!x")
@bot.command()
async def ping(message):
  await asyncio.sleep(1)
  await message.send("pong")
  
@bot.command()
async def speak(ctx,m):
  await ctx.send(m)

@bot.command()
async def rvote(ctx):
  for f in range(1,100):
      await ctx.send("rvote")
      await asyncio.sleep(randint(3600,3800))

@bot.command()
async def rd(ctx):
  for f in range(1,200):
      await ctx.send("rd")
      await asyncio.sleep(randint(600,700))

@bot.command()
async def kd(ctx):
  for f in range(1,100):
      await ctx.send("kd")
      await asyncio.sleep(randint(1800,1900))

@bot.command()
async def kdaily(ctx):
  for f in range(1,10):
      await ctx.send("kdaily")
      await asyncio.sleep(randint(86400,87000))

@bot.command()
async def rdaily(ctx):
  for f in range(1,10):
      await ctx.send("rdaily")
      await asyncio.sleep(randint(86400,87000))
        
@bot.listen()
async def on_message(ctx):
  if ctx.channel.id == 784641906592317460: 
    if "dropping" in ctx.content:
      await asyncio.sleep(1)
      await ctx.add_reaction(str("1️⃣"))
keep_alive()
bot.run(token)  # Starts the bot by passing it a token and telling it it isn't really a bot. 
