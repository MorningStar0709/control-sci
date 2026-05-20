# EXAMPLE 1.5 Concentration control

Consider concentration control for a fluid that flows through a pipe, with no mixing, and through a tank, with perfect mixing. A schematic diagram of the process is shown in Fig. 1.10. The concentration at the inlet of the pipe is $c_{in}$ . Let the pipe volume be $V_{d}$ and let the tank volume be $V_{m}$ . Furthermore, let the flow be q and let the concentration in the tank and at the outlet be c. A mass balance gives

$$V _ {m} \frac {d c (t)}{d t} = q (t) \left(c _ {i n} (t - \tau) - c (t)\right) \tag {1.3}$$

where

$$\tau = V _ {d} / q (t)$$

![](image/bc8ed1551fc745956a31884ba69ef0d8fb5b85026362ff6db0efb85143d805ba.jpg)

<details>
<summary>text_image</summary>

V_d
c_in
V_m
c
</details>

Figure 1.10 Schematic diagram of a concentration control system.

Introduce

$$T ^ {\prime} = V _ {m} / q (t) \tag {1.4}$$

For a fixed flow, that is, when $q(t)$ is constant, the process has the transfer function

$$G _ {0} (s) = \frac {e ^ {- s \tau}}{1 + s T} \tag {1.5}$$

The dynamics are characterized by a time delay and first-order dynamics. The time constant T and the time delay $\tau$ are inversely proportional to the flow q.

The closed-loop system is as in Fig. 1.8 with $f(\cdot) = 1$ and $G_0(s)$ given by Eq. (1.5). A controller will first be designed for the nominal case, which corresponds to $q = 1$ , $T = 1$ , and $\tau = 1$ . A PI controller with gain $K = 0.5$ and integration time $T_i = 1.1$ gives a closed-loop system with good performance in this case. Figure 1.11 shows the step responses of the closed-loop system for different flows and the corresponding control actions. The overshoot will increase with decreasing flows, and the system will become sluggish when the flow increases. For safe operation it is thus good practice to tune the controller at the lowest flow. Figure 1.11 shows that the system can easily cope with a flow change of $\pm 10\%$ but that the performance deteriorates severely when the flow changes by a factor of 2.

Variations in speed give rise to similar problems. This happens for example in rolling mills and paper machines.
