import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://graph.org/file/3f7abc44fe9f39a1eb4fe.jpg",
    "https://graph.org/file/a9418e9ea5d8c3c44c996.jpg",
    "https://graph.org/file/81ecdf048901982ecc8d8.jpg",
    "https://graph.org/file/c24c72f854e85fd43cf1f.jpg",
    "https://graph.org/file/8c385a92033f329da20ff.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="📍𝐎𝐰𝐧𝐞𝐫📍", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="🍒𝐆𝐫𝐨𝐮𝐩🍒", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="☆ 𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑 ☆",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://graph.org/file/a30dfd38dc3cd79ff26b6.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**🌷ʜᴇʏ, ɪ ᴀᴍ 『[ꪜ𝓲ꪶꪶ𝓲ꪖꪀ 𝐴𝑠𝑠𝑖𝑠𝑡𝑎𝑛𝑡](f"t.me/{BOT_USERNAME}")』🎄**
   ╔═════ஜ۩۞۩ஜ════╗

   ♨️𝓜𝓪𝓭𝓮 𝓑𝔂 [𝓥𝓲𝓵𝓵𝓲𝓪𝓷](https://t.me/villen_012)♨️

   ╚═════ஜ۩۞۩ஜ════╝""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............𝙱𝚈 » [ꪜ𝓲ꪶꪶ𝓲ꪖꪀ 𝐴𝑠𝑠𝑖𝑠𝑡𝑎𝑛𝑡](https://t.me/villen_012)............☆"""
