# 2D Realistic Lightning Simulator

A physics-based 2D lightning simulator that uses mathematical formulas to generate unique, realistic lightning bolts with synchronized visual flashes and audio effects.

## Physics & Mathematics Behind the Simulation

Instead of using purely random lines, this simulator relies on mathematical models to recreate the natural, fractal behavior of an electrical discharge in the atmosphere.

* **Fractal Generation:** The lightning path is generated recursively, breaking down main segments into smaller sub-segments using a displacement algorithm.
* **Probability Vectors:** At each step, the algorithm calculates the next point using a drift vector (forcing the lightning downward) combined with a random Gaussian noise (simulating air resistance and dielectric breakdown).
* **Dynamic Luminosity & Sound:** The intensity of the visual flash and the delay of the sound effect are calculated based on the distance and energy of the bolt, respecting the physics of light propagation vs. sound propagation.

## Features

* **Procedural Generation:** Every single lightning bolt is completely unique.
* **Realistic Visual Flash:** Implements a dynamic screen flash that decays naturally over time, matching real-world observation.
* **Synchronized Audio:** Audio triggers dynamically with adaptive volume based on the bolt's characteristics.
* **Interactive Environment:** Instant generation on user trigger.

## Tech Stack & Concepts Used

* **Language:** Python
* **Libraries:** Pygame, Sys, Random
* **Core Concepts:** Vector mathematics, Recursion, Random distributions, Atmospheric physics.
### Installation
To run the simulator, you need to install Pygame. Open your terminal and type:
pip install pygame
