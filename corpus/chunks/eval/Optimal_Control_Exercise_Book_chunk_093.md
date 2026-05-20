# Trajectory plotting
import matplotlib.pyplot as plt 
```

tau = 0.02 # time of system update
tot_time = tau*len(trajectory)
t = np.linspace(0, tot_time, len(trajectory)) # time

x_traj, xdot_traj, theta_traj, thedot_traj,
    ctrl_traj = [], [], [], [], []

for i in range(len(trajectory)):
    x_traj.append(trajectory[i][0][0])
    xdot_traj.append(trajectory[i][1][0])
    theta_traj.append(trajectory[i][2][0])
    thedot_traj.append(trajectory[i][3][0])
    ctrl_traj.append(controls[i][0][0].item())

fig, ax = plt.subplots(1,1, figsize=(16, 8))
ax.plot(t, x_traj, "k", alpha=.8, label=r' $x(t)$ $m$ ')

ax.plot(t, xdot_traj, "-k", alpha=.8, label=r' $\dot{x}(t)$ $m/s$ ')

ax.plot([0, tot_time], [0, 0], ":b", alpha=.5, label=r'Setpoint')

ax.legend(loc='upper right')

ax.set_xlabel(r'Time [$s]')

ax.set_ylabel(r'Value')

ax.set_title("Position and velocity plot")

fig.savefig('image/pendulum_pos_vel.jpg')

We get the following result: We can see from Figure 2 that the system is able to stabilize both the position and velocity of the system.

Angular position and angular velocity plots Using the following code we obtain

```txt
fig, ax = plt.subplots(1, 1, figsize=(16, 8))
ax.plot(t, theta_traj, "g", alpha=.8, label=r'\(\theta (t)\) \([\$rad$]' ) ax.plot(t, thedot_traj, "-g", alpha=.8, label=r'\(\dot{ \theta } (t)\) \([\$rad/s$]' ) ax.plot([0, tot_time], [0, 0], ":b", alpha=.5, label=r'Setpoint') ax.legend(loc='upper right') ax.set_xlabel(r'Time [\$s$]' ) ax.set_ylabel(r'Value') ax.set_title("Angular position and angular velocity plot") fig.savefig('image/pendulum_angular_pos_vel.jpg') ``` We can infer from Figure 3 that the system is able to stabilize both the angular position and angular velocity of the system and that their values are indeed very close to 0.
