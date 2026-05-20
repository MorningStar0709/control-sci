# MATLAB Program 6–1

% --------- Root-locus plot ---

num = [1 3];

den = [1 5 20 16 0];

rlocus(num,den)

v = [-6 6 -6 6];

axis(v); axis('square')

grid;

title ('Root-Locus Plot of G(s) = K(s + 3)/[s(s + 1)(s^2 + 4s + 16)]')

Note that in MATLAB Program 6–1, instead of

$$\mathrm{den} = [ 1 \quad 5 \quad 2 0 \quad 1 6 \quad 0 ]$$

we may enter

$$\text { den } = \text { conv } ([ 1 1 0 ], [ 1 4 1 6 ])$$

The results are the same.

![](image/d1e46c97bd105455411e9b4624b1e21f207c46dcd992eb672b86301b74253c69.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -3.0 | 0.0 |
| -2.5 | 3.5 |
| -2.0 | -4.0 |
| -1.5 | 0.0 |
| 0.0 | 0.0 |
| 2.0 | 6.0 |
</details>

Figure 6–16   
Root-locus plot.

$$
\begin{array}{l} G (s) H (s) = \frac {K}{s (s + 0 . 5) \left(s ^ {2} + 0 . 6 s + 1 0\right)} \\ = \frac {K}{s ^ {4} + 1 . 1 s ^ {3} + 1 0 . 3 s ^ {2} + 5 s} \\ \end{array}
$$

There are no open-loop zeros. Open-loop poles are located at $s = - 0 . 3 + j 3 . 1 4 8 0 .$ , $s = - 0 . 3 - j 3 . 1 4 8 0 , s = - 0 . 5 , \mathrm { a n d } s = 0 .$ .

Entering MATLAB Program 6–2 into the computer, we obtain the root-locus plot shown in Figure 6–17.

MATLAB Program 6–2   
```matlab
% ---- Root-locus plot ----
num = [1];
den = [1 1.1 10.3 5 0];
r = rlocus(num,den);
plot(r,'o')
v = [-6 6 -6 6]; axis(v)
grid
title('Root-Locus Plot of G(s) = K/[s(s + 0.5)(s^2 + 0.6s + 10)]')
xlabel('Real Axis')
ylabel('Imag Axis') 
```

Notice that in the regions near x=–0.3, y=2.3 and x=–0.3, y=–2.3 two loci approach each other. We may wonder if these two branches should touch or not. To explore this situation, we may plot the root loci using smaller increments of K in the critical region.

![](image/c00a80df9bb7c8deb83b6be68f331ce25133fc26dcc4d3aab057231dc88ae78a.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -5.8 | 5.7 |
| -4.2 | 4.6 |
| -3.5 | 4.0 |
| -2.8 | 3.3 |
| -2.0 | 2.8 |
| -1.5 | 2.5 |
| -1.0 | 2.3 |
| -0.5 | 2.1 |
| 0.0 | 2.0 |
| 0.5 | 2.2 |
| 1.0 | 2.5 |
| 1.5 | 2.8 |
| 2.0 | 3.3 |
| 2.5 | 3.8 |
| 3.0 | 4.5 |
| 3.5 | 5.0 |
| 4.0 | 5.5 |
| 4.5 | 6.0 |
| 5.0 | 5.5 |
| 5.5 | 5.0 |
| 6.0 | 4.5 |
| 6.5 | 4.0 |
| 7.0 | 3.5 |
| 7.5 | 3.0 |
| 8.0 | 2.5 |
| 8.5 | 2.0 |
| 9.0 | 1.5 |
| 9.5 | 1.0 |
| 10.0 | 0.5 |
| 10.5 | 0.0 |
| 11.0 | -0.5 |
| 11.5 | -1.0 |
| 12.0 | -1.5 |
| 12.5 | -2.0 |
| 13.0 | -2.5 |
| 13.5 | -3.0 |
| 14.0 | -3.5 |
| 14.5 | -4.0 |
| 15.0 | -4.5 |
| 15.5 | -5.0 |
| 16.0 | -5.5 |
| 16.5 | -6.0 |
</details>

Figure 6–17 Root-locus plot.

Root-Locus Plot of G(s) = K/[s(s+0.5)(s2+0.6s+10)]   
![](image/49f3119907f6d791025515382329b0ebe9089d2a28a4fbe392abbe1c30bb8dc2.jpg)
