from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

class StockData:
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.ts = TimeSeries(key=self.api_key, output_format='pandas')
        
    def get_intraday_data(self, symbol: str):
        data, _ = self.ts.get_intraday(symbol=symbol, outputsize='full', interval='60min')
        return data
    
class Analyze:
    
    def __init__(self, data: pd):
        self.data = data
        
    def arima_predict(self, column: str, order: list, steps: int):
        time_series = self.data[column]
        
        model = ARIMA(time_series, order=order)
        fitted_model = model.fit()

        # Forecast the specified number of steps ahead
        forecast = fitted_model.forecast(steps=steps)
        forecast_index = pd.date_range(start=time_series.index[0] + pd.Timedelta(minutes=60), periods=steps, freq='60T')
        forecast.index = forecast_index

        #forecast_series = pd.Series(forecast, index=forecast_index)
        
        plt.figure(figsize=(10, 6))
        plt.plot(time_series, label="Historical Data", color='blue')
        plt.plot(forecast, label="Forecast", color='red')
        plt.title(f"ARIMA Forecast for {column}")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.show()
        
        return forecast