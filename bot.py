from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print("Бот запущен")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n"
"Чтобы узнать команды, набери: /help")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("ВОТ СПРАВКА ПО БОТУ!\n"
"/start -начало работы с ботом\n"
"/help - справка по боту!\n"
"/name - узнать имя бота!\n"
"А если ты напишешь мне просто текст, я стану повторюшой, и буду тебе отсылать то, что ты мне написал!!! ха-ха-ха!!")

@dp.message_handler(commands=['name'])
async def process_name_command(message: types.Message):
    await message.reply("Меня зовут Алёшка! А как твое имя?")

@dp.message_handler()
async def echo_message(msg: types.Message):
                await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)
