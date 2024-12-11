import subprocess
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np

# Step 1: Generate synthetic data
subprocess.run(["python", "generate_test_data.py"])

# Step 2: Run fitting on synthetic data
subprocess.run(["python", "fit_data_with_error.py", "--dataset", "synthetic_data.csv"])

# Step 3: Validate the fit
synthetic_data = pd.read_csv("synthetic_data.csv")
mass = np.linspace(0.1, 50, len(synthetic_data))
luminosity = synthetic_data['luminosity']

# Define the assumed mass-luminosity relationship used to generate data
def mass_luminosity_relation(mass, k, a):
    return k * mass**a

# Fit the relationship
initial_guess = [1, 3.5]  # These should match the values used in generate_test_data.py
params, _ = curve_fit(mass_luminosity_relation, mass, luminosity, p0=initial_guess)

print("Validation Complete:")
print(f"Fitted Parameters from Synthetic Data: k = {params[0]:.3f}, a = {params[1]:.3f}")

