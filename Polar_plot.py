import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(theta) * np.cos(theta))

plt.figure()
plt.polar(theta, r)
plt.title('Polar Plot')
plt.show()
