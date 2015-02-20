__author__ = 'danelleebreo'

import urllib2, csv


class BadDataError(Exception):
    pass



def make_ticket_url(symbol):
    base_url = "http://ichart.finance.yahoo.com/table.csv?s="
    ticker_url = base_url + symbol.upper()
    return ticker_url


def get_csv_for_stock(symbol):

    response = urllib2.urlopen("http://ichart.finance.yahoo.com/table.csv?s=AAPL")
    response_reader = csv.DictReader(response)
    return response_reader


stocks_to_get = [
    'AAPL',
    'MSFT'
]

stock_data = [get_csv_for_stock(symbol) for symbol in stocks_to_get]
try:
    for data_info in zip(*stock_data):
        date =  data_info[0]["Date"]
        for stock in data_info:
            if stock['Date'] != date:
                raise BadDataError("Incomplete or badly ordered data!")
            print data_info[0]["Date"], ":"
            for stock in data_info:
                print("\t", stock['Close'])
except:
    print BadDataError
    print("Something Went Wrong")












