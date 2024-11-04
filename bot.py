from aiogram import executor

from loader import dp, bot 
from utils.env import ADMIN

import handlers

async def on_startup(dp):

    await bot.send_message(ADMIN, 'Bot ishga tushdi')

executor.start_polling(dp, on_startup=on_startup, skip_updates=False)