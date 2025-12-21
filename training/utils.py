import polars as pl
from pathlib import Path\

# Radius of Earth in Kilometers (use 3959 for Miles)
R = 6371

# Define the Haversine Expression
def haversine_dist(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = pl.col(lat1).radians()
    lat2 = pl.col(lat2).radians()
    lon1 = pl.col(lon1).radians()
    lon2 = pl.col(lon2).radians()
    
    # Differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine Formula
    a = (
        (dlat / 2).sin().pow(2) +
        lat1.cos() * lat2.cos() * (dlon / 2).sin().pow(2)
    )
    
    c = 2 * a.sqrt().arcsin()
    
    return c * R
