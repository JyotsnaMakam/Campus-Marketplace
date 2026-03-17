import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
# 1. Load your Kaggle data
df = pd.read_csv("kaggle_users.csv",encoding='latin1')
# 2. Drop rows where 'Price' or important features are NaN
# This is the safest way to avoid the "NaN error"
df = df.dropna(subset=['tweet_count', 'gender'])
# 3. Fill NaN values in other columns with a default value if needed
df['description'] = df['description'].fillna("No description provided")
# 4. Encode text data into numbers (Models only understand numbers!)
le = LabelEncoder()
df['Category_Encoded'] = le.fit_transform(df['gender'])
# 5. Define features (X) and target (y)
X = df[['Category_Encoded']] # Add more features if your CSV has them
y = df['tweet_count']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=RandomForestRegressor(n_estimators=100)
model.fit(X_train,y_train)
with open('price_predictor.pkl','wb')as f:
  pickle.dump(model,f)
print("Model trained and saved successfully!")  
