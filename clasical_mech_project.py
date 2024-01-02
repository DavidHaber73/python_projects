import numpy as np
import matplotlib.pyplot as plt

# Define the properties of the particle and the electric field
particle_charge = 1.6e-19  # Coulombs
electric_field_strength = 1e5  # Volts per meter
particle_mass = 9.1e-31  # Kilograms

# Parameters for the Hamilton-Jacobi equation
param_A = particle_charge * electric_field_strength / particle_mass
param_B = 0

# Create an array of time points
time_points = np.linspace(0, 1e-8, 100)

# Calculate Hamilton's principal function
principal_function = param_A * time_points**2 / 2 + param_B * time_points

# Calculate Hamilton's characteristic function
characteristic_function = np.sqrt(2 * particle_mass * (principal_function - particle_charge * electric_field_strength * time_points))

# Create a plot of the characteristic function over time
plt.figure(figsize=(10, 6))
plt.plot(time_points, characteristic_function, color = 'green')
plt.title('Time Evolution of Hamilton\'s Characteristic Function')
plt.xlabel('Time (seconds)')
plt.ylabel('Characteristic Function (Joule-seconds)')
plt.grid(True)
plt.show()
 
import numpy as np
import matplotlib.pyplot as plt

# Define the properties of the particle and the electric field
particle_charge = 1.6e-19  # Coulombs
electric_field_strength = 1e5  # Volts per meter
particle_mass = 9.1e-31  # Kilograms

# Initial conditions
initial_velocity = 0  # Initial velocity
initial_position = 0  # Initial position

# Time array
time_step = 1e-18  # Time step
time_array = np.arange(0, 1e-15, time_step)  # Total time

# Initialize velocity and position arrays
velocity = np.zeros_like(time_array)
position = np.zeros_like(time_array)

# Set initial conditions
velocity[0] = initial_velocity
position[0] = initial_position

# Euler method
for i in range(1, time_array.size):
    acceleration = particle_charge * electric_field_strength / particle_mass  # Acceleration
    velocity[i] = velocity[i-1] + acceleration * time_step  # Velocity
    position[i] = position[i-1] + velocity[i] * time_step  # Position

# Create a plot of the characteristic function over time
plt.figure(figsize=(10, 6))
plt.plot(time_array, position)
plt.title('Path of a Charged Particle in an Electric Field')
plt.xlabel('Time (seconds)')
plt.ylabel('Position (meters)')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 9.1e-31  # mass of the particle
q = 1.6e-19  # charge of the particle
E = 10  # electric field

# Hamilton's equations
def wwwhamiltons_equations(r, p):
    drdt = p/m
    dpdt = q*E
    return drdt, dpdt

# Time array
t = np.linspace(0, 10, 100)
dt = t[1] - t[0]

# Initialize arrays to store r, v, and a
r = np.zeros_like(t)
v = np.zeros_like(t)
a = np.zeros_like(t)

# Initial conditions: r(0) = 0, v(0) = 0
r[0] = 0
v[0] = 0

# Solve Hamilton's equations using Euler method
for i in range(len(t) - 1):
    drdt, dpdt = hamiltons_equations(r[i], m*v[i])
    r[i+1] = r[i] + drdt*dt
    v[i+1] = v[i] + dpdt*dt

# Compute a(t)
a = np.gradient(v, t)

# Plot r(t), v(t), and a(t)
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, r, color = "lime")
plt.title('Position vs Time')
plt.xlabel('Time')
plt.ylabel('Position')

plt.subplot(3, 1, 2)
plt.plot(t, v, color = "red")
plt.title('Velocity vs Time')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.subplot(3, 1, 3)
plt.plot(t, a, color = "cyan")
plt.title('Acceleration vs Time')
plt.xlabel('Time')
plt.ylabel('Acceleration')

plt.tight_layout()
plt.show()
