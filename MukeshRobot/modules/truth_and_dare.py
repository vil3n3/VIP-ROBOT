import random

from telegram import Update
from telegram.ext import CallbackContext

import MukeshRobot.modules.truth_and_dare_string as truth_and_dare_string
from MukeshRobot import dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*ᴛʀᴜᴛʜ & ᴅᴀʀᴇ*
 ❍ /truth  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
 ❍ /dare  *:* sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.

☆............𝙱𝚈 » [𓆰ꪑ𝓲𝓽𝘴𝓾𝘳𝓲  𝘬ꪖ ꪜ𝓲ꪶꪶ𝓲ꪖꪀ𓆪](https://t.me/villen_012)............☆
"""
__mod_name__ = "⚡ꜰᴜɴ⚡"
