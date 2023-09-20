import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [12, 32, 42, 52]

plt.scatter(x, y, color='green', marker='X')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.grid(True)
plt.show()
