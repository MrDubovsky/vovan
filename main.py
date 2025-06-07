import telebot
import os

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Вот ссылка на сайт: https://vovan.link/tgru")

print("Бот запущен")
bot.infinity_polling()
