#!bin/bash
# Displays all HTTP Methods the server will accept
curl -X OPTIONS "$1"
