# 1.8 定常线性系统的输出调节问题

本节讨论线性控制系统的调节问题。调节理论在工程中实际有十分广泛的应用，它是控制系统设计的核心内容之一。

最一般线性调节系统的数学模型为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = A _ {1} x _ {1} (t) + A _ {3} x _ {2} (t) + B _ {1} u (t), \\ \dot {x} _ {2} (t) = A _ {2} x _ {2} (t), \\ y (t) = C _ {1} x _ {1} (t) + C _ {2} x _ {2} (t), \\ z (t) = D _ {1} x _ {1} (t) + D _ {2} x _ {2} (t), \end{array} \right. \tag {1.8.1}
$$

其中 $x_{1}(t)$ 为 $n_1$ 维系统状态， $x_{2}(t)$ 为 $n_2$ 维外部输入，它可能是干扰输入，也可能是参考输入， $u(t)$ 为 $r$ 维控制输入， $y(t)$ 为 $m$ 维量测输出， $z(t)$ 为 $q$ 维调节输出； $A_{1}, A_{2}, A_{3}, B_{1}, C_{1}, C_{2}, D_{1}$ 和 $D_{2}$ 分别是具有相应维数的常值矩阵.

如果 $C_2 = 0, D_2 = 0$ , 那么系统 (1.8.1) 代表一个纯调节系统; 如果 $A_3 = 0$ , 那么系统 (1.8.1) 代表纯跟踪系统; $z(t)$ 表示跟踪误差. 一般来说, 系统 (1.8.1) 表示一个带有干扰输入和参考输入的跟踪系统. 因为跟踪问题与调节问题没有本质上的区别, 所以总是把系统 (1.8.1) 看成一个调节系统.

这个模型与前面几节所研究的系统不同之处在于，这里考虑了系统外部干扰输入或参考输入对系统的影响。同时在一般系统中，被调节变量和量测变量可能不同，因此也把它们区分开来。

对一个实际系统，存在外部干扰是不可避免的。在研究调节问题时注意到这一点是有实际工程意义的。对于系统的精度，稳定的外部输入信号是可以忽略不计的，因此总可以假设 $x_{2}(t)$ 是不稳定的。在本节里，始终假设

$$\sigma (A _ {2}) \subset \overline {{{\mathbb {C}}}} ^ {+},$$

这里及今后 $\mathbb{C}^+$ 表示复平面的右半开平面， $\mathbb{C}^{-}$ 表示复平面的左半开平面，而 $\overline{\mathbb{C}}^+$ 表示复平面的右半闭平面。同时，还假设

$$\operatorname{rank} \boldsymbol {B} _ {1} = r, \quad \operatorname{rank} \boldsymbol {D} _ {1} = q, \quad \operatorname{rank} [ \boldsymbol {C} _ {1} \quad \boldsymbol {C} _ {2} ] = m.$$

解决输出调节问题的主要目的是，对系统(1.8.1)设计一个动态补偿器

$$
\left\{ \begin{array}{l} \dot {x} _ {c} (t) = A _ {c} x _ {c} (t) + B _ {c} y (t), \\ u (t) = F _ {c} x _ {c} (t) + F y (t), \end{array} \right. \tag {1.8.2}
$$

其中 $x_{c}(t)$ 是 $l$ 维状态变量， $A_{c}, B_{c}, F_{c}$ 和 $\pmb{F}$ 分别是 $l \times l, l \times m, r \times l$ 和 $r \times m$ 常值矩阵，使得闭环系统

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {x} _ {c} (t) \end{array} \right] = \left[ \begin{array}{c c} A _ {1} + B _ {1} F C _ {1} & B _ {1} F _ {c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c} \\ B _ {c} C _ {1} & A _ {c} \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {c} (t) \end{array} \right] + \left[ \begin{array}{c} A _ {3} + B _ {1} F C _ {2} \\ B _ {c} C _ {2} \end{array} \right] x _ {2}} \\ z (t) = D _ {1} x _ {1} (t) + D _ {2} x _ {2} (t) \end{array} \right. \tag {1.8.3}
$$

具有如下性质：

(1) 它是内部稳定的，即当 $A_{3} = 0, C_{2} = 0$ 时，有

$$
\sigma \left(\left[ \begin{array}{c c} A _ {1} + B _ {1} F C _ {1} & B _ {1} F _ {c} \\ B _ {c} C _ {1} & A _ {c} \end{array} \right]\right) \subset \mathbb {C} ^ {-};
$$

(2) 它是输出调节（或输出无静差）的，即对任意 $x_{20} = x_2(t_0)$ ，都有
