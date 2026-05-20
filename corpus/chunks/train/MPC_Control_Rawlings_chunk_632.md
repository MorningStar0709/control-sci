# 5.6.3 Nominal MPC

In nominal output MPC, the control u is determined by solving an optimal control problem $\bar { \mathbb { P } } _ { N } ( \hat { x } )$ for the nominal deterministic system defined by

$$z ^ {+} = f (z, u) \qquad z (0) = \hat {x}$$

where xˆ is the current estimate of the state x. This yields the implicit control law $\bar { \kappa } _ { N } ( \cdot )$ so the control u applied to the system $x ^ { + } = f ( x , u ) +$ w when the current state estimate is $\hat { x }$ is

$$\boldsymbol {u} = \bar {\kappa} _ {N} (\hat {\boldsymbol {x}})$$

Because the evolution of the state x differs from the evolution of the state estimate $\hat { x }$ , the control $u = \bar { \kappa } _ { N } ( \hat { x } )$ is not necessarily stabilizing. If the ingredients $V _ { f } ( \cdot )$ and $\mathbb { Z } _ { f }$ of the optimal control problem $\bar { \mathbb { P } } _ { N } ( \hat { x } )$ are chosen appropriately, and $\ell ( \cdot )$ is quadratic and positive definite, the value function $\bar { V } _ { N } ^ { 0 } ( \cdot )$ satisfies the usual inequalities:

$$
\begin{array}{l} c _ {1} | z | ^ {2} \leq \bar {V} _ {N} ^ {0} (z) \leq c _ {2} | z | ^ {2} \\ \bar {V} _ {N} ^ {0} (z ^ {+}) \leq \bar {V} _ {N} ^ {0} (z) - c _ {1} | z | ^ {2} \\ \end{array}
$$

where $z ^ { + } = f ( z , \bar { \kappa } _ { N } ( z ) )$ ). These inequalities are sufficient to establish the exponential stability of the origin for the nominal system $z ^ { + } =$ $f ( z , \bar { \kappa } _ { N } ( z ) )$ ) with a region of attraction $\mathcal { Z } _ { N }$ which is the domain of the value function if bounded, or an appropriate level set of the value function otherwise.
