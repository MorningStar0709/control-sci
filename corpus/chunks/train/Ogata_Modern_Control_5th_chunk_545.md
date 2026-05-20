Solution. MATLAB Program 7–17 produces the Nyquist diagram shown in Figure 7–127. From this figure, we see that the Nyquist plot does not encircle the –1+j0 point. Hence, N=0 in the Nyquist stability criterion. Since no open-loop poles lie in the right-half s plane, P=0. Therefore, $Z = N + P = 0 .$ . The closed-loop system is stable.

<table><tr><td>MATLAB Program 7-17</td></tr><tr><td>num = [20 20 10];den = [1 11 10 0];nyquist(num,den)v = [-2 3 -3 3]; axis(v)grid</td></tr></table>

![](image/a6a08052db3eac5c7b0fa80b3c8c703c0e251d18d87a22f8188e8c86a624c1d8.jpg)

<details>
<summary>other</summary>

Nyquist Diagram
| Real Axis | Imaginary Axis |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.8 |
| 1.0 | -1.0 |
| 1.5 | 0.5 |
| 2.0 | 0.0 |
| 2.5 | -0.5 |
| 3.0 | 0.0 |
</details>

Figure 7–127   
Nyquist plot of

$$G (s) = \frac {2 0 (s ^ {2} + s + 0 . 5)}{s (s + 1) (s + 1 0)}.$$

A–7–12. Consider the same system as discussed in Problem A–7–11. Draw the Nyquist plot for only the positive-frequency region.

Solution. Drawing a Nyquist plot for only the positive-frequency region can be done by the use of the following command:

$$[ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist } (\mathrm{num}, \mathrm{den}, \mathrm{w})$$

The frequency region may be divided into several subregions by using different increments. For example, the frequency region of interest may be divided into three subregions as follows:

$$w 1 = 0. 1: 0. 1: 1 0;\mathrm{w} 2 = 1 0: 2: 1 0 0;\mathrm{w} 3 = 1 0 0: 1 0: 5 0 0;\mathrm{w} = [ \mathrm{w1} \mathrm{w2} \mathrm{w3} ]$$

MATLAB Program 7–18 uses this frequency region. Using this program, we obtain the Nyquist plot shown in Figure 7–128.

MATLAB Program 7–18   
num = [20 20 10];
den = [1 11 10 0];
w1 = 0.1:0.1:10; w2 = 10:2:100; w3 = 100:10:500;
w = [w1 w2 w3];
[re,im,w] = nyquist(num,den,w);
plot(re,im)
v = [-3 3 -5 1]; axis(v);
grid
title('Nyquist Plot of G(s) = 20(s^2 + s + 0.5)/[s(s + 1)(s + 10)]')
xlabel('Real Axis')
ylabel('Imag Axis')

Nyquist Plot of G(s) = 20(s2+s+0.5)/[s(s+1)(s+10)]   
![](image/29623f5df2400d8f7d171aac4b1c712ffeac3f6d800dd7296c5a4f7324d2d5a7.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis |
| --- | --- |
| 0.0 | 0.0 |
| 1.0 | -1.0 |
| 1.5 | -0.5 |
| 2.0 | -0.2 |
</details>

Figure 7–128   
Nyquist plot for the positive-frequency region.

A–7–13. Referring to Problem A–7–12, plot the polar locus of $G ( s )$ where

$$G (s) = \frac {2 0 \left(s ^ {2} + s + 0 . 5\right)}{s (s + 1) (s + 1 0)}$$
