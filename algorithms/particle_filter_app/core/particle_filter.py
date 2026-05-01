import numpy as np
from algorithms.particle_filter_app.config import MAP_SIZE, LANDMARKS


def init_particles(n):
    """
    Initialize particles uniformly over the map.
    
    Each particle has:
    [x_position, y_position, orientation(theta), weight]
    """
    return np.column_stack((
        np.random.uniform(0, MAP_SIZE, n),        # x positions
        np.random.uniform(0, MAP_SIZE, n),        # y positions
        np.random.uniform(0, 2*np.pi, n),         # orientations (0 to 2π)
        np.ones(n) / n                            # equal initial weights
    ))


def predict(particles, motion_noise):
    """
    Predict next state of particles based on motion model.
    
    Adds noise to simulate uncertainty in movement.
    """
    v = 2      # linear velocity
    w = 0.2    # angular velocity

    # Update orientation with noise
    particles[:, 2] += w + np.random.normal(0, 0.05, len(particles))

    # Update x and y positions with motion + noise
    particles[:, 0] += v * np.cos(particles[:, 2]) + np.random.normal(0, motion_noise, len(particles))
    particles[:, 1] += v * np.sin(particles[:, 2]) + np.random.normal(0, motion_noise, len(particles))

    # Keep particles inside map boundaries
    particles[:, 0] = np.clip(particles[:, 0], 0, MAP_SIZE)
    particles[:, 1] = np.clip(particles[:, 1], 0, MAP_SIZE)

    return particles


def update(particles, measurement, sensor_noise):
    """
    Update particle weights based on sensor measurements.
    
    Compares expected distance to landmarks vs actual measurement.
    """
    weights = np.zeros(len(particles))

    for i, p in enumerate(particles):
        # Expected distances from particle to each landmark
        expected = np.linalg.norm(LANDMARKS - p[:2], axis=1)

        # Difference between observed and expected
        error = measurement - expected

        # Gaussian likelihood (higher weight = better match)
        weights[i] = np.exp(-np.sum(error**2) / (2 * sensor_noise**2))

    # Avoid division by zero
    weights += 1e-300

    # Normalize weights (sum = 1)
    weights /= np.sum(weights)

    particles[:, 3] = weights
    return particles


def resample(particles):
    """
    Resample particles based on their weights.
    
    Particles with higher weights are more likely to be selected.
    """
    weights = particles[:, 3]

    # Select indices based on probability distribution
    indices = np.random.choice(len(particles), len(particles), p=weights)

    # Replace particles with resampled ones
    particles = particles[indices]

    # Reset weights to uniform after resampling
    particles[:, 3] = 1.0 / len(particles)

    return particles


def estimate(particles):
    """
    Estimate current position as weighted average of particles.
    
    Returns:
        [x_estimate, y_estimate]
    """
    return np.average(particles[:, :2], axis=0, weights=particles[:, 3])