<details>
<summary>radar</summary>

| ω | Real Range | Imaginary Range |
| --- | --- | --- |
| 0.01 | ~8.5 | ~0.0 |
| 0.05 | ~7.5 | ~-0.5 |
| 0.1 | ~6.5 | ~-1.5 |
| 0.2 | ~5.5 | ~-3.5 |
| 0.3 | ~4.5 | ~-5.5 |
| 0.5 | ~3.5 | ~-7.5 |
| 0.8 | ~2.5 | ~-9.5 |
| 1 | ~1.5 | ~-11.5 |
| 2 | ~0.5 | ~-13.5 |
| 3 | ~-0.5 | ~-15.5 |
</details>

Figure 8.5: Uncertain delay system and $G _ { 0 }$

mf= ginput(50) % pick 50 points: the first column of mf is the frequency points and the second column of mf is the corresponding magnitude responses.   
$\scriptstyle \mathbf { m a g g = v p c k ( m f ( : , 2 ) , m f ( : , 1 ) } )$ ; % pack them as a varying matrix.   
$\mathbf { W _ { a } } = \mathbf { f i t m a g ( m a g g ) }$ ; % choose the order of $W _ { a }$ online. A third-order $W _ { a }$ is sufficient for this example.   
$\gg \mathrm { [ { \bf A } , { \bf B } , { \bf C } , { \bf D } ] = u n p c k ( { \bf W _ { a } } ) }$ % converting into state-space.   
$\gg [ \mathbf { Z } , \mathbf { P } , \mathbf { K } ] { = } \mathbf { s s 2 z p } ( \mathbf { A } , \mathbf { B } , \mathbf { C } , \mathbf { D } )$ % converting into zero/pole/gain form.

We get

$$W _ {a} (s) = \frac {0 . 0 3 7 6 (s + 1 1 6 . 4 8 0 8) (s + 7 . 4 5 1 4) (s + 0 . 2 6 7 4)}{(s + 1 . 2 4 3 6) (s + 0 . 5 5 7 5) (s + 4 . 9 5 0 8)}$$

and the frequency response of $W _ { a }$ is also plotted in Figure 8.6. Similarly, define the multiplicative uncertainty

$$\Delta_ {m} (s) := \frac {G (s) - G _ {0} (s)}{G _ {0} (s)}$$

and a $W _ { m }$ can be found such that $| \Delta _ { m } ( j \omega ) | \leq | W _ { m } ( j \omega ) |$ , as shown in Figure 8.7. A $W _ { m }$ is given by

$$W _ {m} = \frac {2 . 8 1 6 9 (s + 0 . 2 1 2) (s ^ {2} + 2 . 6 1 2 8 s + 1 . 7 3 2)}{s ^ {2} + 2 . 2 4 2 5 s + 2 . 6 3 1 9}$$

![](image/39016b2b8cdf89271e5b251b431d3487cb037356d896162e4eb8aeb3bd8f4061.jpg)

<details>
<summary>line</summary>

| x | y (Series 1) | y (Series 2) | y (Series 3) | y (Series 4) | y (Series 5) | y (Series 6) | y (Series 7) | y (Series 8) | y (Series 9) | y (Series 10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10^-2 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 |
| 10^-1 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 |
| 10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 | ~10^0 |
| 10^1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 | ~10^-1 |
| 10^2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 | ~10^-2 |
</details>

Figure 8.6: $\Delta _ { a }$ (dashed line) and a bound $W _ { a }$ (solid line)

![](image/af8a562ea951ad41d0914262ffab5b1ef26c9e7fd1586b3accf6a7cdef41f6bb.jpg)
