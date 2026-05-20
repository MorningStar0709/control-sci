# 9.2 标量传递函数的一些典型实现

从这一节开始,我们把重点转移到去讨论求解实现问题中的方法性问题,要系统地来介绍根据给定的传递函数矩阵计算状态空间描述的系数矩阵的各种具体方法。本节中,首先来研究单输入-单输出系统这一最简单的情况,介绍标量传递函数的一些典型的实现。

限于讨论传递函数 $g(s)$ 为严格真的情况，一般地可将其表为如下的一个有理分式函数：

$$g (s) = \frac {n (s)}{d (s)} = \frac {\beta_ {n - 1} s ^ {n - 1} + \cdots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \cdots + \alpha_ {1} s + \alpha_ {0}} \tag {9.52}$$

其中 $\alpha_{i}(i=0,1,\cdots,n-1)$ 和 $\beta_{j}(j=0,1,\cdots,n-1)$ 均为实常数。下面，我们来介绍(9.52)所示标量传递函数 $g(s)$ 的一些典型的实现。

能控规范形实现 给定传递函数 $g(s)$ 如(9.52)所示, 则其能控规范形 $(A, b, c)$ 为

$$
A = \left[ \begin{array}{c c c c} 0 & 1 & \ddots & \\ & & 1 & \\ - \alpha_ {0} & - \alpha_ {1} & \dots & - \alpha_ {n - 1} \end{array} \right], b = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], c = \left[ \begin{array}{l l l l} \beta_ {0}, & \beta_ {1}, & \dots , & \beta_ {n - 1} \end{array} \right] \tag {9.53}
$$

证 考虑到

$$
\begin{array}{l} (s I - A) ^ {- 1} = \frac {\operatorname{adj} (s I - A)}{\det (s I - A)} = \frac {1}{s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \cdots + \alpha_ {1} s + \alpha_ {0}} \\ \times \left[ \begin{array}{c c c c} * & \dots & * & 1 \\ \vdots & & \vdots & \\ \vdots & & \vdots & s \\ \vdots & & \vdots & \vdots \\ \vdots & & \vdots & \vdots \\ * & \dots & * & s ^ {n - 1} \end{array} \right] \tag {9.54} \\ \end{array}
$$

其中，用“\*”表示的元是证明中无需确知的元。于是，即可得到

$$
\begin{array}{l} c (s I - A) ^ {- 1} b = \frac {1}{s ^ {m} + \alpha_ {n - 1} s ^ {m - 1} + \cdots + \alpha_ {1} s + \alpha_ {0}} [ \beta_ {0}, \dots , \beta_ {n - 1} ] \\ \times \left[ \begin{array}{c c c c} * & \dots & * & 1 \\ \vdots & & \vdots & \\ \vdots & & \vdots & s \\ \vdots & & \vdots & \vdots \\ \vdots & & \vdots & \vdots \\ * & \dots & * & s ^ {n - 1} \end{array} \right] \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] \\ = \frac {\beta_ {n - 1} s ^ {n - 1} + \cdots + \beta_ {1} s + \beta_ {0}}{s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \cdots + \alpha_ {1} s + \alpha_ {0}} = g (s) \tag {9.55} \\ \end{array}
$$

从而结论得证。

对于上述结论,可作如下的几点讨论:

① 不管给定的 $g(s)$ 中分母多项式 $d(s)$ 和分子多项式 $n(s)$ 是否为互质，实现(9.53)总是能控的且具有能控规范形的形式。因此，把形如（9.53）的实现称为 $g(s)$ 的

能控规范形实现。

② 如果给定的 $g(s)$ 中分母多项式 $d(s)$ 和分子多项式 $n(s)$ 为互质，则能控规范形实现(9.53)同时也是 $g(s)$ 的一个最小实现。

这一点可这样来证明：当 $d(s)$ 和 $\pmb{n}(s)$ 为互质时， $n(s) / d(s)$ 本身就是 $g(s)$ 的史密斯-麦克米伦形。因此，由(9.47)可知， $g(s)$ 的最小实现的维数为

$$n _ {\min} = \deg d (s) = n = \dim (A) \tag {9.56}$$

这表明,由(9.53)给出的实现 $(A,b,c)$ 已具有最小维数,从而即为 $g(s)$ 的一个最小实现。

③ 当给定 $g(s)$ 中分母多项式 $d(s)$ 和分子多项式 $n(s)$ 不为互质时，那么由(9.53)给出的实现 $(A, b, c)$ 尽管为能控，但却不是完全能观测的。
