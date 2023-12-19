#!/usr/bin/env sh

#!/bin/bash

while true
do
        timeout -k 3600 3600 python3 frontend.py
done

# to kill the process use the command
# ps -ef | grep python
