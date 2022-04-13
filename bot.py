from telegram.ext import Updater, CommandHandler

import requests, os
from random import seed
from random import random 


url = 'https://myapicodecapsule-kinddn.codecapsules.co.za/get'
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json

# Retrieve values from API
cad_rate = data['usd_rates']['CAD']
eur_rate = data['usd_rates']['EUR']
zar_rate = data['usd_rates']['ZAR']

#Matthias Sprüche
Matze = ["Jo genau!", "Sicher net!", "eh!", "so wia du sesch", "i wäs genau was du denksch", "so wia du sesch"]



seed(1)
#generate a random number

def return_rates():
    return "Hello. Today, USD conversion rates are as follows: USD->CAD = "+str(cad_rate)+", USD->EUR = "+str(eur_rate)+", USD->ZAR = "+str(zar_rate)

def return_matze():
    return Matze[randint(0,5)]

def currency(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_rates())
    
def matthias(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_matze())

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I respond to /currency and /matthiasle. Try me!")






def main():
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    matthias_handler = CommandHandler("matthias", matthias)
    currency_handler = CommandHandler("currency", currency)
    start_handler = CommandHandler("start", start)

    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(start_handler)

    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'https://fuzzysbot-bzgqir.codecapsules.co.za' + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()

if __name__ == '__main__':
    main()
