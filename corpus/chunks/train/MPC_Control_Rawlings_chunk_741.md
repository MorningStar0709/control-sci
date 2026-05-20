# Exercise 6.19: Splitting more than once

Consider the generalization of Exercise 6.15 in which we repeatedly decompose a problem into one-variable-at-a-time optimizations. For a three-variable problem we have the three optimizations

$$u _ {1} ^ {p + 1} = \arg \min _ {u _ {1}} V (u _ {1}, u _ {2} ^ {p}, u _ {3} ^ {p})u _ {2} ^ {p + 1} = \arg \min _ {u _ {2}} V (u _ {1} ^ {p}, u _ {2}, u _ {3} ^ {p}) \quad u _ {3} ^ {p + 1} = \arg \min _ {u _ {3}} V (u _ {1} ^ {p}, u _ {2} ^ {p}, u _ {3})$$

Is it true that

$$V (u _ {1} ^ {p + 1}, u _ {2} ^ {p + 1}, u _ {3} ^ {p + 1}) \leq V (u _ {1} ^ {p}, u _ {2} ^ {p}, u _ {3} ^ {p})$$

Hint: you may wish to consider the following example, $V ( u ) = ( 1 / 2 ) u ^ { \prime } H u + c ^ { \prime } u$ , in which

$$
H = \left[ \begin{array}{c c c} 2 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 2 \end{array} \right] \qquad c = \left[ \begin{array}{c} 0 \\ 1 \\ 1 \end{array} \right] \qquad u ^ {p} = \left[ \begin{array}{c} 1 \\ 0 \\ 1 \end{array} \right]
$$
