import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['A', 'B', 'C', 'D']
values = [4, 3, 2, 5]

N = len(categories)
angles = [n / float(N) * 2 * pi for n in range(N)]
values += values[:1]
angles += angles[:1]

ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories)
ax.plot(angles, values)
ax.fill(angles, values, 'b', alpha=0.1)
plt.title('Radar Chart')
plt.show()
