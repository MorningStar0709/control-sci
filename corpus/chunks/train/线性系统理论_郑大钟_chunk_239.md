$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 5 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ - 2 \end{array} \right] \boldsymbol {u}
y = [ 1 \quad 0 \quad 0 \quad 0 ] x
$$

再指定期望的闭环极点为 $\lambda_{1}^{*} = -1, \lambda_{2,3}^{*} = -1 \pm j, \lambda_{3}^{*} = -2$ ，观测器的特征值为 $s_{1} = -3, s_{2,3} = -3 \pm j2$ ，试设计一个观测器一状态反馈控制系统，并画出系统的组成结构图。

5.24 考虑多变量线性定常系统:

$$
\begin{array}{l} \dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} \\ \mathbf {y} = C \mathbf {x} \\ \end{array}
$$

已知它的一个全维观测器为

$$\hat {\boldsymbol {x}} = (A - L C) \hat {\boldsymbol {x}} + L \boldsymbol {y} + B \boldsymbol {u}$$

试论证它是全维观测器

$$
\begin{array}{l} \dot {\boldsymbol {z}} = F \boldsymbol {z} + G \boldsymbol {y} + H \boldsymbol {u} \\ \hat {x} = T ^ {- 1} z \\ \end{array}
$$

的一种特殊情况, 即其也必满足条件: (i) $TA - FT = GC$ , (ii) $H = TB$ , (iii) $F$ 的特征值均具有负实部。

5.25 设系统 $\dot{x} = Ax + Bu, y = Cx$ 是用输入变换和状态反馈 $\{L, K\}$ 能静态解耦的，试证明：

(i) 此系统的任一代数等价系统也一定是能静态解耦的；

(ii) 对此系统的任意状态反馈系统也必是能静态解耦的。

5.26 已知标准 $LQ$ 调节问题

$$
\begin{array}{l} \dot {x} = A x + B u, \quad x (0) = x _ {0} \\ J = \int_ {0} ^ {\infty} (\boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {u} ^ {T} R \boldsymbol {u}) d t \\ \end{array}
$$

的最优控制律和最优性能值为：

$$
\begin{array}{l} \boldsymbol {u} ^ {*} = - K ^ {*} \boldsymbol {x}, \quad K ^ {*} = R ^ {- 1} B ^ {T} P \\ J ^ {*} = x _ {0} ^ {T} P x _ {0} \\ \end{array}
$$

其中 P 为如下的黎卡提代数方程的正定对称解阵:

$$P A + A ^ {T} P + Q - P B R ^ {- 1} B ^ {T} P = 0$$

现若取加权阵为 $\alpha Q$ 和 $\alpha R, \alpha > 0$ ，试求此种情况下的最优控制律和最优性能值。

5.27 试证：对于任意的常阵 $F$ ，输出反馈系统 $\{A - BFC, B, C\}$ 和受控系统 $\{A, B, C\}$ 具有相同的能控性指数和能观测性指数。
