$$
\begin{array}{l} \overline {{{A}}} _ {c} = \left(\overline {{{A}}} _ {2 2} - G _ {2} \overline {{{A}}} _ {1 2}\right) + \left(\overline {{{B}}} _ {2} - G _ {2} \overline {{{B}}} _ {1}\right) F _ {c}, \\ \overline {{{\boldsymbol {B}}}} _ {c} = \left(\overline {{{\boldsymbol {A}}}} _ {2 1} - \boldsymbol {G} _ {2} \overline {{{\boldsymbol {A}}}} _ {1 1}\right) + \left(\overline {{{\boldsymbol {A}}}} _ {2 2} - \boldsymbol {G} _ {2} \overline {{{\boldsymbol {A}}}} _ {1 2}\right) \boldsymbol {G} _ {2} + \left(\overline {{{\boldsymbol {B}}}} _ {2} - \boldsymbol {G} _ {2} \overline {{{\boldsymbol {B}}}} _ {1}\right) \boldsymbol {F}, \\ \boldsymbol {F} _ {c} = \boldsymbol {K} _ {2} - \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} \boldsymbol {C} _ {2}, \quad \boldsymbol {F} = \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} + (\boldsymbol {K} _ {2} - \boldsymbol {K} _ {1} \boldsymbol {C} _ {1} ^ {- 1} \boldsymbol {C} _ {2}) \boldsymbol {G} _ {2}. \\ \end{array}
$$

根据对偶原理，当 $\operatorname{rank} B = r$ 时，对系统 (1.6.1) 还可以设计一个 $n - r$ 阶动态补偿器

$$
\left\{ \begin{array}{l} \dot {x} _ {0} (t) = A _ {0} x _ {0} (t) + B _ {0} (t) y (t), \\ u (t) = E _ {0} x _ {0} (t) + E y (t), \end{array} \right.
$$

其中 $x_0(t)$ 是 $n - r$ 维状态变量， $A_0, B_0, E_0$ 和 $\pmb{E}$ 分别是 $(n - r) \times (n - r), (n - r) \times m, r \times (n - r)$ 和 $r \times m$ 常值矩阵。这时闭环系统

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} (t) \\ \dot {x} _ {0} (t) \end{array} \right] = \left[ \begin{array}{c c} A + B E C & B E _ {0} \\ B _ {0} C & A _ {0} \end{array} \right] \left[ \begin{array}{c} x (t) \\ x _ {0} (t) \end{array} \right],} \\ y (t) = C x (t) \end{array} \right.
$$

是内部稳定的和输出调节的.

从以上的讨论可以看出，对一个完全能控和完全能观测的系统，用状态反馈加极小阶观测器补偿的办法，可以设计出最低阶数为 $\min \{n - r, n - m\}$ 的动态补偿器.
