$$
\sigma \left(\left[ \begin{array}{c c} A + B F C & B F _ {c} \\ B _ {c} C & A _ {c} \end{array} \right]\right) = \sigma (A + B K) \cup \sigma (\overline {{A}} _ {2 2} - G _ {2} \overline {{A}} _ {1 2}) \subset \mathbb {C} ^ {-}.
$$

由此可见闭环系统 (1.8.26) 是内部稳定的，从而对 $x(t)$ 是输出调节的。这表明系统 (1.8.25) 是系统 (1.6.1) 的一个无静差补偿器。

采用极小阶观测器方法可以给系统提供一个 $n - m$ 阶动态补偿器。如果抛开具体设计过程，可以归纳如下：

已知定常线性系统 (1.6.1) 是完全能控和完全能观测的, 并且 $\operatorname{rank} C = m$ , 那么对这个系统总可以设计一个 $n - m$ 阶的动态补偿器

$$
\left\{ \begin{array}{l} \dot {x} _ {c} (t) = A _ {c} x _ {c} (t) + B _ {c} y (t), \\ u (t) = F _ {c} x _ {c} (t) + F y (t) \end{array} \right.
$$

使得由它和式(1.6.1)构成的闭环系统(1.8.26)是内部稳定的和输出调节的，即这个闭环系统是一个无静差系统。它的极点由 $A + BK$ 和 $\overline{A}_{22} - G_2\overline{A}_{12}$ 的特征值完全决定。动态补偿器的设计步骤如下：

第一步：由 $(A, B)$ 能控，依定理1.6.1，可选择 $r \times n$ 常值控制增益矩阵 $\pmb{K}$ ，使得 $A + BK$ 是稳定的；

第二步：假设 $\operatorname{rank} C_1 = m, C = [C_1 - C_2]$ ，并形成矩阵

$$
\boldsymbol {P} = \left[ \begin{array}{c c} \boldsymbol {C} _ {1} & \boldsymbol {C} _ {2} \\ 0 & \boldsymbol {I} _ {n - m} \end{array} \right],
$$

计算出

$$
\boldsymbol {P} ^ {- 1} = \left[ \begin{array}{c c} \boldsymbol {C} _ {1} ^ {- 1} & - \boldsymbol {C} _ {1} ^ {- 1} \boldsymbol {C} _ {2} \\ 0 & \boldsymbol {I} _ {n - m} \end{array} \right].
$$

第三步：按下列公式计算 $\overline{A}_{ij},\overline{B}_i$ $(i,j = 1,2)$

$$
\left[ \begin{array}{l l} \overline {{A}} _ {1 1} & \overline {{A}} _ {1 2} \\ \overline {{A}} _ {2 1} & \overline {{A}} _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} C _ {1} & C _ {2} \\ 0 & I _ {n - m} \end{array} \right] \left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] \left[ \begin{array}{c c} C _ {1} ^ {- 1} & - C _ {1} ^ {- 1} C _ {2} \\ 0 & I _ {n - m} \end{array} \right].
$$

于是有

$$
\begin{array}{l} \overline {{{A}}} _ {1 1} = \left(C _ {1} A _ {1 1} + C _ {2} A _ {2 1}\right) C _ {1} ^ {- 1}, \\ \overline {{{A}}} _ {1 2} = C _ {1} \left[ A _ {1 2} - A _ {1 1} C _ {1} ^ {- 1} C _ {2} \right] + C _ {2} \left[ A _ {2 2} - A _ {2 1} C _ {1} ^ {- 1} C _ {2} \right], \\ \overline {{{A}}} _ {2 1} = A _ {2 1} C _ {1} ^ {- 1}, \quad \overline {{{A}}} _ {2 2} = A _ {2 2} - A _ {2 1} C _ {1} ^ {- 1} C _ {2}, \\ \overline {{{B}}} _ {1} = C B, \quad \overline {{{B}}} _ {2} = B _ {2}; \\ \end{array}
$$

第四步：依定理1.6.1选择 $(n - m)\times m$ 矩阵 $G_{2}$ ，使得 $\overline{A}_{22} - G_2\overline{A}_{12}$ 是稳定的；

第五步：按照下列公式计算矩阵 $\overline{A}_c, \overline{B}_c, F_c$ 和 $F$ :
