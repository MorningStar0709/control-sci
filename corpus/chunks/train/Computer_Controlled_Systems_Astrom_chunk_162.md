# Stability of Linear Discrete-Time Systems

Consider the linear system

$$x ^ {0} (k + 1) = \Phi x ^ {0} (k) \quad x ^ {0} (0) = a ^ {0} \tag {3.2}$$

To investigate the stability of the solution of (3.2), the initial value is perturbed. Hence

$$x (k + 1) = \Phi x (k) \quad x (0) = a$$

The difference $\tilde{x} = x - x^0$ satisfies the equation

$$\tilde {x} (k + 1) = \Phi \tilde {x} (k) \quad \tilde {x} (0) = a - a ^ {0} \tag {3.3}$$

This implies that if the solution $x^{0}$ is stable, then every other solution is also stable. For linear, time-invariant systems, stability is thus a property of the system and not of a special solution.

The system (3.3) has the solution

$$\tilde {x} (k) = \Phi^ {k} \tilde {x} (0)$$

See (2.17). If it is possible to diagonalize $\Phi$ , then the solution is a combination of terms $\lambda_{i}^{k}$ , where $\lambda_{i}, i = 1, \ldots, n$ are the eigenvalues of $\Phi$ ; see (2.18). In the general case, when $\Phi$ cannot be diagonalized, the solution is instead a linear combination of the terms $p_{i}(k)\lambda_{i}^{k}$ , where $p_{i}(k)$ are polynomials in $k$ of order one less than the multiplicity of the corresponding eigenvalue. To get asymptotic stability, all solutions must go to zero as $k$ increases to infinity. The eigenvalues of $\Phi$ then have the property

$$\left| \lambda_ {i} \right| < 1 \quad i = 1, \dots , n$$

which is formulated as the following theorem.

THEOREM 3.1 ASYMPTOTIC STABILITY OF LINEAR SYSTEMS A discrete-time linear time-invariant system (3.2) is asymptotically stable if and only if all eigenvalues of $\Phi$ are strictly inside the unit disk.

Stability with respect to disturbances in the initial value has already been defined. Other types of stability concepts are also of interest.
