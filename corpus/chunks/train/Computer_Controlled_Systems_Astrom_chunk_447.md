# A Model of the Sample-and-Hold Circuit

A schematic diagram of an analog sample-and-hold circuit is shown in Fig. 7.15. It is assumed that the circuit is followed by an amplifier with very high input impedance. The circuit works as follows: When the sampling switch is closed, the capacitor is charged to the input voltage via the resistor R. When the sampling switch is opened, the capacitor holds its voltage until the next closing.

To describe the system, a function m, which describes the closing and opening of the sampling switch, is introduced. This function is defined by

$$
m (t) = \left\{ \begin{array}{l l} 1 & \text {   if   switch   is   closed   } \\ 0 & \text {   if   switch   is   open   } \end{array} \right.
$$

The current is then given by

$$i = \frac {u - y}{R} m$$

![](image/19dbd7ba5922e2902f6a87a26e326bbc12cad1c5e07aaf6c6e7b33a932df7d67.jpg)

<details>
<summary>bar</summary>

| Time | Value |
| --- | --- |
| t | 1 |
| h | 1 |
| 2h | 1 |
| t | 1 |
</details>

Figure 7.16 Graph of the modulation function m with period h and pulse width $\tau$ .

The current is thus modulated by the function m, which is called the modulation function. If the input impedance of the circuit that follows the sample-and-hold circuit is high, the voltage over the capacitor is given by

$$C \frac {d y (t)}{d t} = i (t) = \frac {u (t) - y (t)}{R} m (t) \tag {7.24}$$

The differential equation of (7.24) is a linear time-varying system. The time variation is caused by the modulation. If the sampling period h is constant and if the switch is closed for $\tau$ seconds at each sampling, the function m has the shape shown in Fig. 7.16. Because m is a periodic function the system becomes a periodic system.

Once a mathematical model of the circuit is obtained the response of the circuit to an input signal u can be investigated. It follows directly from Eq. (7.24) that the voltage across the capacitor is constant when the switch is open, that is, when $m(t) = 0$ . When the switch is closed, the voltage y approaches the input signal u as a first-order dynamic system with the time constant RC. The time constant of the RC circuit must be considerably shorter than the pulse width; otherwise, there is no time to charge the capacitor to the input voltage when the switch is closed.

A simulation of the sample-and-hold circuit is shown in Fig. 7.17. With the chosen parameters, the pulse width is so long that the input signal changes significantly when the switch is closed.

Figure 7.18 shows what happens when the pulse width is shorter. The results shown in Fig. 7.18 represent a reasonable choice of parameter values. The sample-and-hold circuit quickly reaches the value of the input signal and then remains constant over the sampling period.
