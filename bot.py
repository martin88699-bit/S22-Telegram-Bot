import os
import asyncio
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.environ["BOT_TOKEN"]


# =========================
# Render Web Server
# =========================

web = Flask(__name__)


@web.route("/")
def home():
    return "Telegram Bot is running!"


@web.route("/health")
def health():
    return "OK"


def run_web():
    port = int(os.environ.get("PORT", 10000))

    web.run(
        host="0.0.0.0",
        port=port
    )


# =========================
# Telegram Bot
# =========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    kb = [
        [
            InlineKeyboardButton(
                "🎮 开始游戏/START GAME",
                url="https://h5.ddwin01.com/#/Home"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 注册账号/REGISTER",
                url="https://go.crisp.chat/chat/embed/?website_id=029a087e-7f0f-4034-a119-fdef568c3105"
            )
        ],
        [
          InlineKeyboardButton(
                "🎁 优惠活动/PROMOTION",
                callback_data="promotion"
          )
            InlineKeyboardButton(
                "📞 联系客服/CUSTOMER SERVICE",
                url="https://wa.me/601175766643"
            )
        ]
    ]

    await update.message.reply_text(
        "欢迎来到 S22 ENTERTAINMENT CITY",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# Bot Application
# =========================

app = (
    Application
    .builder()
    .token(TOKEN)
    .build()
)

app.add_handler(
    CommandHandler("start", start)
)


async def main():

    # 启动 Render Web Server
    threading.Thread(
        target=run_web,
        daemon=True
    ).start()

    # 启动 Telegram Bot
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("Bot is running...")

    # 一直运行
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
