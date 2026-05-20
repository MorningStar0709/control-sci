The closed-loop poles of the observed-state feedback control system with a minimum-order observer consist of the closed-loop poles due to pole placement and the closed-loop poles due to the minimum-order observer. (Therefore, the pole-placement design and the design of the minimum-order observer are independent of each other.)

A–10–12. Consider a completely state controllable system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-167}y = \mathbf {C x}$$

where x = state vector (n-vector)

$$u = \text { control signal (scalar) }y = \text { output signal (scalar) }$$

A = n \* n constant matrix

$$\mathbf {B} = n \times 1 \text { constant matrix }\mathbf {C} = 1 \times n \text { constant matrix }$$

Suppose that the rank of the following matrix(n + 1) \* (n + 1)

$$
\left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ - \mathbf {C} & 0 \end{array} \right]
$$

is n+1. Show that the system defined by

$$\dot {\mathbf {e}} = \hat {\mathbf {A}} \mathbf {e} + \hat {\mathbf {B}} u _ {e} \tag {10-168}$$

where

$$
\hat {\mathbf {A}} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right], \qquad \hat {\mathbf {B}} = \left[ \begin{array}{c} \mathbf {B} \\ \mathbf {0} \end{array} \right], \qquad u _ {e} = u (t) - u (\infty)
$$

is completely state controllable.

Solution. Define

$$
\mathbf {M} = \left[ \begin{array}{c c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

Because the system given by Equation (10–167) is completely state controllable, the rank of matrix M is n. Then the rank of

$$
\left[ \begin{array}{c c} \mathbf {M} & \mathbf {0} \\ \mathbf {0} & 1 \end{array} \right]
$$

is n+1. Consider the following equation:

$$
\left[ \begin{array}{l l} \mathbf {A} & \mathbf {B} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{l l} \mathbf {M} & \mathbf {0} \\ \mathbf {0} & 1 \end{array} \right] = \left[ \begin{array}{l l} \mathbf {A M} & \mathbf {B} \\ - \mathbf {C M} & 0 \end{array} \right] \tag {10-169}
$$

Since matrix

$$
\left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ - \mathbf {C} & 0 \end{array} \right]
$$

is of rank n+1, the left-hand side of Equation (10–169) is of rank n+1. Therefore, the right-hand side of Equation (10–169) is also of rank n+1. Since
