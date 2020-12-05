# es_etl

This project is to create a streaming etl with python.

## To run

```
virtualenv -p python3 es_etl
source es_etl/bin/activate
pip3 install -r scripts/requirements.txt
```

Run elasticsearch and kibana

1. run logstash with the configuration file
```
bin/logstash -f path/to/logstash_conf1
```

2. Run sensor simulator
```
python3 sensor_simulate.py
```

3. Run ETL 
```
python3 etl.py
```