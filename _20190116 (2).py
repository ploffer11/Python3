import datetime
from collections import namedtuple

def middle(stock, date):
    symbol, current, high, low = stock
    return ((high+low)/2, date)

stock = "FB", 177.46, 178.67, 175.79

mid_value, date = middle(
    stock, datetime.date(2018, 8, 27)
)

Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])
stock2 = Stock("FB", 177.46, 178.67, 175.79)

