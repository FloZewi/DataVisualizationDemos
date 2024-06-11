import numpy as np
import matplotlib.pyplot as plt

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure()
plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Box Plot')
plt.show()
