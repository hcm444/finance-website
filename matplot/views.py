import base64
import io
import urllib
import matplotlib.pyplot as plt
import pandas as pd
# plotting
import yfinance as yf
# yahoo finance
from django.shortcuts import render

# for rendering
stocks = []
# create model here
stock1 = yf.download('MSFT', start='2022-01-01', end='2022-03-28', progress=False, auto_adjust=True)
stock2 = yf.download('NVDA', start='2022-01-01', end='2022-03-28', progress=False, auto_adjust=True)
stock3 = yf.download('APPL', start='2022-01-01', end='2022-03-28', progress=False, auto_adjust=True)
stock4 = yf.download('TSLA', start='2022-01-01', end='2022-03-28', progress=False, auto_adjust=True)


# get info
# Create your views here.
def home(request):
    plt.plot(stock1)
    plt.plot(stock2)
    plt.plot(stock3)
    plt.plot(stock4)
    # plotting
    return render(request, 'home.html', {'data1': (plot())})
    return render(request, 'home.html', {'data2': (plot())})
    return render(request, 'home.html', {'data3': (plot())})
    return render(request, 'home.html', {'data4': (plot())})
    # return to home.html


def plot():
    buffer = io.BytesIO()
    plt.gcf().savefig(buffer, format='png')
    # .png format
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    # base 64 lib
    uri = urllib.parse.quote(string)
    return uri
