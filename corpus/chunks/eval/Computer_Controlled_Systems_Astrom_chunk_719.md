# Example 12.3 Influence of prediction horizon

Consider the process in Example 12.2. From (12.19) it follows that the variance of the prediction error will increase with the prediction horizon. Also (12.17) shows that the F-polynomial is obtained from the division of the C- and A-polynomials. That is, the coefficients $f_{i}$ are the coefficients of the impulse response of the system. Thus

$$
\begin{array}{l} y (k) = \frac {C (q)}{A (q)} e (k) = \frac {q ^ {2} - 0 . 2 q + 0 . 5}{q ^ {2} - 1 . 5 q + 0 . 7} e (k) \\ = (1 + 1. 3 q ^ {- 1} + 1. 7 5 q ^ {- 2} + 1. 7 1 5 q ^ {- 3} + \dots) e (k) = \sum_ {j = 0} ^ {\infty} f _ {j} e (k - j) \\ \end{array}
$$

and the prediction loss is

$$\mathbf {E} \bar {y} ^ {2} (k + m \mid k) = \sigma^ {2} \sum_ {j = 0} ^ {m - 1} f _ {j} ^ {2}$$

Figure 12.2 shows the variance of the prediction error for different values of the prediction horizon m. It is seen that the variance of the prediction error is monotonically increasing with m. Figure 12.3 shows the output, the predicted output, and the accumulated prediction loss, $\sum(y(k)-\hat{y}(k+k-m))^{2}$ , for different prediction horizons.

![](image/7648d6d36e1835019c4aca624033b53d0c0491a5cf52055023c553b0b0acfb41.jpg)

<details>
<summary>scatter</summary>

| Prediction horizon m | Error variance |
| --- | --- |
| 0 | 0 |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |
| 6 | 11 |
| 7 | 11 |
| 8 | 11 |
| 9 | 11 |
| 10 | 11 |
| 11 | 11 |
| 12 | 11 |
| 13 | 11 |
| 14 | 11 |
| 15 | 11 |
| 16 | 11 |
| 17 | 11 |
| 18 | 11 |
| 19 | 11 |
| 20 | 11 |
| 21 | 11 |
| 22 | 11 |
| 23 | 11 |
| 24 | 11 |
| 25 | 11 |
</details>

Figure 12.2 The variance of the prediction error as function of the prediction horizon m for the system in Example 12.3.

![](image/61c5fa10584805eee8999077b7f8c0bb9d83d7c23d5e86fcff781840f5741caa.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 10 | -2.0 |
| 20 | 8.0 |
| 30 | -4.0 |
| 40 | 10.0 |
| 50 | -6.0 |
| 60 | 12.0 |
| 70 | -8.0 |
| 80 | 10.0 |
| 90 | -4.0 |
| 100 | 2.0 |
</details>

![](image/1e3a22a55719056fa8a771f1bc53b4ddb36bd0cc1b97400924ab98caaf67bf96.jpg)

<details>
<summary>line</summary>

| x | y (solid) | y (dashed) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10 | -2 | -3 |
| 20 | 5 | 4 |
| 30 | -5 | -6 |
| 40 | 8 | 7 |
| 50 | -3 | -4 |
| 60 | 10 | 9 |
| 70 | -1 | -2 |
| 80 | 3 | 2 |
| 90 | -4 | -5 |
| 100 | 2 | 1 |
</details>

![](image/3b844918c6b1dac2c06edb190fa625284a6e17c87d70b8e068727cf555030bae.jpg)

<details>
<summary>line</summary>
