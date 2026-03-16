import pandas as pd

# 1. Load the Kaggle data (Note: Twitter data often needs 'latin1' encoding)
try:
 df = pd.read_csv('kaggle_users.csv', encoding='latin1')

# 2. Select the 'name' column and rename it to 'username'
# The Twitter dataset uses 'name' for the display name
 df_cleaned = df[['name']].copy()
 df_cleaned = df_cleaned.rename(columns={'name': 'username'})

# 3. Add the columns our app needs
 df_cleaned['email'] = df_cleaned['username'].astype(str) + "@campus.edu"
 df_cleaned['password'] = "student123"
 df_cleaned['balance'] = 100.0

# 4. Remove empty names and save only the first 100 rows for speed
 df_cleaned = df_cleaned.dropna().head(100)

# 5. Save as our final database file
 df_cleaned.to_csv('users.csv', index=False)
 print("✅ Success! 'users.csv' has been created with Kaggle data.")

except Exception as e:
 print(f"❌ Error: {e}")