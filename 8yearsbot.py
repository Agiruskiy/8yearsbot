from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def years(update: Updater, context: CallbackContext):
    update.message.reply_sticker('CAACAgIAAxkBAAEECn1iIOkPGHzDqt2Zv8I1g-J5o--RjwACFBYAAma5CEmQib3xor7ODCME')

def kremlin(update: Updater, context: CallbackContext):
    update.message.reply_sticker('CAACAgIAAxkBAAEECntiIOijLlvH3YF0f8z32KM3PkOSewACbBUAAmUj8UgWwTqsNu6FTyME')

def main():
# ADD TOKEN
    my_bot = Updater(TOKEN)
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('(8|[вВ].?[сС].?[мМ].?)\s+[лЛ].[тТ]|(2014)'), years))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.user(user_id = 773498806), kremlin))
    my_bot.start_polling()
    my_bot.idle()

main()
