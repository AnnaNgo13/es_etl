from datetime import datetime
import json
from utils import *
import pandas as pd
import logging

def window(records, mapping_file):
    #TODO group by a time window of nb minutes mapping_conf["aggregation"]["window"]
    mapping_conf = parseMapping(mapping_file)
    window = mapping_conf['aggregation']['window']
    fields = [item['output'] for item in mapping_conf['mappings']]
    group_fields = [x for x in fields if x not in mapping_conf["aggregation"]["operations"].keys()]
    op_fields = mapping_conf["aggregation"]["operations"]
    groups = dict()
    for record in records: 
        if (record['deviceName'],record['year'],record['month'],record['day'],record['hour']) in groups.keys():
            groups[(record['deviceName'],record['year'],record['month'],record['day'],record['hour'])].append(record)
            if len(groups[(record['deviceName'],record['year'],record['month'],record['day'],record['hour'])])==window:
                logging.info("completed %s",(record['deviceName'],record['year'],record['month'],record['day'],record['hour']))
                yield aggregate(groups[(record['deviceName'],record['year'],record['month'],record['day'],record['hour'])],group_fields,op_fields)
        else:
            groups.update({(record['deviceName'],record['year'],record['month'],record['day'],record['hour']):[record]})
        # yield record

def aggregate(block, group_fields, op_fields):

    # print("\n******* data in window *******")
    df = pd.DataFrame(block)
    # df.fillna(value=pd.np.nan, inplace=True)
    # print(df)

    # print("\n******* data aggregated *******")
    df = df.groupby(group_fields, dropna=False).agg(op_fields).reset_index()
    # print(df)
    
    return df