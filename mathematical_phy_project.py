import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from scipy.special import factorial
import numpy.polynomial.hermite as Herm
import math

# Constants in natural units
hbar = 1 # in J·s # Planck's constant / 2pi
m = 1.14 # in amu   # mass
omega = 2.145 #in rad·s⁻¹  # angular frequency

# Creating a Potential function
def V(x):
    return 0.5 * m * omega**2 * x**2

# Creating the wave function using Hermite polynomials
def psi(n, x):
    return (1/np.sqrt(2**n * factorial(n))) * (m*omega/(np.pi*hbar))**(1/4) * np.exp(-m*omega*x**2/(2*hbar)) * hermite(n)(np.sqrt(m*omega/hbar)*x)

# Creating an x-values array
x = np.linspace(-3, 3, 2000)

# Plotting the potential
plt.figure(figsize=(6,5))
plt.plot(x, V(x), color='black')

# Plotting the first few wave functions
for n in range(6):
    plt.plot(x, psi(n, x)**2 + n + 0.5)
    
plt.title('Quantum Harmonic Oscillator')
plt.xlabel('Position')
plt.ylabel('Energy')
plt.show()

# Discretized space
dx = 0.0005
x_lim = 2.3
x = np.arange(-x_lim, x_lim, dx)

def hermite(x, n):
    xi = np.sqrt(m * omega / hbar) * x
    herm_coeffs = np.zeros(n + 1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)

def stationary_state(x, n):
    xi = np.sqrt(m * omega/ hbar) * x
    prefactor = 1.0 / math.sqrt(2.0 ** n * math.factorial(n)) * (m * omega / (np.pi * hbar)) ** 0.25
    psi = prefactor * np.exp(-xi ** 2 / 2) * hermite(x, n)
    return psi

# Plotting the probability density for the first few states
plt.figure(figsize=(10, 8), )
for n in range(5):
    plt.subplot(3, 2, n + 1)
    plt.plot(x, np.conjugate(stationary_state(x, n)) * stationary_state(x, n), label="n={}".format(n),color = "green")
    plt.legend()

plt.show()
