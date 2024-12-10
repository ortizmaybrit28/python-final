# Handles downloading and querying data from SIMBAD or other databases.
from astroquery.simbad import Simbad
import pandas as pd

def query_star_data(distance_limit=10):
    Simbad.TIMEOUT = 60  # Ensure a longer timeout for large queries
    Simbad.add_votable_fields('flux(V)', 'fe_h', 'plx', 'sp', 'teff')
    
    query = f"SELECT * WHERE plx > {1000 / distance_limit}"  # Parallax > threshold for 10 parsecs
    result = Simbad.query_criteria(query)
    
    if result is None:
        raise Exception("No data retrieved. Check query or connection.")
    
    df = result.to_pandas()  # Convert to a DataFrame
    return df

# Example Usage
# data = query_star_data()

