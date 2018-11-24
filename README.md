# PSO-parallel-mpi4py
This repository contains the code for parallelization of Particle Swarm Optimization Algorithm on multiple nodes using MPI (via mpi4py python package) using a master-slave model of implementation.

The objective function that has been minimized by the Particle Swarm Optimization Algorithm is the Alpine 1 Function which has been made artificially expensive by introducing a pause of 0.1 seconds.

## Setup
There are two types of nodes in master-slave model of parallelization. There is only one master node in the system and the rest of the other processes are the slave nodes. Therefore, there are two kinds of instructions, one running on the master node and the other running on the slave nodes. 
When rank=0, instructions for master node are executed and nodes with all the other ranks have slave instructions executed as can be seen in the code. Note that the code file on all the nodes should be saved at the same location with the same name. For instance, I saved it as `parPSO.py` in the Documents directory on all the nodes. 

## Running Instructions

Execute the following command on the terminal of the master node:

`mpiexec -f machinefile -n 3 python Documents/parPSO.py`

The above command is for running the parallelized PSO on 3 nodes (1 master, 2 slaves).