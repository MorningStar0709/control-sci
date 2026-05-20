$$g (s) = \mathbf {c} (s l - A) ^ {- 1} \mathbf {b} = \bar {\mathbf {c}} (s l - \overline {{{A}}}) ^ {- 1} \bar {\mathbf {b}}= \frac {\beta_ {n - 1} s ^ {n - 1} + \dots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0}} \tag {5.51}$$

再任意给定期望的一组闭环极点 $\{\lambda_{1}^{*},\lambda_{2}^{*},\cdots,\lambda_{n}^{*}\}$ ，且可定出相应的特征多项式为

$$\alpha^ {*} (s) = \prod_ {i = 1} ^ {n} \left(s - \lambda_ {i} ^ {*}\right) = s ^ {n} + \alpha_ {n - 1} ^ {*} s ^ {n - 1} + \dots + \alpha_ {1} ^ {*} s + \alpha_ {0} ^ {*} \tag {5.52}$$

那么，由极点配置问题的算法可知，实现极点配置的状态反馈增益矩阵为 $K = \bar{K}Q, Q = P^{-1}, P$ 为使 $\{A, b, c\}$ 化为能控规范形 $\{\bar{A}, \bar{b}, \bar{c}\}$ 的变换矩阵，而 $\bar{K} = [\alpha_{0}^{*} - \alpha_{0}, \cdots, \alpha_{s-1}^{*} - \alpha_{s-1}]$ 。于是，即可导出状态反馈系统为

$$
\begin{array}{l} \dot {\boldsymbol {x}} = (A - \boldsymbol {b} K) \boldsymbol {x} + \boldsymbol {b} v (5.53) \\ y = c x (5.53) \\ \end{array}
$$

而其能控规范形为：

$$\dot {\bar {x}} = (\bar {A} - \bar {b} \bar {K}) \bar {x} + \bar {b} v \tag {5.54}y = \bar {c} \bar {x}$$

其中

$$
\bar {A} - \bar {b} \bar {K} = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ 0 & & & 1 & \\ \hline - \alpha_ {0} ^ {*} & - \alpha_ {1} ^ {*} & \dots & - \alpha_ {n - 1} ^ {*} \end{array} \right], \quad \bar {b} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], \quad \bar {c} = [ \beta_ {0}, \beta_ {1}, \dots , \beta_ {n - 1} ]
$$

利用(5.53)和(5.54)，可以导出状态反馈系统的传递函数 $g_{K}(s)$ 为：

$$
\begin{array}{l} g _ {K} (s) = \mathbf {c} (s I - A + \mathbf {b} K) ^ {- 1} \mathbf {b} = \bar {\mathbf {c}} (s I - \bar {A} + \bar {\mathbf {b}} \bar {K}) ^ {- 1} \bar {\mathbf {b}} \\ = \frac {\beta_ {n - 1} s ^ {n - 1} + \dots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + \alpha_ {n - 1} ^ {*} s ^ {n - 1} + \dots + \alpha_ {1} ^ {*} s + \alpha_ {0} ^ {*}} \tag {5.55} \\ \end{array}
$$

比较(5.55)和(5.51)，就可得到结论：引入状态反馈虽能使 $g(s)$ 的极点移动位置，但却不影响 $g(s)$ 的零点。然而，这个结论是在一般意义下得到的。事实上，也可有这样的情况，设某些极点在状态反馈引入后被移动到与 $g(s)$ 的零点相重合而构成对消，则此时状态反馈也影响了 $g(s)$ 的零点，并且造成了被对消掉的那些极点(即振型)成为不可观测。这也是对状态反馈可以使系统失去完全能观测性的一个直观的解释。

进而，讨论多输入-多输出系统的情形。对于多变量线性定常系统

$$
\begin{array}{l} \dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \quad \boldsymbol {x} \in \mathcal {R} ^ {*}, \boldsymbol {u} \in \mathcal {R} ^ {p} \\ \mathbf {y} = C \mathbf {x}, \quad \mathbf {y} \in \mathcal {R} ^ {q} \tag {5.56} \\ \end{array}
$$

其传递函数矩阵

$$G (s) = C (s I - A) ^ {- 1} B \tag {5.57}$$

的零点有多种定义(参见8.1节)。当 $\{A, B, C\}$ 为能控且能观测时， $G(s)$ 的零点可看成为是使
