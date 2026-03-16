import pandas as pd
import os

USER_DB = "users.csv"
BOOKING_DB = "bookings.csv"

def init_db():
# If the file doesn't exist at all, create it.
# But since you ran clean_data.py, it should already be there!
 if not os.path.exists(USER_DB):
  df = pd.DataFrame(columns=["username", "email", "password", "balance"])
  df.to_csv(USER_DB, index=False)

 if not os.path.exists(BOOKING_DB):
  df = pd.DataFrame(columns=["username", "service", "price", "status"])
  df.to_csv(BOOKING_DB, index=False)

def verify_user(username, password):
# This function looks into your Kaggle-populated CSV
 df = pd.read_csv(USER_DB)
# Convert input to string to match CSV format
 user_record = df[(df['username'].astype(str) == str(username)) &
(df['password'].astype(str) == str(password))]
 return not user_record.empty

def add_user(username, email, password):
 df = pd.read_csv(USER_DB)
 if username in df['username'].values:
  return False

# EXACT ORDER: username, password, email, balance
 new_data = [username, email, password, 100.0]

 new_user = pd.DataFrame([new_data], columns=df.columns)
 df = pd.concat([df, new_user], ignore_index=True)
 df.to_csv(USER_DB, index=False)
 return True

def update_balance(username,amount_to_subtract):
  df = pd.read_csv(USER_DB)
  df.loc[df['username']==username, 'balance'] -= amount_to_subtract
  df.to_csv(USER_DB, index=False)