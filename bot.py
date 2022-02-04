import logging
from aiogram import Bot, Dispatcher, executor, types

from checkwords import check_words
from transliterate import to_latin, to_cyrillic

API_TOKEN = '5214638248:AAHjwQz0ldBn0JArGlc2YJdKVvp8dsm2ugs'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
db = Dispatcher(bot)


@db.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply('Assalomu alaykum🙂\nImlo qoidalari asosida ishlovchi botga xush kelibsiz!')


@db.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.answer('Botdan foydalanish uchun so`z yuboring ')


@db.message_handler()
async def check_imlo(message: types.Message):
    word = to_cyrillic(message.text)
    result = check_words(word)
    if result['avalable']:
        response = f"✅{word.capitalize()}\n"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.answer(to_latin(response))


if __name__ == '__main__':
    executor.start_polling(dispatcher=db, skip_updates=True)
