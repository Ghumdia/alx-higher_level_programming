#!bin/bash
# Displays all HTTP Methods the server will accept
curl -sX OPTIONS "$1" | grep "Allow"
