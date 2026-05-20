# Example 6.2 (dc Servo)

The dc servo of Example 2.1 (Chapter 2) is controlled by a 1-DOF control system, with a controller $F(s) = k$ . Calculate the steady-state error for a unit-step reference input $\theta_{d}$ and for a unit step in the load torque $T_{L}$ , assuming stability of the closed-loop system.

Solution From Equation 3.21 (Chapter 3), the loop gain is

$$L (s) = \frac {8 8 . 7 6 k}{s (s + 2 1 . 5 7 6) (s + 2 . 4 7 4)}.$$

The system is of Type 1, and the steady-state error to a step input is zero. From Equation 3.22 (Chapter 3),

$$\frac {\theta}{T _ {L}} = \frac {- 7 . 3 9 6 (s + 2 4)}{s (s + 2 1 . 5 7 6) (s + 2 . 4 7 4)}.$$

For a unit step in $T_{L}$ , the disturbance referred to the output—i.e., the effect on $\theta$ of $T_{L}$ by itself—is

$$
\begin{array}{l} d (s) = \frac {- 7 . 3 9 6 (s + 2 4)}{s ^ {2} (s + 2 1 . 5 7 6) (s + 2 . 4 7 4)} \\ = - \left(\frac {3 . 3 2 5}{s ^ {2}} + \frac {A}{s} + \frac {B}{s + 2 1 . 5 7 6} + \frac {C}{s + 2 . 4 7 4}\right) \\ d (t) = - 3. 3 2 5 t u _ {- 1} (t) + A u _ {- 1} (t) + B e ^ {- 2 1. 5 7 6 t} + C e ^ {- 2. 4 7 4 t}. \\ \end{array}
$$

In the steady state, the contributions of the two stable poles disappear. Because the system is of Type 1, the step component A/s contributes 0 to $e_{ss}$ . That leaves the ramp component. By Equation 6.9,

$$e _ {\text { ramp }} = - \frac {3 . 3 2 5}{k _ {v}}$$

where

$$
\begin{array}{l} k _ {v} = \lim _ {s \rightarrow 0} s L (s) = \frac {8 8 . 7 6 k}{(2 1 . 5 7 6) (2 . 4 7 4)} \\ = 1. 6 6 3 k. \\ \end{array}
$$

Therefore,

$$e _ {\text { ramp }} = \frac {- 3 . 3 2 5}{1 . 6 6 3 k} = \frac {- 2 . 0 0 0}{k}.$$

That is the steady-state error for a unit step in $T_{L}$ . Note that, in this example, the physical signal $T_{L}$ is a step, but the disturbance referred to the output has a ramp component.
