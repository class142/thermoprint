⚠️ dropped development in favor of [Go implementation](https://github.com/class142/escpos-go) ⚠️

## Purpose
Python WS printing random jokes on serial thermo printer using ESCPOS library

## Requisites
* Ethernet-to-serial bridge
* List of jokes (e.g. provided by NodeRed webservice reading JSON file of jokes, http://10.0.0.4:1880/witz)

## Usage
Make HTTP request to http://[container-ip]:9090/process
