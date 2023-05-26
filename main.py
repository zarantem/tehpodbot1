import string

from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from config import token, group_id
from keyboards import first_keyboard, address_keyboard, final_keyboard, admin_keyboard, photo_keyboard
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text



bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

class FSMAdmin(StatesGroup):
    trouble_state=State()
    address_state=State()
    description_state=State()
    photo_state=State()
    get_photo=State()

@dp.message_handler(commands='start', state=None)
async def send_1st_keyboard(message: types.Message, state=FSMContext):
    await FSMAdmin.trouble_state.set()
    await message.answer(text='Укажите с какой проблемой вы стлкнулись:', reply_markup=first_keyboard)

@dp.message_handler(state=FSMAdmin.trouble_state)
async def send_2nd_keyboard(message: types.Message, state=FSMContext):
    trouble = message.text
    await state.update_data(trouble=trouble)
    await FSMAdmin.address_state.set()
    await message.answer(text='Укажите адрес отделения, пожалуйста', reply_markup=address_keyboard)

@dp.message_handler(state=FSMAdmin.address_state)
async def get_description(message: types.Message, state=FSMContext):
    address = message.text
    await state.update_data(address=address)
    await FSMAdmin.description_state.set()
    await message.answer(text='Укажите подробности:\nФИО\nномер телефона\nконкретную проблему')

@dp.message_handler(state=FSMAdmin.description_state)
async def resend_msg_2_group(message: types.Message, state=FSMContext):
    description = message.text
    await state.update_data(description=description)
    await FSMAdmin.photo_state.set()
    await message.answer(text='Вы хотите добавить фото с проблемой?', reply_markup=photo_keyboard)


@dp.message_handler(state=FSMAdmin.photo_state)
async def get_answer(message: types.Message, state=FSMContext):
    if message.text == 'Нет':
        user_id = message.from_user.id
        await message.answer(
            text='Спасибо за подробности, информацию передали специалистам, ожидайте пока они с вами свяжутся',
            reply_markup=final_keyboard)
        data = await state.get_data()
        trouble = data.get('trouble')
        address = data.get('address')
        description = data.get('description')
        message_text = f'{user_id}\n{trouble}\n{address}\n{description}'
        await bot.send_message(chat_id=group_id, text=message_text, reply_markup=admin_keyboard)
        await state.finish()
    else:
        await FSMAdmin.get_photo.set()
        await message.answer(text='добавьте фото в этом сообщении')


@dp.message_handler(state=FSMAdmin.get_photo, content_types=types.ContentTypes.PHOTO)
async def get_photo(message: types.Message, state=FSMContext):
    user_id = message.from_user.id
    photo = message.photo[0].file_id
    await message.answer(text='Спасибо за подробности, информацию передали специалистам, ожидайте пока они с вами свяжутся', reply_markup=final_keyboard)
    data = await state.get_data()
    trouble = data.get('trouble')
    address = data.get('address')
    description = data.get('description')
    message_text = f'{user_id} \n{trouble}\n{address}\n{description}'
    await bot.send_photo(chat_id=group_id, photo=photo, caption=message_text, reply_markup=admin_keyboard)
    await state.finish()


@dp.message_handler(Text(equals='принять'))
async def send_info_2_client(message: types.Message, state=FSMContext):
    user_message = str(message.reply_to_message.text)
    client_id = user_message.partition(' ')[0]
    print(client_id)
    admin_name = message.from_user.first_name
    admin_last_name = message.from_user.last_name
    specialist1 = str(admin_name) + ' ' + str(admin_last_name)
    specialist = string.replace(specialist1, "None", "")
    await bot.send_message(chat_id=client_id, text=f'Ваша заявка принята специалистом {specialist}')


executor.start_polling(dp, skip_updates=True)