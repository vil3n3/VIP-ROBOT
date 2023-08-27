import time
from pyrogram import Client, filters
import openai
from bardapi import Bard
from Hiroko import Hiroko
from pyrogram.enums import ChatAction, ParseMode
from typing import Union, List




openai.api_key = "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"

#bard = Bard(token="__Secure-1PSID.")



@Hiroko.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n\n**ᴇxᴀᴍᴘʟᴇ:**\n\n`/ask 'How to set girlfriend ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"**ʜᴇʟʟᴏ {message.from_user.first_name}**\n\n {x}\n\n**✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ**  {telegram_ping} \n", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        


"""
   
@Hiroko.on_message(filters.command("bard"))
async def bard_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**ʜᴇʟʟᴏ sɪʀ**\n\n**ᴇxᴀᴍᴘʟᴇ:**\n\n` /bard How r u? `")
        else:
            a = message.text.split(' ', 1)[1]
            response=bard.get_answer(f"{a}")["content"]
            await message.reply_text(f"{response}\n", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**:  {e} ")



"""

@Hiroko.on_message(filters.command(["image","photo","img","generate"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**ᴇxᴀᴍᴘʟᴇ:**\n\n`/generate a hot girl`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")
