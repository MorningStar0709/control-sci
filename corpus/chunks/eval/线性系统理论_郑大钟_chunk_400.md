$$D _ {K H} (s) = H ^ {- 1} D _ {h c} S (s) + \left(H ^ {- 1} D _ {l c} + K\right) \Psi (s) \tag {11.95}$$

于是，由(11.94)和(11.95)可立即导出如下的结论。

结论2 对于图11.8所示的包含输入变换的状态反馈系统 $S_{xH}$ ，其中 $H$ 为非奇异常数矩阵, 则附加引入 $H$ 可同时改变分母矩阵 $D(s)$ 的列次系数矩阵 $D_{hc}$ 和低次系数矩阵 $D_{lc}$ , 特别是当取 $H = D_{hc}$ 时, 可使 $D_{KH}(s)$ 的行列式为首 1 多项式, 也即成立

$$D _ {K H} (s) = S (s) + \left(D _ {h c} ^ {- 1} D _ {l c} + K\right) \Psi (s) \tag {11.96}$$

极点配置问题的一种算法 给定开环系统的传递函数矩阵 $G_{o}(s) = N(s)D^{-1}(s)$ ，其中 $N(s)$ 和 $D(s)$ 分别为 $q \times p$ 和 $p \times p$ 的多项式矩阵，且 $D(s)$ 为列既约。表

$$k _ {i} = \delta_ {c i} D (s)$$

为列次数,常设其满足

$$k _ {1} \leqslant k _ {2} \leqslant \dots \leqslant k _ {p} \tag {11.97}$$

并令 $\sum_{i=1}^{p} k_i = n$ 。再任意给定 $n$ 个期望的极点值：

$$\lambda_ {1} ^ {*}, \lambda_ {2} ^ {*}, \dots , \lambda_ {n} ^ {*} \tag {11.98}$$

它们可以是实数或以共轭对出现的复数，且表由它们所给出的首1多项式为

$$\prod_ {i = 1} ^ {n} \left(s - \lambda_ {i} ^ {*}\right) = \alpha^ {*} (s) \tag {11.99}$$

现要来确定输入变换阵H和状态反馈阵K，使成立

$$
\left\{ \begin{array}{l} G _ {H} (s, K) = N (s) D _ {K H} ^ {- 1} (s) \\ \det D _ {K H} (s) = \alpha^ {*} (s) \end{array} \right. \tag {11.100}
$$

进而，若令 $(A_{c}, B_{c}, C_{c})$ 为给定 $N(s)D^{-1}(s)$ 的控制器形实现，那么上述问题等价于确定 $H$ 和 $K$ ，使成立

$$\det (s I - A _ {c} + B H K) = \alpha^ {*} (s) \tag {11.101}$$

也即使闭环系统矩阵的特征值配置于期望值 $\lambda_{i}^{*}(i=1,2,\cdots,n)$ 。所以，通常也称这类问题为特征值配置问题。

求解上述极点配置问题的算法如下:

第1步：对给定 $D(s)$ ，定出 $D_{hc}$ 、 $D_{lc}$ 和 $\Psi(s)$ ，同时计算出 $D_{hc}^{-1}$ 。

第2步：将 $\alpha^{*}(s)$ 进一步表示为

$$
\begin{array}{l} \alpha^ {*} (s) = s ^ {n} + a _ {1} (s) s ^ {n - k _ {1}} + a _ {2} (s) s ^ {n - \left(k _ {1} + k _ {2}\right)} \\ + \dots + a _ {p - 1} (s) s ^ {n - \left(k _ {1} + \dots + k _ {P - 1}\right)} + a _ {p} (s) \tag {11.102} \\ \end{array}
$$

第3步：取

$$
H = D _ {h c} \tag {11.103}
K \Psi (s) = \left[ \begin{array}{c c c c} a _ {1} (s) & \dots & \dots & a _ {p} (s) \\ - 1 & \ddots & & 0 \\ & \ddots & & \vdots \\ & & - 1 & 0 \end{array} \right] - D _ {h c} ^ {- 1} D _ {l c} \Psi (s) \tag {11.104}
$$

则将此代入(11.95)，就有

$$
\begin{array}{l} D _ {K H} (s) = S (s) + D _ {h c} ^ {- 1} D _ {l c} \Psi (s) - D _ {h c} ^ {- 1} D _ {l c} \Psi (s) \\ + \left[ \begin{array}{c c c c} a _ {1} (s) & \dots & \dots & a _ {p} (s) \\ - 1 & \ddots & & 0 \\ & \ddots & & \vdots \\ & & - 1 & 0 \end{array} \right] \\ \end{array}

= \left[ \begin{array}{c c c} s ^ {k _ {1}} + a _ {1} (s) & a _ {2} (s) \dots a _ {p} (s) \\ \hline - 1 & s ^ {k _ {2}} \\ 0 & - 1 & \ddots \\ \vdots & & \ddots \\ 0 & & - 1 \end{array} \right] \tag {11.105}
$$

进而，把(11.105)的最右边的矩阵如虚线分隔那样分块化，即有
