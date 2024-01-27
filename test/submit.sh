#!/bin/bash
#SBATCH --time=12
#SBATCH --job-name=mytestjob
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=e1332814@u.nus.edu.sg

source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate cs3245
python practice_q4.py