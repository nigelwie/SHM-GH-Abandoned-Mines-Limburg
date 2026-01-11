import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

def convert_insar_to_neu(data):

# Only looks at data starting with d_
    start_col = next(i for i, col in enumerate(data.columns) if col.startswith('d_')) 

    for col in data.columns[start_col:]:
        if col.startswith('d_'):
            new_col = f"u_{col}"
            data.rename(columns={col: new_col}, inplace=True)
            data[new_col] = data[new_col] / np.cos(data['pnt_incidangle'] * np.pi / 180)

    return data


def convert_insar_to_u(df, d_regex=r"^d_20"):
    phi = np.deg2rad(df["pnt_incidangle"].to_numpy())

    d = df.filter(regex=d_regex)
    u = d.div(np.cos(phi), axis=0)
    u.columns = [c.replace("d_", "u_") for c in u.columns]

    return pd.concat([df.drop(columns=d.columns), u], axis=1)
