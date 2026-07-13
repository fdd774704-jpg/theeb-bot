import telebot, requests, zipfile, sys

BOT_TOKEN = "   8611270909:AAGUPPLRHD1oa9YVCjTpF-1qJgxFuoJh2RE" 
bot = telebot.TeleBot(BOT_TOKEN)

LIBRARY_URL = "https://drive.google.com/uc?export=download&id=15oLrJGYcNBn5KHcZDtuTi1W3vdi0Axhv"

print("جاري تحميل مكتبة TheebScan...")
r = requests.get(LIBRARY_URL)
open("lib.zip", "wb").write(r.content)
zipfile.ZipFile("lib.zip").extractall("./theebscan")
print("تم تحميل المكتبة ✅")

sys.path.append('./theebscan')
from theebscan import TheebScan
scanner = TheebScan()

@bot.message_handler(commands=['start'])
def start(message): 
    bot.reply_to(message, "اهلاً بك يا طناف في بوت TheebScan 💰\nارسل رقم الحساب اللي تبي تفحصه")

@bot.message_handler(func=lambda m: True)
def scan_account(message):
    account = message.text.strip()
    bot.reply_to(message, f"جاري فحص الحساب: {account} ...")
    try:
        result = scanner.check(account)
        bot.reply_to(message, f"نتيجة الفحص:\n{result}")
    except Exception as e: 
        bot.reply_to(message, f"صار خطأ: {e}")

print("البوت شغال...")
bot.infinity_polling()
