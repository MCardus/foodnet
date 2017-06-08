#!/bin/bash

mongoexport --db $1 --collection $2 --fields $3 --csv --out $4 --host $5
