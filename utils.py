import socket
import json
from es_conf import *

def readFromLogstash():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5002
    BUFFER_SIZE = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((TCP_IP, TCP_PORT))
    except:
        pass

    while (True):
        try:
            yield json.loads(sock.recv(BUFFER_SIZE).decode())
        except KeyError:
            print(KeyError)

def sendToStdout(records):
    for record in records:
        print(record)

def sendToIndex(records):
    es = connect_elasticsearch()
    for record in records:
        store_record(es, "target_index", record)
    es.close()

def parseMapping(mapping_json):
    with open(mapping_json) as json_file:
        data = json.load(json_file)
    
    return data






SOURCE_FUNC={"Logstash":readFromLogstash}
DEST_FUNC={"stdout":sendToStdout,"ES":sendToIndex}