import base64
import io
import urllib
# plotting
import yfinance as yf
# yahoo finance
from django.shortcuts import render

# for rendering
from matplotlib import pyplot as plt


# create model here
# multiple stocks


# get info
# Create your views here.
def home(request):
    stock = yf.download('MSFT', start='2022-01-01', end='2022-03-28',)
    plt.plot(stock)

    # plot them all
    # plotting

    buffer = io.BytesIO()
    plt.gcf().savefig(buffer, format='png')
    # .png format
    buffer.seek(0)
    # base 64 lib
    return render(request, 'home.html', {'data': (urllib.parse.quote(base64.b64encode(buffer.read())))})
    # print each on top
    # return to home.html
