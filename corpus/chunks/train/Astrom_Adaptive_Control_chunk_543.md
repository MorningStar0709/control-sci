# The Ziegler-Nichols Step Response Method

A simple way to determine the parameters of a PID regulator based on step response data was developed by Ziegler and Nichols and published in 1942. The method uses only two of the parameters shown in Fig. 8.1, namely, $a$ and $L$ . The regulator parameters are given in Table 8.1. The Ziegler-Nichols tuning rule was developed by empirical simulations of many different systems. The rule has the drawback that it gives closed-loop systems that are often too poorly damped. Systems with better damping can be obtained by modifying the numerical values in Table 8.1. By using additional parameters it is also possible to determine whether the Ziegler-Nichols rule is applicable. If the time constant $T$ is also determined, an empirical rule is established that the

![](image/8aab6f431ce61453ea9b4870b1c58fcb64bdc11ec6e8ca2344aa77574004799f.jpg)

<details>
<summary>line</summary>

| Time | k |
| --- | --- |
| L | 0.63k |
| T | 0.63k |
</details>

Figure 8.1 Unit step response of a typical industrial process.

Table 8.1 Regulator parameters obtained by the Ziegler-Nichols step response method. 

<table><tr><td>Controller</td><td> $K_c$ </td><td> $T_i$ </td><td> $T_d$ </td></tr><tr><td>P</td><td>1/a</td><td></td><td></td></tr><tr><td>PI</td><td>0.9/a</td><td>3L</td><td></td></tr><tr><td>PID</td><td>1.2/a</td><td>2L</td><td>L/2</td></tr></table>

Ziegler-Nichols rule is applicable if 0.1 < L/T < 0.6. For large values of L/T it is advantageous to use other tuning rules or control laws that compensate for dead time. For small values of L/T, improved performance may be obtained with higher-order compensators. It is also possible to use more sophisticated tuning rules based on three parameters.
