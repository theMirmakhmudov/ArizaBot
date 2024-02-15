import asyncio
import logging
from config import TOKEN
from aiogram import types
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F
from buttons import ariza, full_button

# from aiogram.types import ReplyKeyboardRemove


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
data = []

group_id = -1002047220127


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Salom hurmatli <b>{message.from_user.first_name}</b>",
                         parse_mode="HTML", reply_markup=ariza)


@dp.message(F.text == "Ariza qoldirish 📩")
async def get_arizza(message: types.Message):
    await message.answer("Ariza qoldirish uchun quyidagilarni kiriting 📩", reply_markup=full_button)


@dp.message(F.text == "Ism")
async def ism(message: types.Message):
    await message.answer("Ismingizni kiriting:", reply_markup=full_button)

    @dp.message(F.text)
    async def get_ism(message: types.Message):
        await message.answer("Qabul qilindi",reply_markup=full_button)
        print(message.text)
        data.append(message.text)


@dp.message(F.text == "Telefon raqam")
async def phone_number(message: types.Message):
    await message.answer("Telefon raqamingizni kiriting:", reply_markup=full_button)

    @dp.message(F.text)
    async def get_phone_number(message: types.Message):
        print(message.text)
        data.append(message.text)


@dp.message(F.location)
async def address_location(message: types.Message):
    await message.answer("Lokatsiya qabul qilindi")
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    data.append(latitude)
    data.append(longitude)


@dp.message(F.text == "Tumani")
async def region(message: types.Message):
    await message.answer("Tumaningizni kiriting:", reply_markup=full_button)

    @dp.message(F.text)
    async def get_region(message: types.Message):
        print(message.text)
        data.append(message.text)


@dp.message(F.text == "Ma'lumotlarni Tasdiqlash")
async def check_data(message: types.Message):
    await bot.send_message(group_id, f"Ism : {data[0]}\nTelefon Raqam : {data[1]}\nTuman:{data[-1]}")
    await bot.send_location(group_id, data[2], data[3])
    await message.answer("Ma'lumotlar saqlandi")
    data.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
