import pandas as pd

def process_data(temperature, vibration, current):
    """
    User input ko DataFrame mein convert karta hai 
    taaki model prediction kar sake.
    """
    data = {
        'temperature': [temperature],
        'vibration': [vibration],
        'current': [current]
    }
    return pd.DataFrame(data)