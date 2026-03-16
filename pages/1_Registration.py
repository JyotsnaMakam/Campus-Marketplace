import streamlit as st
from database import verify_user, add_user
if st.button("Back to Home"):
 st.switch_page("main.py")
st.set_page_config(page_title="User Profile")
st.title("👤 Campus User Portal")

tab1, tab2 = st.tabs(["Login", "New Registration"])

with tab1:
 st.header("Login with Kaggle Account")
 u = st.text_input("Username")
 p = st.text_input("Password", type="password")

 if st.button("Log In"):
  if verify_user(u, p):
   st.session_state['logged_in'] = True
   st.session_state['username'] = u
   st.success(f"Welcome, {u}!")
   st.balloons()
  else:
   st.error("Invalid credentials. Hint: Default password is 'student123'")

with tab2:
 st.header("Create New Student Account")
 new_user = st.text_input("Choose a Username", key="reg_user")
 new_email = st.text_input("Campus Email", key="reg_email")
 new_pass = st.text_input("Password", type="password", key="reg_pass")
 

 if st.button("Register"):
  if new_user and new_pass:
   if add_user(new_user, new_email, new_pass):
    st.success("Registration Successful! Now go to the Login tab.")
   else:
    st.error("This username is already taken.")
  else:
    st.warning("Please fill in all fields.")