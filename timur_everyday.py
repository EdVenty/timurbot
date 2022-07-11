import asyncio
import random
from aiogram import Bot, Dispatcher, types
import wikipedia

wikipedia.set_lang('ru')

BOT_TOKEN = "5581295747:AAFn0EPonJTHeHkXS0Ygdx8UlrvffOc4elE"

titles = [
    "Утренняя рассылка Тимуро-фактов!",
    "Держу пари, что вы не знали этого!",
    "Спорим на один обед, что это правда?",
    "ПРОСТО ПРОЧИТАЙ ЭТОТ ФАКТ!!!",
    "Шокирующая правда РенТВ! ОНО СУЩЕСТВУЕТ!",
    "А знали ли вы, что...",
    "Это он! Тот самый!",
    "Саламалекум всем Тимурам!",
    "Проснись и пой - Тимур в запой!"
]

async def send_timur_fact(bot: Bot):
    text = ''
    while len(text.split(' ')) <= 1:
        try:
            title = wikipedia.random()
            text = wikipedia.summary(title, sentences=3)
        except Exception as err:
            pass

    fw = text.split('—', 1)[0].strip()
    text = text.replace(fw, random.choices(['Тимур', 'Тимурка'], [8, 2], k=1)[0])

    await bot.send_message(546475881, 
        f"{random.choice(titles)}\n\n{text}",
        parse_mode=types.ParseMode.HTML
    
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    # aioschedule.every().second.do(send_timur_fact, bot)
    try:
        await send_timur_fact(bot)
    finally:
        await bot.close()

asyncio.run(main())