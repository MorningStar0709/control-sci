$$
D _ {1 1} (s) = s ^ {k _ {1}} + a _ {1} (s), D _ {1 2} (s) = \left[ a _ {2} (s) \dots a _ {p} (s) \right]
D _ {2 1} = \left[ \begin{array}{c} - 1 \\ 0 \\ \vdots \\ 0 \end{array} \right], D _ {2 2} (s) = \left[ \begin{array}{c c c c} s ^ {k _ {2}} & & & \\ - 1 & \ddots & & \\ & \ddots & \ddots & \\ & - 1 & s ^ {k _ {\rho}} \end{array} \right]
$$

于是，可以求出

$$
\begin{array}{l} \det D _ {K H} (s) = \det D _ {2 2} (s) \det \left[ D _ {1 1} (s) - D _ {1 2} (s) D _ {2 2} ^ {- 1} (s) D _ {2 1} (s) \right] \\ = s ^ {\left(k _ {2} + \dots + k _ {p}\right)} \left[ s ^ {k _ {1}} + a _ {1} (s) + a _ {2} (s) s ^ {- k _ {2}} + \dots + a _ {p} (s) s ^ {- \left(k _ {2} + \dots + k _ {p}\right)} \right] \\ = s ^ {n} + a _ {1} (s) s ^ {n - k _ {1}} + a _ {2} (s) s ^ {n - \left(k _ {1} + k _ {2}\right)} + \dots + a _ {p - 1} (s) s ^ {k _ {p}} + a _ {p} (s) \\ = \alpha^ {*} (s) \tag {11.106} \\ \end{array}
$$

这表明,当按式(11.104)来选取H和K时,就能实现极点配置的目标。

第4步：令

$$K = \left[ K _ {1}, K _ {2}, \dots , K _ {p} \right] \tag {11.107}D _ {h c} ^ {- 1} D _ {l c} = \left[ \bar {D} _ {1}, \bar {D} _ {2}, \dots , \bar {D} _ {p} \right] \tag {11.108}$$

其中， $K_{i}$ 为 $p \times k_{i}$ 待定常阵， $\overline{D}_{i}$ 为 $p \times k_{i}$ 已知常阵。由此，注意到 $\Psi(s)$ 的形式的同时，可由(11.104)导出：

$$
K _ {i} \left[ \begin{array}{c} s ^ {k _ {i} - 1} \\ \vdots \\ s \\ 1 \end{array} \right] = \left| \begin{array}{c} - a _ {i} (s) ^ {-} \\ 0 \\ \vdots \\ 0 \\ - 1 \\ 0 \\ \vdots \\ 0 \end{array} \right| - \bar {D} _ {i} \left[ \begin{array}{c} s ^ {k _ {i} - 1} \\ \vdots \\ s \\ 1 \end{array} \right], i = 1, 2, \dots , p \tag {11.109}
$$

因此，采用系数比较法就可由上式来定出 $K_{i}$ ，从而即可定出所要求的状态反馈矩阵 $K_{0}$ 。

例 给定开环系统的传递函数矩阵 $G_{o}(s) = N(s)D^{-1}(s)$ ，其中

$$
N (s) = \left[ \begin{array}{c c} s ^ {2} + s & 0 \\ 2 s + 1 & - 1 \end{array} \right], \quad D (s) = \left[ \begin{array}{c c} s ^ {3} & 0 \\ - 2 s ^ {2} + s + 1 & 4 s + 1 \end{array} \right]
$$

矩阵 $D(s)$ 是列既约的，其列次数为

$$k _ {1} = 3, k _ {2} = 1$$

再给定一组期望的极点为

$$\lambda_ {1} ^ {*} = - 2, \lambda_ {2, 3} ^ {*} = - 1 \pm j 2, \lambda_ {4} ^ {*} = - 5$$

相应的由它们所给出的首1多项式为

$$\alpha^ {*} (s) = \prod_ {i = 1} ^ {4} (s - \lambda_ {i} ^ {*}) = s ^ {4} + 9 s ^ {3} + 2 9 s ^ {2} + 5 5 s + 5 0$$

现在,先求出 $D(s)$ 的各个系数矩阵和低次阵:

$$
D _ {k c} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 4 \end{array} \right], \Psi (s) = \left[ \begin{array}{l l} s ^ {2} & 0 \\ s & 0 \\ 1 & 0 \\ 0 & 1 \end{array} \right], D _ {l c} = \left[ \begin{array}{l l l l} 0 & 0 & 0 & 0 \\ - 2 & 1 & 1 & 1 \end{array} \right]

D _ {k c} ^ {- 1} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & \frac {1}{4} \end{array} \right]
$$

再将 $\alpha^{*}(s)$ 表示为(其中 $k_{1}=3,\ k_{2}=1,\ n=4$ ):

$$\alpha^ {*} (s) = s ^ {4} + (9 s ^ {2} + 2 9 s + 5 5) s + (5 0)$$

也即有
