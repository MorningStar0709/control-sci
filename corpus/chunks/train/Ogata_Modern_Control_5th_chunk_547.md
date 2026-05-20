Solution. The Nyquist plot of the positive-feedback system can be obtained by defining num and den as

$$
\text { num } = \left[ \begin{array}{c c c} - 1 & - 4 & - 6 \end{array} \right]
\mathrm{den} = [ 1 \quad 5 \quad 4 ]
$$

and using the command nyquist(num,den). MATLAB Program 7–20 produces the Nyquist plot, as shown in Figure 7–130.

This system is unstable, because the –1+j0 point is encircled once clockwise. Note that this is a special case where the Nyquist plot passes through –1+j0 point and also encircles this point once clockwise. This means that the closed-loop system is degenerate; the system behaves as if it were an unstable first-order system. See the following closed-loop transfer function of the positivefeedback system:

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {s ^ {2} + 4 s + 6}{s ^ {2} + 5 s + 4 - \left(s ^ {2} + 4 s + 6\right)} \\ = \frac {s ^ {2} + 4 s + 6}{s - 2} \\ \end{array}
$$

<table><tr><td>MATLAB Program 7-20</td></tr><tr><td>num = [-1 -4 -6];den = [1 5 4];nyquist(num,den);gridtitle(&#x27;Nyquist Plot of G(s) = -(s^2 + 4s + 6)/(s^2 + 5s + 4)&#x27;)</td></tr></table>

Figure 7–130 Nyquist plot for positive-feedback system.   
![](image/8e34aac07cc050bdf63e554a11e9c867bc6cbdba4d8576b9157f1b87f0837fac.jpg)

<details>
<summary>other</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -1.5 | 0.0 |
| -1.4 | 0.2 |
| -1.3 | 0.3 |
| -1.2 | 0.4 |
| -1.1 | 0.3 |
| -1.0 | 0.2 |
| -0.9 | 0.0 |
| -0.8 | -0.2 |
| -0.7 | -0.3 |
| -1.1 | -0.4 |
| -0.9 | -0.3 |
| -0.8 | -0.2 |
| -0.7 | -0.1 |
| -1.1 | 0.0 |
| -0.9 | 0.1 |
| -0.8 | 0.2 |
| -0.7 | 0.3 |
| -1.1 | 0.4 |
| -0.9 | 0.3 |
| -0.8 | 0.2 |
| -0.7 | 0.1 |
| -1.1 | 0.0 |
| -0.9 | -0.1 |
| -0.8 | -0.2 |
| -0.7 | -0.3 |
| -1.1 | -0.4 |
| -0.9 | -0.3 |
| -0.8 | -0.2 |
| -0.7 | -0.1 |
| -1.1 | 0.0 |
| -0.9 | -0.1 |
| -0.8 | -0.2 |
| -0.7 | -0.3 |
| -1.1 | -0.4 |
| -0.9 | -0.3 |
| -0.8 | -0.2 |
| -0.7 | 0.0 |
| -1.1 | 0.1 |
| -0.9 | 0.2 |
| -0.8 | 0.3 |
| -0.7 | 0.4 |
| -1.1 | 0.5 |
| -0.9 | 0.4 |
| -0.8 | 0.3 |
| -0.7 | 0.2 |
| -1.1 | 0.1 |
| -0.9 | 0.0 |
| -0.8 | -0.1 |
| -0.7 | -0.2 |
| -1.1 | -0.3 |
| -0.9 | -0.4 |
| -0.8 | -0.5 |
| -0.7 | -0.4 |
| -1.1 | -0.3 |
| -0.9 | -0.2 |
| -0.8 | -0.1 |
| -0.7 | 0.0 |
| -1.1 | 0.1 |
| -0.9 | 0.2 |
| -0.8 | 0.3 |
| -0.7 | 0.4 |
| -1.1 | 0.5 |
| -0.9 | 0.4 |
| -0.8      }<fcel>-0.5<nl>
</details>
