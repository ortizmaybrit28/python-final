# Handles visualization of the HR diagram.
import matplotlib.pyplot as plt
import numpy as np

def plot_hr_diagram(temperatures, luminosities, model=None, coeffs=None):
    plt.figure(figsize=(8, 6))
    plt.scatter(temperatures, luminosities, color='blue', label='Stars')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Luminosity (L/L_sun)')
    plt.gca().invert_xaxis()  # HR diagrams have temperature decreasing
    
    if model and coeffs is not None:
        x_vals = np.linspace(min(temperatures), max(temperatures), 500)
        y_vals = model(x_vals, *coeffs)
        plt.plot(x_vals, y_vals, color='red', label='Model Fit')
    
    plt.legend()
    plt.title('Hertzsprung-Russell Diagram')
    plt.show()

# Example Usage
# plot_hr_diagram(temperatures, luminosities, poly_func, coeffs)

