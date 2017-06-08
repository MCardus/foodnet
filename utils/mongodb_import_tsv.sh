#!/bin/bash  
mongoimport --db $1 --collection $2 --type tsv --file $3 --host $4 --headerline
