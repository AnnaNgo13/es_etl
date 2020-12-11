import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
import numpy as np
import requests


locator = Nominatim(user_agent="openstreetmap", timeout=10)

def extend(dfs):
    for df in dfs:
        # df=df.dropna(subset=["senLocation"])


        a=df['senLocation'].to_json()
        # print(a)
        response = requests.get("http://127.0.0.1:5000/address/?locations="+a)
        # print(response.json())
        df2=pd.DataFrame.from_records(response.json())
        # print(df2)

        df3=pd.merge(df, df2, on='senLocation', how='inner')
        # print(df3)

        yield df3

        # df["municipality"] = np.nan
        # df["state"] = np.nan
        # df["country"] = np.nan
        # df=df.apply(location, axis=1)
        # print(df)
        # yield df


def location(x):
    if isinstance(x["senLocation"], str):
        result = locator.reverse(x["senLocation"]).raw['address']
        x['municipality']=result['municipality']
        x['state']=result['state']
        x['country']=result['country']
    return x