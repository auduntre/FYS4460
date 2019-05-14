#!/usr/bin/env bash

for i in {1..5}; do
    mpirun -n 4 lmp -sf omp -in in.multicylinder -var radius $i
done
