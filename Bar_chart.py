import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

plt.figure()
plt.bar(categories, values, color='blue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
