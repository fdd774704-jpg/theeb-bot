flask import Flask, request
import telebot

# 1. التوكن الخاص بك تم ترتيبه وتثبيته بشكل صحيح ومستقيم هنا
BOT_TOKEN = "8611270909:AAHiDyDpMsVAc8IPVXDrVT8-pQUNsl"

# 2. تم تعديل الرابط هنا ليكون رابط تطبيقك الفعلي المخصص على سيرفر Render
WEBHOOK_URL = "https://theeb-bot-1.onrender.com" 

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@ap

