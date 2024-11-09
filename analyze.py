from stockData import Analyze
import pandas as pd

data = pd.read_json("SPY.json")
data.index = pd.to_datetime(data.index)
client = Analyze(data)
forecast = client.arima_predict(column= '4. close', order=(3, 6, 9), steps=4)