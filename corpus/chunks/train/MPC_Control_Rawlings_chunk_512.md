<details>
<summary>line</summary>

| x | u1 | u2 | u3 | u4 | u5 | u6 |
| --- | --- | --- | --- | --- | --- | --- |
| x₁ | 0.1 |  |  |  |  |  |
| x₂ |  | 0.2 |  |  |  |  |
| x₃ |  |  | 0.3 |  |  |  |
| x₄ |  |  |  | 0.5 |  |  |
| x₅ |  |  |  |  | 0.7 |  |
| x₆ |  |  |  |  | 1.0 | 1.0 |
</details>

Figure 4.16: Six samples of the uniform density on [0, 1], $u _ { i }$ , and the corresponding samples of $p ( x ) , x _ { i }$ . The samples satisfy $x _ { i } = P ^ { - 1 } ( u _ { i } )$ .

The weighted sample of p is also unbiased for all sample sizes, which we can verify as follows

$$
\begin{array}{l} \mathcal {E} _ {\text { is }} \left(\overline {{p}} _ {s} (x)\right) = \mathcal {E} _ {\text { is }} \left(\sum_ {i} w _ {i} \delta (x - x _ {i})\right) \\ = \int p _ {\mathrm{is}} (x _ {1}, \dots , x _ {s}) \sum_ {i} w _ {i} \delta (x - x _ {i}) d x _ {1} \dots d x _ {s} \\ = \int q (x _ {1}) \dots q (x _ {s}) \sum_ {i} w _ {i} \delta (x - x _ {i}) d x _ {1} \dots d x _ {s} \\ = \sum_ {i} \int q (x _ {i}) w _ {i} \delta (x - x _ {i}) d x _ {i} \prod_ {j \neq i} \int q (x _ {j}) d x _ {j} \\ = \sum_ {i} \int q (x _ {i}) \frac {1}{s} \frac {p (x _ {i})}{q (x _ {i})} \delta (x - x _ {i}) d x _ {i} \\ = \frac {1}{s} \sum_ {i} p (x) \\ \end{array}
\mathcal {E} _ {\text { is }} \left(\overline {{p}} _ {s} (x)\right) = p (x)
$$

Notice this result holds for all $s \geq 1$ .

Using the same development, we can represent any function h(x) (not necessarily a density) having the same support as $q ( x )$ as a sampled function

$$
\begin{array}{l} \overline {{h}} _ {s} (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i}) \quad w _ {i} = \frac {1}{s} \frac {h (x _ {i})}{q (x _ {i})} \\ \lim _ {s \to \infty} \overline {{h}} _ {s} (x) = h (x) \tag {4.46} \\ \end{array}
$$

The next example demonstrates using importance sampling to generate samples of a multimodal density.
