from telegram.ext import Updater, CommandHandler

import requests

url = https://myapicodecapsule-kinddn.codecapsules.co.za/
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json

# Retrieve values from API
cad_rate = data['usd_rates']['CAD']
eur_rate = data['usd_rates']['EUR']
zar_rate = data['usd_rates']['ZAR']


def return_rates():
    return "Hello. Today, USD conversion rates are as follows: USD->CAD = "+str(cad_rate)+", USD->EUR = "+str(eur_rate)+", USD->ZAR = "+str(zar_rate)

def currency(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_rates())

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I respond to /currency. Try me!")


def main():
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    currency_handler = CommandHandler("currency", currency)
    start_handler = CommandHandler("start", start)

    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(start_handler)

    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = https://fuzzysbot-bzgqir.codecapsules.co.za/ + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()



    updater.start_polling()

if __name__ == '__main__':
    main()