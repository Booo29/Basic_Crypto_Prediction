# Cryptocurrency Price Prediction

This project uses Python to predict cryptocurrency prices based on historical data. It utilizes the CoinGecko API to fetch market data and the `scikit-learn` library to perform predictions using linear regression.

## Features

- **Cryptocurrency Data Retrieval**: Connects to the CoinGecko API to extract historical price data.
- **Price Visualization**: Generates charts of the historical prices for the selected cryptocurrency.
- **Future Price Prediction**: Uses a linear regression model to predict the price of the cryptocurrency for the upcoming days.
- **Prediction Chart Generation**: Displays the price prediction graphically alongside historical prices.

## Requirements

Make sure to have the following libraries installed:

- `requests`
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

You can install the necessary libraries using pip:

```bash
pip install requests pandas numpy matplotlib scikit-learn.
```

## Example
When running the script with the default values, you will get charts showing the price of Bitcoin in USD and its prediction for the next 7 days.

## License
This project is licensed under the MIT License. See the LICENSE file for more details
