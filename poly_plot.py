import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Number of points for the plot
num_points = 1000
x = np.linspace(-1, 1, num_points)

# Calculate and plot the Legendre polynomials
for n in range(5):
    legendre_poly = legendre(n)
    y = legendre_poly(x)
    plt.plot(x, y, label=f'P_{n}(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Legendre Polynomials')
plt.title('First Five Legendre Polynomials')
plt.legend()
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite

# Number of points for the plot
num_points = 1000
x = np.linspace(-5, 5, num_points)

# Calculate and plot the first five Hermite polynomials
for n in range(5):
    hermite_poly = hermite(n)
    y = hermite_poly(x)
    plt.plot(x, y, label=f'H_{n}(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Hermite Polynomials')
plt.title('First Five Hermite Polynomials')
plt.legend()
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre

# Number of points for the plot
num_points = 1000
x = np.linspace(0, 10, num_points)

# Calculate and plot the first five Laguerre polynomials
for n in range(5):
    laguerre_poly = genlaguerre(n, 0)
    y = laguerre_poly(x)
    plt.plot(x, y, label=f'L_{n}(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Laguerre Polynomials')
plt.title('First Five Laguerre Polynomials')
plt.legend()
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jacobi

# Number of points for the plot
num_points = 1000
x = np.linspace(-1, 1, num_points)

# Parameters for the Jacobi polynomials (alpha, beta)
alpha = 0.5
beta = 0.5

# Calculate and plot the first five Jacobi polynomials
for n in range(5):
    jacobi_poly = jacobi(n, alpha, beta)
    y = jacobi_poly(x)
    plt.plot(x, y, label=f'P_{n}^{alpha, beta}(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Jacobi Polynomials')
plt.title(f'First Five Jacobi Polynomials (alpha={alpha}, beta={beta})')
plt.legend()
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.show()