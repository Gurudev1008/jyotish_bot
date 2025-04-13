import os
import sqlite3
import asyncio
from flask import Flask, request, abort
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

load_dotenv()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
DATABASE_PATH = os.getenv("DATABASE_PATH", "jyotish.db")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get("x-secret") != WEBHOOK_SECRET:
        abort(403)

    data = request.json
    if data and data.get("status") == "success":
        tg_id = data["custom_fields"]["tg_id"]
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO users (tg_id, is_paid) VALUES (?, ?)", (tg_id, 1))
        conn.commit()
        conn.close()

        asyncio.run(bot.send_message(chat_id=tg_id, text="✅ Оплата получена! Отправьте дату, время и место рождения."))
        return "OK"
    return "ignored"
