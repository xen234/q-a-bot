import re
from aiogram import types
from aiogram.utils import executor

from bot_config import dp, database
from bot_config import api, scheduler
from datetime import datetime


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Это Q&A бот для абитриентов и студентов ФКН ВШЭ"
                        "Для просмотра доступных команд наберите /help")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Бот находится в разработке и собирает Ваши запросы для обучения модели. "
                        "Спросите его о чем-нибудь при помощи команды /ask")


@dp.message_handler(commands=['list'])
async def process_list_command(message: types.Message):
    await database.save_question(message.from_user.id, message)


if __name__ == '__main__':
    executor.start_polling(dp)
