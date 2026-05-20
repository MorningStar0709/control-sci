# A–5–11. Consider the closed-loop system defined by

$$\frac {C (s)}{R (s)} = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

Using a “for loop,” write a MATLAB program to obtain unit-step response of this system for the following four cases:

Solution. Define $\omega _ { n } ^ { 2 } = a$ and $2 \zeta \omega _ { n } = b$ . Then, a and b each have four elements as follows:

$$
a = \left[ \begin{array}{c c c c} 1 & 4 & 1 6 & 3 6 \end{array} \right]

b = \left[ \begin{array}{c c c c} 0. 6 & 2 & 5. 6 & 9. 6 \end{array} \right]
$$

Using vectors a and b, MATLAB Program 5–21 will produce the unit-step response curves as shown in Figure 5–59.

<table><tr><td>MATLAB Program 5-21</td></tr><tr><td>a = [1 4 16 36];b = [0.6 2 5.6 9.6];t = 0:0.1:8;y = zeros(81,4);for i = 1:4;num = [a(i)];den = [1 b(i) a(i)];y(:,i) = step(num,den,t);endplot(t,y(:,1),&#x27;o&#x27;,t,y(:,2),&#x27;x&#x27;,t,y(:,3),&#x27;-&#x27;,t,y(:,4),&#x27;-.&#x27;)gridtitle(&#x27;Unit-Step Response Curves for Four Cases&#x27;)xlabel(&#x27;t Sec&#x27;)ylabel(&#x27;Outputs&#x27;)gtext(&#x27;1&#x27;)gtext(&#x27;2&#x27;)gtext(&#x27;3&#x27;)gtext(&#x27;4&#x27;)</td></tr></table>

![](image/84f74b41aca03c6e414e607b2ee3c1d09138fcfa8a68fd248c933c42e07bab78.jpg)

<details>
<summary>line</summary>

| t Sec | Outputs (Curve 1) | Outputs (Curve 2) | Outputs (Curve 3) | Outputs (Curve 4) |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 1 | 1.0 | 1.0 | 0.8 | 0.4 |
| 2 | 1.0 | 1.0 | 0.9 | 0.6 |
| 3 | 1.3 | 1.0 | 0.9 | 0.8 |
| 4 | 1.3 | 1.0 | 0.9 | 0.9 |
| 5 | 1.0 | 1.0 | 0.9 | 0.9 |
| 6 | 0.9 | 1.0 | 0.9 | 0.9 |
| 7 | 0.8 | 1.0 | 0.9 | 0.9 |
| 8 | 0.9 | 1.0 | 0.9 | 0.9 |
</details>

Figure 5–59 Unit-step response curves for four cases.

A–5–12. Using MATLAB, obtain the unit-ramp response of the closed-loop control system whose closedloop transfer function is

$$\frac {C (s)}{R (s)} = \frac {s + 1 0}{s ^ {3} + 6 s ^ {2} + 9 s + 1 0}$$

Also, obtain the response of this system when the input is given by

$$r = e ^ {- 0. 5 t}$$

Solution. MATLAB Program 5–22 produces the unit-ramp response and the response to the exponential input $r = e ^ { - 0 . 5 t }$ . The resulting response curves are shown in Figures 5–60(a) and (b), respectively.
