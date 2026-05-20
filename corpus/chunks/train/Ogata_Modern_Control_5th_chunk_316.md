$$
\begin{array}{l} \underline {{G (s)}} = \left\lfloor - \frac {K \big (T _ {a} s - 1 \big)}{s (T s + 1)} \right. \\ = \sqrt {\frac {K (T _ {a} s - 1)}{s (T s + 1)}} + 1 8 0 ^ {\circ} \\ = \pm 1 8 0 ^ {\circ} (2 k + 1) \quad (k = 0, 1, 2, \dots) \\ \end{array}
$$

or

$$\underline {{\frac {K (T _ {a} s - 1)}{s (T s + 1)}}} = 0 ^ {\circ} \tag {6-16}$$

The root loci can be obtained from Equation (6–16). Figure 6–26(b) shows a root-locus plot for this system. From the diagram, we see that the system is stable if the gain K is less than $1 / T _ { a }$ .

![](image/5460decf5579a41eea970e36e779662e8647a1a6e74304c9f9c8df21afaa82fb.jpg)  
Figure 6–26

(a) Nonminimumphase system;

(b) root-locus plot.

Figure 6–27 Root-locus plot of $G ( s ) = \frac { K ( \bar { 1 } - 0 . 5 s ) } { s ( s + 1 ) } .$   
![](image/c1d60c36660ca84824cc7d74387ae188f0347c565345d6bcc4c47f1cc30375df.jpg)

<details>
<summary>other</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -1 | 0 |
| 0 | 0 |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
</details>

To obtain a root-locus plot with MATLAB, enter the numerator and denominator as usual. For example, if $T = 1$ sec and $T _ { a } = 0 . 5$ enter the following num and den sec, in the program:

$$\mathrm{num} = [ - 0. 5 \quad 1 ]\mathrm{den} = [ 1 \quad 1 \quad 0 ]$$

MATLAB Program 6–8 gives the plot of the root loci shown in Figure 6–27.

```matlab
MATLAB Program 6–8
num = [-0.5 1];
den = [1 1 0];
k1 = 0:0.01:30;
k2 = 30:1:100;
K3 = 100:5:500;
K = [k1 k2 k3];
rlocus(num,den,K)
v = [-2 6 -4 4]; axis(v); axis('square')
grid
title('Root-Locus Plot of G(s) = K(1 - 0.5s)/[s(s + 1)]')
% Place 'x' mark at each of 2 open-loop poles.
% Place 'o' mark at open-loop zero.
gtext('x')
gtext('x')
gtext('o') 
```

Orthogonality of Root Loci and Constant-Gain Loci. Consider the negative feedback system whose open-loop transfer function is $G ( s ) H ( s )$ . In the $G ( s ) H ( s )$ plane, the loci of $| G ( s ) H ( s ) | =$ constant are circles centered at the origin, and the loci corresponding to $/ G ( s ) H ( s ) = \pm 1 8 0 ^ { \circ } ( 2 k + 1 ) ( k = 0 , 1 , 2 , \ldots )$ lie on the negative real axis of the $G ( s ) H ( s )$ plane, as shown in Figure 6–28. [Note that the complex plane employed here is not the s plane, but the $G ( s ) H ( s )$ plane.]

Figure 6–28 Plots of constantgain and constantphase loci in the $G ( s ) H ( s )$ plane.   
![](image/3c05bc2a09394ba8ed506ba63bed7eba94c63e1cc4ed7691af65dafc1e3ae093.jpg)

<details>
<summary>text_image</summary>

Im
G(s) H(s) Plane
0
Re
|G(s) H(s)| = constant
</details>
