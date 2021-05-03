from utils import inputHandler, outputHandler 
from transformations import mapping
from aggregate import window
from external import extend
import logging 
import json

logging.basicConfig(
    filename="logs/etl.log",
    format="%(asctime)s.%(msecs)03d [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.WARN,
    filemode='w'
)

class ETL:

    def __init__(self, etl_conf_file):
        with open(etl_conf_file,"r") as f:
            elt_conf=json.load(f)
            self.input_conf=elt_conf["input"]
            self.output_conf=elt_conf["output"]
            self.mapping_conf=elt_conf["mapping"]['mapping_file']

    def extract(self):
        for record in inputHandler(self.input_conf):
            yield record

    def transform(self):
        for record in window(mapping(self.extract(), self.mapping_conf), self.mapping_conf):
            #extend(window(mapping(self.extract(), self.mapping_conf), self.mapping_conf))
            yield record

    def load(self):
        outputHandler(self.transform(),self.output_conf)

    def start(self):
        try:
            self.load()
        except KeyboardInterrupt:
            print("\nEtl process stopped")
            quit()



if __name__ == "__main__": 

    # import sys
    # args=sys.argv
    # print("file processing: ", args[1])
    # etl = ETL(args[1])

    etl = ETL("etl_conf_zatu_3m.json")
    etl.start() 