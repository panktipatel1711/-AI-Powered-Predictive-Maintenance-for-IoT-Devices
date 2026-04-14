import joblib
import numpy as np
import time
import pandas as pd
import warnings
import os

# 1. Warnings ko ignore karne ke liye (Terminal saaf dikhega)
warnings.filterwarnings("ignore", category=UserWarning)

# 2. Model load karne ka logic
MODEL_PATH = 'models/pdm_model.pkl'

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("\n" + "="*50)
    print("🚀 AI-POWERED PREDICTIVE MAINTENANCE SYSTEM ACTIVE")
    print("="*50 + "\n")
else:
    print(f"❌ Error: Model file '{MODEL_PATH}' nahi mili!")
    print("Pehle 'python src/train_model.py' chalao.")
    exit()

def run_simulation():
    print("Monitoring Live IoT Sensor Feed... (Press Ctrl+C to stop)\n")
    try:
        while True:
            # 3. Live Sensor Data Simulate karna (Random values)
            # Hum wahi logic use kar rahe hain jo training mein tha
            t = np.random.normal(70, 10)      # Temperature
            v = np.random.normal(2, 0.8)      # Vibration
            p = np.random.normal(100, 15)     # Pressure (Optional for logic)

            # 4. Feature DataFrame banana (Taaki Warning na aaye)
            # Note: Training ke waqt jo column names the, wahi yahan use karne hain
            current_data = pd.DataFrame([[t, v, p]], 
                                     columns=['temperature', 'vibration', 'current'])

            # 5. AI Prediction
            prediction = model.predict(current_data)[0]

            # 6. Status Display Logic
            timestamp = time.strftime("%H:%M:%S")
            if prediction == 1:
                status = "⚠️  [CRITICAL] FAILURE PREDICTED! Shutting down motor..."
            else:
                status = "✅ [NORMAL] System Healthy"

            print(f"[{timestamp}] Temp: {t:>5.2f}°C | Vib: {v:>4.2f}mm/s | {status}")
            
            # 1 second ka gap (Real-time feel ke liye)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nExiting... Monitoring Stopped.")
        print("="*50)

if __name__ == "__main__":
    run_simulation()