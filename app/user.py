from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from app.database import requests as rq
from app.database.requests import set_user
from app import keyboards as kb
# from middlewares import BaseMiddleware

user = Router()
question = ''
# user.message.middleware(BaseMiddleware())

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id, name = message.from_user.first_name, tg_id_chat = message.chat.id)
    status = await rq.get_status_send(tg_id=message.from_user.id)
    if status:
        await message.answer('ты уже отправлял вопрос, дождись ответа и при необходимости задай новый')
    else:
        await message.answer(f'{message.from_user.first_name}, добро пожаловать в бот поддержки!')
        await message.answer('Если есть вопрос, напиши его одним сообщением')
        
@user.message(Command('offer'))
async def cmd_start(message: Message):
    await set_user(message.from_user.id, name = message.from_user.first_name, tg_id_chat = message.chat.id)
    status = await rq.get_status_send(tg_id=message.from_user.id)
    if status:
        await message.answer('ты уже отправлял вопрос, дождись ответа и при необходимости задай новый')
    else:
        await message.answer(f'{message.from_user.first_name}, добро пожаловать в бот поддержки!')
        await message.answer('по поводу сотрудничества напиши предложение в одном сообщении')

@user.message(F.text)
async def cmd_start(message: Message):
    status = await rq.get_status_send(tg_id=message.from_user.id)
    if status:
        await message.answer('ты уже отправлял вопрос, дождись ответа и при необходимости задай новый')
    else:
        if len(message.text)>500:
            await message.answer('слишком длинный вопрос, задай вопрос в котором меньше 500 символов')
        else:
            await rq.write_question(message.from_user.id, question = message.text)
            await message.answer('отправить этот вопрос?', reply_markup= kb.send_question)


@user.callback_query(F.data == 'send')
async def cmd_start(callback: CallbackQuery):
    await callback.message.delete()
    await rq.send(callback.from_user.id, True)
    await callback.message.answer('Готово, подожди пока не придёт ответ')
    

@user.callback_query(F.data == 'new_question')
async def cmd_start(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('напиши вопрос одним сообщением')


