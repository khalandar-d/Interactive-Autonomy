import numpy as np
from algorithms.particle_filter_app.core.particle_filter import init_particles
from algorithms.particle_filter_app.utils.metrics import compute_uncertainty


def adapt_particles(particles):
    """
    Adapt the number of particles dynamically based on uncertainty.

    The idea:
    - High uncertainty → increase number of particles (better coverage)
    - Low uncertainty → reduce particles (save computation)

    Args:
        particles (np.ndarray): Current particle set of shape (N, 4)
                                [x, y, theta, weight]

    Returns:
        np.ndarray: Updated particle set with adjusted size
    """

    # Compute uncertainty of current particle distribution
    unc = compute_uncertainty(particles)

    # Determine target number of particles based on uncertainty
    # Scale uncertainty → particle count, and clamp between limits
    target = int(np.clip(unc * 50, 200, 1500))

    if target > len(particles):
        # If uncertainty is high → add more particles
        # Initialize new particles randomly
        extra = init_particles(target - len(particles))

        # Combine existing and new particles
        particles = np.vstack((particles, extra))

    else:
        # If uncertainty is low → reduce number of particles
        # Keep only the first 'target' particles
        particles = particles[:target]

    # Reset weights to uniform after resizing
    particles[:, 3] = 1.0 / len(particles)

    return particles