#!/bin/bash
# displays only the status code of the response
curl -s -o /rafa/null -w "%{http_code}" $1
