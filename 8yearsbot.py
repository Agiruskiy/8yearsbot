from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def years(update: Updater, context: CallbackContext):
    update.message.reply_sticker('CAACAgIAAxkBAAEECn1iIOkPGHzDqt2Zv8I1g-J5o--RjwACFBYAAma5CEmQib3xor7ODCME')

def kremlin(update: Updater, context: CallbackContext):
    update.message.reply_sticker('CAACAgIAAxkBAAEECntiIOijLlvH3YF0f8z32KM3PkOSewACbBUAAmUj8UgWwTqsNu6FTyME')

def main():
# ADD TOKEN
    my_bot = Updater('5133158394:AAGEXbJ_ZTrrD7Guv17g13eBSWmH6qsQ39Q')
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('(8|[вВ].?[сС].?[мМ].?)\s+[лЛ].[тТ]|(2014)'), years))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.user_ids(773498806), kremlin))
    my_bot.start_polling()
    my_bot.idle()

main()
