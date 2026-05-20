# (1) 定义及表达式

初始条件为零时,输出向量的拉氏变换式与输入向量的拉氏变换式之间的传递关系称为传递函数矩阵,简称传递矩阵。设系统动态方程为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t), \quad \boldsymbol {y} (t) = \boldsymbol {C} \boldsymbol {x} (t) + \boldsymbol {D} \boldsymbol {u} (t) \tag {9-46}$$

令初始条件为零,进行拉氏变换有

$$s \boldsymbol {X} (s) = \boldsymbol {A} \boldsymbol {X} (s) + \boldsymbol {B} \boldsymbol {U} (s), \quad \boldsymbol {Y} (s) = \boldsymbol {C} \boldsymbol {X} (s) + \boldsymbol {D} \boldsymbol {U} (s)$$

则 $\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)$

$$\mathbf {Y} (s) = \left[ \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D} \right] \mathbf {U} (s) = \mathbf {G} (s) \mathbf {U} (s) \tag {9-47}$$

系统的传递函数矩阵表达式为

$$\boldsymbol {G} (s) = \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} + \boldsymbol {D} \tag {9-48}$$

若输入 $\pmb{u}$ 为 $p$ 维向量，输出 $\pmb{y}$ 为 $q$ 维向量，则 $\mathbf{G}(s)$ 为 $q\times p$ 矩阵。式(9-47）的展开式为

$$
\left[ \begin{array}{c} Y _ {1} (s) \\ Y _ {2} (s) \\ \vdots \\ Y _ {q} (s) \end{array} \right] = \left[ \begin{array}{c c c c} G _ {1 1} (s) & G _ {1 2} (s) & \dots & G _ {1 p} (s) \\ G _ {2 1} (s) & G _ {2 2} (s) & \dots & G _ {2 p} (s) \\ \vdots & \vdots & & \vdots \\ G _ {q 1} (s) & G _ {q 2} (s) & \dots & G _ {q p} (s) \end{array} \right] \left[ \begin{array}{c} U _ {1} (s) \\ U _ {2} (s) \\ \vdots \\ U _ {p} (s) \end{array} \right] \tag {9-49}
$$

式中 $G_{ij}(s)(i=1,2,\cdots,q;j=1,2,\cdots,p)$ 表示第 i 个输出量与第 j 个输入量之间的传递函数。

例 9-6 已知系统动态方程为

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right]

\left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right]
$$

试求系统的传递矩阵。

解 已知

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right], \quad \mathbf {D} = \mathbf {0}
$$

故
