from aiogram import types

ariza_qoldir = [  # noqa
    [types.KeyboardButton(text="Ariza qoldirish 📩")]
]
ariza = types.ReplyKeyboardMarkup(keyboard=ariza_qoldir, resize_keyboard=True,  # noqa
                                  input_field_placeholder="Ariza qoldirish uchun bosing 📩")  # noqa

full = [  # noqa
    [types.KeyboardButton(text="Ism"), types.KeyboardButton(text="Telefon raqam")],
    [types.KeyboardButton(text="Yashash joyi", request_location=True), types.KeyboardButton(text="Tumani")],
    [types.KeyboardButton(text="Ma'lumotlarni Tasdiqlash")]
]
full_button = types.ReplyKeyboardMarkup(keyboard=full, resize_keyboard=True,  # noqa
                                        input_field_placeholder="Ariza qoldirish uchun quyidagilarni kiriting 📩")  # noqa
