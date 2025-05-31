import json
from signals.signal_generator import generate_signal
from telegram import Bot

def run_bot():
    with open("config.json") as f:
        config = json.load(f)
    
    bot = Bot(token=config["telegram_token"])
    signal = generate_signal()
    
    message = f"""
📡 *Mr adnn SIGNAL AI*
Market: {signal['market']}
Pair: {signal['pair']}
Timeframe: {signal['timeframe']}
Sinyal: *{signal['signal']}*
Harga Open: {signal['price']}
TP: {signal['tp']}
SL: {signal['sl']}
Prediksi: {signal['prediction']}
Next update dalam all time 🕒
"""
    bot.send_message(chat_id=config["chat_id"], text=message, parse_mode="Markdown")
  
