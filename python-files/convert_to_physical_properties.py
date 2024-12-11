import pandas as pd
import numpy as np

# Load cleaned data
data = pd.read_csv("cleaned_data.csv")

# Constants
L_sun = 3.828e33  # Solar luminosity in erg/s

# Compute distance in parsecs
data['distance_pc'] = 1 / data['PLX_VALUE']

# Compute absolute magnitude
data['M_V'] = data['FLUX_V'] - 5 * np.log10(data['distance_pc'] / 10)

# Compute luminosity
data['luminosity'] = 10 ** ((4.74 - data['M_V']) / 2.5)

# Compute effective temperature using B-V color index
data['B-V'] = data['FLUX_B'] - data['FLUX_V']
data['temperature_K'] = 4600 * (
    (1 / (0.92 * data['B-V'] + 1.7)) + (1 / (0.92 * data['B-V'] + 0.62))
)

# Save the dataset with new physical properties
data.to_csv("physical_properties.csv", index=False)

print("Physical properties calculated and saved.")
print(data[['MAIN_ID', 'distance_pc', 'M_V', 'luminosity', 'temperature_K']].head())

