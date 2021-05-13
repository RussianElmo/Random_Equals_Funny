from functions import *
import discord
from discord.ext import commands
import os


TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix=';')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def meme(ctx):
    get_image(get_classes())
    caption = get_caption()
    prepare_image(caption)
    file = discord.File('meme.jpg', filename='meme.jpg')
    await ctx.channel.send(file=file)


@bot.command()
async def addImg(ctx, *, message):
    add_to_file('Images.txt', message)
    await ctx.channel.send('Added successfully')


@bot.command()
async def addCap(ctx, *, message):
    add_to_file('Captions.txt', message)
    await ctx.channel.send('Added successfully')


@bot.command()
async def dispImg(ctx):
    image_list = ''
    with open('Images.txt') as f:
        for image in f.readlines():
            image_list += image
    await ctx.send(image_list)


@bot.command()
async def dispCap(ctx):
    caption_list = ''
    with open('Captions.txt') as f:
        for caption in f.readlines():
            caption_list += caption
    await ctx.send(caption_list)


@bot.command()
async def delImg(ctx, *, message):
    with open('Images.txt', 'r') as f:
        lines = f.readlines()
    with open('Images.txt', 'w') as f:
        for line in lines:
            if line.strip('\n') != message:
                f.write(line)
        lines = f.readlines()
    with open('Images.txt', 'w') as f:
        for line in lines:
            if line != '':
                f.write(line)


@bot.command()
async def deleteCaption(ctx, *, message):
    with open('Captions.txt', 'r') as f:
        lines = f.readlines()
    with open('Captions.txt', 'w') as f:
        for line in lines:
            if line.strip('\n') != message:
                f.write(line)
        lines = f.readlines()
    with open('Captions.txt.txt', 'w') as f:
        for line in lines:
            if line != '':
                f.write(line)


@bot.command()
async def commands(ctx):
    with open('help.txt') as f:
        help_list = ''
        for line in f.readlines():
            help_list += line
        await ctx.send(help_list)


bot.run(TOKEN)
