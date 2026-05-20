# Solution

This system is not difficult to handle with distributed control. The gains are the same as in the original pairing in Example 6.8, and the steady-state coupling between the two subsystems is reasonably weak. Unlike Example 6.8, however, the responses of $y _ { 1 }$ to $u _ { 2 }$ and $y _ { 2 }$ to $u _ { 1 }$ have been slowed so they are not faster than the responses of $y _ { 1 }$ to $u _ { 1 }$ and $y _ { 2 }$ to $u _ { 2 }$ , respectively. Computing the eigenvalues of L and $A + B K$ for noncooperative control gives

$$
\left| \operatorname{eig} (L) \right| = \left[ \begin{array}{c c c c c c c c} 0. 6 1 & 0. 6 1 & 0. 5 9 & 0. 5 9 & 0. 5 6 & 0. 5 6 & 0. 5 3 & 0. 5 3 \dots \end{array} \right]

\left| \operatorname{eig} (A + B K) \right| = \left[ \begin{array}{l l l l l l l} 0. 8 8 & 0. 8 8 & 0. 7 4 & 0. 6 7 & 0. 6 7 & 0. 5 3 & 0. 5 3 \end{array} \right]
$$

The Nash equilibrium is stable since L is stable, and the closed loop is stable since both L and A + BK are stable. -

These examples reveal the simple fact that communicating the actions of the other controllers does not guarantee acceptable closed-loop behavior. If the coupling of the subsystems is weak enough, both dynamically and in steady state, then the closed loop is stable. In this sense, noncooperative MPC has few advantages over completely decentralized control, which has this same basic property.

We next show how to obtain much better closed-loop properties while maintaining the small size of the distributed control problems.
