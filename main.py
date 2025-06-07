import telebot
import os
from flask import Flask
from threading import Thread

TOKEN = os.getenv("BOT_TOKEN")  # ✅ Используй переменную окружения
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Вот ссылка на сайт: https://vovan.link/tgru")

def run_bot():
    bot.infinity_polling()

@app.route('/')
def home():
    return 'Bot is running!'

if __name__ == '__main__':
    Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)
