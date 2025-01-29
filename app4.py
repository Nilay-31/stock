import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

st.title("SARIMA Model Deployment")

# Load saved SARIMA model
if st.button("Load Saved SARIMA Model"):
    try:
        with open('sarima_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
        st.success("Model loaded successfully!")
        
        # Forecast
        steps = st.slider("Forecast Steps", min_value=1, max_value=100, value=30)
        forecast = loaded_model.forecast(steps=steps)

        # Plot forecast
        plt.figure(figsize=(10, 6))
        plt.plot(forecast, label="Forecast", color="blue")
        plt.title("SARIMA Forecast")
        plt.legend()
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error loading model: {e}")
