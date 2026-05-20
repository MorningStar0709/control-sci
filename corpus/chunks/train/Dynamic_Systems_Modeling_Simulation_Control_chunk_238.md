$$
\mathbf {A} = \left[ \begin{array}{c c c} \partial f _ {1} / \partial x _ {1} & \partial f _ {1} / \partial x _ {2} & \partial f _ {1} / \partial x _ {3} \\ \partial f _ {2} / \partial x _ {1} & \partial f _ {2} / \partial x _ {2} & \partial f _ {2} / \partial x _ {3} \\ \partial f _ {3} / \partial x _ {1} & \partial f _ {3} / \partial x _ {2} & \partial f _ {3} / \partial x _ {3} \end{array} \right] \bigg | _ {\mathbf {x} ^ {*}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ - 0. 4 & - 0. 1 x _ {3} & 0. 2 - 0. 1 x _ {2} \\ 1. 5 & 0 & - 0. 7 5 - 0. 0 7 5 x _ {3} ^ {2} \end{array} \right] \bigg | _ {\mathbf {x} ^ {*}} \tag {5.83}
$$

Evaluation of each matrix element at the nominal state vector $\mathbf { X } ^ { * }$ yields the system matrix

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ - 0. 4 & - 0. 2 2 8 9 & 0. 2 \\ 1. 5 & 0 & - 1. 1 4 3 1 \end{array} \right]
$$

The input matrix B is composed of the first-order partial derivatives of $f _ { i } ( { \bf x } , u )$ with respect to input u

$$
\mathbf {B} = \left[ \begin{array}{c} \partial f _ {1} / \partial u \\ \partial f _ {2} / \partial u \\ \partial f _ {3} / \partial u \end{array} \right] \bigg | _ {\mathbf {x} ^ {*}} = \left[ \begin{array}{c} 0 \\ 0 \\ 2 \end{array} \right]
$$

Because input u appears linearly in Eqs. (5.77)–(5.79), the input matrix B contains the linear coefficients of u. The linear state equation is

$$
\delta \dot {\mathbf {x}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ - 0. 4 & - 0. 2 2 8 9 & 0. 2 \\ 1. 5 & 0 & - 1. 1 4 3 1 \end{array} \right] \delta \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 2 \end{array} \right] \delta u \tag {5.84}
$$

Equation (5.84) is the linearized version of the nonlinear system (5.77)– (5.79). The linearized system is in terms of the perturbation variables $\delta \mathbf { x } = \mathbf { x } - \mathbf { x } ^ { * }$ and $\delta u = u - u ^ { * }$ . The nonlinear system has been linearized about the equilibrium state vector shown in Eq. (5.82).
