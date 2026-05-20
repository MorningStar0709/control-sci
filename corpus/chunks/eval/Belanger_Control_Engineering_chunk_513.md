# Solution

The TACV specification curve is the piecewise-linear curve shown in Figure 8.20. For design purposes, we approximate it by the magnitude of the function

$$\frac {1}{W _ {1} (s)} = \frac {. 0 2 8 3 (s / 3 9 . 6 + 1) (s / 1 6 3 . 3 + 1)}{(s / 6 . 2 8 + 1)}.$$

It is convenient to generate $y_{R}(t)$ as the output of a filter 0.5/s, driven by an input w. In this way, $T_{wa}(s)=\frac{0.5}{s}T_{y_{R}a}(s)$ , and $T_{w\ell_{1}}(s)=\frac{0.5}{s}T_{y_{R}\ell_{1}}(s)$ , and the frequency weighting is taken care of.

The specifications are, for all $\omega$ :

(i) $|\frac{0.5}{j\omega} T_{yRa}(j\omega)| \leq \frac{1}{|W_1(j\omega)|}$   
(ii) $|\frac{0.5}{j\omega} T_{y_R\ell_1}(j\omega)| \leq 0.15$

We let $z_{1} = W_{1}a$ and $z_{2} = \ell_{1} / 0.15$ , so the specifications become

$$\| T _ {w z _ {i}} \| _ {\infty} \leq 1, \quad i = 1, 2.$$

As it stands, the problem is ill-posed, because there is nothing to limit u. For an order of magnitude on u, we note that a spring extension of 0.15 m results in a force of 450 N. We therefore write

(iii) $|T_{wu}(j\omega)| \leq 450$ , all $\omega$

Defining $z_{3} = (1 / 450)u$ , we write

$$\| T _ {w z _ {3}} \| _ {\infty} \leq 1.$$

![](image/e84816b42d40b8ae168d75416fc447ee62e9fd9d67fbcdd9d73def2fd4cf7554.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | w to a (dB) | w to u (dB) | w to ℓ₁ (dB) |
| --- | --- | --- | --- |
| 0.1 | ~35 | ~0 | ~0 |
| 1 | ~40 | ~0 | ~0 |
| 10 | ~40 | ~-10 | ~-10 |
| 100 | ~20 | ~-40 | ~-60 |
| 1000 | ~-30 | ~-50 | ~-110 |
</details>

Figure 8.17 Weighted transmissions, nominal weights

We use the model developed in Example 7.11 (Chapter 7), since it already includes $y_{R} = (1 / s)w$ . With $y_{R} = (0.5 / s)w$ instead,

$$
\frac {d}{d t} \left[ \begin{array}{l} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & - 1 \\ 0 & 0 & 1 & 0 \\ - 1 0 & 0 & - 2 & 2 \\ 7 2 0 & - 6 6 0 & 1 2 & - 1 2 \end{array} \right] \left[ \begin{array}{l} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ -. 5 \\ 0 \\ 0 \end{array} \right] w + \left[ \begin{array}{c} 0 \\ 0 \\ . 0 0 3 3 4 \\ -. 0 2 \end{array} \right] u
$$

where $\ell_1 = x_1 - x_2$ , $\ell_2 = x_1 - y_R$ . The controllable-canonical realization of $W_1(s)$ , driven by the acceleration, is
