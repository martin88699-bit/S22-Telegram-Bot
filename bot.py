import os
import asyncio

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


TOKEN = os.environ["BOT_TOKEN"]


# =========================
# 主菜单
# =========================

def get_main_menu():

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
                "📞 客服",
                callback_data="customer_service"
            )
        ]
    ]

    return InlineKeyboardMarkup(kb)


# =========================
# /start
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 欢迎来到测试机器人\n\n"
        "请选择您需要的服务：",
        reply_markup=get_main_menu()
    )


# =========================
# 🎮 开始
# =========================

async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🎮 开始\n\n"
        "按钮测试成功！",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🔙 返回主菜单",
                    callback_data="back_menu"
                )
            ]
        ])
    )


# =========================
# 📝 注册
# =========================

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "📝 注册\n\n"
        "按钮测试成功！",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🔙 返回主菜单",
                    callback_data="back_menu"
                )
            ]
        ])
    )


# =========================
# 🎁 活动
# =========================

async def promotion(update: Update, context: ContextTypes.DEFAULT_TYPE):

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
        ]
    ]

    await query.edit_message_text(
        "🎁 活动\n\n"
        "这里是活动测试页面。",
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
        ]
    ]

    await query.edit_message_text(
        "🎁 活动详情\n\n"
        "按钮跳转测试成功！",
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

    await query.edit_message_text(
        "📞 客服\n\n"
        "这是客服按钮测试页面。",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🔙 返回主菜单",
                    callback_data="back_menu"
                )
            ]
        ])
    )


# =========================
# 🔙 返回主菜单
# =========================

async def back_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "🤖 欢迎来到测试机器人\n\n"
        "请选择您需要的服务：",
        reply_markup=get_main_menu()
    )


# =========================
# 创建 Bot
# =========================

app = (
    Application
    .builder()
    .token(TOKEN)
    .build()
)


# =========================
# Handler
# =========================

app.add_handler(
    CommandHandler("start", start)
)

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


# =========================
# 启动
# =========================

async def main():

    print("Bot starting...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("Bot is running!")

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
