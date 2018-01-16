#!/bin/bash

#SBATCH --nodes 1

#SBATCH --time=36:00:00

#SBATCH --error=job.%J.err #tell it to store the output console text to a file

#SBATCH --output=job.%J.out #tell it to store the error messages to a file

module purge

#module unload vegas

#module unload root

#module unload fermi

#module load fermitools

#source /work/astropa/sw/fermi/fermipy/bin/activate
module load fermi

python /work/astropa/users/jrblaum/IC443/fermipy/FGES_BinnedAnalysis.py > outputsbatch.txt 2>&1
