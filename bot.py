import os
from flask import Flask, request
import telebot

# التوكن الصحيح الخاص بك
BOT_TOKEN = "811270909:AAHiDyDpMsVAc8lPVXDrVT8-pQUNsFYc24U"
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

# الصفحة الرئيسية للتأكد من عمل السيرفر
@app.route('/')
def index():
    return "TheebScan is Live and Running!"

# استقبال الرسائل من تليجرام عبر Webhook
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def respond():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return "OK", 200

# أوامر البوت الأساسية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! بوت TheebScan يعمل الآن بنجاح وبشكل مستقر 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلت رسالتك: {message.text}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
