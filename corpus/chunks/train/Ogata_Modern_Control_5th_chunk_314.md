Figure 6–22 Constant $\zeta$ lines and constant $\omega _ { n }$ circles.

then enter MATLAB Program 6–6 into the computer. The resulting root-locus plot is shown in Figure 6–23.

```matlab
MATLAB Program 6–6
num = [1];
den = [1 4 5 0];
K = 0:0.01:1000;
r = rlocus(num,den,K);
plot(r,'-'); v = [-3 1 -2 2]; axis(v); axis('square')
sgrid([0.5,0.707], [0.5,1,2])
grid
title('Root-Locus Plot with \zeta = 0.5 and 0.707 Lines and \omega_n = 0.5,1, and 2 Circles')
xlabel('Real Axis'); ylabel('Imag Axis')
gtext('\omega_n = 2')
gtext('\omega_n = 1')
gtext('\omega_n = 0.5')
% Place 'x' mark at each of 3 open-loop poles.
gtext('x')
gtext('x')
gtext('x') 
```

If we want to omit either the entire constant $\zeta$ lines or entire constant $\omega _ { n }$ circles, we may use empty brackets [ ] in the arguments of the sgrid command.For example,if we want to overlay only the constant damping ratio line corresponding to $\zeta = 0 . 5$ and no constant $\omega _ { n }$ circles on the root-locus plot, then we may use the command

sgrid(0.5, [])

![](image/ecd3c871ebc4aa2c9967883ecb7e1e259d50f1520c6a15b11faa4269aa9b9c2e.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imag Axis | Line Width (c) |
| --- | --- | --- |
| -2.0 | 1.0 | 0.707 |
| -2.0 | -1.0 | 0.707 |
| 0.0 | 0.0 | 0.5 |
| 0.0 | -2.0 | 0.5 |
</details>

Figure 6–23

Constant z lines and constant $\omega _ { n }$ circles superimposed on a root-locus plot.

Figure 6–24  
Control system.   
![](image/8a67a6770e74997734d54c29d267c074f1fd2e4b2cdcba69e2431f3498cbf744.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["K(s² + 2s + 4)/s(s + 4)(s + 6)(s² + 1.4s + 1)"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

Conditionally Stable Systems. Consider the negative feedback system shown in Figure 6–24.We can plot the root loci for this system by applying the general rules and procedure for constructing root loci, or use MATLAB to get root-locus plots. MAT-LAB Program 6–7 will plot the root-locus diagram for the system. The plot is shown in Figure 6–25.

MATLAB Program 6–7   
```matlab
num = [1 2 4];
den = conv(conv([1 4 0], [1 6]), [1 1.4 1]);
rlocus(num, den)
v = [-7 3 -5 5]; axis(v); axis('square')
grid
title('Root-Locus Plot of G(s) = K(s^2 + 2s + 4)/[s(s + 4)(s + 6)(s^2 + 1.4s + 1)]')
text(1.0, 0.55, 'K = 12')
text(1.0, 3.0, 'K = 73')
text(1.0, 4.15, 'K = 154') 
```
