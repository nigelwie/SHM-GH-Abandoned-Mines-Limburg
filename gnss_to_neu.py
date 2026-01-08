import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

def convert_gnss_to_neu(data):

# Only looks at data starting with d_
    start_col = next(i for i, col in enumerate(data.columns) if col.startswith('d_')) 

    for col in data.columns[start_col:]:
        if col.startswith('d_'):
            new_col = f"u_{col}"
            data.rename(columns={col: new_col}, inplace=True)
            data[new_col] = data[new_col] / np.cos(data['pnt_incidangle'] * np.pi / 180)

    return data
