$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 0 & 1 \\ - 1 & a \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ b \end{array} \right] \boldsymbol {u}
$$

设状态可控,试求 a,b。

9-20 设系统传递函数为

$$G (s) = \frac {s + a}{s ^ {3} + 7 s ^ {2} + 1 4 s + 8}$$

设状态可控,试求 a。

9-21 判断下列系统的输出可控性：

(1) $\dot{\pmb{x}} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix} \pmb{x} + \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \pmb{u}, \quad y = [1, 0, 0] \pmb{x};$

(2) $\dot{\pmb{x}} = \begin{bmatrix} -a & & 0\\ & -b & \\ 0 & -c & \\ & & -d \end{bmatrix}\pmb {x} + \begin{bmatrix} 0\\ 0\\ 1\\ 1 \end{bmatrix}\pmb {u},\quad y = [1\quad 0\quad 0\quad 0]\pmb {x}_{\circ}$

9-22 试判断下列系统的可观测性：

(1) $\dot{\pmb{x}} = \begin{bmatrix} -1 & -2 & -2\\ 0 & -1 & 1\\ 1 & 0 & -1 \end{bmatrix}\pmb {x} + \begin{bmatrix} 2\\ 0\\ 1 \end{bmatrix}\pmb {u},\quad y = [1\quad 1\quad 0]\pmb {x};$

(2) $\dot{\pmb{x}} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{bmatrix} \pmb{x},\quad y = [1\quad 1\quad 1]\pmb{x};$

(3) $\dot{\pmb{x}} = \begin{bmatrix} -1 & 1 &  & 0\\  & -1 &  &  \\ 0 &  & -2 & 1\\  &  &  & -2 \end{bmatrix}\pmb {x},\quad \pmb {y} = \begin{bmatrix} 1 & 0 & 0 & 0\\ 0 & 0 & -1 & 0 \end{bmatrix}\pmb {x};$

$$
(4) \dot {\pmb {x}} = \left[ \begin{array}{c c c} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & - 3 \end{array} \right] \pmb {x}, \quad \pmb {y} = \left[ \begin{array}{c c c} 0 & 1 & 1 \end{array} \right] \pmb {x} _ {\circ}
$$

9-23 试确定使下列系统可观测的 a, b :

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} a & 1 \\ 0 & b \end{array} \right] \boldsymbol {x}, \quad y = [ 1 - 1 ] \boldsymbol {x}
$$

9-24 已知系统各矩阵为

$$
\mathbf {A} = \left[ \begin{array}{l l l} 1 & 3 & 2 \\ 0 & 4 & 2 \\ 0 & 0 & 1 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \\ 1 & 0 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right]
$$

试用传递矩阵判断系统可控性、可观测性。

9-25 将下列状态方程化为可控标准型：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 1 & - 2 \\ 3 & 4 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \boldsymbol {u}
$$

9-26 已知系统传递函数为

$$\frac {Y (s)}{U (s)} = \frac {s + 1}{s ^ {2} + 3 s + 2}$$

试写出系统可控不可观测、可观测不可控、不可控不可观测的动态方程。

9-27 已知系统各矩阵为

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ - 6 & - 2 & 3 & 0 \\ 3 & - 2 & 0 & 4 \end{array} \right], \quad \boldsymbol {b} = \left[ \begin{array}{l} 1 \\ 0 \\ 3 \\ 2 \end{array} \right], \quad \boldsymbol {c} = \left[ \begin{array}{l l l l} - 4 & - 3 & 1 & 1 \end{array} \right]
$$
