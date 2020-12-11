import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
import numpy as np
import json
from flask import Flask, request
from flask_restful import Resource, Api


class Ping(Resource):
    def get(self):  
    	return "Alive" 

class Address(Resource):
    def get(self):  
        locations=json.loads(request.args.get("locations")).values()
        response=list()
        for latlon in locations:
            if isinstance(latlon, str):
                response.append(location(latlon))

        return response


def location(latlon):
    row={}
    if isinstance(latlon, str):
        address = locator.reverse(latlon).raw['address']
        row['senLocation']=latlon
        row['municipality']=address['municipality']
        row['state']=address['state']
        row['country']=address['country']
    # else: 
    #     row['senLocation']=np.nan
    #     row['municipality']=np.nan
    #     row['state']=np.nan
    #     row['country']=np.nan

    return row



if __name__ == "__main__":

	# if len(sys.argv) != 5:
	# 	print("Usage: problem3.py <host> <port> <database> <collection>")
	# 	sys.exit(-1)

    locator = Nominatim(user_agent="openstreetmap", timeout=10)
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Ping, '/')
    api.add_resource(Address, '/address/')
    app.run(debug = True)

