# 6.12.5 Observability matrix

A system is observable if the state, whatever it may be, can be inferred from a finite sequence of outputs.

Observability and controllability are mathematical duals; controllability proves that a sequence of inputs exists that drives the system to any state, and observability proves that a sequence of outputs exists that drives the state estimate to any true state.

The observability matrix can be used to determine if a system is observable.

Theorem 6.12.2 — Observability. A continuous time-invariant linear state-space model is observable if and only if

$$
\operatorname{rank} \left(\left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \vdots \\ \mathbf {C A} ^ {n - 1} \end{array} \right]\right) = n \tag {6.41}
$$

where rank is the number of linearly independent rows in a matrix and n is the number of states.

The observability matrix in equation (6.41) being rank-deficient means the outputs do not contain contributions from every state. That is, not all states are mapped to a linear combination in the output. Therefore, the outputs alone are insufficient to estimate all the states.

The condition number of the observability matrix O is defined as $\frac { \sigma _ { m a x } ( \mathcal { O } ) } { \sigma _ { m i n } ( \mathcal { O } ) }$ where $\sigma _ { m a x }$ is the maximum singular value[17] and $\sigma _ { m i n }$ is the minimum singular value. As this number approaches infinity, one or more of the states becomes unobservable. This number can also be used to tell us which sensors are better than others for the given system; a lower condition number means the outputs produced by the sensors are better indicators of the system state.
