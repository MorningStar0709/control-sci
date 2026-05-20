# Computational Delay

Because the analog-to-digital (A-D) and digital-to-analog (D-A) conversions and the computations take time, there will always be a delay between the measurement and the time the control signal is applied to the process. This delay, which is called the computational delay, depends on how the control law is implemented in the computer. Two ways are illustrated in Fig. 11.1. In Case (a) the measured variable at time $t_{k}$ is used to compute the control signal applied at time $t_{k+1}$ . In Case (b) the control signal is applied as soon as the computations are finished. The disadvantage of Case (a) is that the control action is delayed unnecessarily. In Case (b) the disadvantage is that the time delay may change, depending on the load on the computer or changes in the program. In both cases it can be necessary to include the computational delay in the design of the controller.

![](image/b4f72a6e05c23be582002198ed01d5d0deb17f14ee84bc9b2b297786633f63c8.jpg)

<details>
<summary>line</summary>

| Time Point | y(t_k) | u(t_k) |
| --- | --- | --- |
| t_{k-1} | y(t_k) | u(t_k) |
| t_k | y(t_k) | u(t_k) |
| t_{k+1} | y(t_{k+1}) | u(t_{k+1}) |
| t_{k+1} | Compu-tational delay | u(t_{k+1}) |
</details>

![](image/61b13be879ed4f44673754fbe681bfcded6200c42cafeb9b6e43d820ea40b4ad.jpg)

<details>
<summary>line</summary>

| Time Point | y(t_{k-1}) | y(t_k) | u(t_{k-1}) | u(t_k) |
| --- | --- | --- | --- | --- |
| t_{k-1} | High | High | Low | Low |
| t_k | Medium | Medium | Low | Low |
| t_{k+1} | High | High | Low | Low |
</details>

Figure 11.1 Two ways to synchronize inputs and outputs. (a) The signals measured at time $t_k$ are used to compute the control signal applied at $t_{k+1}$ . (b) The control signal is applied as soon as it is computed.

In Case (b) it is desirable to make the delay as small as possible. This can be done by performing as few operations as possible between the A-D and D-A conversions. Assume that the regulator has the form

$$
\begin{array}{l} u (t) + r _ {1} u (t - 1) + \dots + r _ {k} u (t - k) \\ = t _ {0} u _ {c} (t) + \dots + t _ {m} u _ {c} (t - m) \cdot s _ {0} y (t) - \dots - s _ {l} y (t - l) \\ \end{array}
$$

This equation can be written as

$$u (t) = t _ {0} u _ {\mathrm{c}} (t) - s _ {0} y (t) + u ^ {\prime} (t - 1)$$

where

$$u ^ {\prime} (t - 1) = t _ {1} u _ {c} (t - 1) + \dots + t _ {m} u _ {c} (t - m) - s _ {1} y (t - 1) - \dots - s _ {l} y (t - l)- r _ {1} u (t - 1) - \dots - r _ {k} u (t - k)$$
