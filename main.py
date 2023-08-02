import discord
import random
from discord.ext import commands
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(intents=intents,command_prefix="!")

def generate(pas_len):
    list_numbers = "1234567890"
    list_letter = "qwertyuiopasdfghjklzxcvbnm"
    list_letter = list_letter + list_letter.upper()
    list_symbols = "!@#$%^&*()?|/~"
    list_all = list_numbers + list_letter + list_symbols

    password = ""
    for i in range(pas_len):
        password += random.choice(list_all)
    return password
        

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Привет,я бот и умею генирировать пароли)\nВоспользуйтесь командой :\n!password")
    
@bot.command()
async def password(ctx, pas_len = 8):
    text = "Ваш пароль :"+generate(pas_len)
    await ctx.send(text)
    
    
@bot.command()
async def howAreU(ctx)
    await ctx.send("Нормально как у вас?")
    
@bot.command()
async def help(ctx):
    help = "В боте есть команда password которая генерирует пароль,есть команда howAreU ,и команда hello"
    await ctx.send(help)
    
    
    
    
bot.run("")
