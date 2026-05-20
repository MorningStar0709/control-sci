对 $g_{3}(x)$ , $k_{3} = 5$ , 有 $G_{3} = \{(500), (410), (401), \cdots, (005)\}$ ，从而 $d_{3} = (005)$ , $a_{d_{3}}^{3} = -2.1$ , $a_{(014)}^{3} = 2$ , $a_{(023)}^{3} = -1$ ，对别的 $S \in G_{3}$ , $a_{S}^{3} = 0$ 。容易检验最后一个非零项属于 $Q_{3}$ ，故 $Q_{3} = \{(023)\}$ 。

下面检验导数的负定性. 先用 DDP, 对于 (8.6.28) 的第 2 和第 3 式, 对角占优条件 (8.6.26) 已经满足. 对于第一个公式, 由式 (8.6.26) 得到 $\frac{1}{6} > 2\lambda^2$ , 因此

$$| \lambda | < 0. 2 8 8 6 7 5 1 3 4 6.$$

下面再利用 CRDDP. 设 $m = 3$ , 则由式 (8.6.23) 可得

$$
\left\{ \begin{array}{l} \frac {1}{6} > 2 \lambda^ {2} \cdot \frac {4}{6}, \\ 1 > \frac {2}{6} \cdot 2 \lambda^ {2} + \frac {1}{2} \cdot \frac {5}{6} + 2 \cdot \frac {1}{6}, \\ 2. 1 > 2 \cdot \frac {5}{6} + \frac {1}{2} \cdot \frac {1}{6}. \end{array} \right.
$$

其解是

$$| \lambda | < 0. 3 5 3 5 5 3 3 9 0 6.$$

最后，试用 QFRA. 最小的偶数 $m$ 应是 4. 于是

$$q (x) = - \frac {1}{6} x _ {1} ^ {8} + 2 \lambda^ {2} x _ {1} ^ {6} x _ {2} ^ {2} - x _ {2} ^ {8} - \frac {1}{2} x _ {2} ^ {7} x _ {3} - 2. 1 x _ {3} ^ {8} + 2 x _ {3} ^ {7} x _ {2} - x _ {3} ^ {6} x _ {2} ^ {2}.$$

由该算法得到如下的二次型：

$$
\left[ \begin{array}{c c c} - \frac {1}{6} + \lambda^ {2} & \frac {1}{2} \lambda^ {2} & 0 \\ \frac {1}{2} \lambda^ {2} & - \frac {5}{8} & \frac {5}{1 6} \\ 0 & \frac {5}{1 6} & - 0. 6 \end{array} \right].
$$

要使它负定，应有

$$| \lambda | < 0. 3 9 2 2 5 3 5 2 1 8.$$

事实上，可以证明一般情况下，QFRA 比 CRDDP 强，而 CRDDP 比 DDP 强。但 DDP 最简便，而 QFRA 最复杂。根据问题我们将选择这三种方法中的一个或几个来检验 LFHD 的导数的负定性。

下面开始考虑镇定问题，考虑以下具有Byrnes-Isidori标准型的仿射非线性系统：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} ^ {i} = x _ {2} ^ {i}, \\ \vdots \\ \dot {x} _ {n _ {i} - 1} ^ {i} = x _ {n _ {i}} ^ {i}, \\ \dot {x} _ {n _ {i}} ^ {i} = f _ {i} (\xi) + g _ {i} (\xi) u _ {i}, \quad x ^ {i} \in \mathbb {R} ^ {n _ {i}}, i = 1, \dots , m, \\ \sum_ {i = 1} ^ {m} n _ {i} = n, \quad \xi = (x, w, z), \\ \dot {w} = S w + p (\xi), \quad w \in \mathbb {R} ^ {s}, \quad \operatorname{Re} \{\sigma (S) \} <   0, \\ \dot {z} = C z + q (\xi), \quad z \in \mathbb {R} ^ {t}, \quad \operatorname{Re} \{\sigma (C) \} = 0, \end{array} \right. \tag {8.6.29}
$$

这里 $f_{i}(0) = 0, g_{i}(0) \neq 0, p(\xi)$ 和 $q(\xi)$ 及其导数在原点的值均为零.

由于每个积分链的第一个变量有特殊作用，我们采用记号

$$\boldsymbol {x} = \left(x _ {1}, \overline {{{{x}}}} _ {1}\right),$$

这里

$$x _ {1} = (x _ {1} ^ {1}, \dots , x _ {1} ^ {m}), \qquad \bar {x} _ {1} = (x _ {2} ^ {1}, \dots , x _ {n _ {1}} ^ {1}, \dots , x _ {2} ^ {m}, \dots , x _ {n _ {m}} ^ {m}).$$

当 $C = 0$ 时系统 (8.6.29) 称具有零中心. 本节只考虑这种情况.

设 $\psi_{i}^{(r)}(z), r=2,\cdots,h, i=1,\cdots,m,$ 为 z 的一族阶数为 r 的齐次多项式，定义
