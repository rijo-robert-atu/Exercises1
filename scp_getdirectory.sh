#!/bin/bash
# by: JOR
# Date: 21OCT22
# Function: Get a remote directory via SCP
# Script: scp_getdirectory.sh
cd /home/johnoraw/Scripts/
mkdir -p /home/johnoraw/Scripts/server
mkdir -p /home/johnoraw/Scripts/desktop
# Copy the entire directory local from a remote server, directory desktop
scp -r johnoraw@192.168.48.128:./Scripts/desktop ./

