import streamlit as st
import pandas as pd

st.title("🛒 Your Selected Services")

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
 st.warning("Please log in first to see your bookings.")
else:
 if 'cart' in st.session_state and len(st.session_state['cart']) > 0:
  df_cart = pd.DataFrame(st.session_state['cart'])
  st.table(df_cart[['Name', 'Price', 'Category']])

  total_price = df_cart['Price'].sum()
  st.write(f"### Total Amount: ${total_price}")

  if st.button("Proceed to Payment"):
   st.switch_page("pages/4_Payments.py")
 else:
  st.info("Your cart is empty. Go to the Marketplace to add services!")