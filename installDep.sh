#!/usr/bin/env bash

#This installation is needed for mac users as I faced it.
env LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" pip install cryptography

pip install -r requirements.txt