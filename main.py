from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from model import*


bot_token = '5671173769:AAFE8QhdtD3-xf6Gx0BZcnLk6OG3HpKNACs'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


# Начало работы бота
def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет!\nОзнакомься с условиями игры с ботом:\n" 
           f"На столе лежат 150 конфет.\nИграют два игрока, делая ход друг после друга.\nЗа один ход можно забрать от 1 до 11 конфет.\n" 
           f"Выигрывает тот, кто возьмет конфеты последним.\n\nВыбери кто первым делает ход:\nесли хочешь начать игру первым, жми: /yes \nесли хочешь, чтобы начал бот, жми: /bot\n\n Для выхода из игры напиши: /stop  ")

# Ответ на сообщение "yes"
def turn_player(update, context):
    context.bot.send_message(update.effective_chat.id, 'Какое количество конфет возьмешь?')
    return 1

# Обработка сообщения и вывод игроку ответ на его ход
def step_player(update, context):
    update.message.reply_text(player_output(int(update.message.text)))
    return 1

def turn_bot(update, context):
    context.bot.send_message(update.effective_chat.id, 'Бот взял конфеты\nТеперь бери ты:')
    return 1

# Вывод игроку сообщения на ход бота
def step_bot(update, context):
    update.message.reply_text(bot_output(int(update.message.text)))
    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
turn_player_handler = ConversationHandler(
        entry_points=[CommandHandler('yes', turn_player)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, step_player)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

turn_bot_handler = ConversationHandler(
        entry_points=[CommandHandler('bot', turn_bot)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, step_bot)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

dispatcher.add_handler(turn_player_handler)
dispatcher.add_handler(turn_bot_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
