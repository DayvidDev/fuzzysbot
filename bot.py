from telegram.ext import Updater, CommandHandler

import requests, os, random




url = 'https://myapicodecapsule-kinddn.codecapsules.co.za/get'
data = requests.get(url) # requests data from API
data = data.json() # converts return data to json

# Retrieve values from API
cad_rate = data['usd_rates']['CAD']
eur_rate = data['usd_rates']['EUR']
zar_rate = data['usd_rates']['ZAR']

#Matthias Sprüche
Matze = ['Jo genau!', 'Sicher net!', 'eh!', 'so wia du sesch', 'i wäs genau was du denksch', 'I weiss genau was ihr etz alle denken', 'Fist of Lazarus', 'Voll, voll']
#Sichla
Sichlor = ['Des isch boda kurzfrischtig']



def return_rates():
    return "Hello. Today, USD conversion rates are as follows: USD->CAD = "+str(cad_rate)+", USD->EUR = "+str(eur_rate)+", USD->ZAR = "+str(zar_rate)

def return_matze():
    varstr = random.choice(Matze)
    return str(varstr)
def return_sichla():
    return str(random.choice(Sichlor))

def currency(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_rates())
    
def matthias(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_matze())

def sichla(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=return_sichla())
    
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I bims, dr Matthias. /currency, /matthias, /sichla.")






def main():
    TOKEN = os.getenv('BOTAPIKEY')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    matthias_handler = CommandHandler("matthias", matthias)
    currency_handler = CommandHandler("currency", currency)
    sichla_handler = CommandHandler("sichla", sichla)
    start_handler = CommandHandler("start", start)

    dispatcher.add_handler(matthias_handler)
    dispatcher.add_handler(currency_handler)
    dispatcher.add_handler(sichla_handler)
    dispatcher.add_handler(start_handler)

    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'https://fuzzysbot-bzgqir.codecapsules.co.za' + '/' + TOKEN
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    updater.idle()

if __name__ == '__main__':
    main()
