import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.figure()
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=True, fontsize=10)
plt.title('Contour Plot with Labels')
plt.show()
