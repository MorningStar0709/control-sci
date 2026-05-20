$$
\mathbf {y} (k) = \left[ \begin{array}{c} x _ {3} (k) \\ x _ {1} (k) \end{array} \right]

\mathbf {y} (k + 1) = \left[ \begin{array}{l} x _ {3} (k + 1) \\ x _ {1} (k + 1) \end{array} \right] = \left[ \begin{array}{l} 3 x _ {1} (k) + 2 x _ {3} (k) \\ x _ {1} (k) - x _ {3} (k) \end{array} \right]

\mathbf {y} (k + 2) = \left[ \begin{array}{l} x _ {3} (k + 2) \\ x _ {1} (k + 2) \end{array} \right] = \left[ \begin{array}{l} 3 x _ {1} (k + 1) + 2 x _ {3} (k + 1) \\ x _ {1} (k + 1) - x _ {3} (k + 1) \end{array} \right] = \left[ \begin{array}{l} 9 x _ {1} (k) + x _ {3} (k) \\ - 2 x _ {1} (k) - 3 x _ {3} (k) \end{array} \right]
$$

可看出三步的输出测量值中始终不含 $x_{2}(k)$ ，故 $x_{2}(k)$ 是不可观测状态变量。只要有一个状态变量不可观测，则称系统不完全可观测，简称不可观测。
