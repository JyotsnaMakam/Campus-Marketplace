import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Price Predictor", layout="wide")

st.title("🤖 AI Service Price Predictor")
st.write("Using a **Random Forest Regressor** to estimate market rates based on Kaggle data.")

# 1. Load the model and the encoder
# (Make sure you saved these in Phase 2!)
try:
  with open('price_predictor.pkl', 'rb') as f:
   model = pickle.load(f)

# We need the original data to know what the categories are
  df = pd.read_csv("kaggle_users.csv")
  categories = df['Category'].dropna().unique()

  st.divider()

# 2. User Input
  selected_cat = st.selectbox("Select a Service Category:", categories)

  if st.button("Predict Estimated Price"):
# We must transform the text input just like we did in training
# For a simple version, we find the 'code' of the category
# In a real setup, you'd use your saved LabelEncoder here
   cat_index = list(categories).index(selected_cat)

   prediction = model.predict([[cat_index]])

   st.metric(label="Estimated Market Value", value=f"${prediction[0]:.2f}")
   st.info("This prediction is based on historical service data from your Kaggle dataset.")

except FileNotFoundError:
   st.error("Model file not found. Please run your training script (Phase 2) first!")