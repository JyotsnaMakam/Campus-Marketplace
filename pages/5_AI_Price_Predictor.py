import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="AI Price Predictor", layout="wide")

st.title("🤖 AI Service Price Predictor")
st.markdown("---")

# 1. Check if the model exists before trying to open it
if os.path.exists('price_predictor.pkl'):
 with open('price_predictor.pkl', 'rb') as f:
  model = pickle.load(f)

 st.write("This tool uses a **Random Forest model** to estimate the market value of a service based on its category.")

# 2. Get categories for the dropdown
 df = pd.read_csv("kaggle_users.csv",encoding='latin1')
 categories = sorted(df['gender'].dropna().unique())

# 3. User Interaction
 selected_cat = st.selectbox("Select a gender Category:", categories)

 if st.button("Predict Price"):
# Simple encoding: find the index of the selected category
  cat_index = list(categories).index(selected_cat)

# Make the prediction
  prediction = model.predict([[cat_index]])

  st.success(f"The estimated market price for **{selected_cat}** is: **${prediction[0]:.2f}**")
  st.info("Note: This is a machine learning estimate based on your Kaggle dataset.")

else:
  st.error("⚠️ Model file (price_predictor.pkl) not found!")
  st.info("Please make sure you have run your Phase 2 training script and pushed the .pkl file to GitHub.")