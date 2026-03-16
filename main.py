import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Campus Marketplace", layout="wide")

st.title("🏡 Campus Marketplace Home")

# Check if user is logged in
if 'logged_in' in st.session_state and st.session_state['logged_in']:
 username = st.session_state['username']
 #st.markdown(f"### Welcome back, **{username}**!")

# Dashboard Logic: Fetch current balance from CSV
 df = pd.read_csv("users.csv")
 user_row = df[df['username'] == username]

 if not user_row.empty:
  current_balance = user_row.iloc[0]['balance']

  st.markdown(f"### Welcome back, **{username}**!")

# Dashboard Visuals
  col1, col2, col3 = st.columns(3)
  with col1:
   st.metric(label="Current Balance", value=f"${current_balance:.2f}")
  with col2:
   cart_count = len(st.session_state.get('cart', []))
   st.metric(label="Items in Cart", value=cart_count)
  with col3:
   st.metric(label="Account Status", value="Active ✅")

  st.divider()
  st.info("Navigate to the **Marketplace** in the sidebar to start shopping!")

else:
# --- LOGGED OUT VIEW ---
   st.write("### Welcome to the Campus Marketplace!")

   st.divider()
   st.info("Ready to get started? Log in to access your dashboard and funds.")

# This is the important new button!
   if st.button("👉 Click here to Go to Registration"):
# This will only work once your GitHub folder is lowercase 'pages'
     st.switch_page("pages/1_Registration.py")

   st.divider()