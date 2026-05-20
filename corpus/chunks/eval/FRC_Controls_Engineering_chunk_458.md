# 17.3 Model predictive control

If we can optimize trajectories quickly enough, then we can use trajectory optimization as a feedback policy that reacts better to future events (e.g., nonlinear system dynamics subject to control input limits, keep-out regions). At each timestep, we optimize a trajectory from the current state out to a prediction horizon, then apply the first control input from the optimized trajectory. This is called model predictive control (MPC).

Since we formulate trajectory optimization problems over a finite horizon, we can think of each optimization as reasoning about the next N timesteps. To optimize performance over a longer horizon than N, we can continue solving for an N-step horizon at each timestep. For this reason, MPC is also called receding horizon control.
