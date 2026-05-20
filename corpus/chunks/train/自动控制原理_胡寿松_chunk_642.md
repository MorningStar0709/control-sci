$$\dot {x} _ {1} = - \frac {1}{L} \left(\frac {R _ {1} R _ {2}}{R _ {1} + R _ {2}} + \frac {R _ {3} R _ {4}}{R _ {3} + R _ {4}}\right) x _ {1} + \frac {1}{L} \left(\frac {R _ {1}}{R _ {1} + R _ {2}} - \frac {R _ {3}}{R _ {3} + R _ {4}}\right) x _ {2} + \frac {1}{L} u\dot {x} _ {2} = \frac {1}{C} \left(\frac {R _ {2}}{R _ {1} + R _ {2}} - \frac {R _ {4}}{R _ {3} + R _ {4}}\right) x _ {1} - \frac {1}{C} \left(\frac {1}{R _ {1} + R _ {2}} - \frac {1}{R _ {3} + R _ {4}}\right) x _ {2}$$

其可控性矩阵为

$$
\boldsymbol {S} = \left[ \begin{array}{l l} \boldsymbol {b} & \boldsymbol {A b} \end{array} \right] = \left[ \begin{array}{l l} \frac {1}{L} & - \frac {1}{L ^ {2}} \left(\frac {R _ {1} R _ {2}}{R _ {1} + R _ {2}} + \frac {R _ {3} R _ {4}}{R _ {3} + R _ {4}}\right) \\ 0 & - \frac {1}{L C} \left(\frac {R _ {4}}{R _ {3} + R _ {4}} - \frac {R _ {2}}{R _ {1} + R _ {2}}\right) \end{array} \right]
$$

当 $\frac{R_4}{R_3 + R_4} \neq \frac{R_2}{R_1 + R_2}$ 时， $\operatorname{rank} S = 2 = n$ ，系统可控。但是，当电桥处于平衡状态，即 $R_1 R_1 = R_2 R_3$ 时， $\frac{R_1}{R_1 + R_2} = \frac{R_3}{R_3 + R_4}$ 及 $\frac{R_2}{R_1 + R_2} = \frac{R_4}{R_3 + R_4}$ 成立，这时状态方程变为

$$
\begin{array}{l} \dot {x} _ {1} = - \frac {1}{L} \left(\frac {R _ {1} R _ {2}}{R _ {1} + R _ {2}} + \frac {R _ {3} R _ {4}}{R _ {3} + R _ {4}}\right) x _ {1} + \frac {1}{L} u \\ \dot {x} _ {2} = - \frac {1}{C} \left(\frac {1}{R _ {1} + R _ {2}} - \frac {1}{R _ {3} + R _ {4}}\right) x _ {2} \\ \end{array}
$$

可控性矩阵为

$$
\boldsymbol {S} = \left[ \begin{array}{l l} \boldsymbol {b} & \boldsymbol {A b} \end{array} \right] = \left[ \begin{array}{c c} \frac {1}{L} & - \frac {1}{L ^ {2}} \left(\frac {R _ {1} R _ {2}}{R _ {1} + R _ {2}} + \frac {R _ {3} R _ {4}}{R _ {3} + R _ {4}}\right) \\ 0 & 0 \end{array} \right]
$$

$\operatorname{rank} S = 1 < n$ ，系统不可控， $u$ 不能控制 $x_{2}, x_{2}$ 是不可控状态变量。

例9-11 已知 $\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ , 求 $A^{100} = ?$

解 $\mathbf{A}$ 的特征多项式为

$$
f (\lambda) = | \lambda I - A | = \left| \begin{array}{c c} \lambda - 1 & - 2 \\ 0 & \lambda - 1 \end{array} \right| = \lambda^ {2} - 2 \lambda + 1
$$

根据凯莱-哈密顿定理，有

$$
\begin{array}{l} f (\mathbf {A}) = \mathbf {A} ^ {2} - 2 \mathbf {A} + \mathbf {I} = 0 \\ \mathbf {A} ^ {2} = 2 \mathbf {A} - \mathbf {I} \\ \end{array}
$$

故 $A^3 = AA^2 = 2A^2 - A = 2(2A - I) - A = 3A - 2I$

$$\mathbf {A} ^ {4} = \mathbf {A A} ^ {3} = 3 \mathbf {A} ^ {2} - 2 \mathbf {A} = 3 (2 \mathbf {A} - \mathbf {I}) - 2 \mathbf {A} = 4 \mathbf {A} - 3 \mathbf {I}$$

根据数学归纳法，有
