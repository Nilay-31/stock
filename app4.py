import streamlit as st
import pickle
import pandas as pd

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

        # Convert forecast to DataFrame for Streamlit line chart
        forecast_df = pd.DataFrame({'Forecast': forecast})
        
        # Display forecast
        st.line_chart(forecast_df)
    except Exception as e:
        st.error(f"Error loading model: {e}")
