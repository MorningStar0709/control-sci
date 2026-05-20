MATLAB Program 6–4 is a program that will generate the root-locus plot as shown in Figure 6–20.

```matlab
MATLAB Program 6–4
% ---- Root-locus plot ----
A = [0 1 0;0 0 1;-160 -56 -14];
B = [0;1;-14];
C = [1 0 0];
D = [0];
K = 0:0.1:400;
rlocus(A,B,C,D,K);
v = [-20 20 -20 20]; axis(v)
grid
title('Root-Locus Plot of System Defined in State Space') 
```

Figure 6–20 Root-locus plot of system defined in state space, where A, B, C, and D are as given by Equation (6–15).   
![](image/cf5c2a24248e70e15aec212e7a781c1746797908d87cd226bc7f6d98cf78a5f3.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -10 | 0 |
| -5 | 3 |
| 0 | 0 |
| 0 | -5 |
</details>

Constant $\boldsymbol { \zeta }$ Loci and Constant $\omega _ { n }$ Loci. Recall that in the complex plane the damping ratio $\zeta$ of a pair of complex-conjugate poles can be expressed in terms of the angle f, which is measured from the negative real axis, as shown in Figure 6–21(a) with

$$\zeta = \cos \phi$$

In other words, lines of constant damping ratio $\zeta$ are radial lines passing through the origin as shown in Figure 6–21(b). For example, a damping ratio of 0.5 requires that the complex-conjugate poles lie on the lines drawn through the origin making angles of $\pm 6 0 ^ { \circ }$ with the negative real axis. (If the real part of a pair of complex-conjugate poles is positive, which means that the system is unstable, the corresponding z is negative.) The damping ratio determines the angular location of the poles, while the distance of the pole from the origin is determined by the undamped natural frequency $\omega _ { n }$ . The constant $\omega _ { n }$ loci are circles.

![](image/058f6c43f2cc0b7675baf5c01c2d2bccc312264248e7f35be46917ec5c2b4563.jpg)

<details>
<summary>text_image</summary>

jω
x
ωₙ
φ
0
σ
ωd
x
</details>

![](image/44a3636328cf64dcfdf293557d7f532766fd142dea11aefa7b5b9041eca59c78.jpg)

<details>
<summary>radar</summary>
