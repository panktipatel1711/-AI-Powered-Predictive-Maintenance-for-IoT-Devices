import pandas as pd
import numpy as np

def create_dataset(samples=2000):
    np.random.seed(42)
    # Simulate normal operating hours
    time = pd.date_range(start='2024-01-01', periods=samples, freq='H')
    
    # Normal Sensor Readings
    temp = np.random.normal(65, 5, samples)      # Avg 65 degrees
    vibration = np.random.normal(1.2, 0.2, samples) # Avg 1.2 mm/s
    pressure = np.random.normal(100, 10, samples)  # Avg 100 PSI
    
    df = pd.DataFrame({'timestamp': time, 'temp': temp, 'vibration': vibration, 'pressure': pressure})
    
    # Logic for FAILURE (Target Variable)
    # If temp > 80 and vibration > 1.8, the machine is failing
    df['failure'] = ((df['temp'] > 78) & (df['vibration'] > 1.6)).astype(int)
    
    # Add some random failures (Anomalies)
    anomaly_idx = df.sample(frac=0.02).index
    df.loc[anomaly_idx, 'failure'] = 1
    df.loc[anomaly_idx, 'temp'] += 15
    
    df.to_csv('data/sensor_data.csv', index=False)
    print("Virtual IoT Data Generated: data/sensor_data.csv")

if __name__ == "__main__":
    create_dataset()