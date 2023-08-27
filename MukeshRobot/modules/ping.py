import time
import random
from asyncio import sleep as rest
from pyrogram import Client, filters
from pyrogram.types import Message
from MukeshRobot import boot as tim
from MukeshRobot import Hiroko
from MukeshRobot import OWNER_ID as owner
from MukeshRobot import SUDO_USERS as sudo
from pyrogram import filters, __version__
from platform import python_version
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)



# ------------------------------------------------------------------------------- #


photo = [
"https://graph.org/file/e3ad70d7ffdd94b53b349.jpg",
"https://graph.org/file/fadcdc2852843c2a00a08.jpg",
"https://graph.org/file/78b6e4aea6f16c369bb13.jpg",
"https://graph.org/file/3f7abc44fe9f39a1eb4fe.jpg",
"https://graph.org/file/a9418e9ea5d8c3c44c996.jpg",
"https://graph.org/file/1c93a0687c70e540226f8.jpg",
"https://graph.org/file/8c385a92033f329da20ff.jpg",
"https://graph.org/file/a209dbc37715b6f468447.jpg",
"https://graph.org/file/c24c72f854e85fd43cf1f.jpg",
"https://graph.org/file/81ecdf048901982ecc8d8.jpg",
"https://graph.org/file/8dc10e47849b08640eec4.jpg",
"https://graph.org/file/c2fc593e737fad358cfdb.jpg",
"https://graph.org/file/8e198057d847d87fda7da.jpg",
"https://graph.org/file/8cb5220097f727122ac40.jpg",

]

# ------------------------------------------------------------------------------- #

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


sudo.append(owner)

# ------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command(["ping"], prefixes=["/", "!"]))
async def ping(Client, m: Message):
    start_time = time.time()
    sender = m.from_user
    up = get_readable_time((time.time() - tim))
    end_time = time.time()
    ping1 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    if m.from_user.id in sudo:
        e = await m.reply_photo(photo=random.choice(photo),caption="ɢᴇᴛᴛɪɴɢ ᴘɪɴɢɪɴɢ sᴛᴀᴛᴜs...")
        await rest(2)
        await e.edit_text("ᴘɪɴɢɪɴɢ ✨")
        await rest(1)
        await e.edit_text(PING_TEXT.format(ping1, up, __version__), reply_markup=Button) 
       
    if m.from_user.id not in sudo:
        await m.reply(("ʏᴏᴜʀ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ ʜᴜʜ!!😏😏\nʙsᴅᴋ ɢᴀɴᴅ ᴘᴇ ɪᴛɴᴇ ᴛʜʜᴘᴀᴅ ᴍᴀʀᴜɴɢɪ ᴏᴡɴᴇʀ ɢɪʀɪ ᴄʜʜᴜᴛ ᴊᴀᴀʏᴇɢɪ ʜᴜʜ 🤭 [ʟᴏᴅᴀ](tg://user?id={}) ᴘᴇʀsᴏɴ.").format(sender.id))

# ------------------------------------------------------------------------------- #

PING_TEXT = """
˹ʜɪꝛᴏᴋᴏ ꝛᴏʙᴏᴛ˼ 🇮🇳 sʏsᴛᴇᴍ sᴛᴀᴛs :

**ᴘɪɴɢ ᴘᴏɴɢ:** `{}`
**ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:** `{}`
**ʟɪʙʀᴀʀʏ:** `ᴘʏʀᴏɢʀᴀᴍ`
**ᴍʏ ᴍᴀsᴛᴇʀ: ** `sᴜᴍɪᴛ ʏᴀᴅᴀᴠ`
**ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `3.10.4`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ:** `{}`
"""
# ------------------------------------------------------------------------------- #


Button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ ᴄʟᴏsᴇ ๏",callback_data="close_data")
        ]
    ]
)


# ------------------------------------------------------------------------------- #




@Hiroko.on_message(filters.command("alive"))
async def alive(_,msg:Message):
    start_time = time.time()
    sender = msg.from_user
    up = get_readable_time((time.time() - tim))
    end_time = time.time()
    ping1 = str(round((end_time - start_time) * 1000, 3)) + " ms"    
    x = await msg.reply_photo(photo=random.choice(photo), caption="**ᴀʟɪᴠɪɴɢ....**")    
    await x.edit_caption("**๏ ˹ʜɪꝛᴏᴋᴏ ꝛᴏʙᴏᴛ˼ ɪs ᴀʟɪᴠᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ɢᴏᴏᴅ ᴡɪᴛʜ ᴀ ᴘɪɴɢ ᴏғ :**  `{} ᴍs`\n**๏ ʙᴏᴛs sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ ɪs :** `{}`".format(ping1, up), reply_markup=Button)



# ------------------------------------------------------------------------------- #




