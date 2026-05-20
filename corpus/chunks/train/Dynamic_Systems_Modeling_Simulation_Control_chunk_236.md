where $\delta \mathbf { x } = \mathbf { x } - \mathbf { x } ^ { * }$ and $\delta \mathbf { u } = \mathbf { u } - \mathbf { u } ^ { * }$ . Finally, the linearized system (5.75) may be written in the compact state equation format

$$\delta \dot {\mathbf {x}} = \mathbf {A} \delta \mathbf {x} + \mathbf {B} \delta \mathbf {u} \tag {5.76}$$

where the A and B matrices are the first-order partial derivatives of the nonlinear state equations (5.74)

$$
\mathbf {A} = \left[ \begin{array}{c c c c} \partial f _ {1} / x _ {1} & \partial f _ {1} / x _ {2} & \dots & \partial f _ {1} / x _ {n} \\ \partial f _ {2} / x _ {1} & \partial f _ {2} / x _ {2} & \dots & \partial f _ {2} / x _ {n} \\ \vdots & \vdots & \ddots & \vdots \\ \partial f _ {n} / x _ {1} & \partial f _ {n} / x _ {2} & \dots & \partial f _ {n} / x _ {n} \end{array} \right] \quad \mathbf {B} = \left[ \begin{array}{c c c c} \partial f _ {1} / u _ {1} & \partial f _ {1} / u _ {2} & \dots & \partial f _ {1} / u _ {r} \\ \partial f _ {2} / u _ {1} & \partial f _ {2} / u _ {2} & \dots & \partial f _ {2} / u _ {r} \\ \vdots & \vdots & \ddots & \vdots \\ \partial f _ {n} / u _ {1} & \partial f _ {n} / u _ {2} & \dots & \partial f _ {n} / u _ {r} \end{array} \right]
$$

These matrices are evaluated at the nominal state and input vectors. Therefore, the linearized system matrices will be time varying if $\mathbf { x } ^ { * } ( t )$ and ${ \bf u } ^ { * } ( t )$ vary with time. The following example demonstrates how to develop the linearized state and input matrices for a case with constant input $u ^ { * }$ and a constant nominal state vector $\mathbf { X } ^ { * }$ .
