import numpy as np
from algorithms.particle_filter_app.config import MAP_SIZE, LANDMARKS


def move_robot(robot):
    """
    Move the robot using a simple motion model.

    The robot follows a constant velocity and angular velocity model:
    - v: linear velocity
    - w: angular velocity

    Args:
        robot (np.ndarray): Robot state [x, y, theta]

    Returns:
        np.ndarray: Updated robot state after motion
    """
    v = 2      # linear velocity (forward movement)
    w = 0.2    # angular velocity (rotation)

    # Update orientation
    robot[2] += w

    # Update position based on new orientation
    robot[0] += v * np.cos(robot[2])  # x position
    robot[1] += v * np.sin(robot[2])  # y position

    # Ensure robot stays within map boundaries
    robot[0] = np.clip(robot[0], 0, MAP_SIZE)
    robot[1] = np.clip(robot[1], 0, MAP_SIZE)

    return robot


def sense(robot, noise):
    """
    Simulate sensor measurements from the robot to landmarks.

    Computes the distance from the robot to each landmark and adds Gaussian noise.

    Args:
        robot (np.ndarray): Robot state [x, y, theta]
        noise (float): Standard deviation of measurement noise

    Returns:
        np.ndarray: Noisy distance measurements to each landmark
    """
    # True distances from robot to each landmark
    dists = np.linalg.norm(LANDMARKS - robot[:2], axis=1)

    # Add Gaussian noise to simulate imperfect sensor readings
    noisy_dists = dists + np.random.normal(0, noise, len(dists))

    return noisy_dists