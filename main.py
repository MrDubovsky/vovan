import telebot
import os
import threading
import time
import requests
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

# Запуск бота в отдельном потоке
def run_bot():
    bot.infinity_polling()

# Заглушка Flask
@app.route('/')
def home():
    return 'Bot is running!'

# Функция пинга своего же сервера, чтобы не засыпал Render
def keep_alive():
    while True:
        try:
            url = "https://" + os.getenv("RENDER_EXTERNAL_HOSTNAME", "127.0.0.1") + "/"
            requests.get(url)
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(600)  # каждые 10 минут

# Запускаем всё
if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    threading.Thread(target=keep_alive).start()
    app.run(host='0.0.0.0', port=10000)
