import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# Constants
hbar = 1.0545718e-34  # Planck's constant / (2*pi) in J*s
e = 1.60217662e-19  # Elementary charge in C
m = 9.10938356e-31  # Electron mass in kg
g_factor = 2.002319  # Electron g-factor (approximately 2)

hbar2 = hbar**2
e2 = e**2
S = hbar / 2 * np.array([2, 1, 2])

# Define the unperturbed Hamiltonian for a hydrogen atom
def H0(psi):
    return -hbar2 /(2*m)*second_derivative(psi) - e2 /np.linalg.norm(psi)

# Define the perturbation due to the magnetic field
def H_prime(S, B):
    ndims = len(B.shape)
    if ndims == 1:
        # Handle 1D array
        return - (e / (2 * m)) * g_factor * np.dot(S, B[0])
    else:
        # Handle 2D arrays
        return - (e / (2 * m)) * g_factor * np.dot(S, B)

# Second derivative operator for 3D space and 1D space
def second_derivative(psi):
    ndims = len(psi.shape)
    if ndims == 1:
        # Handle 1D array
        return np.gradient(psi)[0]
    else:
        # Handle multidimensional arrays
        return np.sum(np.gradient(np.gradient(psi), axis=(0, 1, 2)), axis=0)

# Function to compute the total Hamiltonian matrix
def total_hamiltonian(psi, B):
    H0_matrix = H0(psi) * np.identity(2)  # Assume 2x2 matrix for simplicity
    S = hbar / 2 * np.array([[0, 1], [1, 0]])  # Electron spin matrix
    H_prime_matrix = H_prime(S, B)
    return H0_matrix + H_prime_matrix

# Function to calculate Zeeman splitting
def zeeman_splitting(B_values, psi):
    energy_levels = []

    for B_value in B_values:
        # Update magnetic field strength
        B = np.array([3, 10, B_value])

        # Diagonalize the total Hamiltonian
        eigenvalues, _ = eigh(total_hamiltonian(psi, B))
        energy_levels.append(eigenvalues)

    return np.array(energy_levels)

# Magnetic field values (From 0 to 10 Tesla)
B_values = np.linspace(0, 10, 100000)

# Define psi here
psi = np.array([0, 1, 2])# Replace ... with the appropriate value or calculation for psi

# Calculating Zeeman splitting
energies = zeeman_splitting(B_values, psi)

# Plot the results
plt.plot(B_values, energies[:, 0], label='Energy Level 1')
plt.plot(B_values, energies[:, 1], label='Energy Level 2')
plt.xlabel('Magnetic Field (Tesla)')
plt.ylabel('Energy (Joules)')
plt.legend()
plt.show()
