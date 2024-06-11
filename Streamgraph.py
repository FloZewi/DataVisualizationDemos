import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x + 1)
y3 = np.sin(x + 2)

plt.figure()
plt.stackplot(x, y1, y2, y3, labels=['y1', 'y2', 'y3'])
plt.legend(loc='upper left')
plt.title('Streamgraph')
plt.show()
