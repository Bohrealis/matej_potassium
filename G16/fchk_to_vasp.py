import numpy as np

def read_fchk(filename):
    atoms = []
    coordinates = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_atoms = 0
        read_coords = False
        for line in lines:
            if 'Number of atoms' in line:
                num_atoms = int(line.split()[-1])
            if 'Atomic numbers' in line:
                atom_lines = lines[lines.index(line) + 1:lines.index(line) + 1 + num_atoms]
                for atom_line in atom_lines:
                    atoms.append(int(atom_line.strip()))
            if 'Current cartesian coordinates' in line:
                coord_lines = lines[lines.index(line) + 1:lines.index(line) + 1 + num_atoms*3]
                for i in range(num_atoms):
                    x = float(coord_lines[i*3].strip())
                    y = float(coord_lines[i*3+1].strip())
                    z = float(coord_lines[i*3+2].strip())
                    coordinates.append([x, y, z])
                break
    return atoms, np.array(coordinates)

atoms, coordinates = read_fchk('potassium_cluster_1.fchk')
print("Atoms:", atoms)
print("Coordinates:", coordinates)

