import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train():
    # 1. Load data
    df = pd.read_csv('data/sensor_data.csv')
    X = df[['temperature', 'vibration', 'current']]
    
    # 2. FORCE LOGIC (Model ko seekhne do ki failure kab hota hai)
    # Agar Temp > 80 aur Vibration > 3, toh Failure = 1
    y = ((df['temperature'] > 80) & (df['vibration'] > 3.0)).astype(int)
    
    # 3. Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Save Model
    if not os.path.exists('models'): os.makedirs('models')
    joblib.dump(model, 'models/pdm_model.pkl')
    print("NEW Model Trained with Sensitive Logic!")

if __name__ == "__main__":
    train()