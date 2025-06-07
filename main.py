import telebot
import os
import threading
from flask import Flask

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise Exception("BOT_TOKEN не задан!")

# Инициализация бота и Flask
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Вот ссылка на сайт: https://vovan.link/tgru")

# Запускаем бота в отдельном потоке
def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

# Заглушка Flask
@app.route('/')
def home():
    return 'Bot is running!'

# Запуск Flask-сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
