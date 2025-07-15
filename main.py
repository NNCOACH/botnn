from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers import motivation, ask_gpt

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрация хендлеров
motivation.register(dp)
ask_gpt.register(dp)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Ты в NN COACH. Готов стать машиной? 💥")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)