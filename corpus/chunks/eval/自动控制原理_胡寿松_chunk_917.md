# (3) 系统可控、可观测性分析

1) 可控、可观测性判断。系统的可控、可观测性是线性系统分析中的重要问题。考虑线性定常连续系统

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t), \boldsymbol {y} (t) = \boldsymbol {C} \boldsymbol {x} (t)$$

若系统完全可控，则

$$\operatorname{rank} [ \boldsymbol {B} \quad \boldsymbol {A B} \quad \dots \quad \boldsymbol {A} ^ {n - 1} \boldsymbol {B} ] = n$$

式中，n 为矩阵 A 的维数； $S=\left[\begin{array}{ccc}B & AB & \cdots & A^{n-1}B\end{array}\right]$ 为系统的可控性矩阵。

若系统完全可观测，则

$$
\operatorname{rank} \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \vdots \\ \mathbf {C A} ^ {n - 1} \end{array} \right] = n
$$

式中， $n$ 为矩阵 $\mathbf{A}$ 的维数； $\pmb {V} = \left[ \begin{array}{c}\pmb {C}\\ \pmb {C}\pmb {A}\\ \vdots \\ \pmb {C}\pmb {A}^{n - 1} \end{array} \right]$ 为系统的可观测性矩阵。

在 MATLAB 中可分别使用 ctrb 和 obsv 命令求取系统的可控性矩阵和可观测性矩阵, 再用 rank 命令求取矩阵的秩, 与 $n$ 比较后判断系统的可控、可观测性。

命令格式： $S=ctrb(A,B)$

$$\mathrm{V} = \text { obsv(A,C) }$$

式中，S为可控性矩阵；V为可观测性矩阵。

2）可控、可观测性分解。选取合适的线性变换，可以对系统进行结构分解，从而更明显地揭示出系统的结构特性和传递特性。MATLAB中的ctrbf和obsvf命令可以直接用来对系统进行可控、可观测性分解。

MATLAB 缺省的可控性分解结构为

$$
\left[ \begin{array}{l} \dot {\boldsymbol {x}} _ {c} \\ \dot {\boldsymbol {x}} _ {c} \end{array} \right] = \left[ \begin{array}{l l} \overline {{\boldsymbol {A}}} _ {1 1} & \boldsymbol {0} \\ \overline {{\boldsymbol {A}}} _ {2 1} & \overline {{\boldsymbol {A}}} _ {2 2} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} _ {c} \\ \boldsymbol {x} _ {c} \end{array} \right] + \left[ \begin{array}{l} \boldsymbol {0} \\ \overline {{\boldsymbol {B}}} _ {2} \end{array} \right] \boldsymbol {u}, \quad \boldsymbol {y} = [ \overline {{\boldsymbol {C}}} _ {1} - \overline {{\boldsymbol {C}}} _ {2} ] \left[ \begin{array}{l} \boldsymbol {x} _ {c} \\ \boldsymbol {x} _ {c} \end{array} \right].
$$

式中，可控子系统动态方程为

$$\dot {\boldsymbol {x}} _ {c} = \overline {{{\boldsymbol {A}}}} _ {2 1} \boldsymbol {x} _ {c} + \overline {{{\boldsymbol {A}}}} _ {2 2} \boldsymbol {x} _ {c} + \overline {{{\boldsymbol {B}}}} _ {2} \boldsymbol {u}, \quad \boldsymbol {y} _ {2} = \overline {{{\boldsymbol {C}}}} _ {2} \boldsymbol {x} _ {c}$$

不可控子系统动态方程为

$$\dot {\boldsymbol {x}} _ {c} = \bar {\boldsymbol {A}} _ {1 1} \boldsymbol {x} _ {c}, \quad \boldsymbol {y} _ {1} = \bar {\boldsymbol {C}} _ {1} \boldsymbol {x} _ {c}$$

MATLAB 缺省的可观测性分解结构为
