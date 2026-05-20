# THEOREM 4.3 LQG control

Consider the system in Eq. (4.39). Let the monic polynomials $A(q)$ and $C(q)$ have degree n. Assume that $C(q)$ has all its zeros inside the unit disc, and assume that there is no nontrivial polynomial that divides $A(q)$ , $B(q)$ , and $C(q)$ . Let $A_2(q)$ be the greatest common divisor of $A(q)$ and $B(q)$ , let $A_2^+ (q)$ of degree $l$ be the factor of $A_2(q)$ with all its zeros inside the unit disc, and let $A_2^- (q)$ of degree $m$ be the factor of $A(q)$ that has all its zeros outside the unit disc or on the unit circle.

The admissible control law that minimizes Eq. (4.40) with $\rho > 0$ is then given by

$$R (q) u (t) = - S (q) y (t) + T (q) y _ {m} (t) \tag {4.41}$$

where $R$ and $S$ are of degree $n + m$

$$R (q) = A _ {2} ^ {-} (q) \tilde {R} (q) \tag {4.42}S (q) = z ^ {m} \tilde {S} (q)$$

and $\bar{R}(q)$ and $\tilde{S}(q)$ satisfy the Diophantine equation

$$A _ {1} (q) A _ {2} ^ {-} (q) \tilde {R} (q) + q ^ {m} B _ {1} (q) \tilde {S} (q) = P _ {1} (q) C (q) \tag {4.43}$$

with $\deg \tilde{R}(q) = \deg \tilde{S}(q) = n$ and $\tilde{S}(0) = 0$ . Furthermore,

$$A (q) = A _ {1} (q) A _ {2} (q)B (q) = B _ {1} (q) A _ {2} (q)\tilde {B} (q) = B _ {1} (q) A _ {2} ^ {+} (q)$$

The polynomial $P(q)$ is given by

$$P (q) = A _ {2} ^ {+} (q) P _ {1} (q) \tag {4.44}$$

where $P_{1}(q)$ is the solution of the spectral factorization problem

$$r P _ {1} (q) P _ {1} \left(q ^ {- 1}\right) = \rho A _ {1} (q) A _ {2} ^ {-} (q) A _ {1} \left(q ^ {- 1}\right) A _ {2} ^ {-} \left(q ^ {- 1}\right) + B _ {1} (q) B _ {1} \left(q ^ {- 1}\right) \tag {4.45}$$

with $\deg P_1(q) = \deg A_1(q) + \deg A_2^-(q)$ . The polynomial $T(q)$ is given by

$$T (q) = t _ {0} q ^ {m} C (q)$$

where

$$t _ {0} = P _ {1} (1) / B _ {1} (1)$$

A proof of the theorem is found in Åström and Wittenmark (1990).

Remark. By using Eqs. (4.42) the identity (4.43) can be written as

$$A (q) R (q) + B (q) S (q) = A _ {2} (q) P _ {1} (q) C (q)$$

The LQG solution can thus be interpreted as a pole-placement controller, where the poles are positioned at the zeros of $A_{2}$ , $P_{1}$ , and C. The controller also has the property that $A_{2}^{-}$ divides R. This is an example of the internal model principle. Using the internal model principle implies that a model of the disturbance is included in the controller.
