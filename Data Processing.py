import pandas as pd
from sklearn.preprocessing import StandardScaler

def process_data(file_path):
    df = pd.read_csv(file_path)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.select_dtypes(include=['float64', 'int64']))  # Process only numeric columns
    return scaled_data