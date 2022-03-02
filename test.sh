#!/bin/bash

curl -X POST http://127.0.0.1:5000 -H 'content-type: application/json' -d '{"id": "my-map"}'
echo ''
curl -X POST http://127.0.0.1:5000/my-map -H 'content-type: application/json' -d '{"path": "i/like/potatoes","text": "Because reasons"}'
echo ''
curl -X GET http://127.0.0.1:5000/my-map 
echo ''
curl -X POST http://127.0.0.1:5000/my-map -H 'content-type: application/json' -d '{"path": "i/love/tomatoes","text": "Because reasons"}'
echo ''
curl -X GET http://127.0.0.1:5000/my-map 
