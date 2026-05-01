import numpy as np


def compute_uncertainty(particles):
    """
    Compute the uncertainty (spread) of the particle distribution.

    This function estimates how spread out the particles are in space.
    A higher value indicates more uncertainty in the state estimate.

    The uncertainty is computed as the sum of weighted variances in x and y.

    Args:
        particles (np.ndarray): Particle set of shape (N, 4)
                                [x, y, theta, weight]

    Returns:
        float: Total uncertainty (sum of variances in x and y)
    """

    # Extract particle weights
    weights = particles[:, 3]

    # Avoid division issues (ensure no zero weights)
    weights += 1e-300

    # Normalize weights so they sum to 1
    weights /= np.sum(weights)

    # Compute weighted mean position (expected position)
    mean = np.average(particles[:, :2], axis=0, weights=weights)

    # Compute deviation of each particle from the mean
    diff = particles[:, :2] - mean

    # Compute weighted variance in x and y directions
    var = np.average(diff**2, axis=0, weights=weights)

    # Total uncertainty = sum of variances
    return np.sum(var)