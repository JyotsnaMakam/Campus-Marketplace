import streamlit as st
import pandas as pd

st.set_page_config(page_title="Marketplace", layout="wide")

# --- NEW: Cart Header Section ---
if 'cart' not in st.session_state:
 st.session_state['cart'] = []

col_title, col_cart = st.columns([3, 1])
with col_title:
 st.title("🛍️ Campus Service Marketplace")
with col_cart:
# This shows you the count in real-time!
 st.metric("Items in Cart", len(st.session_state['cart']))
 if st.button("🛒 Go to My Bookings"):
  st.switch_page("pages/3_My_Bookings.py")

st.divider()

# --- Services Data ---
services = [
{"ID": 1, "Name": "Python Tutoring", "Price": 25.0, "Category": "Academic"},
{"ID": 2, "Name": "Laundry Service", "Price": 15.0, "Category": "Personal"},
{"ID": 3, "Name": "Tech Repair", "Price": 50.0, "Category": "Technical"},
{"ID": 4, "Name": "Meal Prep", "Price": 30.0, "Category": "Food"}
]

df_services = pd.DataFrame(services)

# Display Services
for index, row in df_services.iterrows():
 with st.container():
  c1, c2, c3 = st.columns([2, 1, 1])
  c1.write(f"### {row['Name']}")
  c1.caption(f"Category: {row['Category']}")
  c2.write(f"## ${row['Price']}")

# When you click this, it adds to the list WITHOUT removing the old ones
 if c3.button(f"Add to Cart", key=f"btn_{row['ID']}"):
  st.session_state['cart'].append(row.to_dict())
  st.toast(f"✅ Added {row['Name']}!") # This is a small popup notification
  st.rerun() # This refreshes the counter at the top immediately