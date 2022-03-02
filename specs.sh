#!/bin/bash

# Ensure argument was passed
if [ $# -eq 0 ]
  then
    echo "Please specify a number (1, 2, 3, 4)"
    exit 1
fi

# Select the specification to run
if [[ $1 -eq 1 ]]; then
    curl -X [verb] [something] -H 'content-type: application/json' -d '{"id": "my-map"}'

elif [[ $1 -eq 2 ]]; then
    curl -X [verb] [something] \
    -H 'content-type: application/json' \
    -d '{
        "path": "i/like/potatoes",
        "text": "Because reasons"
    }'

elif [[ $1 -eq 3 ]]; then
    curl -X [verb] [something] -H 'content-type: application/json'

elif [[ $1 -eq 4 ]]; then
    curl -X [verb] [something] 

else
    echo "Number specified was invalid"
    echo "Please specify a number (1, 2, 3, 4)"
    exit 1

fi
