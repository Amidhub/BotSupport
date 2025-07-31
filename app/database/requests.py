from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, update, delete, desc


async def set_user(tg_id, name, tg_id_chat):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, name=name, tg_id_chat=tg_id_chat))
            await session.commit()

async def write_question(tg_id, question):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id==tg_id).values(question = question))
        await session.commit()
        

async def ban(tg_id, flag):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id==tg_id).values(ban = flag))
        await session.commit()

async def get_questions():
    async with async_session() as session:
        users = await session.scalars(select(User).where(User.send==1))
        return users
    
async def send(tg_id, flag):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id==tg_id).values(send = flag))
        await session.commit()

async def get_status_send(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))
        return user.send

async def get_status_ban(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))
        return user.ban