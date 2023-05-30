from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='5710647323:AAGaWqwHb3aXs3n9LtvgSS-Qe4ylSVyy85s')
dp = Dispatcher(bot)

photo1 = open("level1.jpg", 'rb')
photo2 = open("level2.jpg", 'rb')
photo3 = open("level3.jpg", 'rb')
photo4 = open("level4.jpg", 'rb')
photo_end = open("end.jpg", 'rb')


urlbut = InlineKeyboardMarkup(row_width=1)
button_1 = InlineKeyboardButton('відпочити на канікулах (15 монет)', callback_data='button1')
button_2 = InlineKeyboardButton('захистити ознайомчу практику (15 монет)', callback_data='button1')
button_3 = InlineKeyboardButton('здати першу сесію (15 монет)', callback_data='button1')
urlbut.add(button_1, button_2, button_3)

@dp.message_handler(commands='start')
async def but1(message : types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo1)
    await message.answer('Вітаю , ти у боті Лізи з групи МВП-11 !\n'
                        'цей бот придуманий прокачати студента від 1 до 4 курсу , \n'
                        'необхідно: \n'
                        '-виконувати завдання \n'
                        '-переходити на наступні рівні \n'
                        '-заробляти монети \n'
                        'Студент першокурсник. Стартовий рівень. \n'
                        'Бонус 5 монет. \n'
                        'Обирайте завдання щоб перейти на наступний рівень. ', reply_markup=urlbut)

@dp.callback_query_handler(text='button1')
async def but2(callback : types.CallbackQuery):
    await bot.send_photo(chat_id=callback.message.chat.id, photo=photo2)
    urlbut2 = InlineKeyboardMarkup(row_width=1)
    button_4 = InlineKeyboardButton('Захистити навчальну практику(15 монет) ', callback_data='button2')
    button_5 = InlineKeyboardButton('Влаштуватись на роботу (15 монет) ', callback_data='button2')
    button_6 = InlineKeyboardButton('Здати 4-у сесію (15 монет)', callback_data='button2')
    urlbut2.add(button_4, button_5, button_6)
    await callback.message.answer('Вітаємо на другому курсі ! Твій статус другокурсник ! \n'
                                'Баланс 20 монет. \n'
                                'Обери завдання , щоб перейти на наступний рівень ', reply_markup=urlbut2)
    # await callback.answer()

@dp.callback_query_handler(text='button2')
async def but3(callback : types.CallbackQuery):
    await bot.send_photo(chat_id=callback.message.chat.id, photo=photo3)
    urlbut3 = InlineKeyboardMarkup(row_width=1)
    button_7 = InlineKeyboardButton('написати телеграм бот (15 монет)', callback_data='button3')
    button_8 = InlineKeyboardButton('захистити виробничу практику (15 монет) ', callback_data='button3')
    button_9 = InlineKeyboardButton('піднятись на Говерлу (15 монет)', callback_data='button3')
    urlbut3.add(button_7, button_8, button_9)
    await callback.message.answer('Вітаємо на третьому курсі ! Твій статус третьокурсник!\n'
                                'Баланс 35 монет. \n'
                                'Обери завдання , щоб перейти на наступний рівень', reply_markup=urlbut3)
    # await callback.answer()

@dp.callback_query_handler(text='button3')
async def but4(callback : types.CallbackQuery):
    await bot.send_photo(chat_id=callback.message.chat.id, photo=photo4)
    urlbut4 = InlineKeyboardMarkup(row_width=1)
    button_10 = InlineKeyboardButton('написати телеграм бот (15 монет)', callback_data='button4')
    button_11 = InlineKeyboardButton('захистити виробничу практику (15 монет) ', callback_data='button4')
    button_12 = InlineKeyboardButton('піднятись на Говерлу (15 монет)', callback_data='button4')
    urlbut4.add(button_10, button_11, button_12)
    await callback.message.answer('Вітаємо на четвертому курсі ! Твій статус випускник ! \n'
                                'Баланс 50 монет.  \n'
                                'Обери завдання щоб завершити: ', reply_markup=urlbut4)
    # await callback.answer()

@dp.callback_query_handler(text='button4')
async def but5(callback : types.CallbackQuery):
    await bot.send_photo(chat_id=callback.message.chat.id, photo=photo_end)
    await callback.message.answer('Забирай свій диплом!')
    # await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)