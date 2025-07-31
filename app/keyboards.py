from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

send_question = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Отправить", callback_data = "send")],
                                                      [InlineKeyboardButton(text="Хочу задать другой вопрос", callback_data = "new_question")]
                                                      ])

