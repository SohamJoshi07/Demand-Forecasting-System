import streamlit as st
import joblib
import pandas as pd

model = joblib.load('walmart_forecast_model.pkl')
features = joblib.load('model_features.pkl')

st.title("🛒 Demand Forecasting Tool")

st.header("📅 Forecast Setup")

forecast_date = st.date_input("Select Date to Forecast")

st.header("📊 Recent Sales Information")

st.write("Enter known recent sales figures (from your reports)")

lag_7 = st.number_input("Sales 7 Days Ago", min_value=0)
lag_28 = st.number_input("Sales 28 Days Ago (4 Weeks Ago)", min_value=0)

st.subheader("Last 7 Days Sales (for Average Calculation)")

d1 = st.number_input("Day -1 Sales", min_value=0)
d2 = st.number_input("Day -2 Sales", min_value=0)
d3 = st.number_input("Day -3 Sales", min_value=0)
d4 = st.number_input("Day -4 Sales", min_value=0)
d5 = st.number_input("Day -5 Sales", min_value=0)
d6 = st.number_input("Day -6 Sales", min_value=0)
d7 = st.number_input("Day -7 Sales", min_value=0)


if st.button("Forecast Demand"):

    import pandas as pd

    forecast_date = pd.to_datetime(forecast_date)

    # Calendar features (auto-derived)
    dayofweek = forecast_date.dayofweek
    month = forecast_date.month
    year = forecast_date.year
    week = forecast_date.isocalendar().week

    # Rolling average from user inputs
    rolling_mean_7 = (d1 + d2 + d3 + d4 + d5 + d6 + d7) / 7

    input_data = pd.DataFrame([{
        "dayofweek": dayofweek,
        "month": month,
        "year": year,
        "week": week,
        "lag_7": lag_7,
        "lag_28": lag_28,
        "rolling_mean_7": rolling_mean_7
    }])

    prediction = model.predict(input_data)
    predicted_value = prediction[0]

    st.success(f"📦 Expected Demand: {predicted_value:.2f}")


    import matplotlib.pyplot as plt

    history = [d7, d6, d5, d4, d3, d2, d1]
    history.append(predicted_value)

    labels = ["-7","-6","-5","-4","-3","-2","-1","Forecast"]

    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(labels, history, marker='o')
    ax.set_title("Sales Trend & Forecast")
    ax.set_xlabel("Days Relative to Forecast")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

   

