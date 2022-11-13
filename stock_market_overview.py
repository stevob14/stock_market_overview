from yahoo_fin.stock_info import *
import json

def dec_format(value):
    try:
        change = "{0:.2f}".format(value)
    except(TypeError):
        change = "N/A"
    return change

def comma_format(value):
    try:
        change = "{:,}".format(float(value))
    except(TypeError):
        change = "N/A"
    return change

sp500 = get_quote_table('^GSPC')
dow30 = get_quote_table('^DJI')
nasdaq = get_quote_table('^IXIC')
russel2000 = get_quote_table('^RUT')

## Quote Price, Previous Close

## Change = Quote Price - Previous Close
## pChange = (Change / Quote Price) * 100

sp500_price = sp500['Quote Price']
sp500_close = sp500['Previous Close']

sp500_change = sp500_price - sp500_close
sp500_pchange = (sp500_change / sp500_price) * 100

dow30_price = dow30['Quote Price']
dow30_close = dow30['Previous Close']

dow30_change = dow30_price - dow30_close
dow30_pchange = (dow30_change / dow30_price) * 100

nasdaq_price = nasdaq['Quote Price']
nasdaq_close = nasdaq['Previous Close']

nasdaq_change = nasdaq_price - nasdaq_close
nasdaq_pchange = (nasdaq_change / nasdaq_price) * 100

russel2000_price = russel2000['Quote Price']
russel2000_close = russel2000['Previous Close']

russel2000_change = russel2000_price - russel2000_close
russel2000_pchange = (russel2000_change / russel2000_price) * 100

data = [[comma_format(dec_format(sp500_price)),dec_format(sp500_change),dec_format(sp500_pchange)],[comma_format(dec_format(dow30_price)),dec_format(dow30_change),dec_format(dow30_pchange)],[comma_format(dec_format(nasdaq_price)),dec_format(nasdaq_change),dec_format(nasdaq_pchange)],[comma_format(dec_format(russel2000_price)),dec_format(russel2000_change),dec_format(russel2000_pchange)]]

with open('stock_market_overview.txt','w') as outfile:
    json.dump(data,outfile)
