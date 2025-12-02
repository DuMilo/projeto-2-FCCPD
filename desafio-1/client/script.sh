#!/bin/sh

echo "Iniciando o cliente..."
echo "Tentando conectar em http://servidor-web:8080"

while true; do
  echo "Enviando requisição..."

  curl http://servidor-web:8080
  

  sleep 5
done