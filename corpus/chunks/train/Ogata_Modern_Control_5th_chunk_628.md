The chart contains a single series of lines representing the output values against the real axis. The x-axis is labeled 'Real Axis' and the y-axis is labeled 'Imaginary Axis'. The labels are explicitly provided in the code. There is no additional data series or variables present in the chart.
</details>

![](image/4ca12307e9333c6af3238cbc5691e8888b7452590fa277e5cfa30870993a9c7d.jpg)

<details>
<summary>text_image</summary>

Im
ω = 0-
ω = 0+
ω = +∞
ω = -∞
Re
</details>

Figure 8–59 Redrawn Nyquist plot.

Using the Nyquist plot obtained here, it is not easy to determine the encirclements of the $- 1 + j 0$ point by the Nyquist locus. Therefore, we need to redraw this Nyquist plot qualitatively to show the details near the −1+j0 point. Such a redrawn Nyquist diagram is shown in Figure 8–59.

From this diagram we find that the $- 1 + j 0$ point is encircled counterclockwise three times. Hence, N  −3. Since the open-loop transfer function has three poles in the right-half $s _ { 1 }$ plane, we have P  3.Then, we have $Z = N + P = 0$ . This means that there are no closed-loop poles in the right-half $s _ { 1 }$ plane. The system is therefore stable.

A–8–8. Show that the I-PD-controlled system shown in Figure 8–60(a) is equivalent to the PID-controlled system with input filter shown in Figure 8–60(b).

Figure 8–60 (a) I-PD-controlled system; (b) PID-controlled system with input filter.   
![](image/162ae70e8bc29f69d97c3a35cb06af6623d4f0599ef2f8ab659b8167113769d2.jpg)

Solution. The closed-loop transfer function $C ( s ) / R ( s )$ of the I-PD-controlled system is

$$\frac {C (s)}{R (s)} = \frac {\frac {K _ {p}}{T _ {i} s} G _ {p} (s)}{1 + K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) G _ {p} (s)}$$

The closed-loop transfer function $C ( s ) / R ( s )$ of the PID-controlled system with input filter shown in Figure 8–60(b) is

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {1}{1 + T _ {i} s + T _ {i} T _ {d} s ^ {2}} \frac {K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) G _ {p} (s)}{1 + K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) G _ {p} (s)} \\ = \frac {\frac {K _ {p}}{T _ {i} s} G _ {p} (s)}{1 + K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) G _ {p} (s)} \\ \end{array}
$$

The closed-loop transfer functions of both systems are the same.Thus, the two systems are equivalent.
