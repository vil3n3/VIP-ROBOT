import aiohttp
import asyncio
from MukeshRobot import MukeshRobot
from pyrogram import filters 
from pyrogram.types import Message 
import requests 
from config import COMMAND_HANDLER

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("cuddle",COMMAND_HANDLER))
def cuddle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("shrug",COMMAND_HANDLER))
def shrug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

# --------------------------------------------------------------------------------- #
      
@Hiroko.on_message(filters.command("poke",COMMAND_HANDLER))
def poke(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("facepalm",COMMAND_HANDLER))
def facepalm(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("stare",COMMAND_HANDLER))
def stare(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #
      
@Hiroko.on_message(filters.command("pout",COMMAND_HANDLER))
def pout(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("handhold",COMMAND_HANDLER))
def handhold(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("wave",COMMAND_HANDLER))
def wave(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("blush",COMMAND_HANDLER))
def blush(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("neko",COMMAND_HANDLER))
def neko(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          reply.reply_photo(url)
      else:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          m.reply_photo(url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("dance",COMMAND_HANDLER))
def dance(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("baka",COMMAND_HANDLER))
def baka(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("bore",COMMAND_HANDLER))
def bore(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("laugh", COMMAND_HANDLER))
def laugh(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("smug",COMMAND_HANDLER))
def smug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("thumbsup",COMMAND_HANDLER))
def thumbsup(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("shoot",COMMAND_HANDLER))
def shoot(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("tickle",COMMAND_HANDLER))
def tickle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("feed",COMMAND_HANDLER))
def feed(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("think",COMMAND_HANDLER))
def think(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("wink",COMMAND_HANDLER))
def wink(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("sleep",COMMAND_HANDLER))
def sleep(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
            
# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("punch",COMMAND_HANDLER))
def punch(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
 

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command("cry",COMMAND_HANDLER))
def cry(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/cry").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/cry").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
 # --------------------------------------------------------------------------------- #
  
@Hiroko.on_message(filters.command("kill",COMMAND_HANDLER))
def kill(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kill").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kill").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
# --------------------------------------------------------------------------------- #
      
@Hiroko.on_message(filters.command("smile",COMMAND_HANDLER))
def smile(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/smile").json()
          url = api["url"]
          m.reply_animation(animation=url)
             
 # --------------------------------------------------------------------------------- #
   
@Hiroko.on_message(filters.command("highfive",COMMAND_HANDLER))
def highfive(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/highfive").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/highfive").json()
          url = api["url"]      
          m.reply_animation(animation=url)
             
# --------------------------------------------------------------------------------- #
    
@Hiroko.on_message(filters.regex("slap"))
@Hiroko.on_message(filters.command("slap",COMMAND_HANDLER))
def slap(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           name1 = reply.from_user.first_name
           name2 = m.from_user.first_name
           reply.reply_animation(url,caption="{} (((;ꏿ_ꏿ;))) slaps {} ಠಗಠ".format(name2, name1))
       else:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           m.reply_animation(url,caption=f"**sʟᴀᴘs ʏᴏᴜ ᴡɪᴛʜ ᴍʏ ᴀʟʟ sᴛʀᴇɴɢᴛʜ** {m.from_user.first_name} ಠ‿ಠ")      
         
# --------------------------------------------------------------------------------- #
     
@Hiroko.on_message(filters.regex("hug"))    
@Hiroko.on_message(filters.command("hug",COMMAND_HANDLER))
def hug(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/hug").json()
           url = api["url"]
           name1 = reply.from_user.first_name
           name2 = m.from_user.first_name
           reply.reply_animation(url,caption="{} ( ◜‿◝ )♡ hugs {} ( ╹▽╹ )".format(name2, name1))
       else:
          api = requests.get("https://api.waifu.pics/sfw/hug").json()
          url = api["url"]  
          m.reply_animation(animation=url,caption=f"**ʜᴜɢs ʏᴏᴜ ᴀʟʟ ʟᴏᴠᴇs** {m.from_user.first_name}")
             
 # --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.regex("pat"))
@Hiroko.on_message(filters.command("pat",COMMAND_HANDLER))
def pat(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/pat").json()
           url = api["url"]
           name1 = reply.from_user.first_name
           name2 = m.from_user.first_name
           reply.reply_animation(url,caption="{} ( ◜‿◝ )♡ pats {} ( ╹▽╹ )".format(name2, name1))
       else:
          api = requests.get("https://api.waifu.pics/sfw/pat").json()
          url = api["url"]
          m.reply_animation(animation=url,caption=f"**ᴘᴀᴛs ʏᴏᴜ ᴀʟʟ ʟᴏᴠᴇs** {m.from_user.first_name}")
             
 # --------------------------------------------------------------------------------- #
   
@Hiroko.on_message(filters.command("waifu",COMMAND_HANDLER))
def waifu(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/waifu").json()
           url = api["url"]
           reply.reply_photo(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/waifu").json()
          url = api["url"]       
          m.reply_photo(photo=url)
    

# --------------------------------------------------------------------------------- #


PALM_API_URL = "https://api.qewertyy.me/models"
MODEL_ID = 0
API_TIMEOUT = 10




async def get_palm_response(session, api_params):
    async with session.post(PALM_API_URL, params=api_params) as response:
        if response.status == 200:
            data = await response.json()
            return data.get(
                "content", "Error: Empty response received from the PALM API."
            )
        else:
            return f"Error: Request failed with status code {response.status}."



@Hiroko.on_message(filters.regex(r"(Hiroko|hiroko)"))
async def palm_chatbot(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply("👀")
        return

    input_text = args[1]

    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=API_TIMEOUT)
        ) as session:
            result_msg = await message.reply("...")

            api_params = {"model_id": MODEL_ID, "prompt": input_text}
            api_response = await asyncio.gather(get_palm_response(session, api_params))

            await result_msg.delete()

    except aiohttp.ClientError as e:
        api_response = f"Error: An error occurred while calling the hiroko api. {e}"
    except asyncio.TimeoutError:
        api_response = "Error: The hiroko api request timed out."

    reply = message.reply_to_message
    if reply:
        await reply.reply(api_response[0])
    else:
        await message.reply(api_response[0])
          

# --------------------------------------------------------------------------------- #





