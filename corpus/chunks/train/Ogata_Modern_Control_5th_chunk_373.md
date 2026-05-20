MATLAB Program 6–17   
```matlab
% ***** Root-locus plot *****
num = [1];
den = [1 4 11 14 10];
numa = [1];
dena = [1 4 6 4 1];
r = rlocus(num,den);
plot(r,'-')
hold
Current plot held
plot(r,'o')
rlocus(numa,dena);
v = [-6 4 -5 5]; axis(v); axis('square')
grid
title('Plot of Root Loci and Asymptotes') 
```

Plot of Root Loci and Asymptotes   
![](image/f0219bd99b9eb391b495ea5eef82b54f12ab1a7542ee164e31bdd0ad4b8ac331.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -5.0 | 4.5 |
| -4.5 | 3.8 |
| -4.0 | 3.2 |
| -3.5 | 2.6 |
| -3.0 | 2.0 |
| -2.5 | 1.5 |
| -2.0 | 1.0 |
| -1.5 | 0.5 |
| -1.0 | 0.0 |
| -0.5 | -0.5 |
| 0.0 | -1.0 |
| 0.5 | -1.5 |
| 1.0 | -2.0 |
| 1.5 | -2.5 |
| 2.0 | -3.0 |
| 2.5 | -3.5 |
| 3.0 | -4.0 |
| 3.5 | -4.5 |
</details>

Figure 6–72

Plot of root loci and asymptotes.

the points where the root loci cross the imaginary axis can be found by substituting $s = j \omega$ with the characteristic equation as follows:

$$
\begin{array}{l} [ (j \omega) ^ {2} + 2 j \omega + 2 ] [ (j \omega) ^ {2} + 2 j \omega + 5 ] + K \\ = \left(\omega^ {4} - 1 1 \omega^ {2} + 1 0 + K\right) + j (- 4 \omega^ {3} + 1 4 \omega) = 0 \\ \end{array}
$$

and equating the imaginary part to zero. The result is

$$\omega = \pm 1. 8 7 0 8$$

Thus the exact points where the root loci cross the jv axis are $\omega = \pm 1 . 8 7 0 8 .$ By equating the real. part to zero, we get the gain value K at the crossing points to be 16.25.

A–6–10. Consider a unity-feedback control system with the feed-forward transfer function $G ( s )$ given by

$$G (s) = \frac {K (s + 1)}{(s ^ {2} + 2 s + 2) (s ^ {2} + 2 s + 5)}$$

Plot a root-locus diagram with MATLAB.

Solution. The feedforward transfer function $G ( s )$ can be written as

$$G (s) = \frac {K (s + 1)}{s ^ {4} + 4 s ^ {3} + 1 1 s ^ {2} + 1 4 s + 1 0}$$

A possible MATLAB program to plot a root-locus diagram is shown in MATLAB Program 6–18. The resulting root-locus plot is shown in Figure 6–73.

```matlab
MATLAB Program 6–18
num = [1 1];
den = [1 4 11 14 10];
K1 = 0:0.1:2;
K2 = 2:0.0.2:2.5;
K3 = 2.5:0.5:10;
K4 = 10:1:50;
K = [K1 K2 K3 K4]
r = rlocus(num,den,K);
plot(r, 'o')
v = [-8 2 -5 5]; axis(v); axis('square')
grid
title('Root-Locus Plot of G(s) = K(s+1)/[(s^2+2s+2)(s^2+2s+5)]')
xlabel('Real Axis')
ylabel('Imag Axis') 
```

Figure 6–73 Plot of root loci.   
![](image/b046d558672347cc0d7d5e360f69ec884769f8cdf123a4bbb62bf820be1e4bd8.jpg)

<details>
<summary>other</summary>
