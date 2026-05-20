# Example 7.9 (dc Servo)

The dc servo of Example 2.1 (Chapter 2) is subjected to a load-torque disturbance $T_{L}(t)=0.01e^{-t}u_{-1}(t)$ . (This could model, for instance, a gust of wind acting on an antenna positioned by the motor.)

As in Example 7.6, the system is linearized about the steady state $\theta = \theta_{d}, \omega = i = v = 0$ . Compute the optimal LQ control for the performance index:

$$J = \int_ {0} ^ {\infty} [ 9 (\theta - \theta_ {d}) ^ {2} + v ^ {2} ] d t.$$

Solution The equations are Equation 2.19 (Chapter 2) for the system states, and additional equations

$$\dot {z} = - zT _ {L} = z$$

for the disturbance state. Combining the two sets yields

$$
\frac {d}{d t} \left[ \begin{array}{l} e \\ \omega \\ i \\ z \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 4. 4 3 8 & - 7. 3 9 6 \\ 0 & - 1 2 & - 2 4 & 0 \\ 0 & 0 & 0 & - 1 \end{array} \right] \left[ \begin{array}{l} e \\ \omega \\ i \\ z \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ 2 0 \\ 0 \end{array} \right] v
$$

where, as in Example 7.6, $e = \theta - \theta_d$ .

The $Q$ and $R$ matrices are

$$
Q = \operatorname{diag} \left[ \begin{array}{c c c c} 9 & 0 & 0 & 0 \end{array} \right]; \quad R = 1.
$$

The optimal gain $K = [3 \quad 0.8796 \quad 0.1529 \quad -1.8190]$ (MATLAB 1qr). Figure 7.17 shows the response to the torque disturbance $T_{L} = 0.01e^{-t}u_{1}(t)$ , from the initial state $e = \omega = i = 0$ . [To obtain $T_{L}(t)$ as specified, $z(0) = 0.01$ ]. The response to this disturbance without feedforward—i.e., with only plant state feedback—is also shown. Note that the gains assigned to the first three states are identical to those of Example 7.6. As Problem 7.27 will explore, this is not a coincidence.

![](image/a2a2c4db84402cc6380bfa35b61ee7ed4c6df8924bd6bc8073d407d79e7c166f.jpg)

<details>
<summary>line</summary>

| Time(s) | No Feedforward | Feedforward |
| --- | --- | --- |
| 0.0 | 0.0000 | 0.0000 |
| 0.5 | 3.5e-3 | 1.0e-3 |
| 1.0 | 4.5e-3 | 0.9e-3 |
| 1.5 | 3.0e-3 | 0.5e-3 |
| 2.0 | 1.5e-3 | 0.3e-3 |
| 2.5 | 1.0e-3 | 0.2e-3 |
| 3.0 | 0.7e-3 | 0.1e-3 |
</details>

Figure 7.17 Response to a load torque input with and without feedforward, dc servo
