import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 / (np.exp(x) - 1)

a = 0
b = np.inf

n = 100000

integral = 0

x_values = []
y_values = []

for i in range(n):
    t = np.random.uniform(0,1)
    x = 1/(t+0.0001) - 1
    integral += f(x)*(1/(t+0.0001)**2)
    x_values.append(x)
    y_values.append(f(x))

integral /= n
print(integral)

plt.plot(x_values, y_values, 'g.')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) vs x')
plt.legend(['f(x)'])
plt.show()

