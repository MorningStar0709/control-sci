# 2.5.2.1 Linear Stable Systems

The system to be controlled is $x ^ { + } = A x + B u$ where A is stable (its eigenvalues lie strictly inside the unit circle) and the control u is subject to the constraint $u \in \mathbb { U }$ where U is compact and contains the origin in its interior. The stage cost is $\ell ( x , u ) = ( 1 / 2 ) ( x ^ { \prime } Q x + u ^ { \prime } R u )$ where Q and R are positive definite. To establish stability of the systems under MPC (or RHC), we wish to obtain a global CLF to serve as the terminal cost function $V _ { f } ( \cdot )$ . This is usually difficult because any linear control law $u \ : = \ : K x$ , say, will transgress the control constraint for x sufficiently large. In other words, it is usually impossible to find a $V _ { f } ( \cdot )$ such that there exists a $u \in \mathbb { U }$ satisfying $V _ { f } ( A x + B u ) \le V _ { f } ( x ) - \ell ( x , u )$ for all x in $\mathbb { R } ^ { n }$ . Since A is stable, however, it is possible to obtain a Lyapunov function for the autonomous system $x ^ { + } = A x$ that is a suitable candidate for $V _ { f } ( \cdot )$ ; in fact, for all $Q > 0$ , there exists a $P > 0$ such that

$$A ^ {\prime} P A + Q = P$$

Let $V _ { f } ( \cdot )$ be defined by

$$V _ {f} (x) = (1 / 2) x ^ {\prime} P x$$

With $f ( \cdot ) , \ell ( \cdot )$ , and $V _ { f } ( \cdot )$ defined thus, $\mathbb { P } _ { N } ( x )$ is a parametric quadratic problem if the constraint set U is polyhedral and global solutions may be computed online. The terminal cost function $V _ { f } ( \cdot )$ satisfies

$$V _ {f} (A x) + (1 / 2) x ^ {\prime} Q x - V _ {f} (x) = (1 / 2) x ^ {\prime} \left(A ^ {\prime} P A + Q - P\right) x = 0$$

for all $x \in \mathbb { X } _ { f } : = \mathbb { R } ^ { n }$ . We see that for all $x \in \mathbb { X } _ { f }$ , there exists a u, namely $u = 0$ , such that $V _ { f } ( A x + B u ) \leq V _ { f } ( x ) - \ell ( x , u ) ; \ell ( x , u ) = ( 1 / 2 ) x ^ { \prime } Q x$ when $u = 0$ . Since there are no state or terminal constraints, $\mathcal { X } _ { N } = \mathbb { R } ^ { n }$ . It follows that there exist positive constants $c _ { 1 }$ and $c _ { 2 }$ such that

$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq c _ {1} | x | ^ {2} \\ V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - c _ {1} | x | ^ {2} \\ V _ {N} ^ {0} (x) \leq c _ {2} | x | ^ {2} \\ \end{array}
$$

for all $x \in \mathcal { X } _ { N } = \mathbb { R } ^ { n }$ . Summarizing, we have:

If these assumptions on $V _ { f } ( \cdot ) , \mathbb { X } _ { f } ,$ , and $\ell ( \cdot )$ hold, and Assumption 2.3 is satisfied, then Assumptions 2.12, 2.13, and 2.16(b) are satisfied and $\mathcal { X } _ { N } = \mathbb { X } _ { f } = \mathbb { R } ^ { n }$ . It follows from Theorem 2.24(a) that the origin is globally, exponentially stable for the controlled system $x ^ { + } = A x + B \kappa _ { N } ( x )$ .

An extension of this approach for unstable A is used in Chapter 6.
