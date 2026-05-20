# 6.10.3 Simulation

Python Control will be used to discretize the model and simulate it. One of the frccontrol examples[10] creates and tests a controller for it. Figure 6.5 shows the closed-loop system response.

Notice how the control effort when the reference is reached is nonzero. This is a plant inversion feedforward compensating for the system dynamics attempting to slow the flywheel down when no voltage is applied.
