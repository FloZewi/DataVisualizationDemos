import numpy as np
import matplotlib.pyplot as plt

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.figure()
plt.violinplot(data, showmeans=False, showmedians=True)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Violin Plot')
plt.show()
