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

stocks = 'TSLA'
stocks_start = '2022-01-01'
stocks_end = '2022-03-28'
# create model here
df_yahoo = yf.download(stocks, start=stocks_start, end=stocks_end, progress=False, auto_adjust=True)


# get info
# Create your views here.
def home(request):
    plt.plot(df_yahoo)

    # plotting
    buffer = io.BytesIO()
    plt.gcf().savefig(buffer, format='png')
    # .png format
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    # base 64 lib
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})
    # return to home.html
