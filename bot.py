import os
from flask import Flask, request
import telebot

# ضع التوكن السري الخاص بك هنا مباشرة بين علامتي التنصيص:
BOT_TOKEN = "اكتب_التوكن_الخاص_بك_هنا"
WEBHOOK_URL = "https://onrender.com" 

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/' + BOT_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! تم تشغيل البوت بنجاح وأمان.")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + '/' + BOT_TOKEN)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


