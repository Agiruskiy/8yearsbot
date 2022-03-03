from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def years(update: Updater, context: CallbackContext):
    update.message.reply_sticker('CAACAgIAAxkBAAEECn1iIOkPGHzDqt2Zv8I1g-J5o--RjwACFBYAAma5CEmQib3xor7ODCME')

def main():
# ADD TOKEN
    my_bot = Updater(TOKEN)
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('.*[Вв]оc[еи]мь.*[Лл]ет.*|.*8.*[Лл]ет.*'), years))
    my_bot.start_polling()
    my_bot.idle()

main()