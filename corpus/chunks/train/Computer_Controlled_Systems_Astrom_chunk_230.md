# Example 4.4 Choice of design parameters

Consider the double-integrator plant. Instead of using the parameters $p_{1}$ and $p_{2}$ of the characteristic equation we will introduce two other parameters, which have a more direct physical interpretation. If the desired discrete-time system is obtained by sampling a second-order system with the characteristic polynomial $s^{2} + 2\zeta\omega s + \omega^{2}$ we find that

$$
\begin{array}{l} p _ {1} = - 2 e ^ {- \zeta \omega h} \cos \left(\omega h \sqrt {1 - \zeta^ {2}}\right) \\ p _ {2} = e ^ {- 2 \zeta \omega h} \\ \end{array}
$$

where $\omega$ is the natural frequency and $\zeta$ is the damping (compare with Example 2.16). The parameter $\zeta$ influences the relative damping of the response and $\omega$ influences the response speed. To discuss the magnitude of the control signal, it is assumed that the system has an initial position $x_{0}$ and an initial velocity $v_{0}$ . The initial value of the control signal is then

$$u (0) = - l _ {1} x _ {0} - l _ {2} v _ {0}$$

If the sampling period is short, then the expressions for $p_{1}$ and $p_{2}$ can be approximated using series expansion. The following approximation is then obtained:

$$u (0) \approx - \omega^ {2} x _ {0} + 2 \zeta \omega v _ {0}$$

![](image/92ec607abe398a12dd5bd299c6c2390afb171bf7e0db8fff500f0b99022ccc4e.jpg)

<details>
<summary>line</summary>

| x | Solid Line | Dashed Line |
| --- | --- | --- |
| 0 | 1.0 | 1.5 |
| 5 | 0.0 | 0.5 |
| 10 | 0.0 | 0.0 |
| 15 | 0.0 | 0.0 |
</details>

![](image/ebd56c9986a850111f1248e0595d32054e65ae2601b5a7c46f50233366c0b8fd.jpg)

<details>
<summary>line</summary>

| x | Input |
| --- | --- |
| 0 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
</details>

![](image/e92663d8ac0e5c92104b33feb2f19ac047e49117577fe9efd46385d54920f3d4.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | -5 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
</details>

![](image/6c333ed826b6fb3ecbd3223bd134d2a26809d7f68970685cdc3e818d5e97a9eb.jpg)

<details>
<summary>line</summary>

| Time | Input |
| --- | --- |
| 0 | -5 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
| 11 | 0 |
| 12 | 0 |
| 13 | 0 |
| 14 | 0 |
| 15 | 0 |
</details>
