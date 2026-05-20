# Observability and Detectability

To solve the problem of finding the state of a system from observations of the output, the concept of unobservable states is introduced.

DEFINITION 3.9 UNOBSERVABLE STATES The state $x^0 \neq 0$ is unobservable if there exists a finite $k_1 \geq n - 1$ such that $y(k) = 0$ for $0 \leq k \leq k_1$ when $x(0) = x^0$ and $u(k) = 0$ for $0 \leq k \leq k_1$ .

The system in (3.15) is observable if there is a finite k such that knowledge of the inputs $u(0), \ldots, u(k-1)$ and the outputs $y(0), \ldots, y(k-1)$ is sufficient to determine the initial state of the system. Consider the system in (3.15). The effect of the known input signal always can be determined, and there is no loss of generality to assume that $u(k) = 0$ . Assume that $y(0), y(1), \ldots, y(n-1)$ are given. This gives the following set of equations:

$$y (0) = C x (0)y (1) = C x (1) = C \Phi x (0)$$

\+

$$y (n - 1) = C \Phi^ {n - 1} x (0)$$

Using vector notation gives

$$
\left( \begin{array}{c} C \\ C \Phi \\ \vdots \\ C \Phi^ {n - 1} \end{array} \right) x (0) = \left( \begin{array}{c} y (0) \\ y (1) \\ \vdots \\ y (n - 1) \end{array} \right) \tag {3.21}
$$

The state $x(0)$ can be obtained from (3.21) if and only if the observability matrix

$$
W _ {o} = \left( \begin{array}{c} C \\ C \Phi \\ \vdots \\ C \Phi^ {n - 1} \end{array} \right) \tag {3.22}
$$

has rank n. The state $x(0)$ is unobservable if $x(0)$ is in the null space of $W_{o}$ . If two states are unobservable, then any linear combination is also unobservable; that is, the unobservable states form a linear subspace.

THEOREM 3.8 OBSERVABILITY The system (3.15) is observable if and only if $W_{o}$ has rank $n$ .

DEFINITION 3.10 DETECTABILITY A system is detectable if the only unobservable states are such that they decay to the origin. That is, the corresponding eigenvalues are stable.

The test of observability given by Theorem 3.8 is equivalent to that of observability for continuous-time systems. It is straightforward to show that the observability matrix is independent of the coordinates in the same way as in the controllability matrix.
