#!/bin/bash

#SBATCH --mem=950Gb
#SBATCH --job-name="MatFirst"
#SBATCH --nodes=1
#SBATCH --partition=b64_1024_long
#SBATCH --ntasks-per-node=64
#SBATCH --time=12:00:00

export SLURM_MPI_TYPE=pmix_v3
export OMPI_MCA_btl="self,vader,tcp"

source /uochb/soft/b/spack/20221211-git/share/spack/setup-env.sh

spack load openmpi/uk7bfsn
spack load hdf5/x56z6nm
spack load fftw/3eknhyk
spack load netlib-scalapack/jj6f5kd
spack load openblas/nub7iq2

export LD_LIBRARY_PATH=/uochb/soft/b/spack/20221211-git/opt/spack/linux-almalinux9-zen3/gcc-11.3.0/openblas-0.3.21-nub7iq2c6ix63ib3y22qximn26dplug4/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/uochb/soft/b/spack/20221211-git/opt/spack/linux-almalinux9-zen3/gcc-11.3.0/netlib-scalapack-2.2.0-jj6f5kdm24tgmsmnmic6ucfdwmbhhkgs/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/uochb/soft/b/spack/20221211-git/opt/spack/linux-almalinux9-zen3/gcc-11.3.0/fftw-3.3.10-3eknhyka5jgcrpqsfmyyppxxu672gdmg/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/uochb/soft/b/spack/20221211-git/opt/spack/linux-almalinux9-zen3/gcc-11.3.0/hdf5-1.13.2-x56z6nma5ryzh5b4nqpauswqwxclbfci/lib:$LD_LIBRARY_PATH

# Start VASP Run
vasp_std="srun /uochb/soft/groups/electron/b/vasp/bin/vasp_std"

cp POSCAR.GoodStart POSCAR
cp INCAR.GGAopt INCAR
$vasp_std
sleep 10
cp OUTCAR OUTCAR.GGAopt
cp POSCAR POSCAR.GGAopt
cp vaspout.h5 vaspout.GGAopt.h5
cp vasprun.xml vasprun.GGAopt.xml
./extract_optics.sh
mv optics.dat optics.GGAopt.dat

