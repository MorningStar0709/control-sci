# Example 12.2 Prediction

Consider the system (12.14) defined by the polynomials

$$A (q) = q ^ {2} - 1. 5 q + 0. 7C (q) = q ^ {2} - 0. 2 q + 0. 5$$

and where e has unit variance. Determine first the three-step-ahead prediction of the output. The identity (12.17) gives

$$q ^ {2} (q ^ {2} - 0. 2 q + 0. 5) = (q ^ {2} - 1. 5 q + 0. 7) (q ^ {2} + f _ {1} q + f _ {2}) + g _ {0} q + g _ {1}$$

This gives the triangular linear system of equations

$$
\begin{array}{l} q ^ {3}: - 0. 2 = - 1. 5 + f _ {1} \quad f _ {1} = 1. 3 \\ q ^ {2}: \quad 0. 5 = 0. 7 - 1. 5 f _ {1} + f _ {2} \quad f _ {2} = 1. 7 5 \\ q ^ {1}: \quad 0 = 0. 7 f _ {1} - 1. 5 f _ {2} + g _ {0} \quad g _ {0} = 1. 7 1 5 \\ q ^ {0}: \quad 0 = 0. 7 f _ {2} + g _ {1} \quad g _ {1} = - 1. 2 2 5 \\ \end{array}
$$

The prediction three steps ahead is thus given by

$$\hat {y} (k + 3 \mid k) = \frac {q G (q)}{C (q)} y (k) = \frac {1 . 7 1 5 q ^ {2} - 1 . 2 2 5 q}{q ^ {2} - 0 . 2 q + 0 . 5} y (k)$$

and the variance of the prediction error is

$$\mathbf {E} \tilde {\mathbf {y}} ^ {2} = 1 + (1. 3) ^ {2} + (1. 7 5) ^ {2} = 5. 7 5 2 5$$
