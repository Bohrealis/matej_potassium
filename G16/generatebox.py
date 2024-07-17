import numpy as np

# Parameters for water molecule geometry
OH_bond_length = 0.96  # O-H bond length in Angstroms
HOH_angle = 104.5  # H-O-H bond angle in degrees

# Parameters for the placement
num_water_molecules = 20
box_size = 20.0
min_distance = 2.0

# Function to generate water molecule
def generate_water_molecule():
    angle_rad = np.radians(HOH_angle / 2)
    O = np.array([0.0, 0.0, 0.0])
    H1 = np.array([OH_bond_length, 0.0, 0.0])
    H2 = np.array([OH_bond_length * np.cos(angle_rad), OH_bond_length * np.sin(angle_rad), 0.0])
    return np.array([O, H1, H2])

# Function to translate molecule to a new position
def translate_molecule(molecule, position):
    return molecule + position

# Generate individual water molecules
water_molecules = [generate_water_molecule() for _ in range(num_water_molecules)]

# Randomly place the water molecules in a box
positions = []
molecules_positions = []

for molecule in water_molecules:
    while True:
        position = np.array([np.random.uniform(0, box_size) for _ in range(3)])
        if all(np.linalg.norm(position - pos) > min_distance for pos in positions):
            positions.append(position)
            molecules_positions.append(translate_molecule(molecule, position))
            break

# Function to print coordinates
def print_coordinates(molecules_positions):
    atom_index = 1
    atoms = ['O', 'H', 'H']
    for molecule in molecules_positions:
        for i, atom in enumerate(molecule):
            print(f"{atoms[i]:<2} {atom[0]:>12.6f} {atom[1]:>12.6f} {atom[2]:>12.6f}")
            atom_index += 1

# Print water molecules coordinates
print_coordinates(molecules_positions)

# Add potassium ion separately
K_position = np.array([np.random.uniform(0, box_size) for _ in range(3)])
print(f"K  {K_position[0]:>12.6f} {K_position[1]:>12.6f} {K_position[2]:>12.6f}")

