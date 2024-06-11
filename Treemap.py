import matplotlib.pyplot as plt
import squarify

sizes = [50, 25, 12, 6, 3]
labels = ['A', 'B', 'C', 'D', 'E']
colors = plt.cm.tab20c.colors

plt.figure()
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.axis('off')
plt.title('Treemap')
plt.show()
