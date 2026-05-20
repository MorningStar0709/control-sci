Using the third form in Example 1.1 we can combine these two terms into a single quadratic function

$V _ { 0 } ( x ( 0 ) ) = ( 1 / 2 ) ~ ( x ( 0 ) - \overline { { { x } } } ( 0 ) - \nu ) ^ { \prime } \tilde { \cal H } ^ { - 1 } ( x ( 0 ) - \overline { { { x } } } ( 0 ) - \nu ) + \mathrm { c o n s t a n t }$ in which

$$\nu = P ^ {-} (0) C ^ {\prime} \left(C P ^ {-} (0) C ^ {\prime} + R\right) ^ {- 1} \left(y (0) - C \bar {x} (0)\right)\tilde {H} = P ^ {-} (0) - P ^ {-} (0) C ^ {\prime} (C P ^ {-} (0) C ^ {\prime} + R) ^ {- 1} C P ^ {-} (0)$$

and we set the constant term to zero because it does not depend on $x ( 1 )$ . If we define

$$P (0) = P ^ {-} (0) - P ^ {-} (0) C ^ {\prime} \left(C P ^ {-} (0) C ^ {\prime} + R\right) ^ {- 1} C P ^ {-} (0)L (0) = P ^ {-} (0) C ^ {\prime} \left(C P ^ {-} (0) C ^ {\prime} + R\right) ^ {- 1}$$

and define the state estimate x( ˆ 0) as follows

$$
\begin{array}{l} \hat {x} (0) = \overline {{{{x}}}} (0) + v \\ \hat {x} (0) = \overline {{{{x}}}} (0) + L (0) \left(y (0) - C \overline {{{{x}}}} (0)\right) \\ \end{array}
$$

and we have derived the following compact expression for the function $V _ { 0 }$

$$V _ {0} (x (0)) = (1 / 2) | x (0) - \hat {x} (0) | _ {P (0) ^ {- 1}} ^ {2}$$

State evolution and arrival cost. Now we add the next term in (1.29) to the function $V _ { 0 } ( \cdot )$ and denote the sum as V (·)

$$
\begin{array}{l} V (x (0), x (1)) = V _ {0} (x (0)) + (1 / 2) | x (1) - A x (0) | _ {Q ^ {- 1}} ^ {2} \\ V (x (0), x (1)) = \frac {1}{2} \left(| x (0) - \hat {x} (0) | _ {P (0) ^ {- 1}} ^ {2} + | x (1) - A x (0) | _ {Q ^ {- 1}} ^ {2}\right) \\ \end{array}
$$

Again using the third form in Example 1.1, we can add the two quadratics to obtain

$$V (x (0), x (1)) = (1 / 2) | x (0) - v | _ {\tilde {H} ^ {- 1}} ^ {2} + d$$

in which

$$\nu = \hat {x} (0) + P (0) A \left(A P (0) A ^ {\prime} + Q\right) ^ {- 1} (x (1) - A \hat {x} (0))d = (1 / 2) \left(| v - \hat {x} (0) | _ {P (0) ^ {- 1}} ^ {2} + | x (1) - A v | _ {Q ^ {- 1}} ^ {2}\right)$$

This form is convenient for optimization over the first decision variable $x ( 0 )$ ; by inspection the solution is $x ( 0 ) = \nu$ and the cost is d. We define the arrival cost to be the result of this optimization

$$V _ {1} ^ {-} (x (1)) = \min _ {x (0)} V (x (0), x (1))$$

Substituting v into the expression for d and simplifying gives

$$V _ {1} ^ {-} (x (1)) = (1 / 2) \left| x (1) - A \hat {x} (0) \right| _ {(P ^ {-} (1)) ^ {- 1}} ^ {2}$$

in which

$$P ^ {-} (1) = A P (0) A ^ {\prime} + Q$$

We define $\hat { x } ^ { - } ( 1 ) = A \hat { x } ( 0 )$ and express the arrival cost compactly as

$$V _ {1} ^ {-} (x (1)) = (1 / 2) \left| x (1) - \hat {x} ^ {-} (1) \right| _ {(P ^ {-} (1)) ^ {- 1}} ^ {2}$$
