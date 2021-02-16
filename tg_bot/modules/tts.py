from datetime import datetime

from gtts import gTTS
from telegram import ChatAction, Update, Message
from telegram.ext import CallbackContext, run_async, CommandHandler, MessageHandler

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler


@run_async
def tts(update: Update, context: CallbackContext):
    args = context.args
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    lang = "ml"
    tts = gTTS(reply, lang)
    tts.save("k.mp3")
    with open("k.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        lang = "en"
        tts = gTTS(reply, lang)
        tts.save("k.mp3")
    with open("k.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)

__help__ = """- /tts <text>: convert text to speech.
"""
__mod_name__ = "Text To Speech"


dispatcher.add_handler(CommandHandler('tts', tts, pass_args=True))
