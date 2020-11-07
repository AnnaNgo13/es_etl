import socket
import json
from es_conf import *




es = connect_elasticsearch()

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
            data = json.loads(sock.recv(BUFFER_SIZE).decode())
            print('{"deviceName":{}}'.format(data["deviceName"]))
            # store_record(es, "target_index", '{"deviceName":{}}'.format(data["deviceName"]))
        except:
            pass       


readFromLogstash()