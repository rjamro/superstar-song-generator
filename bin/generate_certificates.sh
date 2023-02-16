#!/bin/sh

ROOT=src/certs/

mkdir ${ROOT}

# generate CA
openssl req -x509 -nodes -newkey rsa:4096 -keyout "${ROOT}ca.key" -out "${ROOT}ca.pem" -subj /O=me

# generate CSR
openssl req -nodes -newkey rsa:4096 -keyout "${ROOT}server.key" -out "${ROOT}server.csr" -subj /CN=server

# create server certificate
openssl x509 -req -in "${ROOT}server.csr" -CA "${ROOT}ca.pem" -CAkey "${ROOT}ca.key" -set_serial 1 -out "${ROOT}server.pem"
