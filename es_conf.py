from elasticsearch import Elasticsearch
import logging

def connect_elasticsearch(host, port):
    _es = None
    _es = Elasticsearch([{'host': host, 'port': port}])
    if _es.ping():
        print('Connected')
    else:
        print('it could not connect!')
    return _es

def create_index(es_object, index_name, mappings):
    created = False

    try:
        if es_object.indices.exists(index_name):
            
            es_object.indices.delete(index_name)
            es_object.indices.create(index=index_name, body=mappings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created

def store_record(elastic_object, index_name, record):
    logging.info("Record is: %s", record)
    try:
        outcome = elastic_object.index(index=index_name, body=record)
        logging.info('Record stored in %s',index_name)
    except Exception as ex:
        print('Error in indexing data to '+index_name+". "+str(ex))    