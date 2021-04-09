from datetime import datetime
import json
from utils import *
import pandas as pd
import logging

def window(records, mapping_file):
    #TODO group by a time window of nb minutes mapping_conf["aggregation"]["window"]
    mapping_conf=parseMapping(mapping_file)
    number=0
    block=[]
    # for record in records:
    #     block.append(record)
    #     if number<mapping_conf["aggregation"]["window"]-1:
    #         number+=1
    #     else:
    #         yield aggregate(block, mapping_conf)
    #         number=0
    #         block=[]
    groups=dict()
    for record in records: 
        if (record['deviceName'],record['year'],record['month'],record['day'],record['hour']) in groups.keys():
            groups[(record['deviceName'],record['year'],record['month'],record['day'],record['hour'])].append(record)
            if len(groups[(record['deviceName'],record['year'],record['month'],record['day'],record['hour'])])==60:
                logging.info("completed %s",(record['deviceName'],record['year'],record['month'],record['day'],record['hour']))
                yield aggregate(groups[(record['deviceName'],record['year'],record['month'],record['day'],record['hour'])],mapping_conf)
        else:
            groups.update({(record['deviceName'],record['year'],record['month'],record['day'],record['hour']):[record]})
        # yield record

def aggregate(block, mapping_conf):

    # print("\n******* data in window *******")
    df=pd.DataFrame(block)
    # df.fillna(value=pd.np.nan, inplace=True)
    # print(df)

    # print("\n******* data aggregated *******")
    group_fields= [x for x in mapping_conf["targetFields"] if x not in mapping_conf["aggregation"]["operations"].keys()]
    df=df.groupby(group_fields, dropna=False).agg(mapping_conf["aggregation"]["operations"]).reset_index()
    # print(df)
    
    return df