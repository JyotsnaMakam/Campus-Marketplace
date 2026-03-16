import streamlit as st
import pandas as pd

st.title("💳 Secure Checkout")

if 'cart' not in st.session_state or len(st.session_state['cart']) == 0:
 st.error("No items to pay for!")
else:
 total_price = sum(item['Price'] for item in st.session_state['cart'])
 st.write(f"#### Total to Pay: ${total_price}")

# Payment Method Selection
 method = st.radio("Select Payment Method", ["Credit Card", "Campus Credits (Cash-like)"])

 if method == "Credit Card":
  st.text_input("Card Number", placeholder="0000 0000 0000 0000")
  col1, col2 = st.columns(2)
  col1.text_input("Expiry", placeholder="MM/YY")
  col2.text_input("CVV", type="password")

 if st.button("Confirm Payment"):
  from database import update_balance  
  update_balance(st.session_state['username'], total_price)  
# Logic to "Clear" the cart and show success
  st.session_state['cart'] = []
  st.success("Payment Successful!")
  st.balloons()
  st.info("Your service will be delivered to your campus email soon.")