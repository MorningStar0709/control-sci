$$
\begin{array}{l} \text { num } = [ 0 \quad 1 \quad 0 ] \\ \mathrm{den} = [ 1 \quad 0. 2 \quad 1 ] \\ \end{array}
$$

and use the step-response command; as given in MATLAB Program 5–9, we obtain a plot of the unit-impulse response of the system as shown in Figure 5–25.

<table><tr><td>MATLAB Program 5-9</td></tr><tr><td>num = [1 0];den = [1 0.2 1];step(num,den);gridtitle(&#x27;Unit-Step Response of sG(s) = s/(s^2 + 0.2s + 1)&#x27;)</td></tr></table>

![](image/21a67af9644df5c5dba8d124561162e27ade4d8bc0ccfedd622949702d587a41.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 5 | -0.6 |
| 10 | 0.45 |
| 15 | -0.35 |
| 20 | 0.2 |
| 25 | -0.1 |
| 30 | 0.05 |
| 35 | -0.05 |
| 40 | 0.0 |
| 45 | 0.0 |
| 50 | 0.0 |
</details>

Figure 5–25 Unit-impulseresponse curve obtained as the unitstep response of $s G ( s ) =$ $s / \bigl ( s ^ { 2 } + 0 . 2 s + 1 \bigr )$ .

Ramp Response. There is no ramp command in MATLAB. Therefore, we need to use the step command or the lsim command (presented later) to obtain the ramp response. Specifically, to obtain the ramp response of the transfer-function system $G ( s )$ , divide $G ( s )$ by s and use the step-response command. For example, consider the closedloop system

$$\frac {C (s)}{R (s)} = \frac {2 s + 1}{s ^ {2} + s + 1}$$

For a unit-ramp input, $R ( s ) = 1 / s ^ { 2 }$ . Hence

$$C (s) = \frac {2 s + 1}{s ^ {2} + s + 1} \frac {1}{s ^ {2}} = \frac {2 s + 1}{(s ^ {2} + s + 1) s} \frac {1}{s}$$

To obtain the unit-ramp response of this system, enter the following numerator and denominator into the MATLAB program:

$$
\begin{array}{l} \mathrm{num} = [ 2 \quad 1 ]; \\ \mathrm{den} = [ 1 \quad 1 \quad 1 \quad 0 ]; \\ \end{array}
$$

and use the step-response command. See MATLAB Program 5–10. The plot obtained by using this program is shown in Figure 5–26.
