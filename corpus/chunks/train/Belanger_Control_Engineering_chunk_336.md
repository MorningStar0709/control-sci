# Example 6.9 (Active Suspension)

For the suspension system of Example 2.2 (Chapter 2), feedback is used from the output $y = x_{1} - x_{2}$ to the force input u. We wish to design a controller that will return the distance y between the two masses to some desired set point in the dc steady state, so as to maintain that distance in spite of load changes. We require gain and phase margins 6 db and $60^{\circ}$ , respectively.

Solution From Equation 3.23 (Chapter 3),

$$\frac {y}{u} = \frac {0 . 0 2 3 3 4 (s ^ {2} + 8 5 . 8 6 1)}{(s ^ {2} + 1 2 . 3 0 5 s + 6 3 9 . 7 6) (s ^ {2} + 1 . 6 9 5 4 s + 9 . 3 7 8 7)}.$$

First we design a pure-gain controller. Figure 6.23 shows the Bode plots. Since the loop gain magnitude is $-\infty$ db where the phase is $180^{\circ}$ ( $\omega = 9.26$ rad/s), a pure-gain controller with any positive value of $k$ achieves the gain margin. The phase is $-180^{\circ} + 60^{\circ} = -120^{\circ}$ at $\omega = 3.51$ rad/s, where the magnitude is $-67.7$ db.

![](image/3c3e80cf6ba74aacea96dbf580709dbb0bb082cac84b7a52005db4633807b637.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (dB) |
| --- | --- |
| 0.1 | -70 |
| 1 | -65 |
| 10 | -120 |
| 100 | -110 |
</details>

![](image/2802736ee57ec74481941c323b66a0036571020d58650970150ecd150fa5de09.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) |
| --- | --- |
| 0.1 | 0 |
| 1 | -50 |
| 10 | -200 |
| 100 | -550 |
</details>

Figure 6.23 Bode plots, active suspension

A gain of 67.7 db makes that frequency the crossover frequency, and the phase margin specification is satisfied for $k \leq 67.7$ db, for which the gain margin also holds.

To meet the dc requirement of zero error, we rely on PI control. We use the maximum value of k consistent with the stability margins because this also maximizes the crossover frequency and hence the bandwidth; so k = 67.7 db (k = 2427).

With $a = 0.1$ , Equation 6.35 yields

$$T = \frac {1}{a \omega_ {c}} = \frac {1}{(. 1) (3 . 5 1)} = 2. 8 5 \mathrm{s}.$$

The PI controller is

$$G _ {c} (s) = 2 4 2 7 \left(1 + \frac {1}{2 . 8 5 s}\right).$$
