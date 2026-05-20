# EXAMPLE 2.14 Closed-loop estimation

Example 2.10 showed that identifiability can be lost owing to feedback. The

![](image/1b1d1c485eb21232991c70dbb6027d670b7b2ebfd7ceab80ffea2d0ba76de7f1.jpg)

<details>
<summary>other</summary>

| â | b̂ |
| --- | --- |
| -1.8 | 0.5 |
| -1.2 | 0.3 |
| -0.6 | 0.7 |
| 0.0 | 1.0 |
| 0.4 | 0.8 |
| 0.8 | 0.6 |
| -1.6 | -0.5 |
| -1.0 | -0.3 |
| -0.4 | -0.7 |
| 0.2 | -0.9 |
| 0.6 | -0.6 |
| 1.0 | -0.3 |
| -1.4 | -1.1 |
| -0.8 | -1.3 |
| 0.2 | -1.0 |
| 0.6 | -0.8 |
| 1.0 | -0.5 |
</details>

Figure 2.10 Phase plane of the estimates when the system (2.53) is simulated for different initial conditions when $u(t) = -0.2y(t)$ . The dashed line shows the identifiable subspace. The dot shows the true parameter values.

estimates when the input is generated through the feedback

$$u (t) = - 0. 2 y (t)$$

are shown in Fig. 2.9(a). The estimates converge to the wrong values. Notice, however, that the estimates are on the straight line (2.51). In Fig. 2.9(b) the feedback is more complex:

$$u (t) = - 0. 3 2 y (t - 1)$$

The two control laws give approximately the same speed and output variance of the closed-loop system. Identifiability is now regained, and the estimates converge to the correct values. The phase plane, that is, $\hat{b}$ as a function of $\hat{a}$ , is shown in Fig. 2.10 for different initial conditions when $u(t) = -0.2y(t)$ . The initial value of the $P$ -matrix is $P(0) = 0.01I$ , and 20,000 steps have been simulated for each initial condition. The estimates converge to the identifiable subspace determined by

$$\hat {a} + 0. 2 \hat {b} + 0. 7 = 0$$

(Compare Eq. (2.51).) This line is dashed in the phase plane. The estimates are approaching the identifiable subspace along straight lines. The same initial conditions are simulated for the control law $u(t) = -0.32y(t - 1)$ in Fig. 2.11. The estimates converge to the correct value $(-0.8, 0.5)$ , independent of the initial values.

![](image/c0a2e4c820390e29e773d4c722bdf1d537cfcdf73d20e845989ed5d80ac39122.jpg)

<details>
<summary>line</summary>

| â | b̂ |
| --- | --- |
| -2 | ~0.5 |
| -1 | ~0.3 |
| 0 | ~-0.5 |
| 1 | ~-0.3 |
</details>

Figure 2.11 Phase plane of the estimates when the system (2.53) is simulated for different initial conditions when $u(t) = -0.32y(t-1)$ . The dot shows the true parameter values.
