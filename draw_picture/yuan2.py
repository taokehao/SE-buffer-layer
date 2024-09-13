import matplotlib.pyplot as plt
import numpy as np

# Define the structure of the diagram
center = (0, 0)
levels = 2  # Number of levels of circles
points_per_level = 8  # Number of points in each level

# Colors for each level
center_color = '#57AF37'
# colors = ['#6A8EC9', '#D9A421', '#CC5B45']
colors = ['#6A8EC9', '#652884']
circle_size = 50  # Increased size of the circles
line_width = 2  # Thickness of the connecting lines
fig_size = (10, 10)  # Size of the figure

# Function to plot the diagram
def plot_diagram(center, levels, points_per_level, colors, center_color, circle_size, line_width, fig_size, filename):
    fig, ax = plt.subplots(figsize=fig_size)

    # Plot the center point with a distinct color
    ax.plot([center[0]], [center[1]], 'o', color=center_color, markersize=circle_size, zorder=10, markeredgecolor='black')

    for level in range(1, levels + 1):
        angle_step = 2 * np.pi / points_per_level
        radius = level
        for point in range(points_per_level):
            angle = point * angle_step
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)
            # Plot the black connecting line
            ax.plot([center[0], x], [center[1], y], 'k-', zorder=1, linewidth=line_width)
            # Plot the circles with edge color
            ax.plot(x, y, 'o', color=colors[level - 1], markersize=circle_size, zorder=10, markeredgecolor='black')

    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig(filename, format='png', transparent=True)
    plt.close()

# Save the diagram as a PNG file with a transparent background
plot_diagram(center, levels, points_per_level, colors, center_color, circle_size, line_width, fig_size, './diagram_transparent.png')
