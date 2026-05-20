$$\mathbf {K} = \left[ \alpha_ {n} - a _ {n} \mid \alpha_ {n - 1} - a _ {n - 1} \mid \dots \mid \alpha_ {2} - a _ {2} \mid \alpha_ {1} - a _ {1} \right] \mathbf {T} ^ {- 1} \tag {10-161}$$

where

$$
\mathbf {T} = \mathbf {M W} = \left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right] \mathbf {W}
$$

For the original system, the observability matrix is

$$
\left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right] = \mathbf {N}
$$

Hence, matrix T can also be written as

$$\mathbf {T} = \mathbf {N W}$$

Since we haveW = W\*,

$$\mathbf {T} ^ {*} = \mathbf {W} ^ {*} \mathbf {N} ^ {*} = \mathbf {W N} ^ {*}$$

and

$$\left(\mathbf {T} ^ {*}\right) ^ {- 1} = \left(\mathbf {W N} ^ {*}\right) ^ {- 1}$$

Taking the conjugate transpose of both sides of Equation (10–146), we have

$$
\mathbf {K} ^ {*} = \left(\mathbf {T} ^ {- 1}\right) ^ {*} \left[ \begin{array}{c} \alpha_ {n} - a _ {n} \\ \alpha_ {n - 1} - a _ {n - 1} \\ . \\ . \\ . \\ \alpha_ {1} - a _ {1} \end{array} \right] = (\mathbf {T} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \alpha_ {n} - a _ {n} \\ \alpha_ {n - 1} - a _ {n - 1} \\ . \\ . \\ . \\ \alpha_ {1} - a _ {1} \end{array} \right] = (\mathbf {W N} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \alpha_ {n} - a _ {n} \\ \alpha_ {n - 1} - a _ {n - 1} \\ . \\ . \\ . \\ \alpha_ {1} - a _ {1} \end{array} \right]
$$

Since ${ \bf K } _ { e } = { \bf K } ^ { * }$ , this last equation is the same as Equation (10–159). Thus, we obtained Equation (10–159) by considering the dual problem.

A–10–11. Consider an observed-state feedback control system with a minimum-order observer described by the following equations:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-162}y = \mathbf {C x}u = - \mathbf {K} \widetilde {x} \tag {10-163}$$

where

$$
\mathbf {x} = \left[ \begin{array}{c} x _ {a} \\ \hdashline \mathbf {x} _ {b} \end{array} \right], \qquad \widetilde {\mathbf {x}} = \left[ \begin{array}{c} x _ {a} \\ \hdashline \widetilde {\mathbf {x}} _ {b} \end{array} \right]
$$

$\left( x _ { a } \right.$ is the state variable that can be directly measured, and $\widetilde { \mathbf { X } } _ { b }$ corresponds to the observed state variables. B
