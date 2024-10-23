import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def get_crypto_data(crypto_name, currency, limit):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}/market_chart?vs_currency={currency}&days={limit}"
    response = requests.get(url)
    data = response.json()
    return data

def get_crypto_price(crypto_name, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data

def get_crypto_data_frame(crypto_name, currency, limit):
    data = get_crypto_data(crypto_name, currency, limit)
    if 'prices' not in data:
        print('Error: Invalid crypto name or currency')
        return None
    else:
        df = pd.DataFrame(data['prices'], columns=['time', 'price'])
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        return df

def get_crypto_price_df(crypto_name, currency):
    data = get_crypto_price(crypto_name, currency)
    df = pd.DataFrame(data)
    return df

def plot_crypto_price(crypto_name, currency, limit):
    df = get_crypto_data_frame(crypto_name, currency, limit)
    plt.figure(figsize=(20, 10))
    plt.plot(df['time'], df['price'], label=crypto_name)
    plt.title(f'{crypto_name} price in {currency}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend([crypto_name])
    plt.grid()
    plt.savefig(f'{crypto_name}_price.png')
    plt.close()

def predict_crypto_price(crypto_name, currency, limit, days):
    df = get_crypto_data_frame(crypto_name, currency, limit)
    df['time_index'] = (df['time']- df['time'].min()).dt.days
    X = df['time_index'].values.reshape(-1, 1)
    y = df['price'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    future_days_index = np.array([X[-1] + i for i in range(1, days + 1)]).reshape(-1, 1)
    future_prices = model.predict(future_days_index)
    future_days = df['time'].max() + pd.to_timedelta(range(1, days + 1), unit='D')
    return future_days, future_prices

def plot_crypto_price_prediction(crypto_name, currency, limit, days):
    df = get_crypto_data_frame(crypto_name, currency, limit)
    future_days, future_prices = predict_crypto_price(crypto_name, currency, limit, days)
    plt.figure(figsize=(20, 10))
    plt.plot(df['time'], df['price'], label=crypto_name)
    plt.plot(future_days, future_prices, label=f'{crypto_name} prediction', linestyle='dashed')
    plt.title(f'{crypto_name} price prediction in {currency}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend([crypto_name, f'{crypto_name} prediction'])
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{crypto_name}_prediction.png')
    plt.close()

def main():
    crypto_name = 'bitcoin'
    currency = 'usd'
    limit = 30
    days = 7
    plot_crypto_price(crypto_name, currency, limit)
    plot_crypto_price_prediction(crypto_name, currency, limit, days)

if __name__ == '__main__':
    main()
