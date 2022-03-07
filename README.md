# Mind Map API

This repository contains a [mind map](https://en.wikipedia.org/wiki/Mind_map) web service that

* provides **REST API** endpoints
* achieves **persistence**
* is written in **Python**

## Launching the service

The service will be available at localhost on port 5000 (http://127.0.0.1:5000)

```bash
# Install dependencies
pip install -r requirements.txt

# Build & start REST API
./bin/run.sh
```

## Unit testing

The mind map webservice is unit tested using **Bitbucket Pipelines**. You can click on the `./unittest.sh` dropdown to see that the unit tests provide **100% coverage**

```
Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
bin/main.py             18      0      0      0   100%
bin/mindmap.py          29      0      4      0   100%
bin/persistance.py      15      0      0      0   100%
bin/tree.py             34      0     22      0   100%
------------------------------------------------------
TOTAL                   96      0     26      0   100%
```

To run the unit tests yourself locally, simply run

```bash
# Run unit tests locally & output coverage
./unittest.sh
```

## Endpoints

### Create a mind map

```bash
$ curl -X POST http://127.0.0.1:5000 \
    -H 'content-type: application/json' \
    -d '{"id": "YOUR_ID_HERE"}'
```

### Add a leaf to the map

```bash
$ curl -X POST http://127.0.0.1:5000/YOUR_ID_HERE \
    -H 'content-type: application/json' \
    -d '{
        "path": "YOUR/PATH/HERE",
        "text": "YOUR TEXT HERE"
        }'
```

### Read a leaf of the map

```bash
$ curl -X GET http://127.0.0.1:5000/YOUR_ID_HERE/YOUR/PATH/HERE

# Expected response:
{
    "path": "YOUR/PATH/HERE",
    "text": "YOUR TEXT HERE"
}
```

### Pretty print the whole tree of the mind map

```bash
$ curl -X GET http://127.0.0.1:5000/YOUR_ID_HERE

# Expected output:
root/
    YOUR/
        PATH/
            HERE
        OTHER/
            LEAF
```
