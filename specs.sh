#!/bin/bash

# Ensure argument was passed
if [ $# -eq 0 ]
  then
    echo "Please specify a number (1, 2, 3, 4)"
    exit 1
fi

# Select the specification to run
if [[ $1 -eq 1 ]]; then
    curl -X POST http://127.0.0.1:5000 -H 'content-type: application/json' -d '{"id": "my-map"}'

elif [[ $1 -eq 2 ]]; then
    curl -X POST http://127.0.0.1:5000/my-map -H 'content-type: application/json' -d '{"path": "i/like/potatoes","text": "Because reasons"}'

elif [[ $1 -eq 3 ]]; then
    curl -X GET http://127.0.0.1:5000/my-map/i/like/potatoes -H 'content-type: application/json'

elif [[ $1 -eq 4 ]]; then
    curl -X GET http://127.0.0.1:5000/my-map 

else
    echo "Number specified was invalid"
    echo "Please specify a number (1, 2, 3, 4)"
    exit 1

fi
