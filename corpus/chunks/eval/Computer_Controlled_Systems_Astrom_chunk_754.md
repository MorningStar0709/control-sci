# Example 12.13 Integral action

Let the system be described by

$$y (k) = \frac {B _ {1} (q)}{A _ {1} (q)} u (k) + \frac {C _ {1} (q)}{q - 1} e (k)$$

which is a special case of Eqs. (12.1) to (12.4) with a drifting disturbance. Hence

$$A (q) = (q - 1) A _ {1} (q)B (q) = (q - 1) B _ {1} (q)C (q) = A _ {1} (q) C _ {1} (q)$$

Unbounded control signals are necessary to compensate for the unbounded disturbance. This implies that the modified loss function (12.66) becomes

$$J _ {l q} ^ {\prime} = E \left[ y ^ {2} (k) + \rho (\Delta u (k)) ^ {2} \right]$$

where

$$\Delta u (k) = u (k) - u (k - 1)$$

This means that the difference and not the absolute value of the control signal is penalized. The solution to the LQG-problem gives a controller with integral action.

The following result can then be established.

THEOREM 12.5 LQG-CONTROL WITH UNSTABLE COMMON FACTORS Consider the system described by (12.5), where $A(z)$ and $C(z)$ are monic polynomials of degree $n$ . Assume that all zeros of $C(z)$ are inside the unit disc and that there is no nontrivial polynomial that divides $A(z), B(z)$ , and $C(z)$ . Let $A_2(z)$ be the greatest common divisor of $A(z)$ and $B(z)$ , let $A_2^+(z)$ of degree $l$ be the factor of $A_2(z)$ with all its zeros inside the unit disc, and let $A_2^- (z)$ of degree $m$ be the factor of $A(z)$ that has zeros on the unit circle or outside the unit disc. The admissible control law that minimizes (12.66) is given by

$$u (k) = - \frac {S (q)}{R (q)} y (k)$$

where $R(z)$ and $S(z)$ are of degree $n + m$

$$
\begin{array}{l} \begin{array}{l} \boldsymbol {R} (z) = A _ {2} ^ {-} (z) \tilde {\boldsymbol {R}} (z) \\ \tilde {\boldsymbol {S}} (z) = \bar {\boldsymbol {m}} \tilde {\boldsymbol {S}} (z) \end{array} \tag {12.67} \\ S (z) = z ^ {m} \bar {S} (z) \\ \end{array}
$$

and $\tilde{R}(z)$ and $\tilde{S}(z)$ satisfies

$$
\begin{array}{l} A _ {1} (z) A _ {2} ^ {-} (z) \tilde {R} (z) + z ^ {m} B _ {1} (z) \tilde {S} (z) = P _ {1} (z) C (z) \\ \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \quad \text {   } \end{array} \tag {12.68}
A ^ {*} (z) X (z) + r P (z) \tilde {S} ^ {*} (z) = q ^ {m} \tilde {B} (z) C ^ {*} (z)
$$

with $\deg \tilde{R}(z) = \deg \bar{S}(z) = n$ , $\deg X(z) < n$ and $\tilde{S}(0) = 0$ . Furthermore

$$A (z) = A _ {1} (z) A _ {2} (z)\boldsymbol {B} (z) = \boldsymbol {B} _ {1} (z) \boldsymbol {A} _ {2} (z)\bar {B} (z) = B _ {1} (z) A _ {2} ^ {+} (z)$$

and $P_{1}(z)$ is the solution of the spectral-factorization problem
