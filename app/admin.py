from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, CommandStart, Command, CommandObject
from app.database import requests as rq

admin = Router()


class Admin(Filter):
    def __init__(self):
        self.admins = [1001163014]

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins
    

@admin.message(Admin(), Command('admin'))
async def cmd_start(message: Message, bot : Bot):
    await message.answer('Добро пожаловать в бот, администратор!')
    await message.answer('Твои специальные команды:')
    await message.answer('/questions')
    await message.answer('/question')
    await message.answer('/answer (передать: tg_id answer)')
    await message.answer('/ban (передать: tg_id')
    
    
@admin.message(Admin(), Command('questions'))
async def questions(message: Message, command: CommandObject):
    try:
        lst_of_question = await rq.get_questions()
    
        for user in lst_of_question:
            await message.answer(f'{user.tg_id}\n{user.question}\n\n')
        
    except:
        await message.answer('ERORR')
    
@admin.message(Admin(), Command('question'))
async def questions(message: Message, command: CommandObject):
    try:
        lst_of_question = await rq.get_questions()
    
        for user in lst_of_question:
            await message.answer(f'{user.tg_id}\n{user.question}\n\n')
            break
        
    except:
        await message.answer('ERORR')

@admin.message(Admin(), Command('answer'))
async def questions(message: Message, command: CommandObject, bot : Bot):
    try:
        tg_id, answer = command.args.split(' ')[0], ' '.join(command.args.split(' ')[1:])
    
        await bot.send_message(tg_id, answer)
        
        await rq.send(tg_id, False)
        
    except:
        await message.answer('ERORR')
        
@admin.message(Admin(), Command('ban'))
async def questions(message: Message, command: CommandObject, bot : Bot):
    try:
        tg_id = command.args
        await rq.ban(tg_id, True)
        await bot.send_message(tg_id, 'ты был забанен')
        
    except:
        await message.answer('ERORR')
    
    
