from aiogram.types import Message

from loader import dp 
from utils import texts

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    id = message.from_user.id
    print(message)

    await message.answer(texts.start(
        first_name=first_name,
        username=username,
        id=id
    ))

