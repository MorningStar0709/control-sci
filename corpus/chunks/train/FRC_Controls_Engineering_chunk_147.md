# Implementation

We want to augment the system with an integral term that integrates the error ${ \bf e } =$ $\mathbf { r } - \mathbf { y } = \mathbf { r } - \mathbf { C } \mathbf { x }$ .

$$\mathbf {x} _ {I} = \int \mathbf {e} d t\dot {\mathbf {x}} _ {I} = \mathbf {e} = \mathbf {r} - \mathbf {C x}$$

The plant is augmented as

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {\mathbf {x}} \\ \mathbf {x} _ {I} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & \mathbf {0} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {x} _ {I} \end{array} \right] + \left[ \begin{array}{c} \mathbf {B} \\ \mathbf {0} \end{array} \right] \mathbf {u} + \left[ \begin{array}{c} \mathbf {0} \\ \mathbf {I} \end{array} \right] \mathbf {r} \\ \left[ \begin{array}{c} \dot {\mathbf {x}} \\ \mathbf {x} _ {I} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & \mathbf {0} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {x} _ {I} \end{array} \right] + \left[ \begin{array}{c c} \mathbf {B} & \mathbf {0} \\ \mathbf {0} & \mathbf {I} \end{array} \right] \left[ \begin{array}{c} \mathbf {u} \\ \mathbf {r} \end{array} \right] \\ \end{array}
$$

The controller is augmented as

$$
\begin{array}{l} \mathbf {u} = \mathbf {K} (\mathbf {r} - \mathbf {x}) - \mathbf {K} _ {I} \mathbf {x} _ {I} \\ \mathbf {u} = \left[ \begin{array}{c c} \mathbf {K} & \mathbf {K} _ {I} \end{array} \right] \left(\left[ \begin{array}{c} \mathbf {r} \\ \mathbf {0} \end{array} \right] - \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {x} _ {I} \end{array} \right]\right) \\ \end{array}
$$
