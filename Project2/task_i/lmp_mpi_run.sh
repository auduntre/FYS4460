#!/usr/bin/env bash

for ((i=4; i<=24; i+=4))
do
    mpirun -n 4 lmp -sf omp -pk omp 1 -in in.liquidi -var radius $i
done
