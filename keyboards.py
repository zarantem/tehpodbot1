from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

printer=KeyboardButton('Принтер')
pc=KeyboardButton('Компьютер')
rmias=KeyboardButton('РМИАС(промед)')
other=KeyboardButton('Прочее')

first_keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
first_keyboard.add(printer).insert(pc).add(rmias).insert(other)

pro_26=KeyboardButton('Проспект Октября 26')
pro_44=KeyboardButton('Проспект Октября 44/1')
rev_167=KeyboardButton('Революционная 167')
park_8=KeyboardButton('Парковая 8')
zorge_54=KeyboardButton('Рихарда Зорге 54')
koms_31=KeyboardButton('Комсомольская 31')
dav_30=KeyboardButton('Хадии Давлетшиной 30')
koms_19=KeyboardButton('Комсомольская 19')
bab_17=KeyboardButton('Бабушкина 17')

address_keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
address_keyboard.add(pro_26).insert(pro_44).add(rev_167).insert(park_8).add(zorge_54).insert(koms_31).add(dav_30).insert(koms_19).add(bab_17)

at_start = KeyboardButton('/start')

final_keyboard=ReplyKeyboardMarkup(resize_keyboard=True).add(at_start)

accepted = KeyboardButton('принять')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(accepted)

yes = KeyboardButton('Да')
no = KeyboardButton('Нет')

photo_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(yes, no)
