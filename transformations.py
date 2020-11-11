from datetime import datetime

test_record= {"applicationID": "5", "applicationName": "Auzon", "deviceName": "HE36228", "devEUI": "434e535302e36228", "rxInfo-gatewayID": "00800000a0003119", "rxInfo-name": "Multitech-Auzon", "rxInfo-rssi": -99, "rxInfo-loRaSNR": 8.8, "rxInfo-location-latitude": 0, "rxInfo-location-longitude": 0, "rxInfo-location-altitude": 0, "txInfo-frequency": 868300000, "txInfo-dr": 5, "adr": False, "fCnt": 0, "fPort": 2, "servertimestampUTC": "2020-10-14T10:21:42.366042", "data-DataChannel": 1, "data-node-timestampUTC": "2020-10-14T09:00:01", "data-node-batteryVoltage": 4.18, "data-node-batteryVoltage-unit": "V", "data-node-batteryVoltage-alarmIsLow": False, "data-CNSSRFConfigMM3Hash32": "2965B5D6", "data-node-geoPos-latitude": 45.3625, "data-node-geoPos-latitude-unit": "°", "data-node-geoPos-longitude": 3.36225, "data-node-geoPos-longitude-unit": "°", "data-CNSSRFSensorTypeMM3Hash32": "C9E815B9", "data-temperature": 13.39, "data-temperature-unit": "°C", "data-temperature-alarmH": False, "data-temperature-alarmL": False, "data-CNSSRFDataTypeId": 45, "data-CNSSRFDataTypeName": "TempHighResSmallRangeDegC"}

def auzon_mapping(input_record):
    

    output_record={}
    #measurement data
    #each measurement will be inserted as one record in the target index.
    try: 

        # Measurements
        output_record["temperature"]=input_record["data-temperature"]

        #sensor info
        output_record["deviceID"]=input_record["devEUI"]
        output_record["deviceName"]=input_record["deviceName"]

        #project info
        output_record["applicationID"]=input_record["applicationID"]
        output_record["applicationName"]=input_record["applicationName"]
        
        #location
        output_record["senLocation"] = str(input_record["data-node-geoPos-latitude"]) + "," +str(input_record["data-node-geoPos-longitude"])
        
        # #time "%d/%m/%Y %H:%M:%S"    2020-10-14T10:21:42.366042
        dt = datetime.strptime(input_record["servertimestampUTC"], "%Y-%m-%dT%H:%M:%S.%f")
        output_record["time"]= dt.strftime('%H:%M:%S')
        output_record["day"] = dt.day
        output_record["month"] = dt.month
        output_record["year"] = dt.year

        return output_record 
    
    except Exception as ex:
        print("Issue with:", ex)
        return None  


def montoldre_mapping(input_record):

    output_record={}
    #measurement data
    #each measurement will be inserted as one record in the target index.
    try: 

        # Measurements
        output_record["temperature"]=input_record["data-temperature"]

        #sensor info
        output_record["deviceID"]=input_record["devEUI"]
        output_record["deviceName"]=input_record["deviceName"]

        #project info
        output_record["applicationID"]=input_record["applicationID"]
        output_record["applicationName"]=input_record["applicationName"]
        
        #location
        output_record["senLocation"] = str(input_record["rxInfo-location-latitude"]) + "," +str(input_record["rxInfo-location-longitude"])

        # #time "%d/%m/%Y %H:%M:%S"    2020-10-14T10:21:42.366042
        dt = datetime.strptime(input_record["servertimestampUTC"], "%Y-%m-%dT%H:%M:%S.%f")
        output_record["time"]= dt.strftime('%H:%M:%S')
        output_record["day"] = dt.day
        output_record["month"] = dt.month
        output_record["year"] = dt.year

        return output_record 
    
    except Exception as ex:
        print("Issue with:", ex)
        return None  


def mapping(input_record):

    if input_record["applicationName"]=="Auzon":
        print ("//////// Mapping Auzon")
        return auzon_mapping(input_record)
    elif input_record["applicationName"]=="Montoldre":
        print("///////// Mapping Montoldre")
        return montoldre_mapping(input_record)



 


#main
if __name__=="__main__":
    print(mapping(test_record))



    
    # if "data-rainAmount" in test_record:
    #     if input_record["data-rainAmount"] is not None:
    #         output_record["measureType"] = "2"
    #         output_record["measureName"] = "rainAmount"
    #         output_record["measureValue1"] = input_record["data-rainAmount"]

    # if "data-illuminance" in test_record:
    #     if input_record["data-illuminance"] is not None:
    #         output_record["measureType"] = "3"
    #         output_record["measureName"] = "illuminance"
    #         output_record["measureValue1"] = input_record["data-illuminance"]

    # if "data-airHumidity" in test_record:
    #     if input_record["data-airHumidity"] is not None:
    #         output_record["measureType"] = "4"
    #         output_record["measureName"] = "airHumidity"
    #         output_record["measureValue1"] = input_record["data-airHumidity"]  

    # if "data-depth1-soilTemperature" in test_record:
    #     if input_record["data-depth1-soilTemperature"] is not None:
    #         output_record["measureType"] = "5"
    #         output_record["measureName"] = "depth1-soilTemperature"
    #         output_record["measureValue1"] = input_record["data-depth1-soilTemperature"]

    # if "data-depth2-soilTemperature" in test_record:
    #     if input_record["data-depth2-soilTemperature"] is not None:
    #         output_record["measureType"] = "5" #the same or 6?
    #         output_record["measureName"] = "depth2-soilTemperature"
    #         output_record["measureValue2"] = input_record["data-depth2-soilTemperature"]

    # if "data-depth3-soilTemperature" in test_record:
    #     if input_record["data-depth3-soilTemperature"] is not None:
    #         output_record["measureType"] = "5" #the same or 7?
    #         output_record["measureName"] = "depth3-soilTemperature"
    #         output_record["measureValue3"] = input_record["data-depth3-soilTemperature"] 