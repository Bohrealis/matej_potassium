Gromacs files here:

System topology - .top file, see documentation

Molecule topology - .itp files, see documentation

Can also copy text from .itp files directly into .top file if you prefer (K and water are super small so it's not a bad option). Otherwise, make sure to edit so that it finds these files correctly. E.g. copy these files into somewhere convenient and make sure the references in .top file are to this new location.

Simulation options file - .mdp files, see documentation

Min - a minimization option file for minimizing energy and removing bad contacts
Annealing - PBC, cut-off for both Coulombic and VdW forces, NVT simulation, 10 ns with 2 fs step size saved every 10 ps

Start structure - pdb from packmol

Generated files:

* tpr file - a binary run file for a simulation containing ALL information, including mdp options, start structure, and topology
* gro file - GROMACS' molecule configuration file, takes from either first or last frome of trajectory, I think the last?
* trr file - uncompressed trajectory, contains coordinates and velocities of all atoms at all timesteps
* edr file - energy file, not really used by us

  File naming:

  I like to use the naming scheme:

  ProjectName.StepName.fileextension

  Where project name is some overall tag for the simulation I'm trying to run. Step name is usually "min" for minimization, "eq" or a variation of that for equilibration and then "prod" for production runs.
