The fact that the response curve is an exponential curve superimposed by damped sinusoidal curves can be seen from Figure 5–56.

A–5–9. When the closed-loop system involves a numerator dynamics, the unit-step response curve may exhibit a large overshoot. Obtain the unit-step response of the following system with MATLAB:

$$\frac {C (s)}{R (s)} = \frac {1 0 s + 4}{s ^ {2} + 4 s + 4}$$

Obtain also the unit-ramp response with MATLAB.

Solution. MATLAB Program 5–19 produces the unit-step response as well as the unit-ramp response of the system.The unit-step response curve and unit-ramp response curve, together with the unit-ramp input, are shown in Figures 5–57(a) and (b), respectively.

Notice that the unit-step response curve exhibits over 215% of overshoot. The unit-ramp response curve leads the input curve.These phenomena occurred because of the presence of a large derivative term in the numerator.

<table><tr><td>MATLAB Program 5-19</td></tr><tr><td>num = [10 4];den = [1 4 4];t = 0:0.02:10;y = step(num,den,t);plot(t,y)gridtitle(&#x27;Unit-Step Response&#x27;)xlabel(&#x27;t (sec)&#x27;)ylabel(&#x27;Output&#x27;)num1 = [10 4];den1 = [1 4 4 0];y1 = step(num1,den1,t);plot(t,t,&#x27;--&#x27;,t,y1)v = [0 10 0 10]; axis(v); gridtitle(&#x27;Unit-Ramp Response&#x27;)xlabel(&#x27;t (sec)&#x27;)ylabel(&#x27;Unit-Ramp Input and Output&#x27;)text(6.1,5.0,&#x27;Unit-Ramp Input&#x27;)text(3.5,7.1,&#x27;Output&#x27;)</td></tr></table>

![](image/36be27a46d28a3377e3391cd7c593bda572b5c23dfa2350a9be20c6613880069.jpg)

<details>
<summary>line</summary>

| t (sec) | Output |
| --- | --- |
| 0 | 0.0 |
| 0.5 | 2.1 |
| 1 | 1.8 |
| 2 | 1.3 |
| 3 | 1.1 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

(a)

![](image/f6f772e5e24066522bbe5aa533a1a2d3e5f056732573c8e38aacd4fe1ed0380c.jpg)

<details>
<summary>line</summary>

| t (sec) | Unit-Ramp Input | Unit-Ramp Output |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 1 | 2 |
| 2 | 2 | 3.5 |
| 3 | 3 | 4.5 |
| 4 | 4 | 5.5 |
| 5 | 5 | 6.5 |
| 6 | 6 | 7.5 |
| 7 | 7 | 8.5 |
| 8 | 8 | 9.5 |
| 9 | 9 | 10 |
| 10 | 10 | 10 |
</details>

Figure 5–57 (a) Unit-step response curve; (b) unit-ramp response curve plotted with unit-ramp input.

A–5–10. Consider a higher-order system defined by

$$\frac {C (s)}{R (s)} = \frac {6 . 3 2 2 3 s ^ {2} + 1 8 s + 1 2 . 8 1 1}{s ^ {4} + 6 s ^ {3} + 1 1 . 3 2 2 3 s ^ {2} + 1 8 s + 1 2 . 8 1 1}$$
