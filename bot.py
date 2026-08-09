from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)


# =========================
# 开始菜单
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
        "🎰 欢迎来到 S22 ENTERTAINMENT CITY\n\n"
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
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🎁 500% 首存奖金",
                callback_data="bonus500"
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
        "🎁 S22 ENTERTAINMENT CITY 优惠活动\n\n"
        "🔥 500% 首存奖金\n\n"
        "💰 最低存款：RM100\n"
        "🎯 流水要求：x22\n"
        "🎰 适用于老虎机游戏\n\n"
        "点击下方查看活动详情 👇",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 500% 活动详情
# =========================

async def bonus500(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    kb = [
        [
            InlineKeyboardButton(
                "🎮 立即开始游戏",
                url="https://h5.ddwin01.com/#/Home"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 返回优惠活动",
                callback_data="promotion"
            )
        ]
    ]

    await query.edit_message_text(
        "🎁 500% 首存奖金\n\n"
        "✨ 开启您的幸运之旅！\n\n"
        "💰 最低存款：RM100\n"
        "🎁 首存奖金：最高 500%\n"
        "🎯 流水要求：x22\n"
        "🎰 适用于老虎机游戏\n\n"
        "📌 参与方式：\n"
        "1️⃣ 注册全新的 S22 ENTERTAINMENT CITY 账号\n"
        "2️⃣ 登录您的账户\n"
        "3️⃣ 完成首次存款，最低 RM100\n"
        "4️⃣ 存款成功后，奖金按照活动规则发放\n\n"
        "祝您游戏愉快 🍀",
        reply_markup=InlineKeyboardMarkup(kb)
    )


# =========================
# 返回主菜单
# =========================

async def back_menu(
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

    await query.edit_message_text(
        "🎰 欢迎来到 S22 ENTERTAINMENT CITY\n\n"
        "请选择您需要的服务：",
        reply_markup=InlineKeyboardMarkup(kb)
    )app.add_handler(
    CallbackQueryHandler(promotion, pattern="^promotion$")
)

app.add_handler(
    CallbackQueryHandler(bonus500, pattern="^bonus500$")
)

app.add_handler(
    CallbackQueryHandler(back_menu, pattern="^back_menu$")
)
