import matplotlib.pyplot as plt

def plot_points(points):
    x, y = zip(*points)
    
    plt.scatter(x, y, color='blue', marker='o', label='Data Points')
    
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Scatter Plot of Data Points')
    
    plt.grid(True)
    plt.legend()
    plt.show()

points = [(0, 12), (1, 32), (2, 42), (3, 52)]
plot_points(points)
