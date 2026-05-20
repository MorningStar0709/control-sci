Note that the weights $w _ { 1 } , \ w _ { 2 }$ do not appear in the converged input sequence. The ${ \bf u } _ { 1 } ^ { \infty } , \ { \bf u } _ { 2 } ^ { \infty }$ pair have the equilibrium property that neither player can improve his position given the other player’s current decision. This point is called a Nash equilibrium (Ba¸sar and Olsder, 1999, p. 4). Notice that the distributed MPC game does not have a Nash equilibrium if the eigenvalues of L are on or outside the unit circle. If the controllers have sufficient time during the control system’s sample time to iterate to convergence, then the effect of the initial control sequence is removed by using the converged control sequence. If the iteration has to be stopped before convergence, the solution is

$$\mathbf {u} ^ {p + 1} = L ^ {p} \mathbf {u} ^ {[ 0 ]} + \sum_ {j = 0} ^ {p - 1} L ^ {j} \overline {{K}} x (0) \quad 0 \leq p$$

in which $\mathbf { u } ^ { [ 0 ] }$ is the $p = 0$ (initial) input sequence. We use the brackets with $p = 0$ to distinguish this initial input sequence from an optimal input sequence.

Stability of the closed-loop system. We assume the Nash equilibrium is stable and there is sufficient computation time to iterate to convergence.

We require a matrix of zeros and ones to select the first move from the input sequence for injection into the plant. For the first player, the

required matrix is

$$
\boldsymbol {u} _ {1} (0) = E _ {1} \mathbf {u} _ {1}
E _ {1} = \left[ \begin{array}{c c c c} I _ {m _ {1}} & 0 _ {m _ {1}} & \ldots & 0 _ {m _ {1}} \end{array} \right] \qquad m _ {1} \times m _ {1} N \text {matrix}
$$

The closed-loop system is then

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] ^ {+} = \underbrace {\left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right]} _ {A} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] +

\underbrace {\left[ \begin{array}{c c} \overline {{B}} _ {1 1} & \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 1} & \overline {{B}} _ {2 2} \end{array} \right]} _ {B} \underbrace {\left[ \begin{array}{c c} E _ {1} & 0 \\ 0 & E _ {2} \end{array} \right] \left[ \begin{array}{c c} I & - L _ {1} \\ - L _ {2} & I \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} K _ {1} & 0 \\ 0 & K _ {2} \end{array} \right]} _ {K} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

Using the plantwide notation for this equation and defining the feedback gain K gives

$$x ^ {+} = (A + B K) x$$
