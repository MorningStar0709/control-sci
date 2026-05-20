0.02s self.A = A self.B = B self.C = C self.D = D ``` ```python # Simulate next step def step(self, u): dx = A * self.x + B * u self.x += dx * self.dt # x_{t+1} = x_t + dx * dt output = C * self.x + D * u return self.x, output # Reset to initial position def reset(self, x_initial = np.matrix(np.random.uniform(-0.1, 0.1, size=6)).T): self.x = x_initial return self.x ``` We set as initial condition the following x0 with the Numpy’s random function generator: ```python # Declare model model = ControlledBoeing747(A, B, C, D) # Initial condition x0 = np.matrix(np.random.uniform(-0.5, 0.5, size=6)).T model.reset(x_initial=x0) ``` and then we run for 1000 time steps, equivalent to a simulation of 20 seconds: ```python # Save trajectory for the graph trajectory_state = [] trajectory_outputs = [] controls = [] # Control loop (each loop is 0.02s of simulation) for i in range(1000): u = -K*x # the control input is u* = -Kx x, y = model.step(u) # propagate trajectory_state.append(x) trajectory_outputs.append(y) controls.append(u) ``` Output plot We use the following functions to get the plot: ```python # Trajectory plotting import matplotlib.pyplot as plt tau = 0.02 # time of system update tot_time = tau * len(trajectory_outputs) t = np.linspace(0, tot_time, len(trajectory_outputs)) # time y, u = [], [] for i in range(len(trajectory_outputs)): y.append(trajectory_outputs[i].item()) u.append(controls[i].item()) fig, ax = plt.subplots(1, 1, figsize=(16, 8)) ax.plot(t, y, "k", alpha=.8, label=r'\(y(t)\)\')
ax.plot([0, tot_time], [0, 0], ":b", alpha=.5, label=r'Setpoint')
ax.legend(loc='upper right')
ax.set_xlabel(r'Time [$s]\)')
ax.set_ylabel(r'Value')
ax.set_title("Output \(y(t)\) plot")
fig.savefig('image/boeing_output.jpg') 
```

![](image/018ec83372be0486c0c5fec60cabc5c103cf1f80ca1d5158231a8715525dec6f.jpg)

<details>
<summary>line</summary>

| Time [s] | y(t) |
| --- | --- |
| 0.0 | 0.20 |
| 2.5 | -0.07 |
| 5.0 | -0.02 |
| 7.5 | 0.02 |
| 10.0 | 0.00 |
| 12.5 | -0.01 |
| 15.0 | -0.01 |
| 17.5 | -0.01 |
| 20.0 | -0.01 |
</details>

Control input plot We use the following code for plotting the control input:

fig, ax = plt.subplots(1, 1, figsize=(16, 8))
ax.plot(t, u, "r", alpha=.8, label=r' $u(t)$ ')

ax.plot([0, tot_time], [0, 0], ":b", alpha=.5, label=r'Setpoint')
ax.legend(loc='upper right')
ax.set_xlabel(r'Time [ $s$ ]')
