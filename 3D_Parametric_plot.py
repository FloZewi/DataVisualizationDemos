import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.title('3D Parametric Plot')
plt.show()
