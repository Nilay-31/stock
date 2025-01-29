import streamlit as st
import pickle
import pandas as pd

st.title("SARIMA Model Deployment")

try:
    # Load saved SARIMA model
    with open('sarima_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)  

    st.success("SARIMA model loaded successfully!")

    # Forecasting example
    steps = st.slider("Forecast Steps", min_value=1, max_value=100, value=30)
    forecast = loaded_model.forecast(steps=steps)

    # Convert forecast to DataFrame for Streamlit visualization
    forecast_df = pd.DataFrame({'Forecast': forecast})

    # Display forecast using Streamlit's built-in chart
    st.line_chart(forecast_df)

except Exception as e:
    st.error(f"Error loading model: {e}")
