#!/bin/bash
# this Bash script that takes in the URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
