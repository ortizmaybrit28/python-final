# generate_test_data.py
import numpy as np
import pandas as pd

np.random.seed(42)
temperatures = np.random.uniform(3000, 10000, 500)  # Random temperature range
luminosities = 10**np.random.uniform(-1, 2, 500)    # Random luminosity

synthetic_data = pd.DataFrame({'temperature_K': temperatures, 'luminosity': luminosities})
synthetic_data.to_csv("synthetic_data.csv", index=False)
print("Synthetic data generated!")

