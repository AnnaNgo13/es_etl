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
            store_record(es, "target_index_3month", record)  #update the target index
    es.close()

def parseMapping(mapping_json):
    with open(mapping_json) as json_file:
        data = json.load(json_file)
    
    return data
    
def readFromFile():
    #update the input file
    file_name="/home/ttngo/code/evaluationELK/dataset/data-aydat-2020-3month.json"
    with open(file_name,"r") as f:
        for line in f.readlines():
            # print(json.loads(line))
            yield json.loads(line)

def saveToFile(dfs):
    #where we can file the output
    with open("output.json","w") as f:
        for df in dfs:
            json_obj=json.loads(df.to_json(orient="records"))
            f.write(json.dumps(json_obj[0])+"\n")


SOURCE_FUNC={"Logstash":readFromLogstash,"file":readFromFile}
DEST_FUNC={"stdout":sendToStdout,"ES":sendToIndex,"file":saveToFile}