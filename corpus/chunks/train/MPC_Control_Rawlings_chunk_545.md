# Solution

The optimal importance function is given in (4.60)

$$q (x _ {i} (k) | x _ {i} (k - 1), y (k)) = p (x _ {i} (k) | x _ {i} (k - 1), y (k))$$

![](image/15f9c0666fce4b4000f7d380add7bbf45cacc9a38d367688bef369f71c07b0f4.jpg)

<details>
<summary>scatter</summary>

| k | x1 | x2 |
| --- | --- | --- |
| 0 | -1.5 | 0.5 |
| 0 | 0.0 | 1.0 |
| 0 | 1.0 | 1.5 |
| 0 | 2.0 | 2.0 |
| 0 | 3.0 | 2.5 |
| 0 | 4.0 | 3.0 |
| 0 | 5.0 | 3.5 |
| 0 | 6.0 | 4.0 |
| 0 | 7.0 | 4.5 |
| 0 | 8.0 | 5.0 |
| 0 | 9.0 | 5.5 |
| 0 | 10.0 | 6.0 |
| 0 | 11.0 | 6.5 |
| 0 | 12.0 | 7.0 |
| 0 | 13.0 | 7.5 |
| 0 | 14.0 | 8.0 |
| 1 | -1.5 | 1.0 |
| 1 | 0.0 | 1.5 |
| 1 | 1.0 | 2.0 |
| 1 | 2.0 | 2.5 |
| 1 | 3.0 | 3.0 |
| 1 | 4.0 | 3.5 |
| 1 | 5.0 | 4.0 |
| 1 | 6.0 | 4.5 |
| 1 | 7.0 | 5.0 |
| 1 | 8.0 | 5.5 |
| 1 | 9.0 | 6.0 |
| 1 | 10.0 | 6.5 |
| 1 | 11.0 | 7.0 |
| 1 | 12.0 | 7.5 |
| 1 | 13.0 | 8.0 |
| 1 | 14.0 | 8.5 |
| 2 | -1.5 | 2.0 |
| 2 | 0.0 | 2.5 |
| 2 | 1.0 | 3.0 |
| 2 | 2.0 | 3.5 |
| 2 | 3.0 | 4.0 |
| 2 | 4.0 | 4.5 |
| 2 | 5.0 | 5.0 |
| 2 | 6.0 | 5.5 |
| 2 | 7.0 | 6.0 |
| 2 | 8.0 | 6.5 |
| 2 | 9.0 | 7.0 |
| 2 | 10.0 | 7.5 |
| 2 | 11.0 | 8.0 |
| 2 | 12.0 | 8.5 |
| 2 | 13.0 | 9.0 |
| 2 | 14.0 | 9.5 |
| 3 | -1.5 | -1.0 |
| 3 | -1.5 | -1.5 |
| 3 | -1.5 | -2.0 |
| 3 | -1.5 | -2.5 |
| 3 | -1.5 | -3.0 |
| 3 | -1.5 | -3.5 |
| 3 | -1.5 | -4.0 |
| 3 | -1.5 | -4.5 |
| 3 | -1.5 | -5.0 |
| 3 | -1.5 | -5.5 |
| 3 | -1.5 | -6.0 |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  | nan |  |

Note: The data is grouped into four groups based on the same parameters (k). The x-axis label 'x₁' and y-axis label 'x₂' are explicitly provided in the image.
</details>

Figure 4.25: Particles’ locations versus time using the optimal importance function; 250 particles. Ellipses show the 95% contour of the true conditional densities before and after measurement.

The conditional density on the right-hand side is given by

$$p (x _ {i} (k) | x _ {i} (k - 1), y (k)) \sim N (\overline {{x}} (k), \overline {{P}})\overline {{x}} (k) = \overline {{P}} \left(Q ^ {- 1} (A x _ {i} (k - 1) + B u (k - 1)) + C ^ {\prime} R ^ {- 1} y (k)\right)\overline {{P}} = \left(Q ^ {- 1} + C ^ {\prime} R ^ {- 1} C\right) ^ {- 1}$$
