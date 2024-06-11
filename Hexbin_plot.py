import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.figure()
plt.hexbin(x, y, gridsize=30, cmap='Blues')
plt.colorbar(label='count in bin')
plt.title('Hexbin Plot')
plt.show()
