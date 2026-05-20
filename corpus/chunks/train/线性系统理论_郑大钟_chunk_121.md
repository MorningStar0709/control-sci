$$
\begin{array}{l} \dot {x} = \left[ \begin{array}{c c c} 1 & 0 & 2 \\ 2 & 1 & 1 \\ 1 & 0 & - 2 \end{array} \right] x + \left[ \begin{array}{l} 1 \\ 2 \\ 1 \end{array} \right] u, n = 3 \\ y = \left[ \begin{array}{l l l} 0 & 1 & 1 \end{array} \right] x \\ \end{array}
$$

定出其特征多项式

和常数

$$\alpha (s) \triangleq \det (s I - A) = s ^ {3} - 5 s + 4\beta_ {2} = \mathbf {c b} = 3\beta_ {1} = c A b + \alpha_ {2} c b = 4\beta_ {0} = c A ^ {2} b + \alpha_ {2} c A b + \alpha_ {1} c b = 0$$

则利用(3.163)和(3.164)，即可导出系统的能控规范形为：

$$
\begin{array}{l} \dot {\bar {x}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 4 & 5 & 0 \end{array} \right] \bar {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] u \\ y = [ 0 \quad 4 \quad 3 ] \bar {x} \\ \end{array}
$$

再利用(3.162)可求出变换阵

$$
P = \left[ A ^ {2} \boldsymbol {b}, A \boldsymbol {b}, \boldsymbol {b} \right] \left[ \begin{array}{c c c} 1 & 0 & 0 \\ \alpha_ {2} & 1 & 0 \\ \alpha_ {1} & \alpha_ {2} & 1 \end{array} \right] = \left[ \begin{array}{c c c} - 4 & 3 & 1 \\ 0 & 5 & 2 \\ 0 & - 1 & 1 \end{array} \right]
$$

而其逆为

$$
P ^ {- 1} = \left[ \begin{array}{c c c} - \frac {1}{4} & \frac {1}{7} & - \frac {1}{2 8} \\ 0 & \frac {1}{7} & - \frac {2}{7} \\ 0 & \frac {1}{7} & \frac {5}{7} \end{array} \right]
$$

于是，又可定出能控规范形中的状态向量为：

$$
\bar {x} = P ^ {- 1} x = \left[ \begin{array}{c c c} - \frac {1}{4} & \frac {1}{7} & - \frac {1}{2 8} \\ 0 & \frac {1}{7} & - \frac {2}{7} \\ 0 & \frac {1}{7} & \frac {5}{7} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] = \left[ \begin{array}{c} - \frac {1}{4} x _ {1} + \frac {1}{7} x _ {2} - \frac {1}{2 8} x _ {3} \\ \frac {1}{7} x _ {2} - \frac {2}{7} x _ {3} \\ \frac {1}{7} x _ {2} + \frac {5}{7} x _ {3} \end{array} \right]
$$

能观测规范形 考虑完全能观测的单输入-单输出线性定常系统

$$\Sigma : \dot {x} = A x + b u \tag {3.170}y = c x$$

且其特征多项式表为（3.160），而常数 $\beta_{n-1},\cdots,\beta_{1},\beta_{0}$ 如（3.161）所定义。再因系统为能观测故有如下的基本属性

$$
\operatorname{rank} \left[ \begin{array}{c} \boldsymbol {c} \\ \boldsymbol {c A} \\ \vdots \\ \boldsymbol {c A ^ {n - 1}} \end{array} \right] = n \tag {3.171}
$$

由此，并注意到能观测性和能控性间的对偶关系，可定出化系统（3.170）为能观测规范形的变换阵为：
