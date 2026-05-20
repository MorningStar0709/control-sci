# 例 9.15 二阶系统的李雅普诺夫稳定性

用李雅普诺夫方法找到如下状态矩阵描述的二阶线性系统的稳定性条件：

$$
\mathbf {A} = \left[ \begin{array}{c c} - \alpha & \beta \\ - \beta & - \alpha \end{array} \right]
$$

解答。对于线性情况，我们可以选取任意正定矩阵 Q，最简单的是 Q=I。对应的李雅普诺夫方程为

$$
\left[ \begin{array}{l l} - \alpha & - \beta \\ \beta & - \alpha \end{array} \right] \left[ \begin{array}{l l} p & q \\ q & r \end{array} \right] + \left[ \begin{array}{l l} p & q \\ q & r \end{array} \right] \left[ \begin{array}{c c} - \alpha & \beta \\ - \beta & - \alpha \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 0 & - 1 \end{array} \right] \tag {9.66}
$$

将式(9.66)乘开并且令各对应元素相等，我们得到

$$- \alpha p - \beta q - \alpha p - \beta q = - 1 \tag {9.67}- \alpha q - \beta r + \beta p - \alpha q = 0 \tag {9.68}\beta q - \alpha r + \beta q - \alpha r = - 1 \tag {9.69}$$

从式(9.67)到式(9.69)解出 $p=r=\frac{1}{2\alpha}$ ，q=0，于是，有

$$
\boldsymbol {P} = \left[ \begin{array}{c c} \frac {1}{2 \alpha} & 0 \\ 0 & \frac {1}{2 \alpha} \end{array} \right]
$$

其各阶行列式为 $\frac{1}{2\alpha}>0$ 和 $\frac{1}{4\alpha^{2}}>0$ ，因此P>0。所以我们得出结论：如果 $\alpha>0$ ，则系统就是稳定的。

对于具有很多状态变量和非数值参数的系统，李雅普诺夫方程的求解会很烦琐，但是，对于计算带有字母参数的系统的稳定性条件而言，这一结果是对劳斯方法的一种等效替代。
