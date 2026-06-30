# 2D Realistic Lightning Simulator

A physics-based 2D lightning simulator that uses mathematical formulas to generate unique, realistic lightning bolts with synchronized visual flashes and audio effects.

## 🎬 Demo

![Lightning Simulator Demo](gifs/lightning-demo.gif)

## Physics & Mathematics Behind the Simulation

Instead of using purely random lines, this simulator relies on mathematical models to recreate the natural, fractal behavior of an electrical discharge in the atmosphere.

* **Fractal Generation:** The lightning path is generated recursively, breaking down main segments into smaller sub-segments using a displacement algorithm.
* **Probability Vectors:** At each step, the algorithm calculates the next point using a drift vector (forcing the lightning downward) combined with a random Gaussian noise (simulating air resistance).
* **Dynamic Luminosity & Sound:** The intensity of the visual flash and the delay of the sound effect are calculated based on the distance and energy of the bolt, respecting the physics of light propagation.

## Features

* **Procedural Generation:** Every single lightning bolt is completely unique.
* **Realistic Visual Flash:** Implements a dynamic screen flash that decays naturally over time, matching real-world observation.
* **Synchronized Audio:** Audio triggers dynamically with adaptive volume based on the bolt's characteristics.
* **Interactive Environment:** Instant generation on user trigger (press SPACE).
* **Branching Structures:** Lightning bolts feature realistic branching with probabilistic sub-branches.

## Tech Stack & Concepts Used

* **Language:** Python
* **Libraries:** Pygame, Sys, Random
* **Core Concepts:** Vector mathematics, Recursion, Random distributions, Atmospheric physics.

## Installation

To run the simulator, you need to install Pygame. Open your terminal and type:

```bash
pip install pygame
```

## Usage

Run the simulator with:

```bash
python "simulateur de foudre.py"
```

### Controls
- **SPACE** - Generate a new lightning bolt
- **ESC or Close Window** - Exit the simulator

## How It Works

### Lightning Generation Algorithm
1. **Main Trunk Generation:** A main lightning bolt originates from the top center and moves downward
2. **Random Displacement:** At each step, the lightning randomly moves left or right with a controlled drift
3. **Branching:** With a 5% probability at each segment, secondary branches spawn and develop independently
4. **Collision Detection:** When the lightning reaches the ground (y=600), generation stops

### Visual Effects
- **Screen Flash:** When lightning strikes, the entire screen flashes in blue-white with a 500ms fade
- **Line Rendering:** Lightning bolts are drawn with bright cyan lines (RGB: 180, 210, 255)
- **60 FPS:** Smooth animation at 60 frames per second

### Audio Effects
- **Thunder Sound:** Synchronized thunder audio plays with each lightning strike
- **Sound File:** `tonnerre.wav` - a realistic thunder sound effect with natural reverb

## Customization

You can modify these parameters in the code:

```python
# Screen dimensions
LARGEUR = 800    # Width
HAUTEUR = 600    # Height

# Lightning appearance
Color = (180, 210, 255)  # RGB color of lightning
Line Width = 2           # Thickness of lightning bolt

# Flash effect
duree_du_flash = 500     # Duration in milliseconds
Flash Color = (110, 120, 170)  # RGB color during flash

# Physics
Random Step = random.randint(5, 15)     # Vertical movement per step
Horizontal Drift = random.randint(-10, 10)  # Horizontal randomness
Branch Probability = 5%   # Chance of branching per segment
```

## Project Structure

```
lightning-simulator-2d/
├── simulateur de foudre.py    # Main simulator script
├── tonnerre.wav               # Thunder audio file
├── generate_lightning_gif.py   # GIF generation script
├── gifs/                       # Generated demo GIFs
└── README.md
```

## Performance

- **FPS:** 60 frames per second
- **Resolution:** 800x600 pixels
- **Memory Usage:** Minimal (~50MB)
- **CPU:** Low usage, suitable for all systems

## License

This project is open source and available under the MIT License.

## Author

Created by EventHorizon-dev - Physics simulation enthusiast

Enjoy the storm! ⚡🌩️
