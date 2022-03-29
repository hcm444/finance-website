import base64
import io
import urllib
import matplotlib.pyplot as plt
# plotting
import yfinance as yf
# yahoo finance
from django.shortcuts import render

# for rendering

stock = 'TSLA'
stock_start = '2022-01-01'
stock_end = '2022-03-28'
# create model here
df_yahoo = yf.download(stock, start=stock_start, end=stock_end, progress=False)


# get info
# Create your views here.
def home(request):
    plt.plot(df_yahoo)
    # plotting
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    # .png format
    buf.seek(0)
    string = base64.b64encode(buf.read())
    # base 64 lib
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})
    # return to home.html
