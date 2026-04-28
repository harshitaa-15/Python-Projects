import requests
import pandas as pd
import plotext as plt
import time
import sys

user_name = input("Enter your name:")

WELCOME_ASCII = r"""
__        __   _                            _
\ \      / /__| | ___ ___  _ __ ___   ___  | |
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
  \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)
"""
# typing effect on ASCII text
for line in WELCOME_ASCII.splitlines():
    print(line)
    time.sleep(0.07)

print("\n")

msg = f"Welcome {user_name}! Enjoy Bloom_Crypto Terminal!"
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
print()

print("/n")



price_lst = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'QTUMETH', 'EOSETH', 'SNTETH', 'BNTETH', 'BCCBTC', 
'GASBTC', 'BNBETH', 'BTCUSDT', 'ETHUSDT', 'HSRBTC', 'OAXETH', 'DNTETH', 'MCOBTC', 'ICNBTC', 'MCOETH', 'WTCBTC', 
'WTCETH', 'LRCBTC', 'LRCETH', 'QTUMBTC', 'YOYOBTC', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'STRATBTC', 'STRATETH',
 'SNGLSBTC', 'SNGLSETH', 'BQXBTC', 'BQXETH', 'KNCBTC', 'KNCETH', 'FUNBTC', 'FUNETH', 'SNMBTC', 'SNMETH', 'NEOETH', 
 'IOTABTC', 'IOTAETH', 'LINKBTC', 'LINKETH', 'XVGBTC', 'XVGETH', 'SALTBTC', 'SALTETH', 'MDABTC', 'MDAETH', 'MTLBTC',
  'MTLETH', 'SUBBTC', 'SUBETH', 'EOSBTC', 'SNTBTC', 'ETCETH', 'ETCBTC', 'MTHBTC', 'MTHETH', 'ENGBTC', 'ENGETH', 'DNTBTC', 
  'ZECBTC', 'ZECETH', 'BNTBTC', 'ASTBTC', 'ASTETH', 'DASHBTC', 'DASHETH', 'OAXBTC', 'ICXBTC', 'ICXETH', 'ELFBTC', 'ELFETH', 
  'AIONBTC', 'AIONETH', 'NEBLBTC', 'NEBLETH', 'BRDBTC', 'BRDETH', 'EDOBTC', 'EDOETH', 'WABIBTC', 'WABIETH', 'LTCETH', 'LTCUSDT', 
  'ETCUSDT', 'TRXBTC', 'TRXETH', 'POWRBTC', 'POWRETH', 'ARKBTC', 'ARKETH', 'YOYOETH', 'XRPBTC', 'XRPETH', 'MODBTC', 'MODETH', 'ENJBTC',
   'ENJETH', 'STORJBTC', 'STORJETH', 'BNBUSDT', 'VENBNB']

print("#==================================SELECT COIN===============================#\n")

for i in range(len(price_lst[:100])):
    print(f"{i+1} {price_lst[i]}", end = "\t ")
    if (i+1) % 10 == 0:
        print("\n")

print("\nChoose two number between 1 to 100 to see the coin price")

while True:
    try:
        choose1 = int(input("Choose1:"))
        break
    except ValueError:
        print("Enter Valid Choice")

while True:
    try:
        choose2 = int(input("Choose2:"))
        break
    except ValueError:
        print("Enter Valid Choice")

prices1 = []
prices2 = []

def fetch_price(choose):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={price_lst[choose - 1]}"
    data = requests.get(url).json()
    return float(data["price"])

def moving_averages(data, w):
    if len(data) < w:
        return []
    ma = []
    for i in range(len(data) - w + 1):
        ma.append(sum(data[i : i + w]) / w)
    return ma

while True:
    try:
        coin1 = fetch_price(choose1)
        coin2 = fetch_price(choose2)

        prices1.append(coin1)
        prices2.append(coin2)

        if len(prices1)>100:
            prices1.pop(0)
            prices2.pop(0)

        coin1_ma = moving_averages(prices1, 10)
        coin2_ma = moving_averages(prices2, 10)

        plt.clear_figure()
        plt.clt()

        plt.subplots(1, 2)

        plt.subplot(1, 1)
        plt.plot(prices1, marker = "-")
        if coin1_ma:
            plt.plot(coin1_ma, label = f"MA-10")
        plt.title(f"Live Prices of {price_lst[choose1 - 1]}")
        plt.xlabel("time")
        plt.theme("dark")
        plt.ylabel("Price(USD)")

        plt.subplot(1, 2)
        plt.plot(prices2, marker = "-")
        if coin2_ma:
            plt.plot(coin2_ma, label = f"MA-10")
        plt.title(f"Live Prices of {price_lst[choose2 - 1]}")
        plt.xlabel("time")
        plt.theme("dark")
        plt.ylabel("Price(USD)")

        plt.show()
        plt.sleep(0.5)

        print(f"Current Price: {coin1}")
        print(f"Current Price: {coin2}")

        time.sleep(0.5)

    
    except KeyboardInterrupt:
        print("\n Stopped By User")
        break
        
