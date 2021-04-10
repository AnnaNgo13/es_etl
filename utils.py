import socket
import json
from es_conf import store_record, connect_elasticsearch

def readFromLogstash(host='127.0.0.1', port=5002):
    BUFFER_SIZE = 20000 #4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except:
        pass

    while (True):
        try:
            yield json.loads(sock.recv(BUFFER_SIZE).decode())
        except KeyError:
            pass
    
def readFromFile(file_name):
    with open(file_name,"r") as f:
        for line in f.readlines():
            # print(json.loads(line))
            yield json.loads(line)

def inputHandler(conf):
    if conf['source_type']=="file":
        for item in readFromFile(conf['file_path']):
            yield item
    elif conf['source_type']=="Logstash":
        readFromLogstash(conf['host'],conf['port'])


# mapping
def parseMapping(mapping_json):
    with open(mapping_json) as json_file:
        data = json.load(json_file)
    
    return data

# output

def saveToFile(dfs, file_name):
    #where we can file the output
    with open(file_name,"w") as f:
        for df in dfs:
            json_obj=json.loads(df.to_json(orient="records"))
            f.write(json.dumps(json_obj[0])+"\n")

def sendToIndex(dfs, host, port, target_index):
    es = connect_elasticsearch(host,port)
    for df in dfs:
        for record in json.loads(df.to_json(orient="records")):
            store_record(es, target_index, record)  #update the target index
    es.close()

def sendToStdout(dfs):
    for df in dfs:
        print("******* Stdout *******")
        print(df)

def outputHandler(dfs, conf):
    if conf["source_type"]=="ES":
        sendToIndex(dfs, conf['host'], conf['port'], conf['target_index'])
    elif conf["source_type"]=="file":
        saveToFile(dfs, conf['file_path'])
    elif conf["source_type"]=="stdout":
        sendToStdout(dfs)



SOURCE_FUNC={"Logstash":readFromLogstash,"file":readFromFile}
DEST_FUNC={"stdout":sendToStdout,"ES":sendToIndex,"file":saveToFile}