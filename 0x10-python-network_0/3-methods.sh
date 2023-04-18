#!/bin/bash
# display all HTTP methods the server will accept
curl -isX OPTIONS $1 | grep "Allow" | cut -d " " -f 2-
