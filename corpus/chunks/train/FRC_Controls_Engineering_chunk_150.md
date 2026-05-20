# 6.8 Double integrator

The double integrator has two states (position and velocity) and one input (acceleration). Their relationship can be expressed by the following system of differential equations, where x is position, v is velocity, and a is acceleration.

$$\dot {x} = v\dot {v} = a$$

We want to put these into the form $\dot { \mathbf { x } } = \mathbf { A } \mathbf { x } + \mathbf { B } \mathbf { u }$ . Let $\mathbf { x } = \left[ x \quad v \right] ^ { \mathsf { T } }$ and $\mathbf { u } = \left[ a \right] ^ { \mathsf { T } }$ . First, add missing terms so that all equations have the same states and inputs. Then, sort them by states followed by inputs.

$$\dot {x} = 0 x + 1 v + 0 a\dot {v} = 0 x + 0 v + 1 a$$

Now, factor out the constants into matrices.

$$
\left[ \begin{array}{c} \dot {x} \\ v \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} x \\ v \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ a ]
\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}
$$
