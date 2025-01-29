import pandas as pd
import streamlit as st
import numpy as np
import datetime as dt
import pickle
from datetime import datetime

# [1] Streamlit Title
st.title('Model Deployment: SARIMA MODEL')
st.subheader('Apple Dataset')

# [2] Load Dataset
df = pd.read_csv(r'C:\Users\PC\Downloads\Data Science\project\AAPL.csv')
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# [3] User Input for Forecast Period
periods_input = st.slider('Predictions for Days?', min_value=1, max_value=60)

# [4] Load SARIMA Model & Forecast
loaded_model = pickle.load(open(r'C:\Users\PC\Downloads\Data Science\pickle_file.sav', 'rb'))
predict = loaded_model.forecast(periods_input)
fort = pd.DataFrame(predict.values, index=pd.date_range('2019-12-31', periods=periods_input), columns=["Adj Close"])

# [5] Prediction Button & Output
if st.button("Predict"):
    st.sidebar.markdown(':red[Predictions on Apple Stock Exchange (Year: 2012 - 2019)]')
    st.sidebar.write('Forecasted Days:', periods_input)
    st.sidebar.write(predict)

    # **Streamlit Line Chart Instead of Matplotlib**
    st.subheader("Actual vs Forecasted Prices")
    combined_df = df[['Adj Close']].copy()
    combined_df = combined_df.append(fort)
    st.line_chart(combined_df)

    # About Section
    st.header("About:")
    st.subheader("Mentor: Neha Gupta")
    st.write("P-185 : Team-6 :")
