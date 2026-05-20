# Exercise 1.37: Conditional densities are positive definite

We show in Example A.44 that if $\xi$ and η are jointly normally distributed as

$$
\begin{array}{l} \left[ \begin{array}{c} \xi \\ \eta \end{array} \right] \sim N (m, P) \\ \sim N \left(\left[ \begin{array}{c} m _ {x} \\ m _ {y} \end{array} \right], \left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right]\right) \\ \end{array}
$$

then the conditional density of $\xi$ given η is also normal

$$(\xi | \eta) \sim N (m _ {x | y}, P _ {x | y})$$

in which the conditional mean is

$$m _ {x \mid y} = m _ {x} + P _ {x y} P _ {y} ^ {- 1} (y - m _ {y})$$

and the conditional covariance is

$$P _ {x | y} = P _ {x} - P _ {x y} P _ {y} ^ {- 1} P _ {y x}$$

Given that the joint density is well defined, prove the marginal densities and the conditional densities also are well defined, i.e., given $P > 0 ,$ , prove $P _ { x } > 0 , P _ { y } > 0 , P _ { x | y } > 0$ , $P _ { y \mid x } > 0$ .
