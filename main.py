import requests
from telegram.ext import Updater, CommandHandler
import telegram
from token_value import token_number

updater = Updater(token=token_number, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Расскажу шутки (jokes) онлайн бесплатно без регистрации!\nНажми /get, чтобы получить шутку (joke)",
    )


def get(update, context):
    body = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    keyboard = [["/get"]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
    text = f"""
    {body["setup"]}





 <b>{body["punchline"]}</b>"""

    dog = requests.get("https://dog.ceo/api/breeds/image/random").json()
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=dog["message"],
        caption=text,
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=reply_markup,
    )


start_handler = CommandHandler("start", start)
get_handler = CommandHandler("get", get)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_handler)
updater.start_polling()
