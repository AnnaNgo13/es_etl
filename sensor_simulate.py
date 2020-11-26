from time import sleep
# import logging
import socket   

indices=["auzon", "montoldre"]

def streamToLogstash(index):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    with open("sensorData/InputData/"+index+"/data20201014.json", "r") as file:
        for line in file:
            # stream line to Logstash
            sock.send(line.encode())
            print("Record sent")
            sleep(3)
    sock.close()

# main

from concurrent import futures

with futures.ProcessPoolExecutor() as executor:
    executor.map(streamToLogstash, indices)








# es = connect_elasticsearch()

# for index in indices:
#     with open("sensorData/"+ index +"_schema.json") as json_file:
        
#         mappings = json.load(json_file)
#         create_index(es, index, mappings)


# def populateIndex(index):
#     with open("sensorData/InputData/"+index+"/data20201014.json", "r") as file:
#         for line in file:
#             # send line to es index
#             store_record(es, index, line)
#             sleep(3)