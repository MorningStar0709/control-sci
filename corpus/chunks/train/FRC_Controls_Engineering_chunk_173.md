# 6.12.1 Controllability matrix

A system is controllable if it can be steered from any state to any state by a finite sequence of admissible inputs.

The controllability matrix can be used to determine if a system is controllable.

Theorem 6.12.1 — Controllability. A continuous time-invariant linear statespace model is controllable if and only if

$$
\operatorname{rank} \left(\left[ \begin{array}{l l l l} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]\right) = n \tag {6.37}
$$

where rank is the number of linearly independent rows in a matrix and n is the number of states.

The controllability matrix in equation (6.37) being rank-deficient means the inputs cannot apply transforms along all axes in the state-space; the transformation the matrix represents is collapsed into a lower dimension.

The condition number of the controllability matrix C is defined as $\frac { \sigma _ { m a x } ( \mathcal { C } ) } { \sigma _ { m i n } ( \mathcal { C } ) }$ where $\sigma _ { m a x }$ is the maximum singular value[17] and $\sigma _ { m i n }$ is the minimum singular value. As this number approaches infinity, one or more of the states becomes uncontrollable. This number can also be used to tell us which actuators are better than others for the given system; a lower condition number means that the actuators have more control authority.
