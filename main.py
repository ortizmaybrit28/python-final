from data-query import query_star_data
from data-filtering import filter_star_data
from data-generation import generate_test_data
from model-fit import fit_polynomial
from plotting import plot_hr_diagram

def main():
    # Step 1: Query data
    try:
        real_data = query_star_data()
        filtered_data = filter_star_data(real_data)
    except Exception as e:
        print(f"Error querying data: {e}")
        filtered_data = None
    
    # Step 2: Generate test data
    synthetic_data = generate_test_data()

    # Step 3: Fit a model
    if filtered_data is not None:
        temperatures = filtered_data['TEFF']
        luminosities = filtered_data['FLUX_V']
        coeffs, errors = fit_polynomial(temperatures, luminosities, degree=2)
    else:
        coeffs, errors = None, None

    # Step 4: Plot the HR diagram
    plot_hr_diagram(
        temperatures=synthetic_data['TEFF'], 
        luminosities=synthetic_data['LUMINOSITY']
    )

if __name__ == "__main__":
    main()

