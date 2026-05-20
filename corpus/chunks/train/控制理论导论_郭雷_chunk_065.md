按照对偶原理，能观测系统也有两个相应的标准形.

定理1.4.3 设系统(1.4.1)是完全能观测的, 则存在一个 $n \times n$ 非奇异矩阵 $\pmb{T}$ , 使得系统(1.4.1)在坐标变换 $\overline{x} = Tx$ 下变成如下的标准形式:

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{c x}}} (t), \end{array} \right. \tag {1.4.12}
$$

其中 $\overline{A} = TAT^{-1},\overline{b} = Tb,\overline{c} = cT^{-1}$ ，并且

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \ddots & \vdots \\ \vdots & & \ddots & \ddots & 0 \\ 0 & \dots & & 0 & 1 \\ - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {n - 2} & - \alpha_ {n - 1} \end{array} \right], \quad \overline {{{c}}} = [ 1, 0, \dots , 0 ]. \tag {1.4.13}
$$

通常系统 (1.4.12)\~(1.4.13) 叫做系统 (1.4.1) 的第一能观测标准形.

证明留作习题.

定理 1.4.4 设系统 (1.4.1) 是完全能观测的，则在一个 $n \times n$ 非奇异矩阵 P，使得系统 (1.4.1) 在坐标变换 $\overline{x} = Px$ 下变成如下的标准形式：

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{c}}} \overline {{{x}}} (t), \end{array} \right. \tag {1.4.14}
$$

其中 $\overline{A} = PAP^{-1}$ , $\overline{b} = Pb$ , $\overline{c} = cP^{-1}$ , 并且

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - \alpha_ {0} \\ 1 & 0 & & \vdots & - \alpha_ {1} \\ 0 & 1 & \ddots & & \vdots \\ \vdots & \ddots & \ddots & 0 & - \alpha_ {n - 2} \\ 0 & \dots & 0 & 1 & - \alpha_ {n - 1} \end{array} \right], \quad \overline {{{c}}} = [ 0 \quad 0 \quad \dots \quad 0 \quad 1 ]. \tag {1.4.15}
$$

通常称系统 (1.4.14), (1.4.15) 为系统 (1.4.1) 的第二能观测标准形.

证明留作习题.

从定常线性系统的标准形很容易求出它的传递函数。假设给定单输入单输出定常线性系统(1.4.1)，它的第二能控标准形为系统(1.4.6)，并设 $\overline{c} = [\beta_0, \beta_2, \dots, \beta_{n-1}]$ 。由于坐标变换不改变系统的传递函数，因此为求系统(1.4.1)的传递函数，只要计算系统(1.4.6)的传递函数即可。根据定义，系统(1.4.6)的传递函数为 $W(s) = \overline{c}(sI_n - \overline{A})^{-1}\overline{b}$ ，其中 $\overline{A}, \overline{b}, \overline{c}$ 分别是系统(1.4.6)的系统矩阵、控制矩阵、量测矩阵。

为计算 $W(s)$ ，首先计算 $(sI_n - \overline{A})^{-1}\overline{b}$ ，容易算出

$$(s I _ {n} - \overline {{{A}}}) ^ {- 1} \overline {{{b}}} = \left[ \frac {1}{\varDelta (s)}, \frac {s}{\varDelta (s)}, \dots , \frac {s ^ {n - 1}}{\varDelta (s)} \right] ^ {\mathrm{T}},$$

其中 $\Delta(s)=s^{n}+\alpha_{n-1}s^{n-1}+\cdots+\alpha_{1}s+\alpha_{0}$ 是矩阵 A（或者 $\overline{A}$ ）的特征多项式.
于是
