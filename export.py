from stockData import StockData

# Initialize API with your key
with open('av-key.txt', 'r') as file:
    api_key = file.read()

stock_data_client = StockData(api_key=api_key)

data = stock_data_client.get_intraday_data('SPY')

data.to_json('SPY.json')
data.to_csv('SPY.csv')