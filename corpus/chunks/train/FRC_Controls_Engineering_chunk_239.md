# Simulation

Python Control will be used to discretize the model and simulate it. One of the frccontrol examples[3] creates and tests a controller for it. Figure 8.3 shows the closed-loop system response.

Given the high inertia in drivetrains, it’s better to drive the reference with a motion profile instead of a step input for reproducibility.
