import openai, asyncio
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('5619487724:AAFeBptlX1aJ9IEAFLMUXN3JZBImJ35quWk') 
openai.api_key = "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"


@bot.message_handler(content_types=['text'])
async def start(message):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": message.text},
            ]
    )
    await bot.send_message(message.chat.id, response['choices'][0]['message']['content'])


asyncio.run(bot.polling(non_stop=True, interval=1, timeout=0))