import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

plt.figure()
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()
