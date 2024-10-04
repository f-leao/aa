import numpy as np

import matplotlib.pyplot as plt

def f(x):
    return x**3

def tangent_line(x, x0):
    return 3*(x0**2)*(x - x0) + f(x0)

# this is another great comment worth looking at!

x = np.linspace(-10, 10, 100)
y = f(x)

plt.plot(x, y, label='y = x^3')
plt.plot(x, tangent_line(x, 1), label='Tangent at x = 1')
plt.plot(x, tangent_line(x, 2), label='Tangent at x = 2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^3 and its tangent lines')
plt.legend()
plt.grid(True)
plt.show()
