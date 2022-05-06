import requests
from pprint import pprint

response = requests.get("https://api.coinlore.net/api/tickers/")
data = response.json()
# data = list(dict.values(data))
print("Co chciał/-a byś zobaczyć?")
print("1. Informacje o wszystkich top 100 kryptowalut")
print("2. Konkretną kryptowalutę")
option = input("Podaj swój wybór: ")
if option == "1":
    pprint(data)
elif option == "2":
    nazwa_krypto = input("Podaj symbol krypto np. Ethereum = ETH: ")
    krypto = data.get('data')
    pprint([char for char in krypto if char.get('symbol') == nazwa_krypto])