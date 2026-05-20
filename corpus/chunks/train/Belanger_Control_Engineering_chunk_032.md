To apply Equation 2.14, we need the current, i. By Kirchhoff's voltage law,

$$L \frac {d i}{d t} + R i = v - K _ {m} \omega_ {m}$$

where $K_{m}\omega$ is the back emf. This becomes

$$\dot {i} = - \frac {R}{L} i + \frac {\nu}{L} - \frac {N K _ {m}}{L} \omega \tag {2.15}$$

where the fact that $\omega_{m} = N\omega$ has been used. Because the angle $\theta$ is of interest, the definition equation

$$\dot {\theta} = \omega \tag {2.16}$$

is added. Equations 2.14, 2.15, and 2.16 are the desired equations. In matrix form,

$$
\frac {d}{d t} \left[ \begin{array}{l} \theta \\ \omega \\ i \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & \frac {N K _ {m}}{J _ {e}} \\ 0 & - \frac {N K _ {m}}{L} & - \frac {R}{L} \end{array} \right] \left[ \begin{array}{l} \theta \\ \omega \\ i \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & - \frac {1}{J _ {e}} \\ \frac {1}{L} & 0 \end{array} \right] \left[ \begin{array}{l} v \\ T _ {L} \end{array} \right]. \tag {2.17}
$$

Since $\theta$ and $\omega$ have been specified as the outputs, the output equation is

$$
\left[ \begin{array}{l} \theta \\ \omega \end{array} \right] = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} \theta \\ \omega \\ i \end{array} \right]. \tag {2.18}
$$

For the specific values $K_{m} = .05$ Nm/A, $R = 1.2 \Omega$ , $L = .05$ H, $J_{m} = 8 \times 10^{-4}$ kg m $^{2}$ , $J = 0.020$ kg m $^{2}$ , and N = 12, the state equations are

$$
\frac {d}{d t} \left[ \begin{array}{c} \theta \\ \omega \\ i \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 4. 4 3 8 \\ 0 & - 1 2 & - 2 4 \end{array} \right] \left[ \begin{array}{c} \theta \\ \omega \\ i \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & - 7. 3 9 6 \\ 2 0 & 0 \end{array} \right] \left[ \begin{array}{c} v \\ T _ {L} \end{array} \right]. \tag {2.19}
$$

The simulation conditions are as follows: with zero initial conditions and $T_{L}=0$ , $v(t)=3\ V$ for $0\leq t\leq2$ and -3 V for $2<t\leq4$ . The result (MATLAB command lsim) is shown in Figure 2.3.

![](image/e742f4eae1c30f4d4a26a7791daeb78d88352b2a86af0c3e784c50e526809ec4.jpg)

<details>
<summary>line</summary>

| Time(s) | θ (rad) | ω (rad/s) | i (A) |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 |
| 0.5 | 1.0 | 3.0 | 1.0 |
| 1.0 | 3.0 | 4.0 | 0.5 |
| 1.5 | 5.0 | 4.5 | 0.0 |
| 2.0 | 8.0 | 5.0 | -4.0 |
| 2.5 | 9.0 | -2.0 | -2.0 |
| 3.0 | 7.0 | -4.0 | -1.0 |
| 3.5 | 5.0 | -4.5 | -0.5 |
| 4.0 | 2.5 | -5.0 | -0.5 |
</details>

Figure 2.3 Time responses for the dc servo
