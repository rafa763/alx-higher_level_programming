#!/bin/bash
# print the size of the response body
curl -sI $1 | grep "Content-Length" | awk '{print $2}'
