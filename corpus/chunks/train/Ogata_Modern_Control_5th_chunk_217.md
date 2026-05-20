# MATLAB Program 5–3

wn = 5;
damping_ratio = 0.4;
[num0, den] = ord2(wn, damping_ratio);
num = 5^2 * num0;
printsys(num, den, 's')
num/den = $\frac{25}{S^2 + 4s + 25}$

Obtaining the Unit-Step Response of the Transfer-Function System. Let us consider the unit-step response of the system given by

$$G (s) = \frac {2 5}{s ^ {2} + 4 s + 2 5}$$

MATLAB Program 5–4 will yield a plot of the unit-step response of this system. A plot of the unit-step response curve is shown in Figure 5–20.

MATLAB Program 5–4   
% ---- Unit-step response ----
% ***** Enter the numerator and denominator of the transfer
% function *****
num = [25];
den = [1 4 25];
% ***** Enter the following step-response command *****
step(num,den)
% ***** Enter grid and title of the plot *****
grid
title ('Unit-Step Response of G(s) = 25/(s^2+4s+25)')

![](image/6267ef9646f62134ba8f3b78dee07d75a993bccab5a18d8ccee02d041d3d3aac.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.25 |
| 1.0 | 1.0 |
| 1.5 | 0.9 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
</details>

Figure 5–20 Unit-step response curve.

Notice in Figure 5–20 (and many others) that the x-axis and y-axis labels are automatically determined. If it is desired to label the x axis and y axis differently, we need to modify the step command. For example, if it is desired to label the x axis as 't Sec' and the y axis as ‘Output,’ then use step-response commands with left-hand arguments, such as

$$c = \text { step } (\text { num }, \text { den }, t)$$

or, more generally,

$$[ y, x, t ] = \operatorname{step} (\text {num}, \text {den}, t)$$

and use plot(t,y) command. See, for example, MATLAB Program 5–5 and Figure 5–21.

<table><tr><td>MATLAB Program 5-5</td></tr><tr><td>% ---- Unit-step response ----</td></tr><tr><td>num = [25];</td></tr><tr><td>den = [1 4 25];</td></tr><tr><td>t = 0:0.01:3;</td></tr><tr><td>[y,x,t] = step(num,den,t);</td></tr><tr><td>plot(t,y)</td></tr><tr><td>grid</td></tr><tr><td>title(&#x27;Unit-Step Response of G(s)=25/(s^2+4s+25)&#x27;)</td></tr><tr><td>xlabel(&#x27;t Sec&#x27;)</td></tr><tr><td>ylabel(&#x27;Output&#x27;)</td></tr></table>

![](image/fd03690b755c7b571f13420f1ae785aadec044a541b0c331108fcff191fe364c.jpg)

<details>
<summary>line</summary>

| t Sec | Output |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.25 |
| 1.0 | 1.0 |
| 1.5 | 0.9 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
</details>
