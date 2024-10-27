import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import io
from utils.crud import get_user_messages

class Chart(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog: chart.py загружен")

    @commands.slash_command(
        description="Отправляет в чат график сообщений, которые Вы писали в игровой чат"
    )
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def show_chart(self, ctx):
        await ctx.respond("*Отправка графика...*")

        result = get_user_messages()

        # Обработка данных
        hour_message_count = {}
        for log in result:
            hour = log.date[11:13]
            hour_message_count[hour] = hour_message_count.get(hour, 0) + 1

        hours = list(hour_message_count.keys())
        message_counts = list(hour_message_count.values())

        # Постройка графика
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 8))
        plt.plot(hours, message_counts, marker='o', linestyle='--', linewidth=2)

        plt.title('Зависимость кол-ва сообщений от времени', fontweight='bold')
        plt.xlabel('Дата и время', fontweight='bold')
        plt.ylabel('Кол-во сообщений', fontweight='bold')
        
        plt.grid(True)
        plt.tight_layout()

        # Сохранение в буфер
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        plt.close()

        # Отправка в канал
        await ctx.send(file=discord.File(buffer, 'message_chart.png'))
        buffer.close()

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(f"Команда на кулдауне. Попробуйте снова через {round(error.retry_after, 2)} сек.", ephemeral=True)
        else:
            raise error

def setup(client):
    client.add_cog(Chart(client))
