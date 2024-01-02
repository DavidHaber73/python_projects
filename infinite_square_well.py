import math
import numpy as np
import matplotlib.pyplot as plt

a = 1
y_axis = []
x_plot = []
probability_density = []

for n in range(1, 5):
    x = -a
    x_values = []
    y_values = []
    density_values = []

    while x <= a:
        if n % 2 == 0:
            y = (np.sin((n * np.pi * x) / (2 * a)) / math.sqrt(2 / a))
        else:
            y = (np.cos((n * np.pi * x) / (2 * a)) / math.sqrt(2 / a))

        x_values.append(x)
        y_values.append(y)
        density = y**2
        density_values.append(density)
        x += 0.0001

    x_plot.append(x_values)
    y_axis.append(y_values)
    probability_density.append(density_values)

plt.figure(figsize=(10, 9))
for i in range(4):
    plt.subplot(4, 2, 2 * i + 1)
    plt.plot(x_plot[i], y_axis[i], color='green')
    plt.title(f'n = {i+1} (Eigenfunction)')
    plt.xlabel('Position (x)')
    plt.ylabel('$\psi(x)$')
    plt.grid()

    plt.subplot(4, 2, 2 * i + 2)
    plt.plot(x_plot[i], probability_density[i], color='cyan')
    plt.title(f'n = {i+1} (Probability Density)')
    plt.xlabel('Position (x)')
    plt.ylabel('Probability Density')
    plt.grid()

plt.tight_layout()
plt.show()
