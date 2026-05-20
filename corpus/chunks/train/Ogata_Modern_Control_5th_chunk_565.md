$$G _ {c} (s) = \frac {s + 0 . 4}{s + 4} \frac {s + 0 . 2}{s + 0 . 0 2} = \frac {(2 . 5 s + 1) (5 s + 1)}{(0 . 2 5 s + 1) (5 0 s + 1)}$$

The Bode diagram of the lag–lead compensator $G _ { c } ( s )$ can be obtained by entering MATLAB Program 7–31 into the computer. The resulting plot is shown in Figure 7–152.

<table><tr><td>MATLAB Program 7-31</td></tr><tr><td>numc = [1 0.6 0.08];denc = [1 4.02 0.08];bode(numc,denc)title(&#x27;Bode Diagram of Lag-Lead Compensator&#x27;)</td></tr></table>

![](image/15d14275645d44497298f53ff3d152b20e7ab24f780d96d2a602bdf4445e6d8c.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg); Magnitude (dB) |
| --- | --- |
| 10⁻³ | 0 |
| 10⁻² | -5 |
| 10⁻¹ | -20 |
| 10⁰ | -15 |
| 10¹ | -5 |
| 10² | 0 |
</details>

Figure 7–152 Bode diagram of the designed lag–lead compensator.

The open-loop transfer function of the compensated system is

$$
\begin{array}{l} G _ {c} (s) G (s) = \frac {(s + 0 . 4) (s + 0 . 2)}{(s + 4) (s + 0 . 0 2)} \frac {4 0}{s (s + 1) (s + 4)} \\ = \frac {4 0 s ^ {2} + 2 4 s + 3 . 2}{s ^ {5} + 9 . 0 2 s ^ {4} + 2 4 . 1 8 s ^ {3} + 1 6 . 4 8 s ^ {2} + 0 . 3 2 s} \\ \end{array}
$$

Using MATLAB Program 7–32 the magnitude and phase-angle curves of the designed open-loop transfer function $G _ { c } ( s ) G ( s )$ can be obtained as shown in Figure 7–153. Note that the denominator polynomial den1 was obtained using the conv command, as follows:

$$
\begin{array}{l} \hline a = [ 1 4. 0 2 0. 0 8 ]; \\ b = [ 1 5 4 0 ]; \\ \text {conv(a,b)} \\ \text {ans =} \\ \hline 1. 0 0 0 0 9. 0 2 0 0 2 4. 1 8 0 0 1 6. 4 8 0 0 0. 3 2 0 0 0 0 0 \end{array}
$$
