import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("🎮 开始游戏", url="https://h5.ddwin01.com/#/Home")],
        [InlineKeyboardButton("📝 注册账号", url="https://go.crisp.chat/chat/embed/?website_id=029a087e-7f0f-4034-a119-fdef568c3105")],
        [InlineKeyboardButton("📞 联系客服", url="https://wa.me/601175766643")]
    ]

    await update.message.reply_text(
        "欢迎来到 S22 ENTERTAINMENT CITY",
        reply_markup=InlineKeyboardMarkup(kb)
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))


async def main():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    print("Bot is running...")

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
