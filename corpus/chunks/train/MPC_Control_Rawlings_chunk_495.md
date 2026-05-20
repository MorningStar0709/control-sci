# Solution

First we take samples $x _ { i }$ from $N ( 0 , 1 )$ for $\xi .$ Figure 4.8 shows the histogram of the sampled density for 5000 samples. Next we compute $y _ { i } = e _ { i } ^ { x }$ to generate the samples of η. The histogram of this sampled density is shown in Figure 4.9. Notice the good agreement between the sampled density and the lognormal density, which is shown as the continuous curve in Figure 4.9. -

Noninvertible transformations. Next consider η to be a noninvertible transformation of $\xi$

$$\eta = f (\xi) \quad f \text { not invertible }$$

Let $\xi \mathrm { s }$ sampled density be given by $\{ x _ { i } , w _ { i } \}$ . The sampled density $\{ f ( x _ { i } ) , w _ { i } \}$ remains a valid sampled density for $\eta ,$ which we show next

$$\xi \sim \{x _ {i}, w _ {i} \} \quad \eta \sim \{f (x _ {i}), w _ {i} \}$$

We wish to show that

$$\mathcal {E} _ {p _ {\eta}} (g (\eta)) = \mathcal {E} _ {p _ {\xi}} (g (f (\xi))) \quad \text { for all } g (\cdot)$$

Taking the expectations

$$\int p _ {\eta} (y) g (y) d y = \int p _ {\xi} (x) g (f (x)) d x$$

![](image/56063fff4f2156cb7d7b78b1b45564c1a5699f24735e1c98ebc5e8337af2d770.jpg)

<details>
<summary>histogram</summary>

| x | pξ |
| --- | --- |
| -4.0 | 0.0000 |
| -3.9 | 0.0000 |
| -3.8 | 0.0000 |
| -3.7 | 0.0000 |
| -3.6 | 0.0000 |
| -3.5 | 0.0000 |
| -3.4 | 0.0000 |
| -3.3 | 0.0000 |
| -3.2 | 0.0000 |
| -3.1 | 0.0000 |
| -3.0 | 0.0000 |
| -2.9 | 0.0000 |
| -2.8 | 0.0000 |
| -2.7 | 0.0000 |
| -2.6 | 0.0000 |
| -2.5 | 0.0000 |
| -2.4 | 0.0000 |
| -2.3 | 0.0000 |
| -2.2 | 0.0000 |
| -2.1 | 0.0000 |
| -2.0 | 0.0000 |
| -1.9 | 0.0000 |
| -1.8 | 0.0000 |
| -1.7 | 0.0000 |
| -1.6 | 0.0000 |
| -1.5 | 0.0000 |
| -1.4 | 0.0000 |
| -1.3 | 0.0000 |
| -1.2 | 0.0000 |
| -1.1 | 0.0000 |
| -1.0 | 0.0000 |
| -0.9 | 0.0000 |
| -0.8 | 0.0000 |
| -0.7 | 0.0000 |
| -0.6 | 0.0000 |
| -0.5 | 0.0000 |
| -0.4 | 0.0000 |
| -0.3 | 0.0000 |
| -0.2 | 0.0000 |
| -0.1 | 0.0000 |
| 0.0 | 0.5125 |
| 0.1 | 1.4989 |
| 0.2 | 1.4989 |
| 0.3 | 1.4989 |
| 0.4 | 1.4989 |
| 0.5 | 1.4989 |
| 0.6 | 1.4989 |
| 0.7 | 1.4989 |
| 0.8 | 1.4989 |
| 0.9 | 1.4989 |
| 1.0 | 1.4989 |
| 1.1 | 1.4989 |
| 1.2 | 1.4989 |
| 1.3 | 1.4989 |
| 1.4 | 1.4989 |
| 1.5 | 1.4989 |
| 1.6 | 1.4989 |
| 1.7 | 1.4989 |
| 1.8 | 1.4989 |
| 1.9 | 1.4989 |
| 2.0 | 1.4989 |
| 2.1 | 1.4989 |
| 2.2 | 1.4989 |
| 2.3 | 1.4989 |
| 2.4 | 1.4989 |
| 2.5 | 1.4989 |
| 2.6 | 1.4989 |
| 2.7 | 1.4989 |
| 2.8 | 1.4989 |
| 2.9 | 1.4989 |
| 3.0 | 1.4989 |
| 3.1 | 1.4989 |
| 3.2 | 1.4989 |
| 3.3 | 1.4989 |
| 3.4 | 1.4989 |
| 3.5 | 1.4989 |
| 3.6 | 1.4989 |
| 3.7 | 1.4989 |
| 3.8 | 1.4989 |
| 3.9 | 1.4989 |
| 4.0 | 1.4989 |
</details>
