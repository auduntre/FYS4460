#!/usr/bin/env bash

for ((i=5; i<=40; i+=5))
do
    mpirun -n 4 lmp -sf omp -pk omp 1 -in in.liquidi -var sphere_count $i
done
