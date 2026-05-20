# (3) 状态反馈对传递函数零点的影响

状态反馈在改变系统极点的同时,是否对系统的零点产生影响?下面来分析回答这一问题。已知完全可控的单输入-单输出线性定常系统可经适当非奇异线性变换化为可控标准型

$$\dot {\boldsymbol {x}} = \bar {\boldsymbol {A}} \boldsymbol {x} + \bar {\boldsymbol {b}} u, \quad y = \bar {c x}$$

被控系统的传递函数为

$$
\begin{array}{l} G (s) = c (s I - A) ^ {- 1} b = \bar {c} (s I - \bar {A}) ^ {- 1} \bar {b} \\ = \frac {\left[ \beta_ {0} \quad \beta_ {1} \quad \cdots \quad \beta_ {n - 1} \right]}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {1} s + a _ {0}} \left[ \begin{array}{c c c c} \times & \dots & \times & 1 \\ \times & \dots & \times & s \\ \vdots & & \vdots & \vdots \\ \times & \dots & \times & s ^ {n - 1} \end{array} \right] \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \\ = \frac {\beta_ {n - 1} s ^ {n - 1} + \cdots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {1} s + a _ {0}} \\ \end{array}
$$

引入状态反馈后的闭环系统传递函数为

$$
\begin{array}{l} G _ {K} (s) = \boldsymbol {c} (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {b k}) ^ {- 1} \boldsymbol {b} = \bar {\boldsymbol {c}} (s \boldsymbol {I} - \bar {\boldsymbol {A}} + \bar {\boldsymbol {b k}}) ^ {- 1} \bar {\boldsymbol {b}} \\ = \frac {\left[ \beta_ {0} \quad \beta_ {1} \quad \cdots \quad \beta_ {n - 1} \right]}{s ^ {n} + a _ {n - 1} ^ {*} s ^ {n - 1} + \cdots + a _ {1} ^ {*} s + a _ {0} ^ {*}} \left[ \begin{array}{c c c c} \times & \dots & \times & 1 \\ \times & \dots & \times & s \\ \vdots & & \vdots & \vdots \\ \times & \dots & \times & s ^ {n - 1} \end{array} \right] \left[ \begin{array}{l} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \\ = \frac {\beta_ {n - 1} s ^ {n - 1} + \cdots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + a _ {n - 1} ^ {*} s ^ {n - 1} + \cdots + a _ {1} ^ {*} s + a _ {0} ^ {*}} \\ \end{array}
$$

上述推导表明, 由于 $\operatorname{adj}(s\mathbf{I} - \overline{\mathbf{A}})$ 与 $\operatorname{adj}(s\mathbf{I} - \overline{\mathbf{A}} + \overline{\mathbf{b}\mathbf{k}})$ 的第 $n$ 列相同, 故 $G(s)$ 与 $G_{K}(s)$ 的分子多项式相同, 即闭环系统零点与被控系统零点相同, 状态反馈对 $G(s)$ 的零点没有影响, 仅使 $G(s)$ 的极点改变为闭环系统极点。然而可能有这种情况: 引入状态反馈后恰巧使某些极点移到 $G(s)$ 的零点处而构成极、零点对消, 这时既失去了一个系统零点, 又失去了一个系统极点, 并且被对消掉的那些极点可能不可观测。这也是对状态反馈可能使系统失去可观测性的一个直观解释。
