J _ {i} \underset {\left(\sigma_ {i} \times \sigma_ {i}\right)} {=} - \left[ \begin{array}{c c c} J _ {i 1} & & \\ & J _ {i 2} & \\ & & \ddots \\ & & J _ {i \alpha_ {i}} \end{array} \right] \quad \hat {C} _ {i} = \left[ \hat {C} _ {i 1}, \hat {C} _ {i 2}, \dots , \hat {C} _ {i \alpha_ {i}} \right] \tag {3.88}

J _ {i k} \left(\sigma_ {i k \times r _ {i k}}\right) = \left[ \begin{array}{c c c c c} \lambda_ {i} & 1 & & & \\ & \lambda_ {i} & 1 & & \\ & & \ddots & \ddots & 1 \\ & & & \ddots & \lambda_ {i} \end{array} \right] \quad \hat {C} _ {i k} = [ \hat {c} _ {i i k}, \hat {c} _ {2 i k}, \dots , \hat {c} _ {r i k} ] \tag {3.88a}
$$

而 $(r_{i1} + r_{i2} + \dots + r_{i\alpha_i}) = \sigma_i$ ，由 $\hat{C}_{ik}(k - 1, 2, \dots, \alpha_i)$ 的第一列所组成的矩阵

$$[ \hat {c} _ {1 i 1}, \hat {c} _ {1 i 2}, \dots , \hat {c} _ {1 i a _ {i}} ] \tag {3.89}$$

对 $i=1,2,\cdots,l$ 均为列线性无关。

例1 已知线性定常系统的对角线规范形为：

$$
\left[ \begin{array}{l} \dot {\overline {{x}}} _ {1} \\ \dot {\overline {{x}}} _ {2} \\ \dot {\overline {{x}}} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 7 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} \overline {{x}} _ {1} \\ \overline {{x}} _ {2} \\ \overline {{x}} _ {3} \end{array} \right]

y = \left[ \begin{array}{c c c} 4 & 0 & 7 \\ 0 & 3 & 1 \end{array} \right] \left[ \begin{array}{l} \overline {{x}} _ {1} \\ \overline {{x}} _ {2} \\ \overline {{x}} _ {3} \end{array} \right]
$$

不难看出，此规范形中 $\hat{C}$ 不包含元素全为零的列，所以系统为完全能观测。

例2 给定线性定常系统的约当规范形为：

$$
\hat {x} = \left[ \begin{array}{c c c c c c c c} - 2 & 1 & & & & & \\ 0 & - 2 & & & & & \\ \hline & & - 2 & & & & \\ & & & - 2 & & & \\ & & & & 3 & 1 & \\ & & & & 0 & 3 & \\ & & & & & & 3 \end{array} \right] \hat {x}

\mathbf {y} = \left[ \begin{array}{c c c c c c c c c} 4 & 0 & 0 & 0 & 0 & 2 & 0 & 0 \\ 0 & 0 & 3 & 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 5 & 3 & 0 & 0 \end{array} \right] \hat {\mathbf {x}}
$$

容易定出

$$
\left[ \hat {c} _ {1 1 1}, \hat {c} _ {1 1 2}, \hat {c} _ {1 1 3} \right] = \left[ \begin{array}{l l l} 4 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{array} \right]

\left[ \hat {c} _ {1 2 1}, \quad \hat {c} _ {1 2 2} \right] = \left[ \begin{array}{l l} 2 & 0 \\ 1 & 1 \\ 3 & 0 \end{array} \right]
$$

显然,它们都是列线性无关的,因此可知系统为完全能观测。

能观测性指数 考虑完全能观测的线性定常系统(3.75)，其中 $A$ 和 $C$ 分别是 $n \times n$ 和 $q \times n$ 的常值矩阵。定义

$$
\overline {{{Q}}} _ {k} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {k - 1} \end{array} \right] \tag {3.90}
$$
