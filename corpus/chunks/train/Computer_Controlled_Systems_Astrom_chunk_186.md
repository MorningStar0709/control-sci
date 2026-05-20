# Example 3.8 Reachable subspaces

Given the system

$$
x (k + 1) = \left( \begin{array}{c c} 1 & 1 \\ - 0. 2 5 & 0 \end{array} \right) x (k) + \left( \begin{array}{c} 1 \\ - 0. 5 \end{array} \right) u (k) \quad x (0) = \binom {2} {2}
$$

is it possible to find a control sequence such that $x^T(2) = \left(-0.5, 1\right)$ ? From (3.16),

$$x (2) = \Phi^ {2} x (0) + \Phi \Gamma u (0) + \Gamma u (1)$$

or

$$\binom {- 0. 5} {1} = \binom {3. 5} {- 1} + \binom {1} {- 0. 5} (0. 5 u (0) + u (1))$$

which gives the condition

$$0. 5 u (0) + u (1) = - 4$$

One possible sequence of controls is $u(0) = -2$ and $u(1) = -3$ . Assume instead that $x^T(2) = \left( \begin{array}{cc} 0.5 & 1 \end{array} \right)$ . This gives the system of equations

$$\binom {- 3} {2} = \binom {1} {- 0. 5} (0. 5 u (0) + u (1))$$

which does not have a solution. The reason, of course, is that the system is not reachable. The controllability matrix is

$$
W _ {c} = \left( \begin{array}{c c} 1 & 0. 5 \\ - 0. 5 & - 0. 2 5 \end{array} \right)
$$

By starting at the origin, it is possible to reach only those points of the state space that belong to the subspace spanned by the vector $[1 - 0.5]^{T}$ . In the example, it is possible to reach other points due to the effect of the initial value.

Assume that new coordinates are introduced by a nonsingular transformation matrix T (compare with Sec. 2.5). In the new coordinates,

$$
\begin{array}{l} \tilde {W} _ {c} = \left( \begin{array}{l l l l} \tilde {\Gamma} & \tilde {\Phi} \tilde {\Gamma} & \dots & \tilde {\Phi} ^ {n - 1} \tilde {\Gamma} \end{array} \right) \\ = \left( \begin{array}{l l l l} T \Gamma & T \Phi T ^ {- 1} T \Gamma & \dots & T \Phi^ {n - 1} T ^ {- 1} T \Gamma \end{array} \right) \tag {3.17} \\ = T W _ {c} \\ \end{array}
$$

If $W_{c}$ has rank n, then $\tilde{W}_{c}$ also has rank n. This means that the reachability of a system is independent of the coordinates.
