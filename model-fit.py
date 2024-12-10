# Fits the model to the data and evaluates errors.
import numpy as np
import scipy.optimize as opt

def fit_polynomial(temperatures, luminosities, degree=2):
    def poly_func(x, *coeffs):
        return sum(c * x**i for i, c in enumerate(coeffs))
    
    coeffs, cov_matrix = opt.curve_fit(poly_func, temperatures, luminosities, p0=[1]*degree)
    return coeffs, np.sqrt(np.diag(cov_matrix))  # Coefficients and their uncertainties

# Example Usage
# coeffs, errors = fit_polynomial(temperatures, luminosities)


