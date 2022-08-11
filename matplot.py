import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)
y1 = 0.5 * x
y2 = 0.5 * x**2
y3 = 0.5 * x**3

plt.plot(x, y1, label="linear")
plt.plot(x, y2, label="quadratic")
plt.plot(x, y3, label="cubic")

plt.legend()
plt.show()