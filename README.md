# ES_ETL

This project is to create a streaming ETL with python. Its primary objective is to seamlessly integrate data from various sources and efficiently load it into Elasticsearch.

## System requirements

* Linux Ubuntu machine with 16 GB RAM and a 6-core Intel Core i5 CPU 8400 and 500 GB disk space

* ELK stack v7.6.0

* Python 3.6

## Datasets

Dataset Sharing Notice

Please note that the dataset associated with this project cannot be shared in this GitHub repository.
If you require access to the dataset for research or other purposes, please contact us through Github.

## Installation Steps

Prepare python environment
```
virtualenv -p python3 es_etl
source es_etl/bin/activate
pip install -r scripts/requirements.txt
```

Deploy elasticsearch and kibana. Instructions with Docker are [here](https://www.elastic.co/fr/blog/getting-started-with-the-elastic-stack-and-docker-compose).

## Run

To start a run of the streaming ETL, It is required to configure the file [etl_conf.json](https://github.com/AnnaNgo13/es_etl/blob/main/etl_conf.json)

Below a helper to configure the configuration file

Conf.json defines the input, output and mappings configuration for IAT

```
{
    "input":xxx,
    "mapping":xxx,
    "output":xxx
}
```

### Input
For file
```
    {
        "source_type":"file",
        "file_path":"/home/ttngo/code/evaluationELK/dataset/data-aydat-2020-3month.json"
    }
```
For Logstash
```
    {
        "source_type":"Logstash",
        "host":127.0.0.1,
        "port":5002
    }
```

### Mapping
{
    "mapping_file":"mappings_aydat.json"
}


### Output
For file
```
    {
        "source_type":"file",
        "file_path":"output.json"
    }
```
For ES
```
    {
        "source_type":"ES",
        "host":"127.0.0.1",
        "port":9200,
        "target_index":"target_index_3month"
    }
```
For standard output
```
    {"source_type":"stdout"}
```

After configuration, run the ETL process
```
python3 etl.py
```

## References
<a id="1">[1]</a> 
Ngo, Thi Thu Trang, David Sarramia, Myoung-Ah Kang, and François Pinet. 
An Analytical Tool for Georeferenced Sensor Data based on ELK Stack.
In 7th International Conference on Geographical Information Systems Theory, Applications and Management, SCITEPRESS-Science and Technology Publications (2021).

<a id="1">[2]</a> 
Ngo, Thi Thu Trang, David Sarramia, Myoung-Ah Kang, and François Pinet. 
A New Approach Based on ELK Stack for the Analysis and Visualisation of Geo-referenced Sensor Data.
in the Springer Nature Computer Science journal (2023).