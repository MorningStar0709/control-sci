# Poles

Consider a continuous-time system described by the nth-order state-space model

$$\frac {d x}{d t} = A x + B u \tag {2.35}y = C x$$

The poles of the system are the eigenvalues of A, which we denote by $\lambda_{i}(A), i = 1, \ldots, n$ . The zero-order-hold sampling of (2.35) gives the discrete-time system

$$x (k h + h) = \Phi x (k h) + \Gamma u (k h)y (k h) = C x (k h)$$

Its poles are the eigenvalues of $\Phi, \lambda_i(\Phi), i = 1, \ldots, n$ . Because $\Phi = \exp(Ah)$ it follows from the properties of matrix functions (see Appendix B) that

$$\lambda_ {i} (\Phi) = e ^ {\lambda_ {i} (A) h} \tag {2.36}$$

Equation (2.36) gives the mapping from the continuous-time poles to the discrete-time poles. Figure 2.5 illustrates a mapping of the complex $s$ -plane into the $z$ -plane, when $z = \exp(sh)$ . For instance, the left half of the $s$ -plane is mapped into the unit disc of the $z$ -plane. The map is not bijective—several points in the $s$ -plane are mapped into the same point in the $z$ -plane (see Fig. 2.6). This is an illustration of the aliasing effect discussed in Example 1.4. For poles inside the fundamental strip $S_0$ in Fig. 2.6, there is a simple relationship between continuous- and discrete-time poles. (Also compare with Example 2.5.)

![](image/dc5e2e9ab53c2b1a3950fe7a72b1dbf4bba56ce28f87c83c3c67fa0c49efeca0.jpg)  
Figure 2.5 The conformal map $z = \exp(sh)$ .

![](image/0b4093ee40b01e94f46935822d8863ea3f24ce115c9331c896968d7238b36716.jpg)

<details>
<summary>text_image</summary>

3π/h
p
π/h
P1x
S0 P1x
-π/h
p
-3π/h
px
x
</details>

Figure 2.6 Each strip in the left half of the s-plane is mapped into the unit disc. This means that the pair of poles, $p_{1}$ and $p_{2}$ , are both mapped into the pair p.

![](image/ccab341d405dd8fb46250bcc02f080d2bc719e88a705e1a48456159b7f70cbc6.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1 |
</details>

![](image/d53473fe2301c498f1066e4f5deb6ce6a1722a29083ef3da2dd6d6bea565fe2f.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 1.1 |
| 2.0 | 1.05 |
| 2.5 | 1.02 |
| 3.0 | 1.01 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
| 5.5 | 1.0 |
| 6.0 | 1.0 |
</details>

![](image/d804d9cb3d1d0bc05bd8689e3ca58a4d306bf63e0591a46646c628b3958059d8.jpg)

<details>
<summary>scatter</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 1.0 |
| 3 | 1.1 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
</details>

![](image/c84f8483e251f90ce22f1c6cef47072231b0b7be1abc1238f0db558075057f36.jpg)

<details>
<summary>scatter</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 1 | 0.8 |
| 2 | 1.3 |
| 3 | 1.1 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
</details>

Figure 2.7 Step responses of the discrete-time system in Example 2.16 for different values of h when $\zeta = 0.5$ and $\omega_{0} = 1.83$ , which gives the rise time $T_{r} = 1$ : (a) h = 0.125, (b) h = 0.25, (c) h = 0.5, and (d) h = 1.0.
