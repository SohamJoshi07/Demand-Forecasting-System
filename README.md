📊 Walmart Demand Forecasting System

An end-to-end Machine Learning–based Demand Forecasting system built using retail sales data and deployed with an interactive Streamlit dashboard.
The model predicts future product demand based on historical sales patterns, helping businesses make smarter inventory and supply chain decisions.

---

🚀 Project Overview

Demand forecasting is a critical task in retail analytics. In this project:

Large-scale Walmart sales data is preprocessed and optimized for memory usage

Time-series features such as lag sales and rolling averages are engineered

A Machine Learning model is trained to capture demand behavior

Given recent sales inputs, the system predicts future demand

A Streamlit web app provides a business-friendly forecasting interface

This project demonstrates a complete Data Science lifecycle: preprocessing → feature engineering → model training → evaluation → deployment.

---

✨ Features

Time-series demand forecasting model

Lag-based feature engineering (weekly & monthly signals)

Rolling mean demand analysis

Memory-efficient handling of large datasets

Real-time forecasting via Streamlit UI

Visual trend + forecast graph for business interpretation

Production-style project structure (no raw data stored in repo)

---

🛠 Tech Stack

Python

Pandas / NumPy

Scikit-learn

LightGBM

Matplotlib

Streamlit

Joblib (for saving trained model)

---

📂 Project Structure
Walmart-Forecasting/
│
├── dashboard.py               # Streamlit forecasting application
├── Main.ipynb                 # Data preprocessing & model training
├── walmart_forecast_model.pkl # Saved model (local use)
├── model_features.pkl         # Feature schema
├── requirements.txt           # Project dependencies
├── .gitignore                 # Prevents dataset upload
├── README.md                  # Project documentation

---

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/Walmart-Forecasting.git
cd Walmart-Forecasting

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run dashboard.py


The app will open automatically in your browser.

---

📥 Dataset

The dataset is not included due to GitHub’s 100MB file limit.

Download the dataset from Kaggle (Walmart M5 Forecasting dataset)
and place the CSV files inside a local /data folder before running the notebook.

---

🧪 Example Workflow

User Inputs:

Forecast Date: 2026-02-15
Sales 7 Days Ago: 420
Sales 28 Days Ago: 390
Last 7 Days Sales: [410, 430, 415, 398, 402, 421, 417]


Model Output:

Predicted Demand: 436 Units


The dashboard also visualizes the recent sales trend along with the forecasted value.

---

📌 Use Cases

Retail inventory planning

Supply chain demand estimation

Sales trend analysis

Business decision support dashboards

Time-series forecasting learning project

---

📈 Future Improvements

Multi-store forecasting support

Deep learning–based time-series models (LSTM / Transformers)

Automated data pipeline integration

Cloud deployment for real-time usage

Advanced seasonal decomposition

---

👤 Author

Soham Joshi
Aspiring Data Scientist focused on solving real-world business problems using Machine Learning.

---

⭐ Acknowledgements

Inspired by real-world retail forecasting systems used by companies like Walmart, Amazon, and Target to optimize supply chain and inventory decisions.

If you like this project, don’t forget to ⭐ the repository!

