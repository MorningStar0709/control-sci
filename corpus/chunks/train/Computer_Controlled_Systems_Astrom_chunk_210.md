# Example 3.15 Controller-induced hidden oscillation

The double integrator previously used in this section can be used to show how a controller may introduce hidden oscillations. The model of (3.25) can be written as the difference equation

$$y (k) = 2 y (k - 1) - y (k - 2) + 0. 5 u (k - 1) + 0. 5 u (k - 2)$$

![](image/307dd4ec13a4622f86f616fbd9819a9df4148e3f3f51ecd491d604878b59200b.jpg)  
Figure 3.19 Step response of the system in Example 3.14. (a) Continuous-time (solid line) and sampled output (dots) when (a) h = 2; (b) h = 1.8.

Let the purpose of the control be to follow the reference trajectory $u_{r}(k)$ . If the control signal is chosen such that the right-hand side is equal to the reference value at time k - 1, the following causal controller is obtained:

$$u (k) = \frac {2 q}{q + 1} u _ {c} (k) - \frac {2 (2 q - 1)}{q + 1} y (k) \tag {3.30}$$

The closed-loop system is given by

$$
\begin{array}{l} y (k) = \frac {q (q - 1)}{(q + 1) (q ^ {2} - 2 q + 1 - (- 2 q + 1))} u _ {c} (k) \\ = \frac {q (q + 1)}{q ^ {2} (q + 1)} u _ {c} (k) = u _ {c} (k - 1) \\ \end{array}
$$

The output is equal to the reference value after one step. By using the controller in (3.27) with K = 1 and $T_{d} = 1.5$ , it took two steps. The step response and the control signal when using the control law (3.30) are shown in Fig. 3.20. At the sampling points, the system has the desired performance, but there is an oscillation in the continuous-time output. This hidden oscillation is caused by the oscillation in the control signal. It is thus important to simulate a system in order to investigate the behavior between the sampling points.

The closed-loop system is of third order, the process has two modes, and the controller has one mode. The zero on the stability boundary is canceled by a pole. This mode is not observable in the closed-loop discrete-time system. This means that observability of the closed-loop system has been lost by an improper choice of the controller.

To summarize, there are no hidden oscillations if the unobservable open-loop modes are not oscillatory and if unstable or poorly damped process zeros are not canceled by the regulator.

![](image/dcf46a29d0b1daba2b6dac1c2ffd86ada38a1340312544665a7d130b2023bd99.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 2 |
| 1 | 1 | -4 |
| 2 | 0 | 4 |
| 3 | 1 | -4 |
| 4 | 0 | 4 |
| 5 | 1 | -4 |
| 6 | 0 | 4 |
| 7 | 1 | -4 |
| 8 | 0 | 4 |
| 9 | 1 | -4 |
| 10 | 0 | 4 |
</details>

Figure 3.20 The step response and the control signal of the double integrator when the controller of (3.30) is used.
