$$\phi = \angle G (j \omega) = \angle (1 + j 0) - \angle (1. 2 + j 0. 0 2 \omega) \tag {9.24}$$

Using Eq. (9.14) to compute each angle (or argument) we obtain

$$\phi = \angle G (j \omega) = \tan^ {- 1} \left(\frac {0}{1}\right) - \tan^ {- 1} \left(\frac {0 . 0 2 \omega}{1 . 2}\right) \tag {9.25}$$

Substituting frequency $\omega = 5 0$ rad/s into Eq. (9.25), the phase angle is $\phi = - 0 . 6 9 4 7$ rad (or, $\phi = - 3 9 . 8 1 ^ { \circ } )$ . Finally, substituting the magnitude and phase of $G ( j \omega )$ ) into Eq. (9.21) the frequency response is

$$I _ {\mathrm{ss}} (t) = 1. 2 8 0 4 \sin (5 0 t - 0. 6 9 4 7) \mathrm{A} \tag {9.26}$$

Equation (9.26) is the frequency response of the current of the RL circuit driven by a sinusoidal voltage input. At steady state the current $I ( t )$ oscillates at the same frequency as the voltage input (50 rad/s) and with an amplitude of 1.2804 A. A phase difference of $\phi = - 0 . 6 9 4 7$ rad exists between the output and input, and because the phase angle is negative, the current (output) “lags” behind the input (voltage source). The time shift $\Delta t$ between input and output sinusoids can be computed from the phase lag and the frequency:

$$\Delta t = \left| \frac {\phi}{\omega} \right| = \left| \frac {- 0 . 6 9 4 7 \mathrm{rad}}{5 0 \mathrm{rad/s}} \right| = 0. 0 1 3 9 \mathrm{s} \tag {9.27}$$

Figure 9.6 shows the frequency response (9.26) plotted on the same graph with the voltage input $e _ { \mathrm { i n } } ( t ) =$ 2 sin 50t V. The voltage input (left y axis) and steady-state current (right y axis) are both sinusoidal signals with the same frequency, and the time lag (or phase difference) between the two signals is apparent.

We can verify our result by computing the magnitude and phase angle of $G ( j \omega )$ using the following MATLAB commands:

$$
\begin{array}{l} > > \mathrm{w} = 5 0; \\ > > G j 5 0 = 1 / (1. 2 + 0. 0 2 * j * w); \\ > > \text {   magGj50   } = \text {   abs   (Gj50)   } \\ > > \text { phaseGj50 } = \text { angle(Gj50) } \\ \% \text{ define input frequency,} \omega = 50 \text{ rad / s} \\ \% \text{define sinusoidal transfer function} G(j50) \\ \% \text{ compute the magnitude of } G(j50) \\ \% \text {compute the phase angle of} G (j 5 0) (\text {rad}) \\ \end{array}
$$

![](image/b8f24cb19740426adba4cf750b89ddc3e725825ed8e69a48e69e2cb000b33633.jpg)

<details>
<summary>line</summary>

| Time, s | Input voltage, e_in(t) (V) | Output current, I_ss(t) (A) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | -2.0 | -1.0 |
| 0.2 | 0.0 | 0.0 |
| 0.3 | 2.0 | 1.0 |
| 0.4 | 0.0 | 0.0 |
| 0.5 | -2.0 | -1.0 |
</details>

Figure 9.6 Frequency response of RL circuit (Example 9.1).

After executing these commands we obtain

$$\operatorname{magGj} 5 0 = 0. 6 4 0 2 \text { and } \operatorname{phaseGj} 5 0 = - 0. 6 9 4 7$$

which matches our previous results.
