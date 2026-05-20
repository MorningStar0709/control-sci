# Example 3.13 Steady-state errors for step and ramp inputs

Consider the system

$$y (k) = H (q) u (k) = \frac {q - 0 . 5}{(q - 0 . 8) (q - 1)} u (k)$$

Closing the system, as in Fig. 3.5, gives

$$e (k) = \frac {(q - 0 . 8) (q - 1)}{(q - 0 . 8) (q - 1) + q - 0 . 5} u _ {c} (k)$$

Assume that $u_{c}$ is a unit step. Because the closed-loop system is stable, the final-value theorem can be used to show that the steady-state error is zero. This can be seen simply by putting q = 1. Another way is to observe that the open-loop system contains one integrator, that is, a pole in +1. If $u_{c}$ is a unit ramp, use Table 2.3 in Sec. 2.7 to find the z-transform of the ramp. The steady-state error is then given by

$$\lim _ {k \rightarrow \infty} e (k) = \lim _ {z \rightarrow 1} \frac {(z - 0 . 8) (z - 1)}{(z - 0 . 8) (z - 1) + z - 0 . 5} \cdot \frac {z (1 - z ^ {- 1})}{(z - 1) ^ {2}} = 0. 4$$
