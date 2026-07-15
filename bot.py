import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

# جلب التوكن تلقائيًا من البيئة لضمان الأمان والتشغيل الصحيح
TOKEN = os.environ.get("BOT_TOKEN")
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
        "مرحبًا بك في بوابة الذيــب الملكية 👑\n\n"
        "أنت هنا في المكان المخصص لكبار الشخصيات.\n"
        "اضغط على زر الدفع الفاخر بالأسفل لتفعيل اشتراكك فورًا:",
        reply_markup=markup
    )

# ============================
#   إعداد الـ Webhook للسيرفر
# ============================
@app.route('/' + TOKEN if TOKEN else '', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Forbidden", 403

@app.route('/')
def index():
    return "Theeb Royal Bot is Running 👑", 200

# ============================
#   تشغيل السيرفر على ريندر
# ============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

