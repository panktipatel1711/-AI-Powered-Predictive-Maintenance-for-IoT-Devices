import joblib
import os

def make_prediction(processed_df):
    """
    Models folder se pkl file load karke result nikalta hai.
    """
    model_path = 'models/pdm_model.pkl'
    
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        prediction = model.predict(processed_df)
        return prediction[0] # 0 = Normal, 1 = Failure
    else:
        return "Error: Model file not found!"