$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 3 & 1 & 0 & 1 & 2 \\ \hline 0 & 0 & 0 & 0 & 1 \\ 4 & 3 & 1 & - 1 & - 4 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 1 & 0 \\ \hline 0 & 0 \\ 0 & 1 \end{array} \right] \boldsymbol {u}
$$

再给定期望的一组闭环特征值为： $\lambda_{1}^{*} = -1, \lambda_{2,3}^{*} = -2 \pm j, \lambda_{4,5}^{*} = -1 \pm j2$ 。

方案1：利用算法II，先求出：

$$\alpha_ {1} ^ {*} (s) = (s + 1) (s + 2 - j) (s + 2 + j) = s ^ {3} + 5 s ^ {2} + 9 s + 5\alpha_ {2} ^ {*} (s) = (s + 1 - j 2) (s + 1 + j 2) = s ^ {2} + 2 s + 5$$

再根据反馈阵的算式,即得:

$$
K = \left[ \begin{array}{c c c c c} 8 & 1 0 & 5 & 1 & 2 \\ \hdashline 4 & 3 & 1 & 4 & - 2 \end{array} \right]
$$

并且，容易定出，反馈系统的系统矩阵为：

$$
\lambda - B K = \left[ \begin{array}{r r r r r} 0 & 1 & 0 & & \\ 0 & 0 & 1 & & \\ - 5 & - 9 & - 5 & & \\ \hline & & & 0 & 1 \\ & & & & - 2 \end{array} \right]
$$

而其特征多项式就是：

$$\det (s I - A + B K) = \left(s ^ {3} + 5 s ^ {2} + 9 s + 5\right) \left(s ^ {2} + 2 s + 5\right)$$

从而满足极点配置要求。

方案 2: 先求出:

$$\alpha^ {*} (s) = \prod_ {i = 1} ^ {5} (s - \lambda_ {i} ^ {*}) = s ^ {5} + 7 s ^ {4} + 2 4 s ^ {3} + 4 8 s ^ {2} + 5 5 s + 2 5$$

可知期望的闭环系统矩阵应为：

$$
A - B K = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ - 2 5 & - 5 5 & - 4 8 & - 2 4 & - 7 \end{array} \right]
$$

于是，利用给出的阵 $A$ 和上述得到的矩阵 $(A - BK)$ ，可得：

$$
B K = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 3 & 1 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 & 0 \\ 2 9 & 5 8 & 4 9 & 2 3 & 3 \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] K
$$

由此，即可定出所要求的反馈增益矩阵为

$$
K = \left[ \begin{array}{c c c c c} 3 & 1 & 0 & 0 & 2 \\ 2 9 & 5 8 & 4 9 & 2 3 & 3 \end{array} \right]
$$

上述计算方法实质上即为算法I。

并且，通过比较由两种方案所得到的增益矩阵可以看出，一般地说，按算法Ⅱ导出的K中元的值从整体上要小于按算法Ⅰ导出的K中的元。

状态反馈对传递函数矩阵的零点的影响 通过引入状态反馈，可以任意配置闭环系统矩阵的特征值，或者等价地说可以任意配置闭环系统传递函数矩阵的极点。但是，与此同时，一个有待进一步研究的问题是，状态反馈在改变受控系统的极点的同时，是否也对系统的零点有影响。我们下面将对此问题作出具体的分析。

首先讨论单输入-单输出系统的情形。给定完全能控的线性定常受控系统：

$$
\begin{array}{l} \dot {x} = A x + b u \\ y = c x \end{array} \tag {5.49}
$$

通过引入适当的线性非奇异变换,可将其化为能控规范形:

$$
\begin{array}{l} \dot {\bar {x}} = \bar {A} \bar {x} + \bar {b} u \\ y = \bar {c} \bar {x} \end{array} \tag {5.50}
$$

其中

$$
\bar {A} = \left[ \begin{array}{c c c c c c} 0 & 1 & & & & \\ \vdots & & \ddots & & \\ \vdots & & & \ddots & \\ 0 & & & & 1 \\ \hline - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {n - 1} \end{array} \right], \quad \bar {\boldsymbol {b}} = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], \quad \tilde {\boldsymbol {c}} = [ \beta_ {0}, \beta_ {1}, \dots , \beta_ {n - 1} ]
$$

并且，容易定出，系统的传递函数 $g(s)$ 为
