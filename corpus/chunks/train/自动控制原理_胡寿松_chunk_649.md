$$
\operatorname{rank} \left[ \begin{array}{c} \boldsymbol {C} \\ \lambda_ {i} \boldsymbol {I} - \boldsymbol {A} \end{array} \right] = n; \quad i = 1, 2, \dots , n \tag {9-132}
$$

或等价地表示为

$$
\operatorname{rank} \left[ \begin{array}{c} \boldsymbol {C} \\ s \boldsymbol {I} - \boldsymbol {A} \end{array} \right] = n; \quad \forall s \in C \tag {9-133}
$$

对角线规范型判据 线性定常连续系统(9-124)完全可观测的充分必要条件是：

当矩阵 A 的特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 两两相异时，由式(9-124)线性变换导出的对角线规范型为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c} \lambda_ {1} & & & 0 \\ & \lambda_ {2} & & \\ 0 & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \boldsymbol {x}, \quad \boldsymbol {y} = \overline {{\boldsymbol {C}}} \boldsymbol {x} \tag {9-134}
$$

式中， $\bar{C}$ 不包含元素全为零的列。

例 9-16 已知线性定常连续系统的对角线规范型为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 8 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 2 \end{array} \right] \boldsymbol {x}, \quad \boldsymbol {y} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & 3 \end{array} \right] \boldsymbol {x}
$$

试判定系统的可观测性。

解 显然, 此规范型中 $\bar{C}$ 不包含元素全为零的列, 故系统为完全可观测。
