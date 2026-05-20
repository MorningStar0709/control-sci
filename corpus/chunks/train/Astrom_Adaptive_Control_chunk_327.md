Notice that polynomial $Q(s)$ has only terms of even power and that all coefficients $q_{i}$ are positive, since $G(s)$ is SPR. Let Q be a diagonal matrix with elements $q_{i}$ . Introduce the following realization of the transfer function:

$$
\frac {d x}{d t} = \left( \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} & - a _ {n} \\ 1 & 0 & & 0 & 0 \\ \vdots & & & \vdots & \\ 0 & 0 & \dots & 1 & 0 \end{array} \right) x + \left( \begin{array}{c} 1 \\ 0 \\ \vdots \\ 0 \end{array} \right) u
$$

With this choice we have

$$
(s I - A) ^ {- 1} B = \frac {1}{A (s)} \left( \begin{array}{c} s ^ {n - 1} \\ s ^ {n - 2} \\ \vdots \\ 1 \end{array} \right) \tag {5.53}
$$

and

$$B ^ {T} (- s I - A) ^ {- T} Q (s I - A) ^ {- 1} B = \frac {Q (s)}{A (s) A (- s)} = G (s) + G (- s) \tag {5.54}$$

Since $G(s)$ is SPR, the matrix $A$ has no eigenvalues in the right half-plane or on the imaginary axis. Let $P$ be the solution to Eq. (5.50). This matrix is positive definite because $Q$ is positive definite and $A$ has all its eigenvalues in the left half-plane. Furthermore, let $\tilde{C} = B^T P$ . We now show that $\tilde{C} = C$ . Since $P$ is the solution to Eq. (5.50), it follows that

$$\tilde {C} (s I - A) ^ {- 1} B + B ^ {T} (- s I - A) ^ {- T} \tilde {C} ^ {T} = B ^ {T} (- s I - A) ^ {- T} Q (s I - A) ^ {- 1} B$$

But according to Eq. (5.54) the right-hand side is equal to $G(s) + G(-s)$ . Since a partial fraction expansion is unique, it follows from Eq. (5.52) that

$$G (s) = C (s I - A) ^ {- 1} B = \tilde {C} (s I - A) ^ {- 1} B$$

which implies that $\tilde{C} = C$ , and the theorem is proven.

□
