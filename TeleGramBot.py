import telebot
from telebot import types

from constants import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands = ["Hello", "Start"])
def greet(message):
    bot.reply_to(message, "Hello!")

@bot.message_handler(commands = ["Hi"])
def hi(message):
    bot.send_message(message.chat.id, "What's up?")

@bot.message_handler(commands = ["boo"])
@bot.message_handler(func=lambda msg: msg.from_user.username == "Sok Ang")
def sent_message(message):
    bot.send_dice(message.chat.id)

@bot.message_handler(commands = ["game"])
def send_game(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("/boo")
    btn2 = types.KeyboardButton("/Hello")
    btn3 = types.KeyboardButton("/Hi")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="What do you want?", reply_markup=markup)


bot.polling()