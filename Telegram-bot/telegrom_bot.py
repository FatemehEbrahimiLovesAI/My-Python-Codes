# this is my bot's id = @FatemehEbrahimiGithub_bot

import telebot
from telebot import types

bot = telebot.TeleBot("7705336445:AAFA8QW9WWUfic0aYXBSFvhynevxdgxRUyk")

ADMINS = [6817826525]

def user_panel():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("give me a nickname!")
    btn2 = types.KeyboardButton("tell me a joke!")
    btn3 = types.KeyboardButton("tell me a fact!")
    markup.add(btn1, btn2, btn3)
    return markup

def admin_panel():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("add nickname")
    btn2 = types.KeyboardButton("add joke")
    btn3 = types.KeyboardButton("add fact")
    markup.add(btn1, btn2, btn3)
    return markup

# dandeling /start command 
@bot.message_handler(commands=['start'])
def start(message):
    #if it is a admin
    if message.chat.id in ADMINS:
        bot.send_message(message.chat.id, "Welcome Admin! How can I assist you today?", reply_markup=admin_panel())
    # if it is a user
    else:
      bot.send_message(message.chat.id, "Welcome to the bot! How can I help you today?", reply_markup=user_panel())


@bot.message_handler(func=lambda message: True)
def user_respond_handler(message):
    if message.text == "give me a nickname!":
        bot.send_message(message.chat.id, "This feature is under construction. Please wait.")
    elif message.text == "tell me a joke!":
        bot.send_message(message.chat.id, "This feature is under construction. Please wait.")
    elif message.text == "tell me a fact!":
        bot.send_message(message.chat.id, "This feature is under construction. Please wait.")
    elif message.text == "add nickname":
        bot.send_message(message.chat.id, "This feature is under construction. Please wait.")
    elif message.text == "add joke":
        bot.send_message(message.chat.id, "This feature is under construction. Please wait.")
    elif message.text == "add fact":
        bot.send_message(message.chat.id, "This feature is under construction. Please wait.")

bot.polling()
