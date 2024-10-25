import discord
from discord.ext import commands
import os
import sys
from backend import client, discord_token, log, presence
import discord.utils


@client.event
async def on_ready():
    log.info(f"Бот включён. Работает как {client.user}")
    await client.change_presence(activity=discord.Game(name=presence))
    
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

try:
    client.run(discord_token)
except discord.LoginFailure:
    log.critical("Неправильный токен бота. Проверь, пожалуйста, ещё раз")
    sys.exit()
except Exception as err:
    log.critical(f"Ошибка подключения к дискорду: {err}")
    sys.exit()
