from utils import SOURCE_FUNC, DEST_FUNC
from transformations import mapping
from aggregate import window
from external import extend

class ETL:

    def __init__(self, source, destination, mapping_conf):
        self.input=SOURCE_FUNC[source]
        self.output=DEST_FUNC[destination]
        self.mapping_conf=mapping_conf

    def extract(self):
        for record in self.input():
            yield record

    def transform(self):
        for record in extend(window(mapping(self.extract(), self.mapping_conf), self.mapping_conf)):
            yield record

    def load(self):
        self.output(self.transform())

    def start(self):
        try:
            self.load()
        except KeyboardInterrupt:
            print("\nEtl process stopped")
            quit()


SOURCE="Logstash"
#DEST="stdout"
DEST="ES"
MAPPING="mappings.json"


if __name__ == "__main__": 

    etl = ETL(SOURCE, DEST, MAPPING)
    etl.start() 