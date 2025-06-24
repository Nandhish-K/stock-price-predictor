from django.shortcuts import render
from .ml_model import predict_stock_price
import plotly.graph_objs as go
import plotly.offline as opy

def get_stock_plot(df):
    trace = go.Scatter(
        x=df.index,
        y=df.values,
        mode='lines+markers',
        name='Close Price',
        line=dict(color='royalblue', width=2)
    )
    layout = go.Layout(title='Stock Price - Last 30 Days', xaxis_title='Date', yaxis_title='Price')
    fig = go.Figure(data=[trace], layout=layout)
    div = opy.plot(fig, auto_open=False, output_type='div')
    return div

def home(request):
    prediction = None
    stock_data = None
    graph = None

    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        days = int(request.POST.get('days'))

        prediction, stock_data = predict_stock_price(symbol, days)

        # ✅ Add this block AFTER you get stock_data and prediction
        if prediction and stock_data is not None:
            graph = get_stock_plot(stock_data)

    return render(request, 'predictor/index.html', {
        'prediction': prediction,
        'stock_data': stock_data,
        'graph': graph
    })
