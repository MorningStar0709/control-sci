$$\det (s I - A) = \alpha \det D (s) \tag {8.16}$$

其中 $\alpha$ 为非零常数。于是，依据关系式(8.16)和结论1，进一步可得到

$$G (s) \text {的极点} = \det D (s) = 0 \text {的根} = \det (s I - A) = 0 \text {的根} \tag {8.17}$$

再根据实现理论知， $(A, B, C)$ 和 $N(s)D^{-1}(s)$ 之间存在如下的史密斯形意义下的等价

关系：

$$
\left[ \begin{array}{l l} s I - A & B \\ - C & 0 \end{array} \right] \sim \left[ \begin{array}{l l} \bar {D} (s) & I \\ - N (s) & 0 \end{array} \right] \quad \bar {D} (s) = \left[ \begin{array}{l l} I & 0 \\ 0 & D (s) \end{array} \right] \tag {8.18}
$$

而进一步可有

$$
\left[ \begin{array}{l l} \bar {D} (s) & I \\ - N (s) & 0 \end{array} \right] \left[ \begin{array}{l l} 0 & - I \\ I & D (s) \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ 0 & N (s) \end{array} \right] \tag {8.19}
$$

其中等式左边的第二个矩阵为单模阵。由此可知，又有

$$
\left[ \begin{array}{l l} \bar {D} (s) & I \\ - N (s) & 0 \end{array} \right] \stackrel {{S}} {{\sim}} \left[ \begin{array}{c c} I & 0 \\ 0 & N (s) \end{array} \right] \tag {8.20}
$$

这样，根据等价变换的传递性质，可进而导出

$$
\left[ \begin{array}{c c} s I - A & B \\ - C & 0 \end{array} \right] \sim \left[ \begin{array}{c c} I & 0 \\ 0 & N (s) \end{array} \right] \tag {8.21}
$$

或将其表为

$$
\left[ \begin{array}{c c} I & \mathbf {0} \\ \mathbf {0} & N (s) \end{array} \right] = U (s) \left[ \begin{array}{c c} s I - A & B \\ - C & \mathbf {0} \end{array} \right] V (s) \tag {8.22}
$$

其中 $U(s)$ 和 $V(s)$ 为单模阵。于是，依据结论1和式(8.22)，就即可得到

$G(s)$ 的零点 $=$ 使 $N(s)$ 降秩的 $s$ 值 $=$ 使 $\left[ \begin{array}{cc}I & 0\\ 0 & N(s) \end{array} \right]$ 降秩的 $s$ 值 $=$ 使 $\left[ \begin{array}{cc}sI - A & B\\ -C & 0 \end{array} \right]$ 降秩的 $s$ 值 (8.23)

从而，就完成了证明。

对零点的物理解释 传递函数矩阵的零点反映了系统对与其关联的某类输入函数有着阻塞的作用。我们用下面的一个结论，来具体地阐明零点的这种物理特性。

结论 给定多变量系统的传递函数矩阵 $G(s)$ ，系统的联合能控和能观测的状态空间描述表为 $(A, B, C)$ ，再令 $z_0$ 为 $G(s)$ 的一个零点，则对满足关系式

$$
\left\{ \begin{array}{l} C \boldsymbol {x} _ {0} = \mathbf {0} \\ (z _ {0} I - A) \boldsymbol {x} _ {0} = - B \boldsymbol {u} _ {0} \end{array} \right. \tag {8.24}
$$

的初始状态 $x_0$ 和常向量 $\pmb{u}_0$ ，系统对形如

$$\boldsymbol {u} (t) = \boldsymbol {u} _ {0} e ^ {x _ {0} t} \tag {8.25}$$

的一类输入向量具有阻塞作用，即由其引起的系统输出 $y(t)$ 将恒等于零。

证 已知 $z_0$ 为 $G(s)$ 的一个零点, 则据(8.15)可知, 矩阵 $\begin{bmatrix} sI - A & B \\ -C & 0 \end{bmatrix}$ 在 $s = z_0$ 处降秩, 这表明必存非零向量 $\begin{bmatrix} x_0 \\ u_0 \end{bmatrix}$ 使成立

$$
\left[ \begin{array}{c c} z _ {0} I - A & B \\ - C & 0 \end{array} \right] \left[ \begin{array}{l} x _ {0} \\ u _ {0} \end{array} \right] = 0 \tag {8.26}
$$

而式(8.26)即等同于(8.24)。进而，又有
