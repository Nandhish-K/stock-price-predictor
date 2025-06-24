import numpy as np
from sklearn.linear_model import LinearRegression

def predict_stock_price(days):
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([100, 120, 130, 150, 170])
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict(np.array([[days]]))
    return prediction[0]
