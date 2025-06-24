from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .ml_model import predict_stock_price

def home(request):
    prediction = None
    if request.method == 'POST':
        days = int(request.POST.get('days'))
        prediction = predict_stock_price(days)
    return render(request, 'predictor/index.html', {'prediction': prediction})
