$$\boldsymbol {B} _ {1} \boldsymbol {F} _ {c} \boldsymbol {V} _ {2} = \boldsymbol {A} _ {3}, \quad \boldsymbol {A} _ {c} \boldsymbol {V} _ {2} = \boldsymbol {V} _ {2} \boldsymbol {A} _ {2}.$$

这就是所要的结论.

充分性. 设式 (1.8.40) 成立, 并且闭环系统 (1.8.39) 内部稳定, 那么等式 (1.8.41) 成立. 再依引理 1.8.1 知, 对任意 $x_{2}(t_{0}) = x_{20}$ 都有 $\lim_{t \to \infty} z(t) = 0$ . 这说明动态补偿器 (1.8.2) 是系统 (1.8.39) 的一个全状态输出调节器.

下面分析定理1.8.2的两个条件．等式 $B_{1}F_{c}V_{2} = A_{3}$ 表明

$$\operatorname{rank} \boldsymbol {B} _ {1} = \operatorname{rank} [ \boldsymbol {B} _ {1}, \boldsymbol {A} _ {3} ],$$

这就是定理1.8.1的条件(1.8.31). 由等式 $A_{c}V_{2} = V_{2}A_{2}$ 可知，如果 $\operatorname{rank} A_{3} = n_{2}$ ，那么必有 $\operatorname{rank} V_{2} = n_{2}$ . 取 $l \times l$ 可逆矩阵

$$
\boldsymbol {T} = \left[ \begin{array}{c c} \boldsymbol {T} _ {1} & \boldsymbol {T} _ {2} \end{array} \right],
$$

并对补偿器 (1.8.2) 做坐标变换

$$z _ {c} = T ^ {- 1} x _ {c}.$$

这时补偿器 (1.8.2) 变成

$$\dot {z} _ {c} (t) = \overline {{{A}}} _ {c} z _ {c} (t) + \overline {{{B}}} _ {c} y (t),u (t) = \overline {{{F}}} _ {c} z _ {c} (t) + F y (t),$$

其中 $\overline{A}_c = T^{-1}A_cT, \overline{B}_c = T^{-1}B_c, \overline{F}_c = F_cT,$ 并且

$$
\overline {{{A}}} _ {c} = \left[ \begin{array}{l l} A _ {c _ {1}} & 0 \\ A _ {c _ {2}} & A _ {2} \end{array} \right],
$$

而 $A_{c_1}, A_{c_2}$ 分别为 $l_1 \times l_1, l_1 \times n_2$ 矩阵， $l_1 + n_2 = l$ . 这时，动态补偿器 (1.8.2) 代数等价于

$$
\left\{ \begin{array}{l} \dot {z} _ {c _ {1}} (t) = A _ {c _ {1}} z _ {c _ {1}} (t) + B _ {c _ {1}} y (t), \\ \dot {z} _ {c _ {2}} (t) = A _ {c _ {2}} z _ {c _ {1}} (t) + A _ {2} z _ {c _ {2}} (t) + B _ {c _ {2}} y (t), \\ u (t) = F _ {c _ {1}} z _ {c _ {1}} (t) + F _ {c _ {2}} z _ {c _ {2}} (t) + F y (t), \end{array} \right.
$$

这里

$$
\overline {{{B}}} _ {c} = \left[ \begin{array}{l} B _ {c _ {1}} \\ B _ {c _ {2}} \end{array} \right] \quad \overline {{{F}}} _ {c} = \left[ \begin{array}{l l} F _ {c _ {1}} & F _ {c _ {2}} \end{array} \right].
$$

同时在这个坐标变换下，有

$$
\boldsymbol {A} _ {3} = \boldsymbol {B} _ {1} \overline {{\boldsymbol {F}}} _ {c} \boldsymbol {T} ^ {- 1} \boldsymbol {V} _ {2}, \quad \boldsymbol {T} ^ {- 1} \boldsymbol {V} _ {2} = \left[ \begin{array}{l} 0 \\ I _ {n _ {2}} \end{array} \right].
$$

于是有

$$\boldsymbol {B} _ {1} \boldsymbol {F} _ {c _ {2}} = \boldsymbol {A} _ {3}.$$

所以控制分量 $F_{c_2}z_{c_2}(t)$ 就是干扰补偿部分.

另外，在这个坐标变换下，闭环系统为
