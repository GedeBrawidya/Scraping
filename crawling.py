import requests
import pandas as pd
import matplotlib.pyplot as plt

# Ganti dengan API key Anda
API_KEY = '815ae33f-31e9-4031-8d20-5d34c955b04d'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '10',  # Ambil 10 cryptocurrency pertama
    'convert': 'IDR'
}

headers = {
    'X-CMC_PRO_API_KEY': API_KEY,
    'Accept': 'application/json',
}

response = requests.get(url, headers=headers, params=parameters)

data = response.json()

# Ambil data yang dibutuhkan
coins = data['data']
coins_data = []

for coin in coins:
    coins_data.append({
        'name': coin['name'],
        'symbol': coin['symbol'],
        'price': coin['quote']['IDR']['price'],
        'market_cap': coin['quote']['IDR']['market_cap'],
        'volume_24h': coin['quote']['IDR']['volume_24h'],
        'percent_change_24h': coin['quote']['IDR']['percent_change_24h'],
        'rank': coin['cmc_rank']
    })

# Simpan data ke dalam DataFrame pandas
df = pd.DataFrame(coins_data)

print(df)

plt.hist(df['price'], bins=10, color='blue', alpha=0.7)
plt.title('Distribusi Harga Cryptocurrency')
plt.xlabel('Harga (IDR)')
plt.ylabel('Frekuensi')
plt.show()


