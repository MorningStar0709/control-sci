# Example 7.15 (dc Servo)

In Example 7.9, a state feedback law was worked out for the dc servo subjected to an exponential load-torque disturbance. An observer-based regulator is to be designed for the system, with the angle being the only measurement.

(a) Design a full-order observer with error-system eigenvalues at $-5 \pm j5$ and $-7 \pm j7$ .   
(b) The load torque $0.01e^{-t}$ is applied at $t = 0$ when $\theta = \theta_d$ and $\omega = i = 0$ . Compute and compare the responses of (i) the state feedback control system and (ii) the response of the observer-based control system, with all observer states initially at zero.   
(c) Compute the controller transfer function.

Solution From Example 7.9, the state feedback gain is

$$
K = \left[ \begin{array}{l l l l} 3 & 0. 8 7 9 6 & 0. 1 5 2 9 & - 1. 8 1 9 0 \end{array} \right].
$$

(a) In Example 7.12, an observer design was worked out for this system, but for a constant load-torque input. It is reworked for this exponential torque ( $e^{-t}$ ). The observer gain is

$$
G = \left[ \begin{array}{c} - 1 \\ 2 6 5. 7 \\ - 1 1 2. 7 \\ - 2 0. 6 6 \end{array} \right].
$$

(b) Simulations for the load torque $-0.01e^{-t}$ are shown in Figure 7.25. Not surprisingly, the performance is better when the full state is directly available.

(c) The controller transfer function is computed from Equations 7.90 and 7.91:

$${\frac {u}{e}} = {\frac {9 2 . 8 (s + 2 1 . 6) (s + 2 . 4 3 8 \pm j 1 . 1 7 0 3)}{(s + 1 . 3 3 2) (s + 1 1 . 4 7) (s + 7 . 1 2 7 \pm j 1 2 . 1 4)}}.$$

![](image/109aa255f845e5d4c0718b496d9272f5ed86e2c50da18fc1e68795d91eac0794.jpg)

<details>
<summary>line</summary>

| Time(s) | State feedback (rad ×10⁻³) | Observed state feedback (rad ×10⁻³) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | -1.0 | -4.5 |
| 1.0 | -0.5 | -3.0 |
| 1.5 | 0.0 | -2.0 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.0 | 0.0 |
| 3.0 | 0.0 | 0.0 |
</details>

Figure 7.25 Responses for state feedback and observer-based feedback, dc servo
