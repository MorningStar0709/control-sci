$$
G (s) = \left[ \begin{array}{c c} \left[ \begin{array}{c c} W _ {e} P _ {1} & 0 \\ 0 & 0 \end{array} \right] & \left[ \begin{array}{c} W _ {e} P _ {2} \\ W _ {u} \end{array} \right] \\ \left[ \begin{array}{c c} P _ {1} & W _ {n} \end{array} \right] & P _ {2} \end{array} \right]
$$

where $P _ { 1 }$ and $P _ { 2 }$ denote the transfer matrices from $F _ { 1 }$ and $F _ { 2 }$ to $\left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right]$ , respectively. Let

$$W _ {1} = \frac {5}{s / 2 + 1}, W _ {2} = 0.$$

That is, we only want to reject the effect of the disturbance force $F _ { 2 }$ on the position $x _ { 1 }$ . Then the optimal $\mathcal { H } _ { 2 }$ performance is $\| \mathcal { F } _ { \ell } ( G , K _ { 2 } ) \| _ { 2 } = 2 . 6 5 8 4$ and the $\mathcal { H } _ { \infty }$ performance with the optimal $\mathcal { H } _ { 2 }$ controller is $\| \mathcal { F } _ { \ell } ( G , K _ { 2 } ) \| _ { \infty } = 2 . 6 0 7 9$ while the optimal $\mathcal { H } _ { \infty }$ performance with an $\mathcal { H } _ { \infty }$ controller is $\Vert \mathcal { F } _ { \ell } ( G , K _ { \infty } ) \Vert _ { \infty } = 1 . 6 1 0 1$ . This means that the effect of the disturbance force $F _ { 2 }$ in the desired frequency rang $0 \leq \omega \leq 2$ will be effectively reduced with the $\mathcal { H } _ { \infty }$ controller $K _ { \infty }$ by $5 / 1 . 6 1 0 1 = 3 . 1 0 5 4$ times at $x _ { 1 }$ . On the other hand, let

$$W _ {1} = 0, \quad W _ {2} = \frac {5}{s / 2 + 1}.$$

That is, we only want to reject the effect of the disturbance force $F _ { 2 }$ on the position $x _ { 2 } .$ Then the optimal $\mathcal { H } _ { 2 }$ performance is $\| \mathcal { F } _ { \ell } ( G , K _ { 2 } ) \| _ { 2 } = 0 . 1 6 5 9$ and the $\mathcal { H } _ { \infty }$ performance with the optimal $\mathcal { H } _ { 2 }$ controller is $\| \mathcal { F } _ { \ell } ( G , K _ { 2 } ) \| _ { \infty } = 0 . 5 2 0 2$ while the optimal $\mathcal { H } _ { \infty }$ performance with an $\mathcal { H } _ { \infty }$ controller is $\| \mathcal { F } _ { \ell } ( G , K _ { \infty } ) \| _ { \infty } = 0 . 5 1 8 9$ . This means that the effect of the disturbance force $F _ { 2 }$ in the desired frequency rang $0 \leq \omega \leq 2$ will be effectively reduced with the $\mathcal { H } _ { \infty }$ controller $K _ { \infty }$ by $5 / 0 . 5 1 8 9 = 9 . 6 3 5 8$ times at $x _ { 2 }$ .

![](image/4ee4d7a17085002eccb9593ab3c8c7e0e28eafae529bb01f7fcacf38d12189c7.jpg)

<details>
<summary>line</summary>

| frequency (rad/sec) | H∞ Control | H₂ Control |
| --- | --- | --- |
| 0.1 | ~4.5 | ~4.5 |
| 1.0 | ~6.0 | ~6.0 |
| 10.0 | ~3.0 | ~0.5 |
</details>
