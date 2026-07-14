import os
import sys
import zipfile
import requests
import telebot
from flask import Flask
from threading import Thread

# 1. تشغيل سيرفر وهمي في الخلفية لمنع منصة Render من إيقاف الخدمة
app = Flask(__name__)

@app.route('/')
def home():
    return "TheebScan is Live!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# تشغيل خادم الويب في مسار منفصل
Thread(target=run_flask).start()

# 2. إعدادات البوت والتوكن الخاص بك
BOT_TOKEN = "8611270909:AAGUPPLRHD1oa9YVCjTpF-1qJgxFuoJh2RE"
bot = telebot.TeleBot(BOT_TOKEN)

LIBRARY_URL = "https://google.com"

print("جاري تحميل مكتبة TheebScan...")
try:
    r = requests.get(LIBRARY_URL)
    with open("lib.zip", "wb") as f:
        f.write(r.content)
    with zipfile.ZipFile("lib.zip") as z:
        z.extractall("./theebscan")
    print("تم تحميل المكتبة ✅")
except Exception as e:
    print(f"فشل تحميل المكتبة: {e}")

sys.path.append('./theebscan')
try:
    from theebscan import TheebScan
    scanner = TheebScan()
except Exception as e:
    print(f"خطأ في استيراد المكتبة: {e}")
    scanner = None

@bot.message_handler(commands=['start'])
def start(message): 
    bot.reply_to(message, "أهلاً بك يا طناف في بوت TheebScan 💰\nارسل رقم الحساب الذي تريد فحصه.")

@bot.message_handler(func=lambda m: True)
def scan_account(message):
    account = message.text.strip()
    bot.reply_to(message, f"جاري فحص الحساب: {account} ...")
    
    if not scanner:
        bot.reply_to(message, "المكتبة غير جاهزة حالياً، يرجى المحاولة لاحقاً.")
        return

    try:
        result = scanner.check(account)
        bot.reply_to(message, f"نتيجة الفحص:\n{result}")
    except Exception as e: 
        bot.reply_to(message, f"حدث خطأ أثناء الفحص: {e}")

# 3. تشغيل البوت بنظام الفحص المستمر والآمن وتجاهل أخطاء الشبكة المؤقتة
print("البوت يعمل الآن تلقائياً...")
bot.infinity_polling(timeout=10, long_polling_timeout=5)


