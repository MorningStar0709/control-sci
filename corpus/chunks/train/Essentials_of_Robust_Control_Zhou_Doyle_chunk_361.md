$$
\left[ \begin{array}{c} e \\ \tilde {u} \end{array} \right] = \left[ \begin{array}{c c} W _ {e} (I + P K) ^ {- 1} & W _ {e} (I + P K) ^ {- 1} P \\ - W _ {u} K (I + P K) ^ {- 1} & - W _ {u} K (I + P K) ^ {- 1} P \end{array} \right] \left[ \begin{array}{c} d \\ d _ {i} \end{array} \right] =: T _ {z w} \left[ \begin{array}{c} d \\ d _ {i} \end{array} \right].
$$

Then the problem can be set up in an LFT framework with

$$
G (s) = \left[ \begin{array}{c c c} W _ {e} & W _ {e} P & - W _ {e} P \\ 0 & 0 & - W _ {u} \\ \hdashline I & P & - P \end{array} \right] = \left[ \begin{array}{c c c c c c c} - 0. 2 & 2 & 2 & 0 & 2 & 0 & 0 \\ 0 & - 1 & 0 & 0 & 0 & 2 0 & - 2 0 \\ 0 & 0 & - 2 & 0 & 0 & 3 0 & - 3 0 \\ 0 & 0 & 0 & - 1 0 & 0 & 0 & - 3 \\ \hline 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & - 3 & 0 & 0 & - 1 \\ \hdashline 0 & 1 & 1 & 0 & 1 & 0 & 0 \end{array} \right].
$$

A suboptimal $\mathcal { H } _ { \infty }$ controller can be computed by using the following command:

$$\gg \left[ \mathbf {K}, \mathbf {T} _ {\mathbf {z w}}, \gamma_ {\text { subopt }} \right] = \operatorname{hinfsyn} (\mathbf {G}, \mathbf {n} _ {\mathbf {y}}, \mathbf {n} _ {\mathbf {u}}, \gamma_ {\min}, \gamma_ {\max}, \mathbf {t o l})$$

where $n _ { y }$ and $n _ { u }$ are the dimensions of $y$ and u; $\gamma _ { \mathrm { m i n } }$ and $\gamma _ { \mathrm { m a x } } ~ \mathrm { a r e } .$ , respectively a lower bound and an upper bound for $\gamma _ { \mathrm { o p t } } ;$ and tol is a tolerance to the optimal value. Set $n _ { y } = 1 , n _ { u } = 1 , \gamma _ { \operatorname* { m i n } } = 0 , \gamma _ { \operatorname* { m a x } } = 1 0$ , $\mathrm { t o l } = 0 . 0 0 0 1$ ; we get $\gamma _ { \mathrm { s u b o p t } } = 0 . 7 8 4 9$ and a suboptimal controller

$$K = \frac {1 2 . 8 2 (s / 1 0 + 1) (s / 7 . 2 7 + 1) (s / 1 . 4 + 1)}{(s / 3 2 4 4 9 4 4 7 . 6 7 + 1) (s / 2 2 . 1 9 + 1) (s / 1 . 4 + 1) (s / 0 . 2 + 1)}.$$

If we set tol = 0.01, we would get $\gamma _ { \mathrm { s u b o p t } } = 0 . 7 8 7 5$ and a suboptimal controller

$$\tilde {K} = \frac {1 2 . 7 8 (s / 1 0 + 1) (s / 7 . 2 7 + 1) (s / 1 . 4 + 1)}{(s / 2 3 3 5 . 5 9 + 1) (s / 2 1 . 9 7 + 1) (s / 1 . 4 + 1) (s / 0 . 2 + 1)}.$$

The only significant difference between K and $\tilde { K }$ is the exact location of the far-away stable controller pole. Figure 14.1 shows the closed-loop frequency response of $\overline { { \tau } } \left( T _ { z w } \right)$ and Figure 14.2 shows the frequency responses of S, T, KS, and SP .

![](image/89b317781ea236b3e65e8408a5cacd7f219ccdb85037d114fcce4d304fd8d185.jpg)

<details>
<summary>line</summary>

| frequency (rad/sec) | Value |
| --- | --- |
| 0.01 | 1.0 |
| 0.1 | 1.0 |
| 1 | 1.0 |
| 10 | 1.0 |
| 100 | 1.0 |
| 1000 | 0.5 |
| 10000 | 0.1 |
</details>
