# 8.5.1 State-space model

Below is the model for a pendulum

$$\ddot {\theta} = - \frac {g}{l} \sin \theta$$

where $\theta$ is the angle of the pendulum and l is the length of the pendulum.

Since state-space representation requires that only single derivatives be used, they should be broken up as separate states. We’ll reassign $\dot { \theta }$ to be $\omega$ so the derivatives are easier to keep straight for state-space representation.

$$\dot {\omega} = - \frac {g}{l} \sin \theta$$

Now separate the states.

$$\dot {\theta} = \omega\dot {\omega} = - \frac {g}{l} \sin \theta$$

This makes our state vector ${ \left[ \theta \quad \omega \right] } ^ { \mathsf { T } }$ and our nonlinear model the following.

$$
f (\mathbf {x}, \mathbf {u}) = \left[ \begin{array}{c} \omega \\ - \frac {g}{l} \sin \theta \end{array} \right]
$$
