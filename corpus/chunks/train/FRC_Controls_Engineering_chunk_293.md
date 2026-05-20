# 9.5.2 Single noisy observations

Variable $z _ { 1 }$ is the noisy measurement of the variable x. The value of the noisy measurement is the random variable defined by the probability density function $p ( z _ { 1 } | x )$ .

The probability density function of x given the measurement $z _ { 1 }$ is

$$p (x | z _ {1}) = \frac {p (x , z _ {1})}{p (z _ {1})} = \frac {p (z _ {1} | x) p (x)}{p (z _ {1})}$$

where $\begin{array} { r } { p ( z _ { 1 } ) = \int _ { X } p ( z _ { 1 } | x ) } \end{array}$ dx, but $z _ { 1 }$ is given so we can write

$$p (x | z _ {1}) = \frac {1}{C} p (z _ {1} | x) p (x) \quad \text { or } \quad p (x | z _ {1}) \sim p (z _ {1} | x) p (x)$$

The probability density $p ( x | z _ { 1 } )$ summarizes our complete knowledge about x.

![](image/33309735e8e2ddf0f9e05ee9184d79a7b3574aa5bd9432202a1be3885fef93a1.jpg)

In both the single and double measurement cases, the estimation of the variable x is a data/information fusion problem. In the single measurement case, we combine the prior probability with the probability resulting from the measurement.
