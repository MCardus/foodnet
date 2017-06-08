#!/bin/bash  
mongoimport --db $1 --collection $2 --type json --file $3 --host $4
