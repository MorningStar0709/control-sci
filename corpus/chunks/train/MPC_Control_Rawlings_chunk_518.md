# Solution

The exact and sampled density of the importance function q(x) using 5000 samples is the same as Figure 4.17. The weighted density for p(x) is shown in Figure 4.19. Comparing Figure 4.19 to Figure 4.18 shows the representation of the bimodal distribution with 5000 samples using h(x) is of comparable quality to the one using p(x) itself. The bias is not noticeable using 5000 samples. -

Weighted importance sampling. In applications of importance sampling to state estimation, the importance function is often available as a weighted sample in which the weights are not all equal. Therefore, as a final topic in importance sampling, we consider the case in which a weighted sample of the importance function is available

$$q _ {s} (x) = \sum_ {i = 1} ^ {s} w _ {i} ^ {-} \delta (x - x _ {i}) \quad w _ {i} ^ {-} \geq 0$$

We have the two cases of interest covered previously.

(a) We can evaluate $p ( x )$ . For this case we define the sampled density for $p ( x )$ as

$$\overline {{{p}}} _ {s} (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i}) \quad w _ {i} = w _ {i} ^ {-} \frac {p (x _ {i})}{q (x _ {i})}$$

![](image/d5dc991ec88ab8a54731d62b1db1c26184845fc2946b35aedb289928e3a4ae60.jpg)

<details>
<summary>histogram</summary>

| x | p(x) |
| --- | --- |
| -7.5 | 0.005 |
| -6.5 | 0.02 |
| -5.5 | 0.05 |
| -4.5 | 0.11 |
| -3.5 | 0.20 |
| -2.5 | 0.12 |
| -1.5 | 0.08 |
| -0.5 | 0.03 |
| 0.5 | 0.01 |
| 1.5 | 0.02 |
| 2.5 | 0.08 |
| 3.5 | 0.15 |
| 4.5 | 0.20 |
| 5.5 | 0.13 |
| 6.5 | 0.07 |
| 7.5 | 0.01 |
</details>

Figure 4.19: Exact density $p ( x )$ and its histogram based on 5000 importance samples evaluating $h ( x )$ in place of $p ( x ) =$ $h ( x ) / \int h ( x ) d x$ .

For this case, the sampled density is unbiased for all sample sizes and converges to $p ( x )$ as the sample size increases.

(b) We cannot evaluate $p ( x )$ , but can evaluate only $h ( x )$ with $p ( x ) =$ $h ( x ) / \int h ( x ) d x$ . For this case, we define the sampled density as

$$\overline {{p}} _ {s} (x) = \sum_ {i = 1} ^ {s} \overline {{w}} _ {i} \delta (x - x _ {i})w _ {i} = w _ {i} ^ {-} \frac {h (x _ {i})}{q (x _ {i})} \quad \overline {{w}} _ {i} = \frac {w _ {i}}{\sum_ {j} w _ {j}} \tag {4.50}$$

For this case, the sampled density is biased for all finite sample sizes, but converges to $p ( x )$ as the sample size increases.

The proofs of these properties are covered in Exercises 4.21 and 4.22.

![](image/1c6e6ce293cf030a60b507a99cc4b5e0775e17df570fff59731d0e2a73d30f63.jpg)

<details>
<summary>text_image</summary>
