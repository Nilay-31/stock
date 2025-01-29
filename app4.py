import pickle
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Sample data (replace with your actual time series data)
data = pd.read_csv('your_timeseries_data.csv', parse_dates=True, index_col='Date')

# Train SARIMA model
sarima_model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))  # Example parameters
sarima_result = sarima_model.fit(disp=False)

# Pickle the model
with open('sarima_model.pkl', 'wb') as file:
    pickle.dump(sarima_result, file)

# Load the pickled SARIMA model
with open('sarima_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Make predictions (example: forecast the next 12 time points)
forecast = loaded_model.forecast(steps=12)
print(forecast)

from flask import Flask, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pickled model
with open('sarima_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/forecast', methods=['GET'])
def forecast():
    # Assuming you're predicting for the next 12 periods
    forecast = loaded_model.forecast(steps=12)
    return jsonify(forecast.tolist())

if __name__ == '__main__':
    app.run(debug=True)
