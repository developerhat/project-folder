#!/bin/bash

echo "hello $USER"
echo "how goes it today" 
read response 

if [[ $response = good ]]; then
	echo "Great!"
else
	echo "sorry to hear"
fi
