# es_etl

This project is to create a streaming etl with python. Its main purpose is to integrate data from different sources and load it into Elasticsearch

## To run

```
virtualenv -p python3 es_etl
source es_etl/bin/activate
pip3 install -r scripts/requirements.txt
```

1. Run elasticsearch and kibana

2. Update etl_conf.json (Instructions [here](https://github.com/AnnaNgo13/es_etl/blob/main/etl_conf_helper.md))

3. Run ETL process
```
python3 etl.py
```
