$$
P (s) = \left[ \begin{array}{c c c c c} - 0. 2 & 0. 1 & 1 & 0 & 1 \\ - 0. 0 5 & 0 & 0 & 0 & 0. 7 \\ 0 & 0 & - 1 & 1 & 0 \\ \hline 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \end{array} \right] = \frac {1}{a (s)} \left[ \begin{array}{c c} s & (s + 1) (s + 0. 0 7) \\ - 0. 0 5 & 0. 7 (s + 1) (s + 0. 1 3) \end{array} \right]
$$

where $a ( s ) = ( s + 1 ) ( s + 0 . 1 7 0 7 ) ( s + 0 . 0 2 9 2 9 )$ .

It is appropriate to point out that the skewed problem setup, although more complicated than that of the nonskewed problem, is particularly suitable for control system design. To be more specific, consider the transfer function from w and $\tilde { d }$ to z and e:

$$
\left[ \begin{array}{l} z \\ e \end{array} \right] = G (s) \left[ \begin{array}{l} w \\ \tilde {d} \end{array} \right]
$$

where

$$
\begin{array}{l} G (s) := \left[ \begin{array}{c c} - W _ {2} T _ {i} W _ {1} & - W _ {2} K S _ {o} W _ {d} \\ W _ {e} S _ {o} P W _ {1} & W _ {e} S _ {o} W _ {d} \end{array} \right] \\ = \left[ \begin{array}{c c} - W _ {2} & 0 \\ 0 & W _ {e} \end{array} \right] \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} P & I \end{array} \right] \left[ \begin{array}{c c} W _ {1} & 0 \\ 0 & W _ {d} \end{array} \right] \\ \end{array}
$$

![](image/579cc0399b41059407e752c2dd5650b8e516a8029de6e084b4275710a9fb01f6.jpg)

<details>
<summary>line</summary>

| frequency | condition number |
| --- | --- |
| 10^-3 | ~5 |
| 10^-2 | ~4 |
| 10^-1 | ~2 |
| 10^0 | ~4 |
| 10^1 | ~20 |
| 10^2 | ~200 |
</details>

Figure 8.16: Condition number $\kappa ( \omega ) = \bar { \sigma } ( P ( j \omega ) ) / \underline { { \sigma } } ( P ( j \omega ) )$

Then a suitable performance criterion is to make $\| G ( s ) \| _ { \infty }$ small. Indeed, small $\| G ( s ) \| _ { \infty }$ implies that $T _ { i } , K S _ { o } , S _ { o } P$ and $S _ { o }$ are small in some suitable frequency ranges, which are the desired design specifications discussed in Section 6.1 of Chapter 6. It will be clear in Chapter 16 and Chapter $1 7$ that the $\| G \| _ { \infty }$ is related to the robust stability margin in the gap metric, ν-gap metric, and normalized coprime factor perturbations. Therefore, making $\| G \| _ { \infty }$ small is a suitable design approach.
