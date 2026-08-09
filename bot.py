import os
import asyncio
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# =========================
# Telegram Bot Token
# =========================

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
# 主菜单
# =========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    kb = [
        [
            InlineKeyboardButton(
                "🎮 开始游戏",
                url="https://h5.ddwin01.com/#/Home"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 注册账号",
                url="https://go.crisp.chat/chat/embed/?website_id=029a087e-7f0f-4034-a119-fdef568c3105"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 优惠活动",
                callback_data="promotion"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 联系客服",
                url="https://wa.me/601175766643"
            )
        ]
    ]

    await update.message.reply_text(
        "🎉 欢迎来到 S22 ENTERTAINMENT CITY\n\n"
        "请选择您需要的服务：",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 优惠活动
# =========================

async def promotion(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    # 告诉 Telegram 已经收到按钮点击
    await query.answer()

    text = (
        "🎁 S22 ENTERTAINMENT CITY 优惠活动\n\n"

        "🔥 500% 首存奖金\n\n"

        "💰 最低存款：RM100\n"
        "🎰 适用于：老虎机游戏\n"
        "🔄 流水要求：x22\n\n"

        "📋 参与方式\n"
        "1️⃣ 注册全新的 S22 账号\n"
        "2️⃣ 登录您的账号\n"
        "3️⃣ 完成首次存款，最低 RM100\n"
        "4️⃣ 存款成功后按照活动规则获得优惠\n\n"

        "📞 如需帮助，请联系客服。"
    )

    kb = [
        [
            InlineKeyboardButton(
                "📝 注册账号",
                url="https://go.crisp.chat/chat/embed/?website_id=029a087e-7f0f-4034-a119-fdef568c3105"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 联系客服",
                url="https://wa.me/601175766643"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 返回主菜单",
                callback_data="main_menu"
            )
        ]
    ]

    await query.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 返回主菜单
# =========================

async def main_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🎮 开始游戏",
                url="https://h5.ddwin01.com/#/Home"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 注册账号",
                url="https://go.crisp.chat/chat/embed/?website_id=029a087e-7f0f-4034-a119-fdef568c3105"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 优惠活动",
                callback_data="promotion"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 联系客服",
                url="https://wa.me/601175766643"
            )
        ]
    ]

    await query.message.reply_text(
        "🎉 欢迎来到 S22 ENTERTAINMENT CITY\n\n"
        "请选择您需要的服务：",
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


# /start
app.add_handler(
    CommandHandler("start", start)
)


# 🎁 优惠活动按钮
app.add_handler(
    CallbackQueryHandler(
        promotion,
        pattern="^promotion$"
    )
)


# 🔙 返回主菜单
app.add_handler(
    CallbackQueryHandler(
        main_menu,
        pattern="^main_menu$"
    )
)


# =========================
# Main
# =========================

async def main():

    # 启动 Render Web Server
    threading.Thread(
        target=run_web,
        daemon=True
    ).start()

    # 初始化 Telegram Bot
    await app.initialize()

    await app.start()

    await app.updater.start_polling()

    print("Bot is running...")

    # 保持程序一直运行
    await asyncio.Event().wait()


# =========================
# Run
# =========================

if __name__ == "__main__":
    asyncio.run(main())
