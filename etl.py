from utils import SOURCE_FUNC, DEST_FUNC
from transformations import mapping
from aggregate import window
from external import extend
import logging 

logging.basicConfig(
    filename="logs/etl.log",
    format="%(asctime)s.%(msecs)03d [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    filemode='w'
)

class ETL:

    def __init__(self, source, destination, mapping_conf):
        self.input=SOURCE_FUNC[source]
        self.output=DEST_FUNC[destination]
        self.mapping_conf=mapping_conf

    def extract(self):
        for record in self.input():
            yield record

    def transform(self):
        for record in window(mapping(self.extract(), self.mapping_conf), self.mapping_conf):
            #extend(window(mapping(self.extract(), self.mapping_conf), self.mapping_conf))
            yield record

    def load(self):
        self.output(self.transform())

    def start(self):
        try:
            self.load()
        except KeyboardInterrupt:
            print("\nEtl process stopped")
            quit()


SOURCE="file"
DEST="ES"  # update "ES" means elasticsearch
# DEST="ES"
MAPPING="mappings_aydat.json"


if __name__ == "__main__": 

    etl = ETL(SOURCE, DEST, MAPPING)
    etl.start() 