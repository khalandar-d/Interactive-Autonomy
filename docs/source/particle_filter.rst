Particle Filter
===============

Overview
--------

The Particle Filter is a probabilistic algorithm used for state estimation under uncertainty.

Core Idea
---------

We represent belief using multiple particles and update them using:

- Motion model (prediction)
- Sensor model (correction)

Steps
-----

1. Initialize particles
2. Predict next state
3. Update weights using sensor data
4. Resample particles

Application in Self-Driving
---------------------------

- Vehicle localization
- Sensor fusion
- Handling noisy measurements

Use Case Diagram
----------------

The following diagram illustrates the interaction between the user and the particle filter system.

.. uml:: diagrams/particle_filter_usecase.puml