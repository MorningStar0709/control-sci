# Example 8.9 As in Example 8.8, let

$$P (s) = \frac {1}{s ^ {2} + 0 . 2 s + 1}; \quad W _ {1} (s) = \frac {s + 1}{(s + . 0 1) (s + 1 0)}W _ {2} (s) = 1; \quad W _ {3} (s) = 2 \times 1 0 ^ {- 3} (s + 1 0) ^ {2}.$$

The design objectives are:

(i) $|Ty_d e^{(j\omega)} W_1(j\omega)| \leq 0.1$ , all $\omega$ .   
(ii) $|Ty_d u(j\omega)| \leq 1$ , all $\omega$ .   
(iii) $|Ty_{d}y(j\omega)W_{3}(j\omega)| \leq 1$ , all $\omega$ .

If possible, obtain $H^{2}$ and $H^{\infty}$ controllers that meet those specifications.

Solution The output of $W_{1}$ , driven by $e$ , is $z_{1}$ ; therefore, specification (i) is $|T_{y_d z_1}(j\omega)| \leq 0.1$ . We redefine $z_{1}$ by multiplying it by 10, to normalize all three specifications to an RHS of 1.

Since $z_{2} = u$ and $z_{3} = W_{3}y$ , we have

$$\| T _ {y _ {d} z _ {i}} \| _ {\infty} \leq 1, \quad i = 1, 2, 3.$$

From Example 8.8, the state description is

$$
A = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - 1 & - 0. 2 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ - 1 & 0 & - 0. 1 & - 1 0. 0 1 \end{array} \right]; \quad B _ {1} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 1 \end{array} \right]; \quad B _ {2} = \left[ \begin{array}{l} 0 \\ 1 \\ 0 \\ 0 \end{array} \right]

C _ {1} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ . 1 9 8 & . 0 3 9 6 & 0 & 0 \end{array} \right]; \quad C _ {2} = \left[ \begin{array}{l l l l} - 1 & 0 & 0 & 0 \end{array} \right]

D _ {1 2} = \left[ \begin{array}{c} 0 \\ 1 \\ 2 \times 1 0 ^ {- 3} \end{array} \right]; \quad D _ {2 1} = 1.
$$

With the multiplication of $z_{1}$ by 10, the matrix $C_{1}$ becomes

$$
C _ {1} = \left[ \begin{array}{c c c c} 0 & 0 & 1 0 & 1 0 \\ 0 & 0 & 0 & 0 \\ . 1 9 8 & . 0 3 9 6 & 0 & 0 \end{array} \right].
$$

Figure 8.15 shows the result of the $H^{2}$ design (MATLAB h2syn); the $\infty$ -norm of the closed-loop system is computed to be 0.355.

![](image/f3220f18296af58d73aaba65b3ca79306636fecf3721beaf04a76ade97b21f84.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | y_d to e (dB) | y_d to u (dB) | y_d to y (dB) |
| --- | --- | --- | --- |
| 0.1 | ~0 | ~0 | ~-20 |
| 1 | ~-20 | ~-25 | ~-30 |
| 10 | ~-40 | ~-60 | ~-80 |
| 100 | ~-60 | ~-90 | ~-120 |
</details>

Figure 8.15 Weighted transmissions for the $H^2$ design

![](image/1616d3e1ce842340b0c8550a90e1c84b18d951533958a537fcc047e949df83b3.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | y_d to u (dB) | y_d to e (dB) | y_d to y (dB) |
| --- | --- | --- | --- |
| 0.1 | ~0 | ~-15 | ~-20 |
| 1 | ~-5 | ~-10 | ~-30 |
| 10 | ~-20 | ~-25 | ~-60 |
| 100 | ~-40 | ~-40 | ~-90 |
</details>

Figure 8.16 Weighted transmissions for the $H^{\infty}$ design

In Figure 8.16, we display the $H^{\infty}$ solution (MATLAB hinfsyn), which is really quite similar to the $H^{2}$ case. The $\infty$ -norm of the closed-loop system is 0.336, only slightly less than that of the $H^{2}$ solution.
