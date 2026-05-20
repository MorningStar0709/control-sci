# Example 13.3 Influence of model structure

Let the system be described by the model

$$
\begin{array}{l} y (k) - 1. 5 y (k - 1) + 0. 7 y (k - 2) \\ = u (k - 1) + 0. 5 u (k - 2) + e (k) - e (k - 1) + 0. 2 e (k - 2) \\ \end{array}
$$

where e has zero mean and standard deviation 0.5. This is a “standard” system that has been used often in the literature to test different identification methods. In (13.17), $C(q) \neq q"$ , which implies that the least-squares method will give biased estimates. However, the input-output relation of the process can be approximated by using the least-squares method for a higher-order model. Figure 13.2 shows a simulation of the system. The input is a Pseudo Random Binary Signal (PRBS) sequence with amplitude $\pm1$ . The data have been used to identify models of different orders using the least-squares and maximum-likelihood methods.

Figure 13.3 shows the step responses of the true system in (13.17) and of the estimated models when using the least-squares method with model orders n = 1, 2, and 4, and the maximum-likelihood method when the model order is 2. The least-squares method gives a poor description for a second-order model, and a good model is obtained when the model order is increased to 4. The maximum-likelihood method gives very good estimates of the dynamics and the noise characteristics for a second-order model. The estimated parameters for second-order models when using the least-squares method and the maximum-likelihood method are shown in Table 13.1.

![](image/9ab51c15a2edeb842f9169ac7e6eddaa41203aab4537a7f7a38359f29fde9c4c.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 100 | 8 |
</details>

![](image/47ae15e902504ac57d03ffd7cb96640e6ea4c2b4d8dacae22a0e0f420c922eeb.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 10 | 9 |
| 20 | 8 |
| 30 | 8 |
| 40 | 8 |
| 50 | 8 |
| 60 | 8 |
| 70 | 8 |
| 80 | 8 |
| 90 | 8 |
| 100 | 8 |
</details>

![](image/f0b28fc1d729ddb3ffca0c03c51f5c46c743c40048b5e53887f4c9bd8947b5b1.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 10 | 10 |
| 20 | 7 |
| 30 | 7 |
| 40 | 7 |
| 50 | 7 |
| 60 | 7 |
| 70 | 7 |
| 80 | 7 |
| 90 | 7 |
| 100 | 7 |
</details>

![](image/5afd7151876a1f956d8a6844e4471c5781167185f2c8677af430f1bf0a3c673b.jpg)

<details>
<summary>line</summary>

| Time | Output |
| --- | --- |
| 0 | 0 |
| 10 | 10 |
| 20 | 7 |
| 30 | 8 |
| 40 | 7.5 |
| 50 | 7.5 |
| 60 | 7.5 |
| 70 | 7.5 |
| 80 | 7.5 |
| 90 | 7.5 |
| 100 | 7.5 |
</details>
