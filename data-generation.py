# Generates synthetic star data for testing.
import numpy as np
import pandas as pd

def generate_test_data(num_stars=100):
    # Generate synthetic temperatures and luminosities
    temperatures = np.random.uniform(3000, 10000, size=num_stars)
    luminosities = 10**np.random.uniform(-2, 2, size=num_stars)  # Spread across 4 orders of magnitude
    
    # Package into a DataFrame
    data = pd.DataFrame({
        'TEFF': temperatures,
        'LUMINOSITY': luminosities
    })
    return data

# Example Usage
# synthetic_data = generate_test_data()

