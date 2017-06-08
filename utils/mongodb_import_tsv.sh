#!/bin/bash  
# Sample call: sh utils/mongodb_import_tsv.sh foodnet food_corpus data/food_corpus.tsv 172.31.45.65
mongoimport --db $1 --collection $2 --type tsv --file $3 --host $4 --headerline
