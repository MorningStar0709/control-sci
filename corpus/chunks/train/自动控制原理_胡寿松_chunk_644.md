$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 5 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \\ 0 & 1 \\ - 2 & 0 \end{array} \right] \boldsymbol {u}, \quad n = 4
$$

试判别系统的可控性。

解 根据状态方程可写出

$$
[ s \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} ] = \left[ \begin{array}{c c c c c c} s & - 1 & 0 & 0 & 0 & 1 \\ 0 & s & 1 & 0 & 1 & 0 \\ 0 & 0 & s & - 1 & 0 & 1 \\ 0 & 0 & - 5 & s & - 2 & 0 \end{array} \right]
$$

考虑到 $\mathbf{A}$ 的特征值为 $\lambda_1 = \lambda_2 = 0, \lambda_3 = \sqrt{5}, \lambda_4 = -\sqrt{5}$ , 所以只需对它们来检验上述矩阵的秩。通过计算可知, 当 $s = \lambda_1 = \lambda_2 = 0$ 时, 有

$$
\operatorname{rank} [ s \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} ] = \operatorname{rank} \left[ \begin{array}{c c c c} - 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & - 1 & 0 \\ 0 & - 5 & 0 & - 2 \end{array} \right] = 4
$$

当 $s = \lambda_3 = \sqrt{5}$ 时，有

$$
\operatorname{rank} [ s \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} ] = \operatorname{rank} \left[ \begin{array}{c c c c} \sqrt {5} & - 1 & 0 & 1 \\ 0 & \sqrt {5} & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 2 & 0 \end{array} \right] = 4
$$

当 $s = \lambda_4 = -\sqrt{5}$ 时，有

$$
\operatorname{rank} [ s \boldsymbol {I} - \boldsymbol {A} \quad \boldsymbol {B} ] = \operatorname{rank} \left[ \begin{array}{c c c c} - \sqrt {5} & - 1 & 0 & 1 \\ 0 & - \sqrt {5} & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 2 & 0 \end{array} \right] = 4
$$

计算结果表明,充分必要条件式(9-112)成立,故系统完全可控。

对角线规范型判据 若线性定常连续系统(9-83)矩阵 A 的特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 两两相异，由线性变换式(9-83)可变为对角线规范型

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c} \lambda_ {1} & & & 0 \\ & \lambda_ {2} & & \\ 0 & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \boldsymbol {x} + \overline {{\boldsymbol {B}}} \boldsymbol {u} \tag {9-117}
$$

则系统(9-83)完全可控的充分必要条件是,在式(9-117)中, $\bar{B}$ 不包含元素全为零的行。

证明 可用秩判据予以证明,推证过程略。

例 9-13 已知线性定常连续系统的对角线规范型为

$$
\left[ \begin{array}{l} \dot {\bar {x}} _ {1} \\ \dot {\bar {x}} _ {2} \\ \dot {\bar {x}} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 8 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 2 \end{array} \right] \left[ \begin{array}{l} \bar {x} _ {1} \\ \bar {x} _ {2} \\ \bar {x} _ {3} \end{array} \right] + \left[ \begin{array}{c c} 0 & 1 \\ 3 & 0 \\ 0 & 2 \end{array} \right] \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right]
$$

试判定系统的可控性。

解 由于此规范型中 $\bar{B}$ 不包含元素全为零的行, 故系统完全可控。
