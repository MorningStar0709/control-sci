a) 假设系统 (1.6.1) 是单输入的，即 $r = 1$ 。这时 $\pmb{B}$ 为 $n \times 1$ 矩阵，记 $\pmb{B} = \pmb{b}$ 。由于 $(A, b)$ 能控，因此存在一个坐标变换 $\overline{x} = Tx$ ，使得系统 (1.6.1) 变成第二能控标准形

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) - \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{C}}} \overline {{{x}}} (t), \end{array} \right. \tag {1.6.8}
$$

其中

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - \alpha_ {0} & - \alpha_ {1} & - \alpha_ {2} & \dots & - \alpha_ {n - 1} \end{array} \right], \quad \overline {{{b}}} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], \quad \overline {{{C}}} = C T ^ {- 1}.
$$

任给一个复数对称集合

$$\Lambda_ {0} = \{\lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {n} \}.$$

希望寻找一个状态反馈规律，使得闭环系统的全部极点为 $\Lambda_0$ ，而这组极点对应于闭环系统的特征多项式为

$$
\begin{array}{l} f (\lambda) = \left(\lambda - \lambda_ {1}\right) \left(\lambda - \lambda_ {2}\right) \dots \left(\lambda - \lambda_ {n}\right) \\ = \lambda^ {n} + \beta_ {n - 1} \lambda^ {n - 1} + \dots + \beta_ {1} \lambda + \beta_ {0}, \\ \end{array}
$$

其中诸 $\beta_{i}$ 由 $\lambda_{j}(j=1,2,\cdots,n)$ 唯一决定；反之，由诸 $\beta_{i}$ 又可唯一决定每个 $\lambda_{j}$ .

对系统 (1.6.8) 取状态反馈控制规律

$$u (t) = - \overline {{{\boldsymbol {k}}}} ^ {\mathrm{T}} \overline {{{\boldsymbol {x}}}} (t) \tag {1.6.9}$$

其中 $\overline{k}^{\mathrm{T}} = (\overline{k}_{0}, \overline{k}_{1}, \cdots, \overline{k}_{n-1})$ 为实的行向量。将状态反馈控制规律 (1.6.9) 作用于系统 (1.6.8) 得

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = (\overline {{{A}}} - \overline {{{b k}}} ^ {\mathrm{T}}) \overline {{{x}}} (t), \\ y (t) = \overline {{{C}}} \overline {{{x}}} (t). \end{array} \right. \tag {1.6.10}
$$

闭环系统 (1.6.10) 的系统矩阵为

$$
\overline {{\boldsymbol {A}}} - \overline {{\boldsymbol {b k}}} ^ {\mathrm{T}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - (\alpha_ {0} + \overline {{k}} _ {0}) & - (\alpha_ {1} + \overline {{k}} _ {1}) & - (\alpha_ {2} + \overline {{k}} _ {2}) & \dots & - (\alpha_ {n - 1} + \overline {{k}} _ {n - 1}) \end{array} \right].
$$

不难计算，闭环系统(1.6.10)的特征多项式为

$$f _ {c} (\lambda) = \lambda^ {n} + (\alpha_ {n - 1} + \overline {{{k}}} _ {n - 1}) \lambda^ {n - 1} + \dots + (\alpha_ {1} + \overline {{{k}}} _ {1}) \lambda + (\alpha_ {0} + \overline {{{k}}} _ {0}).$$
