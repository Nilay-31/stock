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
      loaded_model = load(open('sarima_model.pkl', 'rb')) 
        fct = pd.DataFrame(loaded_model.forecast(30))
        fct
        # Convert forecast to DataFrame for Streamlit line chart
        forecast_df = pd.DataFrame({'Forecast': forecast})
        
        # Display forecast
        st.line_chart(forecast_df)
    except Exception as e:
        st.error(f"Error loading model: {e}")
