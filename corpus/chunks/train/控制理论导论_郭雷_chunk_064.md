定理1.4.2 设定常线性系统(1.4.1)是完全能控的，则存在一个 $n \times n$ 非奇异矩阵 $\pmb{P}$ ，使得系统(1.4.1)在坐标变换 $\overline{x} = Px$ 下变成如下的标准形式：

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{c x}}} (t), \end{array} \right. \tag {1.4.6}
$$

其中 $\overline{A} = PAP^{-1},\overline{b} = Pb,\overline{c} = cP^{-1}$ ，并且

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \ddots & \vdots \\ \vdots & \vdots & \ddots & \ddots & 0 \\ 0 & 0 & \dots & 0 & 1 \\ - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {n - 2} & - \alpha_ {n - 1} \end{array} \right], \quad \overline {{{b}}} = \left[ \begin{array}{l} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right]. \tag {1.4.7}
$$

通常称系统 (1.4.6), (1.4.7) 为系统 (1.4.1) 的第二能控标准形, 也称 Brunovsky 标准形.

证明 令 $q^{\mathrm{T}}$ 为 $Q_{c}^{-1}$ 中最后一行所组成的向量，取

$$
\boldsymbol {P} = \left[ \begin{array}{c} \boldsymbol {q} ^ {\mathrm{T}} \\ \boldsymbol {q} ^ {\mathrm{T}} \boldsymbol {A} \\ \vdots \\ \boldsymbol {q} ^ {\mathrm{T}} \boldsymbol {A} ^ {n - 1} \end{array} \right].
$$

可以证明，这个矩阵 $P$ 是非奇异的。事实上，如果有向量 $\pmb{x_0}$ 使得 $Px_0 = 0$ ，则有

$$\boldsymbol {q} ^ {\mathrm{T}} \boldsymbol {A} ^ {\prime} x _ {0} = 0, \quad i = 0, 1, \dots , n - 1. \tag {1.4.8}$$

当 i=0 时，有 $q^{T}x_{0}=0$ 。而若 q 与 $b, Ab, \cdots, A^{n-2}b$ 直交，那么 $x_{0}$ 必能表示成 $b, Ab, \cdots, A^{n-2}b$ 的线性组合，从而有不全为零的实数 $\beta_{0}, \beta_{1}, \cdots, \beta_{n-2}$ 使得

$$\boldsymbol {x} _ {0} = \sum_ {k = 0} ^ {n - 2} \beta_ {k} \boldsymbol {A} ^ {k} \boldsymbol {b}. \tag {1.4.9}$$

在上式的两边左乘 $q^{\mathrm{T}}A$ ，并利用等式(1.4.8)得出

$$\sum_ {k = 0} ^ {n - 2} \beta_ {k} \boldsymbol {q} ^ {\mathrm{T}} \boldsymbol {A} ^ {k + 1} \boldsymbol {b} = 0. \tag {1.4.10}$$

利用 $\pmb{q}$ 的性质由(1.4.10)推知 $\beta_{n - 2} = 0$ ，同理，在式(1.4.9)的两边左乘 $\pmb{q}^{\mathrm{T}}\pmb{A}^{2}$ ，并利用等式(1.4.8)可得， $\beta_{n - 3} = 0$ .以此类推得出

$$\beta_ {k} = 0, \quad k = 0, 1, \dots , n - 2.$$

这表明 $x_0 = 0$ ，故 $\pmb{P}$ 是非奇异的.

取坐标变换 $\overline{x} = Px$ ，则系统 (1.4.1) 在这个坐标变换下变成如下代数等价系统：

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{c x}}} (t), \end{array} \right. \tag {1.4.11}
$$

其中 $\overline{A} = PAP^{-1}$ , $\overline{b} = Pb$ , $\overline{c} = cP^{-1}$ . 利用矩阵 $P$ 的性质, 并使用 Cayley-Hamilton 定理可以证明, $\overline{A}$ 和 $\overline{b}$ 有我们所希望的结构形式. 再由坐标变换保持系统的能控性不变知, 系统 (1.4.11) 是完全能控的, 从而定理得证.
