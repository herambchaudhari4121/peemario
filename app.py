import os
import sys
import base64
import json
from termcolor import colored, cprint
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError
from better_profanity import profanity
import requests
import mmllib
import pafy
import youtube_dl
from random_word import RandomWords
from pyfiglet import Figlet
import ffmpeg
from textblob import TextBlob
import numpy as np
import pandas as pd
import boto3
from RedditReader import Subreddit
from botocore.exceptions import NoCredentialsError
import threading
import asyncio
import schedule
import time
import random
import string
import discord
from discord.ext import commands
# consumer_key = os.environ["consumer_key"]
# consumer_secret = os.environ["consumer_secret"]
# access_token_key = os.environ["access_token_key"]
# access_token_secret = os.environ["access_token_secret"]
# api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
token = os.environ['BOT_TOKEN']
bot = commands.Bot(command_prefix='n!')
prefix = 'n!'
fartbaby = []
sanjay = []
ACCESS_KEY = 'AKIAI5VZR2QXQVFDZYZA'
SECRET_KEY = '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'
client = discord.Client()
d = {}
# Hello Horse it is trump justto see if it is even working
heylisten = 'trump'
admins = [511989134043381760, 258401707556470785]
df = pd.DataFrame(data=d)
nomoresayingcusswords = ["Why would you say such a thing.", "Swearing is bad, you know.",
                         "You really need your mouth washing young boy.", "No saying cuss words in this house!"]
steam = ["raping", "writing a diss track on elmo", "eating food", "being a swag dude"]
minion = ["http://shiretoko.miemasu.net/CgiStart?page=Single&Mode=Motion&",
          "http://61.211.241.239/CgiStart?page=Single&Mode=Motion&Language=1",
          "http://webcam.stanburyvillageschool.co.uk/top.htm?"]

os.system('')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# test commit aheueheheuehheueh
# ok it works!
def log(message):
    print("[" + str(time.clock_gettime) + "]" + message)


@bot.event
async def on_ready():
    art = f"""{bcolors.OKCYAN}  __                          
   _________  / /_  ____  ____  __  ______ 
  / ___/ __ \/ __ \/ __ \/ __ \/ / / / __ \
 / /  / /_/ / /_/ / /_/ / / / / /_/ / /_/ /
/_/   \____/_.___/\____/_/ /_/\__,_/\____/ 
                                           """
    log(art)
    log(f'{bcolors.ENDC}' + 'i sent one {0.user}'.format(bot))
async def downloadyt(ctx,url):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=False)
            ydl.prepare_filename(info_dict)
            with youtube_dl.YoutubeDL({'format': '136'}) as ydl:
                ydl.download([url])
            return True
    except Exception:
        await ctx.send("Something went wrong.")
        return False
    await ctx.send()
    log('hello! ' + arg)
    try:
        await ctx.send(video.title, file=discord.File("video.mp4"))
    except discord.HTTPException:
        await ctx.send("Da youtube video made like ya mom and was big and fat. \n So, it could not be sent. Sorry. Bitch.")
        os.remove('video.mp4')
    os.remove('video.mp4')
@bot.event
async def on_command_error(ctx, error):
    await ctx.channel.send("Free error for you! Contact bot owner if confused\n```" + str(error) + "```")
@bot.command(brief='Download a video from YouTube.')
async def dl(ctx, arg):
    letters = string.ascii_lowercase
    yeezy = ''.join(random.choice(letters) for i in range(10)) 
    video = pafy.new(arg)
    thepoopbaby = '```\n' + 'Video title: ' + video.title + '\nViews: ' + str(
        video.viewcount) + '\nUploaded by: ' + video.author + '```'
    await ctx.send(thepoopbaby)
    log('hello! ' + arg)
    best = video.getbest()
    fuckah = yeezy + "."
    best.download(filepath="ytdl/" + fuckah + best.extension, quiet=False)
    fartypants = fuckah + best.extension
    await ctx.send('http://18.223.24.247:8069/ytdl/' + fartypants)

@bot.command(brief='Downloads a YouTube video with custom bitrate ("awesomify")')
async def awesomify(ctx, arg1, arg2, arg3):
    video = pafy.new(arg1)
    thepoopbaby = '```\n' + 'Video title: ' + video.title + '\nViews: ' + str(
        video.viewcount) + '\nUploaded by: ' + video.author + '```'
    await ctx.send(thepoopbaby)
    log('hello! ' + arg1)
    best = video.getbest()
    best.download(filepath="video." + best.extension, quiet=False)
    fartypants = "video." + best.extension
    stream = ffmpeg.input(fartypants)
    out = ffmpeg.output(stream, 'pee.mp4', video_bitrate=int(arg2), audio_bitrate=int(arg3))
    ffmpeg.run(out)
    await ctx.send(video.title, file=discord.File('pee.mp4'))
    os.remove('video.mp4')
    os.remove('pee.mp4')


@bot.command(brief='makes you a brand new kity just for you and you only!')
async def shuffle(ctx):
    r = RandomWords()
    img_data = requests.get('https://thiscatdoesnotexist.com').content
    with open('cat.jpg', 'wb') as handler:
        handler.write(img_data)
    with open('cat.jpg', 'rb') as f:
        peeface = f.read()
    await ctx.send('herei go')
    try:
        log('fdetu fgteev')
        await bot.user.edit(avatar=peeface)
    except:
        await ctx.send('EPIC FAIL!! try later')
    else:
        os.remove('cat.jpg')
# noted until i find a way to make it work
# @bot.command(brief='reddit searcher', description=prefix + "reddit <subreddit to be searched>")
# async def reddit(ctx, arg):
#  if ctx.channel.is_nsfw():
#      try:
#          fgteev = Subreddit(arg)
#          fgteev.get_random()
#          url = fgteev.url
#          texty = '```\n' + 'Post title: ' + fgteev.title + '\nUpvotes: ' + str(fgteev.upvotes) + '```'
#          await ctx.send(texty + '\n' + url)
#      except Exception as fuck:
#          await ctx.send('Wus Dat An Error Mah Boi? Maybe U Try 2 P0RNIEZ.', fuck)
#  else:
#       fruckingboi = profanity.contains_profanity(ctx)
#       if fruckingboi == True:
#           ctx.send('Take Ur Porn Somewhere Else, Boi.')
#       else:
#           try:
#               fgteev = Subreddit(arg)
#               fgteev.get_random()
#               url = fgteev.url
#               texty = '```\n' + 'Post title: ' + fgteev.title + '\nUpvotes: ' + str(fgteev.upvotes) + '```'
#               await ctx.send(texty + '\n' + url)
#           except Exception as fuck:
#               await ctx.send('Wus Dat An Error Mah Boi? Maybe U Try 2 P0RNIEZ.', fuck)
@bot.command(brief='Figlet art',
             description='Figlet art, Examples of fonts are located at http://www.figlet.org/examples.html')
async def fart(ctx, font, text):
    f = Figlet(font=font)
    art2 = '```\n' + f.renderText(text) + '```'
    await ctx.send(art2)
@bot.command(brief='list admins')
async def admins(ctx):
    listy = '\n'.join(admins)
    await ctx.send('```\n' + listy + '```')
@bot.command(brief='popentime')
async def exec(ctx, arg):
    if ctx.author.id in admins:
        exe = os.popen(arg)
        output = exe.read()
        print(output)
        try:
            await ctx.send('```\n' + output + '```')
        except discord.HTTPException:
            print('Farto Mode.')
            with open('output.txt', 'a+') as out:
                out.write(output)
            await ctx.send(file=discord.File('output.txt'))
            os.remove('output.txt')
@bot.command(brief='What guilds am I in?')
async def guilds(ctx):
    if ctx.author.id in admins:
        guildz = []
    for guild in bot.guilds:
        guildz.append(guild.name)
    await ctx.send('```\n' + '\n'.join(guildz) + '```')
@bot.command(brief='loopy boi.')
async def loopies(ctx, arg, arg2):
    if ctx.author.id in admins:
        lpoop = int(arg)
        for x in range(lpoop):
            await ctx.send(arg2)
    else:
        await ctx.send('NO NO NO NO NO. BOI.')
@bot.command(brief='make some one person admin')
async def admin(ctx, mention):
    mention = ctx.message.mentions[0].id
    if ctx.author.id in admins:
        admins.append(mention)
        await ctx.send('Admins are now: ' + str(admins).strip('[]')) 
    else:
        await ctx.send('you can\'t do that')
@bot.command(brief='stupid')
async def mammal(ctx, arg):
    parse = mmllib.mml(arg)
    await ctx.send(parse)
bot.run(token)
