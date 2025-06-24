import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_stock_price(symbol, future_days):
    try:
        df = yf.download(symbol, period="30d", interval="1d")['Close']
        if df.empty:
            return None  # Invalid symbol or no data
        df = df.dropna()

        X = np.arange(len(df)).reshape(-1, 1)
        y = df.values

        model = LinearRegression()
        model.fit(X, y)

        future_day = len(df) + future_days
        prediction = model.predict(np.array([[future_day]]))

        return float(prediction[0]), df
    except Exception as e:
        print("Error:", e)
        return None, None
