from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text
    print("ID: " + str(id) + "MENSAJE: " + mensaje)


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Bienvenido a maincra_bot')


def hola_mundo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola, maincra!')


def imagen(bot, update):
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('i_choose_you.jpg', 'rb'))


def main():
    updater = Updater('139249691:AAFweIL2JpEGWX44__XMcrkPjSzWP5yEk4k')
    dispatcher = updater.dispatcher
    listener_handler = MessageHandler(Filters.text, listener)
    dispatcher.add_handler(listener_handler)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("holamundo", hola_mundo))
    dispatcher.add_handler(CommandHandler("imagen", imagen))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
