import numpy as np
from matplotlib import pyplot as plt

plt.style.use('seaborn-darkgrid')

x_axis = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

x_indexes = np.arange(len(x_axis))
width = 0.25


#plt.xkcd()


y_axis_one = [15, 33, 45, 56, 67, 69, 70, 77, 89, 89, 90, 95, 98, 101, 120, 121]

plt.bar(x_indexes - width,  y_axis_one, color="black", width=width, label="random data one")

y_axis_two = [23, 38, 47, 68, 70, 79, 85, 87, 89, 89, 95, 100, 101, 111, 123, 128]

plt.bar(x_indexes, y_axis_two, color="gray", width=width, label="random data two")

y_axis_three = [25, 39, 40, 65, 69, 80, 77, 79, 80, 91, 82, 100, 70, 67, 106, 130]

plt.bar(x_indexes + width, y_axis_three, color="cyan", width=width, label="random data three")


plt.legend()
plt.xticks(ticks=x_indexes, labels=x_axis)
plt.title('Plot from random number using Matplotlib')
plt.xlabel('random X numbers')
plt.ylabel('Random Y numbers')
plt.tight_layout()
plt.show()
plt.savefig('plot2.png')