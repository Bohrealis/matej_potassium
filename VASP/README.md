# Vasp

Vasp expects an INCAR, POSCAR, POTCAR, and KPOINTS file to run calculations. It expects these files with those exact names and no extensions, so usually successive calculations are performed with copy commands to move files around to and from these basic names.

INCAR - input options file for the calculation
POSCAR - positions of atoms (which Vasp calls "ions" because you usually treat them as either just nuclei, or nuclei with core electrons, either way they're ionic)
POTCAR - for most calculations, we'll be using a Projector Augmented Wave (PAW) plane wave basis set. This is a method of pseudopotentials, meaning that core electrons are treated as a variation in the potential rather than as electrons to solve for. This is a really good balance between accuracy and speed so you'll basically always use it, but Vasp needs to you tell it what exact parameters you use for the plane wave. It has several different options for all atoms and they're in a special folder. This file is basically made by finding the right file and copy-pasting it into a new file in an order that matches the POSCAR file (or for Linux masters, it's a cat command)

extract_optics.sh is a script developed by Vasp to grab the optics data from relevant calculations. It only sometimes works correctly so... it's a special little child that must be treated carefully.

vasp_me_crazy.sh is a runscript for Aurem. 
