# Ladder Realizations

Ladder realizations are other representations that avoid the coefficient sensitivity in the implementations. One representation of the ladder network is obtained by making a continued-fraction expansion in the pulse-transfer operator in the following way:

$$H (z) = \alpha_ {0} + \frac {1}{\beta_ {1} z + \frac {1}{\alpha_ {1} + \frac {1}{\beta_ {2} z + \frac {1}{\vdots}}} \alpha_ {n - 1} + \frac {1}{\beta_ {n} z + \frac {1}{\alpha_ {n}}}} \tag {9.20}$$

Another realization is obtained by making the continued-fraction expansion in $z^{-1}$ . The ladder forms have low sensitivity against coefficient errors and round-off errors. If

$$H (z) = \frac {B (z)}{A (z)}$$

where $\deg A(z) = \deg B(z) = n$ , the coefficients $\alpha_{i}$ and $\beta_{i}$ can be computed in the following way: Compute $\alpha_{0} = B(z)\operatorname{div}A(z)$ , $A_{1}(z) = A(z)$ , and $B_{1}(z) = B(z)\bmod A(z)$ and repeat for $i = 1$ to $n$

$$
\begin{array}{l} \beta_ {i} = A _ {i} \operatorname{div} z B _ {i} \quad A _ {i + 1} = A _ {i} \bmod z B _ {i} \\ \alpha_ {i} = B _ {i} \operatorname{div} A _ {i + 1} \quad B _ {i + 1} = B _ {i} \bmod A _ {i + 1} \\ \end{array}
$$

The ladder-network representation can be expressed by the following state equations:

$$
\begin{array}{l} \beta_ {1} x _ {1} (k + 1) = \frac {1}{\alpha_ {1}} \left(x _ {2} (k) - x _ {1} (k)\right) + u (k) \\ \beta_ {2} x _ {2} (k + 1) = \frac {1}{\alpha_ {1}} \left(x _ {1} (k) - x _ {2} (k)\right) + \frac {1}{\alpha_ {2}} \left(x _ {3} (k) - x _ {2} (k)\right) \\ \beta_ {i} x _ {i} (k + 1) = \frac {1}{\alpha_ {i - 1}} \left(x _ {i - 1} (k) - x _ {i} (k)\right) + \frac {1}{\alpha_ {i}} \left(x _ {i + 1} (k) - x _ {i} (k)\right) \\ \end{array}
$$

•
•
•

•
•
•

$$\beta_ {n} x _ {n} (k + 1) = \frac {1}{\alpha_ {n - 1}} \left(x _ {n - 1} (k) - x _ {n} (k)\right) - \frac {1}{\alpha_ {n}} x _ {n} (k)y (k) = x _ {1} (k) + \alpha_ {0} u (k)$$

![](image/7c5b72e6554cfa107b968f845a4122160758745faf8a776ebafa97199fd20578.jpg)

<details>
<summary>flowchart</summary>
