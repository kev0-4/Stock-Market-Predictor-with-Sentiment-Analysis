import pandas as pd
import joblib
import numpy as np
import yfinance as yf

def get_forex_prediction(forex_index):
    forex_mapping = {
        0:'AUD-USD-ASK.joblib', 1:'AUD-USD-BID.joblib', 2:'EUR-USD-ASK.joblib', 3:'EUR-USD-BID.joblib',
        4:'GBP-USD-ASK.joblib', 5:'GBP-USD-BID.joblib', 6:'NZD-USD-ASK.joblib', 7:'NZD-USD-BID.joblib',
        8:'USD-CAD-ASK.joblib', 9:'USD-CAD-BID.joblib', 10:'USD-CHF-ASK.joblib', 11:'USD-CHF-BID.joblib',
        12:'USD-JPY-ASK.joblib', 13:'USD-JPY-BID.joblib', 14:'XAG-USD-ASK.joblib', 15:'XAG-USD-BID.joblib'
    }

    # forex_index = 0
    forex = yf.Ticker(forex_mapping[forex_index][:3]+'=X')
    data = forex.history(period="1d", interval="1m")
    data.info()
    #Close high Low Volume
    forex_close = data['Close'].iloc[-1]
    forex_high = data['High'].iloc[-1]
    forex_low = data['Low'].iloc[-1]
    forex_volume = data['Volume'].iloc[-1]

    model = joblib.load(forex_mapping[forex_index])
    forex_prediction = model.predict(pd.DataFrame([{'Close':forex_close, 'High':forex_high,'Low':forex_low, 'Volume':forex_volume}]))
    print(forex_prediction)
get_forex_prediction(5)