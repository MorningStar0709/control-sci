# Example 3.10 A system with unobservable states

Consider the system

$$
x (k + 1) = \left( \begin{array}{c c} 1. 1 & - 0. 3 \\ 1 & 0 \end{array} \right) x (k)

y (k) = \left( \begin{array}{c c} 1 & - 0. 5 \end{array} \right) x (k)
$$

The observability matrix is

$$
W _ {o} = \left( \begin{array}{l} C \\ C \Phi \end{array} \right) = \left( \begin{array}{l l} 1 & - 0. 5 \\ 0. 6 & - 0. 3 \end{array} \right)
$$

The rank of $W_{o}$ is 1, and the unobservable states belong to the null space of $W_{o}$ , that is, [0.5-1]. Figure 3.11 shows the output for four different initial states. All initial states that lie on a line parallel to [0.5-1] give the same output [see Fig. 3.11(b) and (d)].
