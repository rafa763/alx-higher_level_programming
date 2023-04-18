#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -X POST -d @$2 $1 -H 'content-type: application/json'
