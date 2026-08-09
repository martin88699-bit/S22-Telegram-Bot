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
        "🎁 活动/Promotion\n\n"
        "欢迎奖金500％/WELCOME BONUS 500％。\n\n"
        "点击下面查看详情/CLICK BAWAH PILIH：",
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
                "🏠 返回主菜单/BACK MENU",
                callback_data="back_menu"
            )
        ],
    ]

    await query.edit_message_text(
        "🎁 活动详情\n\n"
        "欢迎奖金500％。\n\n"
        "
500% 首存奖金
开启您的幸运之旅！参与 S22 ENTERTAINMENT CITY 500% 首存奖金，存款最低 RM100，更长的游戏时间，以及更多中奖机会，畅玩所有老虎机游戏！

活动详情
最低存款
RM100

流水要求
x18

参与方式
注册全新的 S22 ENTERTAINMENT CITY 账号。

登录您的账户。

完成首次存款，最低 RM100。

存款成功后，奖金将自动发放至奖金钱包（Bonus Wallet）

适用游戏
本活动适用于所有老虎机游戏。

仅符合资格的老虎机有效投注计入流水要求。

条款与条件
本活动仅限新会员参加，并仅适用于首次成功存款。

会员必须完成 18 倍流水要求（以存款金额 + 奖金金额计算）后，方可申请提款。

示例：

存款：RM100

奖金：RM100

总金额：RM200

所需流水：RM3600（RM200x18流水）

第一次充值100％ X18倍流水
第二次充值100％ X18倍流水
第三次充值100％ X18倍流水
第四次充值100％ X18倍流水
第五次充值100％ X18倍流水

总数500％ BONUS

奖金将发放至奖金钱包（Bonus Wallet），完成全部流水要求后方可提款或转账。

仅符合资格的老虎机游戏有效投注计入流水要求。取消、无效、退款或作废投注均不计入流水。

本活动奖金有效期为 30 天。逾期未完成流水要求，未使用的奖金及相关盈利将自动失效。

体育、真人娱乐场、捕鱼、彩票、街机、虚拟游戏、棋牌游戏及其他非老虎机游戏类别的投注均不计入流水要求。

本活动每位会员仅可领取一次，奖金不得转让、兑换现金或与其他首存优惠同时使用。

会员不得同时享有多个进行中的优惠活动。必须完成、取消或放弃当前优惠后，方可领取新的优惠。

如发现任何滥用奖金、异常投注、套利、对冲、串通或利用系统漏洞等行为，S22 有权立即取消所有奖金及相关盈利。

每位用户、每个家庭、IP 地址、设备、电子邮箱、手机号码、付款方式或公共电脑仅允许注册一个账户。重复或关联账户将被取消活动资格。

活动一经激活，在完成流水要求或放弃奖金前，不得进行提款或转账。

S22 保留随时修改、暂停、终止本活动或调整相关条款与条件的权利，恕不另行通知。

如有任何争议，S22 保留最终解释权及最终决

。",
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
