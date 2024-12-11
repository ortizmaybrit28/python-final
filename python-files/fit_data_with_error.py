import argparse
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the mass-luminosity relationship
def mass_luminosity_relation(mass, k, a):
    return k * mass**a

# Argument parser to select dataset
parser = argparse.ArgumentParser(description="Perform mass-luminosity fitting on a dataset.")
parser.add_argument('--dataset', type=str, default="cleaned_data.csv", 
                    help="Path to the dataset (default: cleaned_data.csv)")
args = parser.parse_args()

# Load dataset
data = pd.read_csv(args.dataset)
print(f"Using dataset: {args.dataset}")

# Generate mock mass data based on temperature if mass is not directly available
mass = np.linspace(0.1, 50, len(data))  # Replace with actual mass if available
luminosity = data['luminosity']

# Fit the mass-luminosity relationship
initial_guess = [1, 3.5]
params, covariance = curve_fit(mass_luminosity_relation, mass, luminosity, p0=initial_guess)

# Extract parameters and errors
k_fit, a_fit = params
k_err, a_err = np.sqrt(np.diag(covariance))

print(f"Fitted Parameters: k = {k_fit:.3f} ± {k_err:.3f}, a = {a_fit:.3f} ± {a_err:.3f}")

# Plot HR diagram with fit
fitted_luminosity = mass_luminosity_relation(mass, k_fit, a_fit)
plt.figure(figsize=(8, 6))
plt.scatter(data['temperature_K'], luminosity, c='blue', edgecolor='k', alpha=0.8, s=20)
plt.plot(data['temperature_K'], fitted_luminosity, color='red', linewidth=2, label=f"Fit: L = {k_fit:.2f} * M^{a_fit:.2f}")
plt.gca().invert_xaxis()
plt.legend()
plt.title("HR Diagram with Mass-Luminosity Fit")
plt.xlabel("Effective Temperature (K)")
plt.ylabel("Luminosity (Solar Units)")

plt.xscale('log')
plt.yscale('log')

plt.grid()
plt.tight_layout()
plt.savefig("mass_luminosity_fit.png")
plt.show()

# Residual Analysis
residuals = luminosity - mass_luminosity_relation(mass, k_fit, a_fit)
plt.figure(figsize=(8, 6))
plt.scatter(mass, residuals, edgecolor='k', alpha=0.7)
plt.axhline(0, color='red', linestyle='--', linewidth=1.5)
plt.xlabel("Mass (Solar Masses)")
plt.ylabel("Residuals")
plt.title("Residuals of Mass-Luminosity Fit")

plt.xscale('log')
plt.yscale('log')

plt.grid()
plt.tight_layout()
plt.savefig("residuals_plot.png")
plt.show()

