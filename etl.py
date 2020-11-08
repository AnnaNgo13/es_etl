from utils import *
from transformations import *

class ETL:

    def __init__(self, source, destination):
        self.input=SOURCE_FUNC[source]
        self.output=DEST_FUNC[destination]

    def extract(self):
        for record in self.input():
            yield record

    def transform(self):
        for record in self.extract():
            # transform the record
            transformed_record = mapping(record)
            yield transformed_record

    def load(self):
        self.output(self.transform())

    def start(self):
        self.load()


SOURCE="Logstash"
DEST="stdout"
# DEST="ES"


if __name__ == "__main__": 

    etl = ETL(SOURCE, DEST)
    etl.start() 