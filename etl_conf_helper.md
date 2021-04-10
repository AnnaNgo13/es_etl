# How to setup conf.json

Conf.json defines the input, output and mappings conf for IAT

```
{
    "input":xxx,
    "mapping":xxx,
    "output":xxx
}
```

## Input
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

## Mapping
{
    "mapping_file":"mappings_aydat.json"
}


## Output
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