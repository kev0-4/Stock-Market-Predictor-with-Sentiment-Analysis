import pandas as pd
import joblib
import numpy as np
import real_time_sentiment as rts

def run_model(company_symbol):
    company_mapping = {
        0: 'ADANIPORTS.NS', 1: 'APOLLOHOSP.NS', 2: 'ASIANPAINT.NS', 3: 'AXISBANK.NS',
        4: 'BAJAJ-AUTO.NS', 5: 'BAJAJFINSV.NS', 6: 'BPCL.NS', 7: 'BRITANNIA.NS', 8: 'CIPLA.NS', 9: 'COALINDIA.NS',
        10: 'DIVISLAB.NS', 11: 'DRREDDY.NS', 12: 'EICHERMOT.NS', 13: 'GRASIM.NS', 14: 'HCLTECH.NS', 15: 'HDFCLIFE.NS',
        16: 'HDFCBANK.NS', 17: 'HEROMOTOCO.NS', 18: 'HINDALCO.NS', 19: 'HINDUNILVR.NS', 20: 'ICICIBANK.NS',
        21: 'INDUSINDBK.NS', 22: 'INFY.NS', 23: 'ITC.NS', 24: 'JIOFIN.NS', 25: 'JSWSTEEL.NS', 26: 'KOTAKBANK.NS',
        27: 'LT.NS', 28: 'LTIM.NS', 29: 'M&M.NS', 30: 'MARUTI.NS', 31: 'NESTLEIND.NS', 32: 'NIFTY50.NS', 33: 'NTPC.NS',
        34: 'ONGC.NS', 35: 'POWERGRD.NS', 36: 'RELIANCE.NS', 37: 'SBILIFE.NS', 38: 'SBIN.NS', 39: 'SUNPHARMA.NS',
        40: 'TCS.NS', 41: 'TATACONSUM.NS', 42: 'TATAMOTORS.NS', 43: 'TATASTEEL.NS', 44: 'TECHM.NS', 45: 'TITAN.NS',
        46: 'ULTRACEMCO.NS', 47: 'UPL.NS', 48: 'WIPRO.NS'
        }

    company = company_mapping[company_symbol]
    print(company)
    data = pd.DataFrame({
        'Close_Lagged': [rts.get_current_closing(company_mapping[company_symbol])],  # Provide your desired values
        'Sentiment_Score': [rts.get_current_sentiment(company_mapping[company_symbol])],  # Provide your desired values
        'Company': [company_symbol],  # Provide your desired values
    })

    # Create the test DataFrame
    test_data = pd.DataFrame(data)

    model = joblib.load('stock_price_predictor_model.joblib')  # Replace with your model filename

    # Extract features from test data (similar to how you did it in the training code)
    X_test = test_data[['Close_Lagged', 'Sentiment_Score','Company']]  # Modify the feature names as needed

    # Make predictions using the loaded model
    y_pred = model.predict(X_test)

    # Print or visualize the predictions
    print(y_pred)
    return y_pred


run_model(48)