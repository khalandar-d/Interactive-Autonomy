import streamlit as st
import time
import numpy as np

from algorithms.particle_filter_app.core.robot import move_robot, sense
from algorithms.particle_filter_app.core.particle_filter import *
from algorithms.particle_filter_app.core.adaptive import adapt_particles
from algorithms.particle_filter_app.utils.metrics import compute_uncertainty
from algorithms.particle_filter_app.utils.visualization import plot_state


# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Particle Filter Simulator", layout="wide")


# ---------------------- UI CONTROLS ----------------------
# Sidebar controls allow user to adjust simulation parameters

motion_noise = st.sidebar.slider("Motion Noise", 0.1, 5.0, 1.0)
sensor_noise = st.sidebar.slider("Sensor Noise", 1.0, 20.0, 5.0)
adaptive = st.sidebar.checkbox("Adaptive Particles", True)
speed = st.sidebar.slider("Speed", 0.01, 0.2, 0.05)


# ---------------------- SESSION STATE INIT ----------------------
# Initialize simulation state only once

if "particles" not in st.session_state:
    st.session_state.particles = init_particles(500)          # initial particles
    st.session_state.robot = np.array([50.0, 50.0, 0.0])      # robot state [x, y, theta]
    st.session_state.running = False                          # simulation status


# ---------------------- SIMULATION STEP ----------------------
def step():
    """
    Perform one iteration of the particle filter.

    Steps:
    1. Move robot (ground truth)
    2. Generate sensor measurements
    3. Predict particle states
    4. Update particle weights
    5. Resample particles
    6. Optionally adapt particle count
    """

    # Move robot using motion model
    robot = move_robot(st.session_state.robot)

    # Simulate sensor measurements with noise
    meas = sense(robot, sensor_noise)

    # Particle filter pipeline
    p = predict(st.session_state.particles, motion_noise)   # prediction step
    p = update(p, meas, sensor_noise)                       # weight update
    p = resample(p)                                         # resampling

    # Adaptive particle count (optional)
    if adaptive:
        p = adapt_particles(p)

    # Update session state
    st.session_state.robot = robot
    st.session_state.particles = p


# ---------------------- CONTROL BUTTONS ----------------------

# Start simulation
if st.button("Play"):
    st.session_state.running = True

# Pause simulation
if st.button("Pause"):
    st.session_state.running = False

# Reset simulation
if st.button("Reset"):
    st.session_state.particles = init_particles(500)
    st.session_state.robot = np.array([50.0, 50.0, 0.0])
    st.session_state.running = False


# ---------------------- RUN LOOP ----------------------
# If running, perform one step per render cycle

if st.session_state.running:
    step()


# ---------------------- METRICS ----------------------
# Compute uncertainty of particle distribution

unc = compute_uncertainty(st.session_state.particles)
st.write(f"Uncertainty: {unc:.2f}")


# ---------------------- VISUALIZATION ----------------------
# Plot current state: particles, robot, estimate, landmarks

fig = plot_state(
    st.session_state.particles,
    st.session_state.robot,
    estimate(st.session_state.particles)
)

st.pyplot(fig)


# ---------------------- LOOP CONTROL ----------------------
# Control simulation speed and trigger rerun

time.sleep(speed)
st.rerun()