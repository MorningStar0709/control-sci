# 1) 利用状态反馈的极点可配置条件。

定理 9-5 利用状态反馈任意配置闭环极点的充分必要条件是被控系统可控。

证明 下面就单输入 - 多输出系统来证明该定理。这时被控系统 $(A, B, C)$ 中的 $B$ 为一列向量，记为 $b$ 。

充分性：若系统 $(A, b)$ 可控，则通过非奇异线性变换 $x = P^{-1}\bar{x}$ 可变换为可控标准型

$$\dot {\boldsymbol {x}} = \bar {\boldsymbol {A}} \boldsymbol {x} + \bar {\boldsymbol {b}} \boldsymbol {u}$$

式中

$$
\overline {{{\boldsymbol {A}}}} = \boldsymbol {P} \boldsymbol {A} \boldsymbol {P} ^ {- 1} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right], \quad \overline {{{\boldsymbol {b}}}} = \boldsymbol {P} \boldsymbol {b} = \left[ \begin{array}{l} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right]
$$

在单输入情况下，引入状态反馈

$$u = v - k x = v - k P ^ {- 1} \bar {x} = v - \bar {k} \bar {x}$$

其中

$$
\bar {k} = k P ^ {- 1} = \left[ \begin{array}{c c c c} \bar {k} _ {0} & \bar {k} _ {1} & \dots & \bar {k} _ {n - 1} \end{array} \right]
$$

则引入状态反馈后闭环系统的状态阵为

$$
\overline {{{\boldsymbol {A}}}} - \overline {{{\boldsymbol {b k}}}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ (- a _ {0} - \overline {{{k}}} _ {0}) & (- a _ {1} - \overline {{{k}}} _ {1}) & (- a _ {2} - \overline {{{k}}} _ {2}) & \dots & (- a _ {n - 1} - \overline {{{k}}} _ {n - 1}) \end{array} \right] \tag {9-227}
$$

对于式(9-227)这种特殊形式的矩阵,容易写出其闭环特征方程

$$
\begin{array}{l} \det [ s I - (\bar {A} - \bar {b k}) ] = s ^ {n} + \left(a _ {n - 1} + \bar {k} _ {n - 1}\right) s ^ {n - 1} + \left(a _ {n - 2} + \bar {k} _ {n - 2}\right) s ^ {n - 2} \\ + \dots + \left(a _ {1} + \bar {k} _ {1}\right) s + \left(a _ {0} + \bar {k} _ {0}\right) = 0 \tag {9-228} \\ \end{array}
$$

显然，该 $n$ 阶特征方程中的 $n$ 个系数，可通过 $\bar{k}_0, \bar{k}_1, \dots, \bar{k}_{n-1}$ 来独立设置，也就是说 $(\overline{A} - \overline{bk})$ 的特征值可以任意选择，即系统的极点可以任意配置。

必要性：如果系统 $(A, b)$ 不可控，就说明系统的有些状态将不受 $u$ 的控制，则引入状态反馈时就不可能通过控制来影响不可控的极点。证毕。

2）利用输出反馈的极点可配置条件。

定理9-6 用输出至状态微分的反馈任意配置闭环极点的充分必要条件是被控系统可观测。
