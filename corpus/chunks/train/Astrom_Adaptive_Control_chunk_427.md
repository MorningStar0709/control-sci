# Extensions

The results can be extended in several different directions. Similar results can also be given in the continuous-time case, in which the underlying model can be written as

$$A (p) y (t) = B (p) u (t)$$

where A and B are polynomials in the differential operator p = d/dt. Assumptions A1-A4 are then replaced by the following assumptions:

A1': The pole excess $\deg A - \deg B$ is known.

A2': Upper bounds on the degrees of the polynomials $A$ and $B$ are known.

A3': The polynomial B has all its zeros in the left half-plane.

A4': The sign of $b_0$ is known.

The results can also be extended to systems with disturbances generated from known dynamics.

The gradient estimation algorithm can be replaced by other, more efficient methods. Theorem 6.3 then needs to be generalized. Many types of least-squares-like algorithms can be covered by replacing the function $V = \tilde{\theta}^T\tilde{\theta}$ in Theorem 6.3 by $V = \tilde{\theta}^T P^{-1}\tilde{\theta}$ and adding assumptions that guarantee that the eigenvalues of $P$ stay bounded. Other control laws can also be treated. One important situation that has not been treated is the case in which the control signal is kept bounded by saturation. Theorem 6.3 still holds, but Theorem 6.7 does not, since Eq. (6.42) does not hold when the control signal saturates.
