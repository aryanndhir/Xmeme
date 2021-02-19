#!/bin/bash

# Any installation related commands

sudo apt update

sudo apt install -y python3-pip python3 python3-dev libpq-dev nginx curl

sudo -H pip3 install --upgrade pip

sudo -H pip3 install virtualenv
