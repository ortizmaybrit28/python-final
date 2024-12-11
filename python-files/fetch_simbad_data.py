from astroquery.simbad import Simbad
import pandas as pd

# Configure Simbad query
custom_simbad = Simbad()
custom_simbad.TIMEOUT = 300  # Allow extra time for large queries

# Add desired fields
custom_simbad.add_votable_fields('plx', 'flux(V)', 'flux(B)', 'otype')

try:
    # Query stars with specific criteria (e.g., brighter than 10th magnitude)
    result_table = custom_simbad.query_criteria('Vmag < 10')

    # Convert to pandas DataFrame
    if result_table is not None:
        data = result_table.to_pandas()

        # Save data for further processing
        data.to_csv("simbad_data.csv", index=False)
        print("Data fetched and saved to simbad_data.csv!")
    else:
        print("No data returned from the query.")
except Exception as e:
    print(f"Error fetching data: {e}")

