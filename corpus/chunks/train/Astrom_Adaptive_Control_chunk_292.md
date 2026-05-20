# EXAMPLE 5.6 Lyapunov functions for a linear system

Consider the linear system (5.22) with

$$
A = \left( \begin{array}{l l} a _ {1} & a _ {2} \\ a _ {3} & a _ {4} \end{array} \right)
$$

where it is assumed that all eigenvalues of $A$ are in the left half-plane. Let the matrix $Q$ be

$$
Q = \left( \begin{array}{c c} q _ {1} & 0 \\ 0 & q _ {2} \end{array} \right)
$$

where $q_{1}$ and $q_{2}$ are positive. Assume that the matrix P has the form

$$
P = \left( \begin{array}{c c} p _ {1} & p _ {2} \\ p _ {2} & p _ {3} \end{array} \right)
$$

Equation (5.23) then becomes

$$
\left( \begin{array}{c c c} 2 a _ {1} & 2 a _ {3} & 0 \\ a _ {2} & a _ {1} + a _ {4} & a _ {3} \\ 0 & 2 a _ {2} & 2 a _ {4} \end{array} \right) \left( \begin{array}{c} p _ {1} \\ p _ {2} \\ p _ {3} \end{array} \right) = \left( \begin{array}{c} - q _ {1} \\ 0 \\ - q _ {2} \end{array} \right)
$$

This is a linear equation. Theorem 5.2 implies that it always has a solution when A is stable and that the solution is a positive definite matrix P. □
