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
        ],
        [
            InlineKeyboardButton(
                "🎁 无限充值RM50送RM5/UNLIMITED TOPUP RM50FREE 5",
                callback_data="topup_bonus"
            )  
        ],  
        [              
            InlineKeyboardButton(
                "📞 线上客服/ONLINE CUSTOMER SERVICE ",
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

        
        "1️⃣ 第一次充值100％ x22流水\n"
        "2️⃣ 第二次充值100％ x22流水\n"
        "3️⃣ 第三次充值100％ x22流水\n"
        "4️⃣ 第四次充值100％ x22流水\n"
        "5️⃣ 第五次充值100％ x22流水\n\n"
        
        "🧧总数500％奖金"
        "📞 如需帮助，请联系客服。"
        
        "🎁 PROMOSI S22 ENTERTAINMENT CITY\n\n"

        "🔥 500% WELCOME BONUS\n\n"

        "💰 Deposit Minimum: RM100\n"
        "🎰 Permainan: Slot Sahaja\n"
        "🔄 Turnover：x22\n\n"

        "📋 Cara Menyertai\n"
        "1️⃣ Daftar akaun S22 yang baharu\n"
        "2️⃣ Log masuk ke akaun anda\n"
        "3️⃣ Buat deposit pertama dengan minimum RM100\n"
        "4️⃣ Selepas deposit berjaya, anda boleh menikmati promosi mengikut terma dan syarat promosi.\n\n"

        
        "1️⃣ Deposit Pertama — Bonus 100% × Turnover x22\n"
        "2️⃣ Deposit Kedua — Bonus 100% × Turnover x22\n"
        "3️⃣ Deposit Ketiga — Bonus 100% × Turnover x22\n"
        "4️⃣ Deposit KeEmpat — Bonus 100% × Turnover x22\n"
        "5️⃣ Deposit KeLima — Bonus 100% × Turnover x22 \n\n"

        "🧧TOTAL BONUS 500％"
        "📞 Jika anda memerlukan bantuan, sila hubungi khidmat pelanggan kami."
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
# 无限充值 RM50 送 RM5
# =========================

async def topup_bonus(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    text = (
        "🎁 无限充值 RM50 送 RM5\n\n"

        "💰 每次充值：RM50\n"
        "🎁 赠送奖金：RM5\n"
        "🔄 流水要求：x1\n\n"

        "📋 活动方式\n"
        "1️⃣ 每次充值 RM50\n"
        "2️⃣ 每次可获得 RM5 奖金\n"
        "3️⃣ 奖金流水要求为 x1\n"
        "4️⃣ 符合活动条件即可重复参与\n\n"

        "🧧 无限充值，RM50送RM5\n\n"

        "📞 如需帮助，请联系客服。"

       "🎁 UNLIMITED DEPOSIT TANPA HAD RM50 DAPAT RM5 \n\n"

        "💰 Setiap deposit: RM50\n"
        "🎁 Bonus diberikan: RM5\n"
        "🔄 Turnover：x1\n\n"

        "📋Cara Menyertai\n"
        "1️⃣ Setiap deposit RM50\n"
        "2️⃣ Setiap deposit akan menerima bonus RM5\n"
        "3️⃣ Turnover x1\n"
        "4️⃣ Boleh menyertai promosi ini berulang kali mengikut terma dan syarat


        "🧧UNLIMITED DEPOSIT TANPA HAD, RM50 DAPAT RM5\n\n"

        "📞Jika anda memerlukan bantuan, sila hubungi khidmat pelanggan kami."   
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
# 🎁 优惠活动按钮
app.add_handler(
    CallbackQueryHandler(
        topup_bonus,
        pattern="^topup_bonus$"
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
