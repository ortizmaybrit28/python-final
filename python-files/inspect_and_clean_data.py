import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("simbad_data.csv")

# Inspect the dataset
print("Initial dataset shape:", data.shape)
print("Columns:", data.columns)
print(data.head())

# Drop rows with missing essential data
required_columns = ['PLX_VALUE', 'FLUX_V', 'FLUX_B']
clean_data = data.dropna(subset=required_columns)

# Filter out unrealistic values for parallax (e.g., <= 0)
clean_data = clean_data[clean_data['PLX_VALUE'] > 0]

# Save the cleaned data
clean_data.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved. Shape:", clean_data.shape)

