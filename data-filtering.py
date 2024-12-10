#  Includes logic to clean and filter the data.
import pandas as pd
import numpy as np

def filter_star_data(df):
    # Ensure essential columns are present
    required_columns = ['FLUX_V', 'TEFF', 'PLX']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    
    # Filter stars based on quality criteria
    df = df.dropna(subset=['FLUX_V', 'TEFF', 'PLX'])  # Remove missing values
    df['distance'] = 1000 / df['PLX']  # Calculate distance from parallax
    df = df[df['distance'] <= 10]  # Keep stars within 10 parsecs
    
    return df

# Example Usage
# filtered_data = filter_star_data(data)

