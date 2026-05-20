# Example A.44: Conditional normal density

Show that if $\xi$ and η are jointly normally distributed as

$$
\left[ \begin{array}{l} \xi \\ \eta \end{array} \right] \sim N \left(\left[ \begin{array}{l} m _ {x} \\ m _ {y} \end{array} \right], \left[ \begin{array}{l l} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right]\right)
$$

then the conditional density of $\xi$ given η is also normal

$$(\xi | \eta) \sim N (m, P)$$

in which the mean is

$$m = m _ {x} + P _ {x y} P _ {y} ^ {- 1} (y - m _ {y}) \tag {A.34}$$

and the covariance is

$$P = P _ {x} - P _ {x y} P _ {y} ^ {- 1} P _ {y x} \tag {A.35}$$
