#!/bin/sh
bin/generate_certificates.sh

cp default-env .env

echo '===================================================================='
echo '| Remember to generate your own openai api key and copy it to .env |'
echo '===================================================================='

docker-compose up --build --no-start
