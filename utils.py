import socket
import json
from es_conf import store_record, connect_elasticsearch

def readFromLogstash():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5002
    BUFFER_SIZE = 20000 #4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((TCP_IP, TCP_PORT))
    except:
        pass

    while (True):
        try:
            yield json.loads(sock.recv(BUFFER_SIZE).decode())
        except KeyError:
            pass

def sendToStdout(dfs):
    for df in dfs:
        print("******* Stdout *******")
        print(df)

def sendToIndex(dfs):
    es = connect_elasticsearch()
    for df in dfs:
        for record in json.loads(df.to_json(orient="records")):
            store_record(es, "target_index", record)
    es.close()

def parseMapping(mapping_json):
    with open(mapping_json) as json_file:
        data = json.load(json_file)
    
    return data



SOURCE_FUNC={"Logstash":readFromLogstash}
DEST_FUNC={"stdout":sendToStdout,"ES":sendToIndex}