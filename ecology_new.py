import random
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def info(ctx):
    await ctx.send('Привет. Я бот об экологии. Я помогу тебе понять какие экологические проблемы существуют и как их предотвратить.\n','\n'
                   'problems-расскажет тебе какие экологические проблемы есть в мире по сей день\n'
                   'mems-покажет тебе мемы связанные с экологией\n')

@bot.command()
async def problems(ctx):
    eco_problems='1. Загрязнение воды', "2. Загрязнение воздуха","3. Вымирание животных","4. Природный катаклизм"
    # ecoco=random.choice(eco_problems)
    await ctx.send(eco_problems)


@bot.command()
async def mems(ctx):
    eco_pictures = os.listdir('eco')
    random_pictures=random.choice(eco_pictures)
    with open(f'eco/{random_pictures}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("")