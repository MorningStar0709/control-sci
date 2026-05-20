# Linearization with the Jacobian

Here’s the original nonlinear model in state-space representation.

$$
f (\mathbf {x}, \mathbf {u}) = \left[ \begin{array}{c} \omega \\ - \frac {g}{l} \sin \theta \end{array} \right]
$$

If we want to linearize around an arbitrary point, we can take the Jacobian with respect to x.

$$
\frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {g}{l} \cos \theta & 0 \end{array} \right]
$$

For full state feedback, knowledge of all states is required. If not all states are measured directly, an estimator can be used to supplement them.

We may only be measuring $\theta$ in the pendulum example, not ${ \dot { \theta } } ,$ , so we’ll need to estimate the latter. The C matrix the observer would use in this case is

$$
\mathbf {C} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right]
$$

Therefore, the output vector is

$$
\mathbf {y} = \mathbf {C x}
\mathbf {y} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} \theta \\ \omega \end{array} \right]
\mathbf {y} = 1 \theta + 0 \omega\mathbf {y} = \theta
$$
