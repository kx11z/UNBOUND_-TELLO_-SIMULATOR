# tello_sim — Tello Flight Simulator with Real-Time 3D Visualization

A simulator for dry-running [DJI Tello](https://www.ryzerobotics.com/tello) drone
commands in Python 3. Plan a flight in code, watch the drone fly its path in a
**live, interactive 3D plot**, and — when you're happy with it — deploy the exact
same command sequence to a real Tello over Wi-Fi.

The command set mirrors the Tello SDK via
[easyTello](https://github.com/Virodroid/easyTello), so what you simulate is what
the real drone runs.

## Features

- **Live 3D flight view** — the drone animates from waypoint to waypoint in real
  time as each command runs.
- **Interactive plot** — click-drag to rotate the 3D scene, scroll to zoom. The
  view angle you set is preserved across the animation.
- **Auto-expanding axes** — the plot starts at a comfortable window and grows
  automatically so the drone is never drawn off the graph, no matter how far it flies.
- **Save / load flights** — persist a flight plan to JSON and replay it later.
- **Deploy to a real Tello** — send the simulated command log to an actual drone.

## Installation

Requires **Python 3**. Install the dependencies:

```bash
pip install pandas matplotlib easytello
```

Or install the package itself (from the repo root):

```bash
pip install .
```

On headless Linux you may also need the system OpenGL library (see `apt.txt`):

```bash
sudo apt-get install libgl1-mesa-glx
```

## Quick start

```python
from tello_sim import Simulator

d = Simulator()

d.takeoff()
d.forward(100)   # fly forward 100 cm
d.ccw(90)        # rotate 90° counter-clockwise
d.flip("l")      # flip left
d.forward(100)
d.land()

d.show()         # hold the 3D plot open — click-drag to rotate, scroll to zoom
```

Run it as a script so you get an interactive GUI window:

```bash
python main.py
```

> **Note:** Interactive rotation requires a GUI backend (MacOSX / Tk / Qt), which
> you get automatically when running a `.py` script. If a window doesn't appear,
> install a backend such as `pip install PyQt5`.

### Using it in a Jupyter notebook

The default inline backend renders static images you can't rotate. Enable an
interactive backend **before** flying:

```python
%matplotlib widget      # or: %matplotlib notebook
from tello_sim import Simulator
...
```

## Command reference

All distances are in **centimeters** and all angles in **degrees**.

| Command | Description |
| --- | --- |
| `takeoff()` | Take off (to ~81 cm). |
| `land()` | Land. |
| `up(dist)` / `down(dist)` | Change altitude. |
| `forward(dist)` / `back(dist)` | Move along the current heading. |
| `left(dist)` / `right(dist)` | Strafe sideways. |
| `cw(deg)` / `ccw(deg)` | Rotate clockwise / counter-clockwise. |
| `flip(direc)` | Flip `"f"`, `"b"`, `"l"`, or `"r"`. |
| `show()` | Keep the 3D plot open and interactive (call last; blocks until closed). |

### Plotting

- `plot_3d_path()` — static 3D plot of the full flight path.
- `plot_horz_steps(e)` — top-down 2D path (X/Y).
- `plot_altitude_steps(e)` — altitude over each step.

`e` controls the width of the faint "error tube" / error bar drawn around the path.

## Saving, loading, and replaying flights

Every command you issue is recorded. Save the plan to JSON and load it back later:

```python
d.save("my_flight.json")     # write the command log

d2 = Simulator()
d2.load_commands("my_flight.json")   # replay the whole flight
```

A command file is a list of `{"command": ..., "arguments": [...]}` objects — see
[`commands.json`](commands.json) for an example.

Reset the simulator back to the starting state at any time:

```python
d.reset()
```

## Deploying to a real Tello

Connect your computer to the drone's Wi-Fi network, then:

```python
d.deploy()   # sends the recorded command log to a real Tello via easyTello
```

## License

MIT. Based on the original
[Fireline-Science/tello_sim](https://github.com/Fireline-Science/tello_sim).
