# 3.6 能控规范形和能观测规范形: 单输入-单输出情形

对于完全能控或完全能观测的线性定常系统，如果从能控或能观测这个基本属性出发来构造一个非奇异的变换阵，那么将可把系统的状态空间描述在这一线性变换下化成为只有能控系统或能观测系统才具有的标准形式。通常，分别称这种标准形式的状态空间描述为能控规范形和能观测规范形。在第5章中将可看到，当综合系统的状态反馈控制和状态观测器时，这两种规范形是很有用的。这一节中，我们先就单输入-单输出系统这类简单的情况，来讨论能控规范形和能观测规范形的形式和变换阵的构造方法。

能控规范形 考虑完全能控的单输入-单输出线性定常系统

$$
\begin{array}{l l} \Sigma : & \dot {\boldsymbol {x}} = A \boldsymbol {x} + \boldsymbol {b u} \\ & y = c x \end{array} \tag {3.158}
$$

其中， $A$ 为 $n\times n$ 常阵， $\pmb{b}$ 和 $\pmb{c}$ 分别为 $n\times 1$ 和 $1\times n$ 常阵。由于系统为完全能控，所以它具有如下的基本属性

$$\operatorname{rank} [ \boldsymbol {b} | A \boldsymbol {b} | \dots | A ^ {n - 1} \boldsymbol {b} ] = n \tag {3.159}$$

再令系统的特征多项式为

$$\det (s I - A) \triangleq \alpha (s) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0} \tag {3.160}$$

同时，进一步定义如下的 $n$ 个常数：

$$
\beta_ {n - 1} = \mathbf {c b}
\begin{array}{l} \beta_ {n - 2} = c A b + \alpha_ {n - 1} c b \\ \dots \dots \end{array} \tag {3.161}
\beta_ {1} = \boldsymbol {c} A ^ {n - 2} \boldsymbol {b} + \alpha_ {n - 1} \boldsymbol {c} A ^ {n - 3} \boldsymbol {b} + \dots + \alpha_ {2} \boldsymbol {c b}\beta_ {0} = \mathbf {c} A ^ {n - 1} \mathbf {b} + \alpha_ {n - 1} \mathbf {c} A ^ {n - 2} \mathbf {b} + \dots + \alpha_ {1} \mathbf {c b}
$$

那么,就可从(3.159)和(3.160)出发,来构造如下的变换阵:

$$
P = \left[ \boldsymbol {e} _ {1}, \boldsymbol {e} _ {2}, \dots , \boldsymbol {e} _ {n} \right] = \left[ A ^ {n - 1} \boldsymbol {b}, \dots , A \boldsymbol {b}, \boldsymbol {b} \right] \left[ \begin{array}{c c c c c} 1 & & & & \\ & \ddots & & & \\ \alpha_ {n - 1} & & \ddots & & \\ \vdots & \ddots & & \ddots & \\ \alpha_ {1} & \dots & \alpha_ {n - 1} & 1 \end{array} \right] \tag {3.162}
$$

容易看出， $P$ 在系统为能控的条件下是非奇异的，也即只有对能控系统才是可实施此种变换的。于是，在此基础上，就可导出系统能控规范形的基本结论。

结论 对完全能控的单输入-单输出线性定常系统（3.158），引入线性非奇异变换 $\pmb{x} = P^{-1}\pmb{x}$ ，即可导出其能控规范形为：

$$
\begin{array}{l} \Sigma_ {c}: \quad \dot {\bar {x}} = A _ {c} \bar {x} + b _ {c} u \tag {3.163} \\ y = c _ {c} \bar {x} \\ \end{array}
$$

其中 $A_{c} = P^{-1}AP = \left[ \begin{array}{c|ccc}0 & 1 & & \\ \vdots & \ddots & \ddots & \\ \vdots & & \ddots & \\ 0 & & & 1\\ \hline -\alpha_{0} & -\alpha_{1}\dots -\alpha_{n - 1} \end{array} \right],\quad b_{c} = P^{-1}b = \left[ \begin{array}{c}0\\ \vdots \\ 0\\ 1 \end{array} \right]$

$$\mathbf {c} _ {c} = \mathbf {c} P = \left[ \beta_ {0}, \beta_ {1}, \dots , \beta_ {s - 1} \right] \tag {3.164}$$

证 (i) 推导 $A_{c}$ : 利用 $A_{c} = P^{-1}AP$ , 可导出
