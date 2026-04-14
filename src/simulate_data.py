import pandas as pd
import numpy as np
import os

def generate_sensor_data(rows=2000):
    # 1. Folder create karne ka logic
    if not os.path.exists('data'):
        os.makedirs('data')
        print("📁 'data' folder ban gaya hai.")

    np.random.seed(42)
    
    # 2. Synthetic Data Generate karna
    # Hum 2000 rows bana rahe hain taaki AI model achhe se seekh sake
    data = {
        'temperature': np.random.normal(70, 10, rows),    # Average 70 degrees
        'vibration': np.random.normal(2, 1, rows),       # Average 2mm/s
        'current': np.random.normal(500, 50, rows),      # Average 500mA
    }
    
    df = pd.DataFrame(data)

    # 3. FAILURE LOGIC (Most Important)
    # Hum AI ko sikha rahe hain ki khatra kab hota hai:
    # Agar Temp 80 se upar ho YA Vibration 3 se upar ho, toh failure = 1
    df['failure'] = ((df['temperature'] > 80) | (df['vibration'] > 3.0)).astype(int)

    # 4. CSV Save karna
    file_path = 'data/sensor_data.csv'
    df.to_csv(file_path, index=False)
    
    print(f" done!! {rows} rows ka dataset ban gaya: {file_path}")
    print(f" Failures detect hue: {df['failure'].sum()} units mein.")

if __name__ == "__main__":
    generate_sensor_data()