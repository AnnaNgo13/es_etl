import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
import numpy as np


locator = Nominatim(user_agent="openstreetmap", timeout=10)

def extend(dfs):
    for df in dfs:
        # df=df.dropna(subset=["senLocation"])
        df["municipality"] = np.nan
        df["state"] = np.nan
        df["country"] = np.nan
        df=df.apply(location, axis=1)
        print(df)
        yield df


def location(x):
    if isinstance(x["senLocation"], str):
        result = locator.reverse(x["senLocation"]).raw['address']
        x['municipality']=result['municipality']
        x['state']=result['state']
        x['country']=result['country']
    return x