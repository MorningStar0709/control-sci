$$G _ {c} (s) = K _ {c} \frac {\left(s + \frac {1}{T _ {1}}\right) \left(s + \frac {1}{T _ {2}}\right)}{\left(s + \frac {\beta}{T _ {1}}\right) \left(s + \frac {1}{\beta T _ {2}}\right)}$$

Then the open-loop transfer function of the compensated system is $G _ { c } ( s ) G ( s )$ . Since the gain K of the plant is adjustable, let us assume that $K _ { c } = 1$ . Then $\operatorname* { l i m } _ { s \to 0 } G _ { c } ( s ) = 1$ From the requirement. on the static velocity error constant, we obtain

$$
\begin{array}{l} K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = \lim _ {s \rightarrow 0} s G _ {c} (s) \frac {K}{s (s + 1) (s + 4)} \\ = \frac {K}{4} = 1 0 \\ \end{array}
$$

Hence,

$$K = 4 0$$

We shall first plot a Bode diagram of the uncompensated system with $K = 4 0 . \mathbf { M A T L A B }$ Program 7–30 may be used to plot this Bode diagram.The diagram obtained is shown in Figure 7–151.

<table><tr><td>MATLAB Program 7-30</td></tr><tr><td>num = [40];den = [1 5 4 0];w = logspace(-1,1,100);bode(num,den,w)title(&#x27;Bode Diagram of G(s) = 40/[s(s + 1)(s + 4)]&#x27;)</td></tr></table>

![](image/b4e6da151593aa4652eea053da70bcf356bea97e657fee794bde0647f42e39ae.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.1 | -100 | 40 |
| 1 | -150 | 20 |
| 10 | -250 | -30 |
</details>

Figure 7–151

Bode diagram of

$$G (s) = 4 0 / \left[ s (s + 1) (s + 4) \right].$$

From Figure 7–151, the phase margin of the gain-adjusted but uncompensated system is found to be $- 1 6 ^ { \circ }$ , which indicates that this system is unstable. The next step in the design of a lag–lead compensator is to choose a new gain crossover frequency. From the phase-angle curve for $G ( j \omega )$ , we notice that the phase crossover frequency is $\omega = 2 \mathrm { r a d / s e c }$ . We may choose the new gain crossover frequency to be 2 radsec so that the phase-lead angle required at $\omega = 2 \mathrm { r a d / s e c }$ is about $5 0 ^ { \circ }$ . A single lag–lead compensator can provide this amount of phaselead angle quite easily.
