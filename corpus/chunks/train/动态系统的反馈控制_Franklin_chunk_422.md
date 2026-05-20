# 例7.12 从状态描述求解热系统的零点

计算由式 $(7.12)$ 描述的热系统的零点。

解答。利用式 $(7.64)$ 计算该系统的零点：

$$
\begin{array}{l} \det \left[ \begin{array}{c c c} s + 7 & 1 2 & - 1 \\ - 1 & s & 0 \\ 1 & 2 & 0 \end{array} \right] = 0 \\ - 2 - s = 0 \\ s = - 2 \\ \end{array}
$$

注意所得的结果与式(7.9)给出的传递函数的零点是一致的。这个结果可以用如下 Matlab 语句实现：

$$
\begin{array}{l} \operatorname{sysG} = \operatorname{ss} (\mathrm{Ac}, \mathrm{Bc}, \mathrm{Cc}, \mathrm{Dc}); \\ [ z, \text { gain } ] = \text { tzero(sysG) } \\ \end{array}
$$

并且得到 z=-2.0 和增益 gain=1

式(7.55)的特征方程和式(7.64)的零点多项式结合起来，以紧凑形式用状态描述矩阵表示传递函数为

$$
G (s) = \frac {\det \left[ \begin{array}{c c} s I - A & - B \\ C & D \end{array} \right]}{\det (s I - A)} \tag {7.65}
$$

（详见附录 WB 及网址 www.fpe7e.com），式(7.65)是用于理论研究的一个紧凑公式，其对数据误差是很敏感的。Emami-Naeini 和 Van Dooren(1982)给出了求传递函数的一种在数值上稳定的算法。通过给定传递函数，我们可以计算频率响应 $G(j\omega)$ ；如前所述，用式(7.54)和式(7.63)可以求出极点和零点，并依此求解出瞬态响应，详见第3章。
