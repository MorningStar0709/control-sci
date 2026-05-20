# 1.4 定常线性系统的能控能观标准形

本节研究单输入单输出定常线性系统

$$
\left\{ \begin{array}{l} {\dot {x} (t) = A x (t) + b u (t),} \\ {y (t) = c x (t),} \end{array} \right. \tag {1.4.1}
$$

这里 $u(t)$ 为标量控制输入， $y(t)$ 为标量量测输出， $b$ 为 $n$ 维列向量， $c$ 为 $n$ 维行向量.

令 $\pmb{A}$ 的特征多项式为

$$\det (s I _ {n} - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0}. \tag {1.4.2}$$

系统 (1.4.1) 的能控性矩阵和能观测性矩阵分别为

$$
Q _ {c} = [ b, A b, \dots , A ^ {n - 1} b ],
Q _ {o} = \left[ \begin{array}{c} c \\ c A \\ \vdots \\ c A ^ {n - 1} \end{array} \right].
$$

定理 1.4.1 已知定常线性系统 (1.4.1). 设它是完全能控的, 则存在一个 $n \times n$ 非奇异矩阵 $T$ , 使得在坐标变换 $\bar{x} = Tx$ 下系统 (1.4.1) 变成如下的标准形式:

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{c}}} \overline {{{x}}} (t), \end{array} \right. \tag {1.4.3}
$$

其中 $\overline{A} = TAT^{-1}$ , $\overline{b} = Tb$ , $\overline{c} = cT^{-1}$ . 并且

$$
\overline {{{A}}} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - \alpha_ {0} \\ 1 & 0 & \ddots & \vdots & - \alpha_ {1} \\ 0 & 1 & \ddots & 0 & \vdots \\ \vdots & \ddots & \ddots & 0 & - \alpha_ {n - 2} \\ 0 & \dots & 0 & 1 & - \alpha_ {n - 1} \end{array} \right], \quad \overline {{{b}}} = \left[ \begin{array}{l} 1 \\ 0 \\ \vdots \\ 0 \end{array} \right]. \tag {1.4.4}
$$

通常称系统 (1.4.3)\~(1.4.4) 为系统 (1.4.1) 的第一能控标准形.

证明 因为系统 (1.4.1) 完全能控, 所以矩阵 $Q_{c}$ 是非奇异的. 令 $\pmb{T} = \pmb{Q}_{c}^{-1}$ , 则在坐标变换 $\bar{x} = Tx$ 下, 有

$$
\left\{ \begin{array}{l} \dot {\overline {{{x}}}} (t) = \overline {{{A}}} \overline {{{x}}} (t) + \overline {{{b}}} u (t), \\ y (t) = \overline {{{c x}}} (t), \end{array} \right. \tag {1.4.5}
$$

其中 $\overline{A} = TAT^{-1},\overline{b} = Tb,\overline{c} = cT^{-1}$ ，不难计算，

$$
\begin{array}{l} \overline {{{A}}} = T A Q _ {c} = T [ A b, A ^ {2} b, \dots , A ^ {n - 1} b, A ^ {n} b ] \\ = T \left[ A b, A ^ {2} b, \dots , A ^ {n - 1} b, - \alpha_ {n - 1} A ^ {n - 1} b - \dots - \alpha_ {1} A b - \alpha_ {0} b \right] \\ = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - \alpha_ {0} \\ 1 & 0 & \ddots & \vdots & - \alpha_ {1} \\ 0 & 1 & \ddots & 0 & \vdots \\ \vdots & \ddots & \ddots & 0 & - \alpha_ {n - 2} \\ 0 & \dots & 0 & 1 & - \alpha_ {n - 1} \end{array} \right]. \\ \end{array}
\bar {\boldsymbol {b}} = \boldsymbol {T} \boldsymbol {b} = \boldsymbol {Q} _ {c} ^ {- 1} \boldsymbol {b} = [ 1 0 \dots 0 ] ^ {\mathrm{T}}.
$$

这表明由方程 (1.4.5) 给出的系统有所要求的形式。显然，它与系统 (1.4.1) 代数等价，因而也是完全能控的。
