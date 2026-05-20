命题 8.5.3 考虑非线性系统 (8.5.1), 其中 p = m. 设 $G = \operatorname{span}\{g_{1}, \cdots, g_{m}\}$ 是对合的. 如果相对阶向量 $(\rho_{1}, \cdots, \rho_{m})$ 在 $x_{0} \in M$ 有定义, 且解耦矩阵 $A(x_{0})$ 是非奇异的, 则存在 $x_{0}$ 的一个邻域 U, 使得系统 (8.5.1) 能局部表示为 Byrnes-Isidori 正则型式 (8.5.16).

证明 利用引理 8.5.2, 可找到 $\{z_{j+1}^{i} = L_{f}^{j}h_{i} \mid i = 1, \cdots, m, j = 1, \cdots, \rho_{i} - 1\}$ , 它们是线性无关的。由于 $G$ 是对合的，我们可选择适当的局部坐标，使得

$$
G = \operatorname{span} \left\{\left[ \begin{array}{c} I _ {m} \\ 0 \end{array} \right] \right\}.
$$

现在解耦矩阵变为

$$
A (x) = \left[ \begin{array}{c} \mathrm{d} _ {f} ^ {\rho_ {1}} h _ {1} \\ \vdots \\ \mathrm{d} L _ {f} ^ {\rho_ {m}} h _ {m} \end{array} \right] G := H (x) G.
$$

很明显我们能选择 n-m 个函数 $\{\xi_{i}\}$ 使得 $\langle d\xi_{i},G\rangle=0$ 。现在除 $L_{f}^{k}h_{i}, i=1,\cdots,m, k=0,\cdots,\rho_{i}-1$ 外，我们还能找到 $n-\sum_{i=1}^{m}(\rho_{i})$ 个函数 $\{w_{j}\}$ ，使得 $L_{f}^{k}h_{i}, i=1,\cdots,m, k=0,\cdots,\rho_{i}-1$ 及 $\{w_{j}\}$ 形成一个局部坐标。在这个坐标下，系统 (8.5.1) 能局部表示为正则形式 (8.5.16)。

最后，我们考虑仿射非线性系统输入输出映射的 Fliess 展式。对于线性系统

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, \\ y = C x, \end{array} \right.
$$

其输入输出响应可表示为

$$y = C \left(\mathrm{e} ^ {A (t - t _ {0})} x _ {0} + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {A (t - \tau)} B u (\tau) \mathrm{d} \tau\right). \tag {8.5.17}$$

一个自然的问题是：对于仿射非线性系统 (8.5.1)，式 (8.5.17) 是否有其对应的形式？回答是肯定的。这个表现形式称为 Fliess 展式。下面我们简单令 $t_0 = 0$ 。

首先，我们需要一些表示。记

$$g _ {0} = f, \quad u _ {0} = 1,$$

则仿射非线性系统可表示为

$$
\left\{ \begin{array}{l} \dot {x} = \sum_ {i = 0} ^ {m} g _ {i} u _ {i}, \\ y = h (x). \end{array} \right. \tag {8.5.18}
$$

其次，我们递推地定义一组多重积分如下：

$$
\left\{ \begin{array}{l} \int_ {0} ^ {t} \mathrm{d} \xi_ {i} = \int_ {0} ^ {t} u _ {i} (\tau) \mathrm{d} \tau , \\ \int_ {0} ^ {t} \mathrm{d} \xi_ {i _ {k + 1}} \mathrm{d} \xi_ {i _ {k}} \dots \mathrm{d} \xi_ {i _ {1}} = \int_ {0} ^ {t} u _ {i _ {k + 1}} (\tau) \int_ {0} ^ {\mathrm{T}} d \xi_ {i _ {k}} \dots \mathrm{d} \xi_ {i _ {1}}, \quad k \geqslant 1. \end{array} \right. \tag {8.5.19}
$$

由定义可得

$$
\left\{ \begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} \int_ {0} ^ {t} \mathrm{d} \xi_ {i} = u _ {i}, \\ \frac {\mathrm{d}}{\mathrm{d} t} \int_ {0} ^ {t} \mathrm{d} \xi_ {i _ {k + 1}} \dots \mathrm{d} \xi_ {i _ {1}} = u _ {i _ {k + 1}} (t) \int_ {0} ^ {t} \mathrm{d} \xi_ {i _ {k}} \dots \mathrm{d} \xi_ {i _ {1}}. \end{array} \right. \tag {8.5.20}
$$

那么我们有以下 Fliess 展式 (8.5.21):

定理 8.5.2 存在 T > 0, 使得系统 (8.5.1) 在初始点 $x(0) = x_{0}$ 的输入输出关系可表示为
