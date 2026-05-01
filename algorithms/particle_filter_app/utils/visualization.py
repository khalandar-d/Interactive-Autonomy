import matplotlib.pyplot as plt
from algorithms.particle_filter_app.config import MAP_SIZE, LANDMARKS


def plot_state(particles, robot, estimate):
    """
    Visualize the current state of the particle filter.

    Displays:
    - Particles (colored by weight)
    - True robot position
    - Estimated position
    - Landmarks

    Args:
        particles (np.ndarray): Particle set of shape (N, 4)
                                [x, y, theta, weight]
        robot (np.ndarray): True robot state [x, y, theta]
        estimate (np.ndarray): Estimated position [x, y]

    Returns:
        matplotlib.figure.Figure: Figure object for rendering
    """

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))

    # Set map boundaries
    ax.set_xlim(0, MAP_SIZE)
    ax.set_ylim(0, MAP_SIZE)

    # Plot particles:
    # Color represents weight (importance of each particle)
    ax.scatter(
        particles[:, 0], particles[:, 1],
        c=particles[:, 3],          # color by weight
        s=6,                        # small size for density
        cmap='viridis',
        alpha=0.7
    )

    # Plot true robot position (ground truth)
    ax.scatter(
        robot[0], robot[1],
        c='red',
        s=120,
        marker='x',
        label='Robot'
    )

    # Plot estimated position (from particle filter)
    ax.scatter(
        estimate[0], estimate[1],
        c='cyan',
        s=100,
        marker='o',
        label='Estimate'
    )

    # Plot landmarks (known reference points)
    ax.scatter(
        LANDMARKS[:, 0], LANDMARKS[:, 1],
        c='white',
        edgecolors='black',
        s=120,
        marker='s',
        label='Landmarks'
    )

    # Add legend and title
    ax.legend()
    ax.set_title("Live Particle Distribution")

    return fig