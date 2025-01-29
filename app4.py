import streamlit as st
import pickle
import pandas as pd

st.title("SARIMA Model Deployment")

# Load saved SARIMA model
with open('sarima_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)  # Ensure correct indentation

print("SARIMA model loaded successfully!")

# Forecasting example
steps = 30  # Number of future steps to predict
forecast = loaded_model.forecast(steps=steps)

print("Forecasted values:", forecast)
        # Display forecast
        st.line_chart(forecast_df)
    except Exception as e:
        st.error(f"Error loading model: {e}")
