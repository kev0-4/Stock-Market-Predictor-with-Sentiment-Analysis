import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, accuracy_score, mean_absolute_error
from statsmodels.tsa.stattools import adfuller
from sklearn.linear_model import Ridge
import joblib  # Import joblib for model serialization

# Load your dataset
data = pd.read_csv('final_nifty_sentiments_dummy.csv')  # Replace with your dataset file
data.drop('description',inplace=True,axis=1)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Time Series Analysis
def analyze_time_series(data):
    # Visualize stock price data
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price')
    plt.title('Stock Price Over Time')
    plt.legend()
    plt.show()

    # Check stationarity with Dickey-Fuller test
    result = adfuller(data['Close'])
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[4])

    # If not stationary, perform differencing
    if result[1] > 0.05:
        data['Close_diff'] = data['Close'] - data['Close'].shift(1)
        data.dropna(inplace=True)
        analyze_time_series(data)  # Re-run analysis on differenced data
    else:
        print('Data is stationary.')

# Analyze and preprocess the time series data
analyze_time_series(data)

# Feature Engineering
data['Sentiment_Score'] = data['Compound']  # Replace with your chosen sentiment feature
data['Close_Lagged'] = data['Close'].shift(1)
data['Company'] = data['Company'].shift(1)
data.dropna(inplace=True)

# Define features and target variable
X = data[['Close_Lagged', 'Sentiment_Score','Company']]
y = data['Open']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Create and train your machine learning model (Linear Regression)
model = Ridge()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
#print(y_pred)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae:.2f}')


# Calculate percentage difference for each data point
percentage_difference = ((y_test - y_pred) / y_test) * 100
# Calculate the mean percentage difference (average across all data points)
mean_percentage_difference = percentage_difference.mean()

print(f'Mean Percentage Difference: {mean_percentage_difference:.2f}%')

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot the predictions against actual data
plt.figure(figsize=(12, 6))
plt.plot(data.index[-len(y_test):], y_test, label='Actual Close Price', color='blue')
plt.plot(data.index[-len(y_test):], y_pred, label='Predicted Close Price', color='red')
plt.title('Actual vs. Predicted Stock Price')
plt.legend()
plt.show()

# Save the trained model using joblib
model_filename = 'stock_price_predictor_model.joblib'
joblib.dump(model, model_filename)
print(f"Model saved as {model_filename}")
