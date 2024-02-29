#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -X GET -H "X-School-User-Id: 98" -s "$1"
