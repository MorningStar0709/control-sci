$$
\left[ \begin{array}{c c} \mathbf {C B} & \mathbf {C A B} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \end{array} \right]
$$

the rank of this matrix is 1. Hence, the system is completely output controllable.

To test the observability condition, examine the rank of $[ \mathbf { C } ^ { * } \vdots \mathbf { A } ^ { * } \mathbf { C } ^ { * } ]$ Since.

$$
\left[ \begin{array}{c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right]
$$

the rank of $\left[ \mathbf { C } ^ { * } \vdots \mathbf { A } ^ { * } \mathbf { C } ^ { * } \right]$ is 2. Hence, the system is completely observable.

Conditions for Complete Observability in the s Plane. The conditions for complete observability can also be stated in terms of transfer functions or transfer matrices. The necessary and sufficient conditions for complete observability is that no cancellation occur in the transfer function or transfer matrix. If cancellation occurs, the canceled mode cannot be observed in the output.

EXAMPLE 9–15 Show that the following system is not completely observable:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {x} = \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right], \quad \mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = [ 4 5 1 ]
$$

Note that the control function u does not affect the complete observability of the system. To examine complete observability, we may simply set $u = 0 .$ For this system, we have

$$
\left[ \begin{array}{c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & (\mathbf {A} ^ {*}) ^ {2} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c c} 4 & - 6 & 6 \\ 5 & - 7 & 5 \\ 1 & - 1 & - 1 \end{array} \right]
$$

Note that

$$
\left| \begin{array}{c c c} 4 & - 6 & 6 \\ 5 & - 7 & 5 \\ 1 & - 1 & - 1 \end{array} \right| = 0
$$

Hence, the rank of the matrix $[ \mathbf { C } ^ { * } \ \vdots \ \mathbf { A } ^ { * } \mathbf { C } ^ { * } \ \vdots ( \mathbf { A } ^ { * } ) ^ { 2 } \mathbf { C } ^ { * } ]$ is less than 3. Therefore, the system is not completely observable.

In fact, in this system, cancellation occurs in the transfer function of the system. The transfer function between $X _ { 1 } ( s )$ and $U ( s )$ is

$$\frac {X _ {1} (s)}{U (s)} = \frac {1}{(s + 1) (s + 2) (s + 3)}$$
