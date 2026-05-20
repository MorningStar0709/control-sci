$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = A _ {1 1} x _ {1} (t) + A _ {1 2} x _ {2} (t) + B _ {1} u (t), \\ \dot {x} _ {2} (t) = A _ {2 1} x _ {1} (t) + A _ {2 2} x _ {2} (t) + B _ {2} u (t), \\ y (t) = x _ {1} (t). \end{array} \right. \tag {1.7.15}
$$

由系统 (1.7.15) 看出，状态变量 $x_{1}(t)$ 是直接能量测的。记

$$z (t) \stackrel {\text { def }} {=} \dot {x} _ {1} (t) - A _ {1 1} x _ {1} (t) - B _ {1} u (t) = \dot {y} (t) - A _ {1 1} y (t) - B _ {1} u (t),$$

则可将系统 (1.7.15) 写成

$$
\left\{ \begin{array}{l} \dot {x} _ {2} (t) = A _ {2 2} x _ {2} (t) + A _ {2 1} y (t) + B _ {2} u (t), \\ z (t) = A _ {1 2} x _ {2} (t). \end{array} \right. \tag {1.7.16}
$$

这里把 $y(t)$ 和 $u(t)$ 都作为已知输入信号处理.

对系统 (1.7.16) 设计状态观测器，需要说明 $(A_{22}, A_{12})$ 是完全能观测的.

引理 1.7.1 已知系统 (1.7.15), (1.7.16). $(A_{22}, A_{12})$ 完全能观测的充分必要条件是 $(A, C)$ 完全能观测.

证明 由于

$$
(A, C) = \left(\left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right], [ I _ {m} \quad 0 ]\right),
$$

所以

$$
\begin{array}{l} \operatorname{rank} \boldsymbol {Q} _ {o} = \operatorname{rank} \left[ \begin{array}{c c} I _ {m} & 0 \\ \boldsymbol {A} _ {1 1} & \boldsymbol {A} _ {1 2} \\ \boldsymbol {A} _ {1 1} ^ {2} + \boldsymbol {A} _ {1 2} \boldsymbol {A} _ {2 1} & \boldsymbol {A} _ {1 1} \boldsymbol {A} _ {1 2} + \boldsymbol {A} _ {1 2} \boldsymbol {A} _ {2 2} \\ \vdots & \vdots \end{array} \right] \\ = \operatorname{rank} \left[ \begin{array}{c c} I _ {m} & 0 \\ 0 & A _ {1 2} \\ 0 & A _ {1 2} A _ {2 2} \\ \vdots & \vdots \\ 0 & A _ {1 2} A _ {2 2} ^ {n - m - 1} \end{array} \right] = m + \operatorname{rank} \left[ \begin{array}{c} A _ {1 2} \\ A _ {1 2} A _ {2 2} \\ \vdots \\ A _ {1 2} A _ {2 2} ^ {n - m - 1} \end{array} \right]. \\ \end{array}
$$

由此可见， $\operatorname{rank}Q_{o} = n$ 的充分必要条件是

$$
\operatorname{rank} \left[ \begin{array}{c} A _ {1 2} \\ A _ {1 2} A _ {2 2} \\ \vdots \\ A _ {1 2} A _ {2 2} ^ {n - m - 1} \end{array} \right] = n - m.
$$

这说明 $(A, C)$ 完全能观测的充分必要条件是 $(A_{22}, A_{12})$ 完全能观测，从而引理得证.

假设系统 (1.6.1) 是完全能观测的，则 $(A_{22}, A_{12})$ 也是完全能观测的，从而系统 (1.7.16) 的状态观测器是存在的。也就是说，存在一个 $(n - m) \times m$ 常值矩阵 $G_2$ ，使得 $A_{22} - G_2 A_{12}$ 是稳定的。这样，系统 (1.7.16) 的状态观测器方程可写成

$$\dot {x} _ {2 e} (t) = \left(A _ {2 2} - G _ {2} A _ {1 2}\right) x _ {2 e} (t) + A _ {2 1} y (t) + B _ {2} u (t) + G _ {2} z (t). \tag {1.7.17}$$

将 $z(t)$ 的表达式代到观测器方程 (1.7.17) 中可得出
