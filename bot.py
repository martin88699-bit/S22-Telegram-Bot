import os
import asyncio
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# =========================
# BOT TOKEN
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
        port=port,
    )


# =========================
# 主菜单
# =========================

def main_menu():

    kb = [
        [
            InlineKeyboardButton(
                "🎮 开始",
                callback_data="start_game"
            )
        ],
        [
            InlineKeyboardButton(
                "📝 注册",
                callback_data="register"
            )
        ],
        [
            InlineKeyboardButton(
                "🎁 活动",
                callback_data="promotion"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 联系客服",
                callback_data="customer_service"
            )
        ],
    ]

    return InlineKeyboardMarkup(kb)


# =========================
# /start
# =========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🤖 欢迎来到测试机器人\n\n"
        "请选择下面的按钮：",
        reply_markup=main_menu()
    )


# =========================
# 🎮 开始
# =========================

async def start_game(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🔙 返回主菜单",
                callback_data="back_menu"
            )
        ]
    ]

    await query.edit_message_text(
        "🎮 开始\n\n"
        "这是开始页面测试。",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 📝 注册
# =========================

async def register(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🔙 返回主菜单",
                callback_data="back_menu"
            )
        ]
    ]

    await query.edit_message_text(
        "📝 注册\n\n"
        "这是注册页面测试。",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 🎁 活动
# =========================

async def promotion(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🎁 查看活动详情",
                callback_data="promotion_detail"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 返回主菜单",
                callback_data="back_menu"
            )
        ],
    ]

    await query.edit_message_text(
        "🎁 活动\n\n"
        "目前有一个测试活动。\n\n"
        "点击下面查看详情：",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 🎁 活动详情
# =========================

async def promotion_detail(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🔙 返回活动",
                callback_data="promotion"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 返回主菜单",
                callback_data="back_menu"
            )
        ],
    ]

    await query.edit_message_text(
        "🎁 活动详情\n\n"
        "这里是活动详情测试页面。\n\n"
        "以后可以把你的普通活动内容放在这里。",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 📞 客服
# =========================

async def customer_service(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "💬 在线客服",
                url="https://example.com"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 返回主菜单",
                callback_data="back_menu"
            )
        ],
    ]

    await query.edit_message_text(
        "📞 联系客服\n\n"
        "请选择下面的客服入口：",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 🔙 返回主菜单
# =========================

async def back_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🤖 欢迎来到测试机器人\n\n"
        "请选择下面的按钮：",
        reply_markup=main_menu()
    )


# =========================
# 用户输入文字
# =========================

async def text_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "⚠️ 请使用机器人提供的按钮进行操作。"
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


# =========================
# 按钮处理
# =========================

app.add_handler(
    CallbackQueryHandler(
        start_game,
        pattern="^start_game$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        register,
        pattern="^register$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        promotion,
        pattern="^promotion$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        promotion_detail,
        pattern="^promotion_detail$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        customer_service,
        pattern="^customer_service$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        back_menu,
        pattern="^back_menu$"
    )
)


# 用户发送普通文字
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        text_message
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

    # 初始化 Bot
    await app.initialize()

    # 启动 Bot
    await app.start()

    # 启动 Polling
    await app.updater.start_polling()

    print("Telegram Bot is running...")

    # 保持运行
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
