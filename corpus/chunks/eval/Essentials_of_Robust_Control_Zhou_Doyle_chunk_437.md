<table><tr><td rowspan="2"> $K = 0.1$ </td><td> $r$ </td><td>0.5</td><td>0.7</td><td>0.9</td><td>1.1</td><td>1.3</td><td>1.5</td></tr><tr><td> $b_{\text{opt}}(P_1)$ </td><td>0.0125</td><td>0.0075</td><td>0.0025</td><td>0.0025</td><td>0.0074</td><td>0.0124</td></tr><tr><td rowspan="2"> $K = 1$ </td><td> $r$ </td><td>0.5</td><td>0.7</td><td>0.9</td><td>1.1</td><td>1.3</td><td>1.5</td></tr><tr><td> $b_{\text{opt}}(P_1)$ </td><td>0.1036</td><td>0.0579</td><td>0.0179</td><td>0.0165</td><td>0.0457</td><td>0.0706</td></tr><tr><td rowspan="2"> $K = 10$ </td><td> $r$ </td><td>0.5</td><td>0.7</td><td>0.9</td><td>1.1</td><td>1.3</td><td>1.5</td></tr><tr><td> $b_{\text{opt}}(P_1)$ </td><td>0.0658</td><td>0.0312</td><td>0.0088</td><td>0.0077</td><td>0.0208</td><td>0.0318</td></tr></table>

![](image/e418512cc5ef007acaa4828333a2b2765a093ea3264e12d107dfc5cb0e4428fb.jpg)

<details>
<summary>line</summary>

| x | K=10 | K=1 | K=0.1 |
| --- | --- | --- | --- |
| 10^-2 | 10^1 | 10^0 | 10^-1 |
| 10^-1 | 10^1 | 10^0 | 10^-1 |
| 10^0 | 10^0 | 10^-1 | 10^-1 |
| 10^1 | 10^-1 | 10^-2 | 10^-2 |
| 10^2 | 10^-2 | 10^-3 | 10^-3 |
</details>

Figure 16.7: Frequency responses of $P _ { 1 }$ for $r = 0 . 9$ and $K = 0 . 1 , 1$ , and 10

Example 16.2 Consider a nonminimum phase plant

$$P _ {2} (s) = \frac {K (s - 1)}{s (s + 1)}.$$

The frequency responses of $P _ { 2 } ( s )$ with $K = 0 . 1 , 1$ , and 10 are shown in Figure 16.8. The following table shows clearly that $b _ { \mathrm { o p t } } ( P _ { 2 } )$ will be small if $| P _ { 2 } ( j \omega ) |$ is large around $\omega = 1$ , the modulus of the right-half plane zero.

<table><tr><td>K</td><td>0.01</td><td>0.1</td><td>1</td><td>10</td><td>100</td></tr><tr><td> $b_{\text{opt}}(P_2)$ </td><td>0.7001</td><td>0.6451</td><td>0.3827</td><td>0.0841</td><td>0.0098</td></tr></table>

![](image/643c94f4eb3ddd8ac676ef7383db829f045984d99ca6e548da48a5614089226f.jpg)

<details>
<summary>line</summary>

| x | K=10 | K=1 | K=0.1 |
| --- | --- | --- | --- |
| 10^-2 | 10^3 | 10^2 | 10^1 |
| 10^-1 | 10^2 | 10^1 | 10^0 |
| 10^0 | 10^1 | 10^0 | 10^-1 |
| 10^1 | 10^0 | 10^-1 | 10^-2 |
| 10^2 | 10^-1 | 10^-2 | 10^-3 |
</details>

Figure 16.8: Frequency responses of $P _ { 2 }$ for $K = 0 . 1 , 1$ , and 10
