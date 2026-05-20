# Example 3.7 A controllable system which is not reachable

The system

$$x (k + 1) = \Phi x (k) + \Gamma u (k)$$

where

$$
\Phi = \left( \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right) \quad \Gamma = \left( \begin{array}{l} 1 \\ 0 \end{array} \right)
$$

is reachable because

$$
W _ {c} = \left( \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right)
$$

has full rank. Assume that $\Gamma$ is changed to $\Gamma^T = \left(0 - 1\right)$ ; then

$$
W _ {c} = \left( \begin{array}{l l} 0 & 0 \\ 1 & 0 \end{array} \right)
$$

and the system is not reachable. The system is, however, controllable because $\Phi^{2} = 0$ . The origin is reached in two steps for any initial condition by using $u(0) = u(1) = 0$ .

By the Cayley-Hamilton theorem it is found from (3.16) that all states that can be reached from the origin are spanned by the columns of the controllability matrix $W_{c}$ . This implies that the reachable states belong to the linear subspace spanned by the columns of $W_{c}$ .
