import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

# وضع التوكن الخاص بك مباشرة هنا ليعمل البوت فوراً وبدون تعقيد Render
TOKEN = "8611270909:AAHiDyDpMsVAc8IPVXDrVT8-pQUNsFYc24U"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# ============================
#   رسالة /start الملكية
# ============================
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    pay_button = InlineKeyboardButton(
        text="👑 بوابة الدفع الملكية (VIP)",
        url="https://paypal.me/TheebRoyalGate"
    )
    markup.add(pay_button)

    bot.send_message(
        message.chat.id,
        "مرحباً بك في بوابة الذيــب الملكية 👑\n\n"
        "اضغط على زر الدفع الفاخر بالأسفل لتفعيل اشتراكك:",
        reply_markup=markup
    )

# ============================
#   Webhook
# ============================
@app.route('/' + TOKEN, methods=['POST'])
def receive_update():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/")
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{request.host}/{TOKEN}")
    return "Webhook set", 200

# ============================
#   تشغيل السيرفر على Render
# ============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


