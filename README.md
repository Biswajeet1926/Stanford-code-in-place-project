# Battlefield Car Avoidance Game

A simple 3D car avoidance game built with the Ursina Engine. You control a car on a straight track and must dodge oncoming cars. If you collide, your car spins out, then resets.

---

## Table of Contents

1. [Features](#features)
2. [Demo](#demo)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Controls](#controls)
7. [File Structure](#file-structure)
8. [Game Mechanics](#game-mechanics)
9. [Assets](#assets)
10. [Troubleshooting](#troubleshooting)

---

## Features

* 3D environment with a textured track
* Player car that you can move left/right
* Four oncoming cars with randomized speeds and spawning positions
* Continuous track scrolling illusion
* Collision detection: on impact, the player car spins before resetting

---

## Demo

![image alt](https://github.com/Biswajeet1926/Stanford-code-in-place-project/blob/main/Race-Cars/assets/Screenshot%202025-06-02%20144507.png?raw=true)


---

## Prerequisites

* **Python 3.7+**
* **Ursina Engine**
* An environment that supports OpenGL (most modern Windows/macOS/Linux machines)

---

## Installation

1. **Clone or download this repository**

   ```bash
   git clone https://github.com/your-username/ursina-car-avoidance.git
   cd ursina-car-avoidance
   ```

2. **Create (and activate) a Python virtual environment** *(recommended)*

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install Ursina**

   ```bash
   pip install ursina
   ```

4. **Verify that you have the required assets**
   Make sure there is an `assets/` folder next to `squid.py` containing:

   * `track.png` (texture for the ground)
   * `car0.png` (player car)
   * `car1.png`, `car2.png`, `car3.png`, `car4.png` (oncoming cars)

---

## Usage

1. **Navigate to the project folder** (if you haven’t already)

   ```bash
   cd ursina-car-avoidance
   ```
2. **Run the game script**

   ```bash
   python squid.py
   ```
3. The game window will open. Use **A** / **D** (or **Left** / **Right** arrows) to move your car left and right. Dodge the oncoming cars on the track.

---

## Controls

* **Move Left:** `A` or `←`
* **Move Right:** `D` or `→`

No other inputs are required—your car automatically drives forward, and opponents continuously approach.

---

## File Structure

```

Race-Cars/
├── assets/
│   ├── car0.png        # Player’s car
│   ├── car1.png        # Enemy car #1
│   ├── car2.png        # Enemy car #2
│   ├── car3.png        # Enemy car #3
│   ├── car4.png        # Enemy car #4
│   └── track.png       # Ground texture for the track
├── race_cars.py        # Main game script (Ursina)
└── README.md           # This is readme file
```

* **`assets/`**
  Contains all PNG assets used by the game. Each car image should face upward (north) in its source file, since the code rotates them as needed.

* **`squid.py`**
  The single Python file containing the entire game logic (initialization, update loop, entity definitions, collision handling, etc.)

---

## Game Mechanics

1. **Track Scrolling**

   * The track is a long, flat cube with a repeating texture (`track.png`).
   * In each update, the texture’s vertical offset is increased, creating an illusion of forward motion.

2. **Player Car**

   * Instance of the `Car` class with a texture `car0.png`.
   * Can move horizontally between two boundaries (`x` in \[–0.28, +0.24]).
   * If it collides with any oncoming car, a `collision` flag is set and the car spins 360° around its Y-axis, then resets.

3. **Oncoming Cars**

   * Four instances of `Car` (with `car1.png` … `car4.png`), each placed at different initial `x` and `z` positions.
   * Each car chooses a random downward speed every frame. Cars facing “forward” (rotation\_y = 0) move slower; cars facing “backward” (rotation\_y = 180) move faster.
   * When an oncoming car’s `z` position goes below –0.3 (off the bottom), it is teleported back up to `z = +0.4`, repeating the approach loop.

4. **Collision Detection**

   * In each update, the code checks horizontal (`x`) and depth (`z`) distances between the player car and every oncoming car.
   * If both `|x₁ − x₂| < 0.05` and `|z₁ − z₂| < 0.05`, a collision has occurred.
   * Upon collision, the player’s `rotation_y` is incremented rapidly (spin). Once a full 360° is reached, `rotation_y` resets to 0 and the `collision` flag clears.

---

## Assets

* **`assets/car0.png`**

  * Player’s car sprite (recommended size: 40×40 px), facing **upwards**.

* **`assets/car1.png`, `car2.png`, `car3.png`, `car4.png`**

  * Oncoming car sprites (recommended size: 35×35 px), each also created facing **upwards**.
  * In code, `rotation_y` is set to 0 or 180 so they appear to drive toward the player.

* **`assets/track.png`**

  * A repeating ground texture. Should look like a road or racing track, at least 512×512 px (the code will tile/scale it).

> **Tip:** If your assets aren’t exactly the recommended dimensions, you can still use them—just adjust the constants `PLAYER_WIDTH`, `PLAYER_HEIGHT`, `ENEMY_WIDTH`, and `ENEMY_HEIGHT` at the top of `squid.py` to match your PNG sizes.

---

## Troubleshooting

* **`ModuleNotFoundError: No module named 'ursina'`**

  * Make sure you installed Ursina in the same Python environment where you’re running `squid.py`.
  * If you have multiple Python versions, run:

    ```bash
    python3 -m pip install ursina
    ```
  * Verify your IDE’s interpreter matches the one where Ursina is installed.

* **Assets not found / texture errors**

  * Ensure the `assets/` folder is in the same directory as `squid.py`.
  * Double-check capitalization/spelling of file names (`car0.png`, `track.png`, etc.).
  * Paths in `squid.py` assume `assets/` is a sibling folder. If you move files, update the strings accordingly.

* **Car positions “too big” or “too small”**

  * The code uses normalized coordinates (e.g. `x` in \[–1..+1], `z` in \[–1..+1]). If your track or camera settings change, you may need to tweak camera position (`camera.position`) or scale values for cars/track.

---

### Enjoy the Game!

Feel free to experiment—swap in different car textures, adjust speeds, change camera angles, or add new features (power-ups, sound effects, multiple lanes). Ursina makes it easy to iterate rapidly. Have fun building and playing!
