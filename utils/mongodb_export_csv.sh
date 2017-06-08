#!/bin/bash
#Example sh utils/mongodb_export_csv.sh foodnet clean_recipes ingredients,title clean_spanish_recipes.csv 172.31.45.65
mongoexport --db $1 --collection $2 --fields $3 --csv --out $4 --host $5
