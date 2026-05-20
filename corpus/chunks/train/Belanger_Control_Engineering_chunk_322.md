# Solution

Figure 6.15 shows the Bode plots (MATLAB bode). Since $|L(j\omega)| = 1$ (0 db) at $\omega = 1.52$ rad/s, that frequency is the crossover frequency. Because the phase at that frequency is $-169.9^{\circ}$ , the phase margin is $180 - 169.9^{\circ} = 10.1^{\circ}$ .

![](image/aaadff324e6ba998a07d0e36c6ee713b2ff988d6d2352d3fde90e7557df7a95b.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Phase (deg) |
| --- | --- |
| 10^0 | -135 |
| 10^1 | -250 |
</details>

![](image/ebe56031c417ed8665d2afa82cf077c493aa0e5a37a51784a7b0bc82604767ce.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (db) |
| --- | --- |
| 10⁻¹ | ~18 |
| 10⁰ | ~0 |
| 10¹ | ~-60 |
| 10² | ~-100 |
</details>

Figure 6.15 Bode plots

From the phase plot, the phase is $180^{\circ}$ (negative real-axis crossing in the Nyquist plot) at $\omega = 1.73$ rad/s, at which frequency the magnitude is -2.47 db. The gain margin is 2.47 db. (MATLAB margin will return both the gain and phase margins.)

It is convenient to work from Bode plots to design a pure-gain controller for specified stability margins. We have, for k > 0,

$$2 0 \log | k L (j \omega) | = 2 0 \log k + 2 0 \log | L (j \omega) | \tag {6.23}$$

and

$$\not \prec k L (j \omega) = \not \prec L (j \omega). \tag {6.24}$$

From Equation 6.24, the phase curve for $kL(j\omega)$ is the same as for $L(j\omega)$ . From Equation 6.23, the gain curve for $kL(j\omega)$ is just the gain curve for $|L(j\omega)|$ shifted by $20\log k$ . If $k > 1$ , $\log k > 0$ and the gain curve is shifted up; the shift is downward if $k < 1$ .

The following example will serve to illustrate the design procedure.
