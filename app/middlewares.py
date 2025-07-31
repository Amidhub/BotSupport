from aiogram import BaseMiddleware
from aiogram.types import Message
from app.database import requests as rq
from typing import Callable, Dict, Any, Awaitable


class CounterMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] = self.counter
        return await handler(event, data)
    
class CheckBan(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
        ) -> Any:
        try:
            ban = await rq.get_status_ban(event.from_user.id) 
        except:
            ban = False
        if ban == True and event.from_user.id != 1001163014:
            await event.answer(text ="Ты был забанен")
        else:
            return await handler(event, data)