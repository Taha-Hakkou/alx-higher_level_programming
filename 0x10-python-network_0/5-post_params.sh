#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST --data "email=test@gmail.com" --data "subject=I will always be here for PLD" -s "$1"
