这样的坐标卡称为对 $\Delta$ 的平整坐标卡.

引理8.2.2 设 $\Delta$ 定义如上. 如果 $\Delta$ 是 $f$ 不变的, 那么在平整坐标系统下系统(8.1.1)可表示为

$$
\left\{ \begin{array}{l} \dot {z ^ {1}} - f ^ {1} (z), \\ \dot {z ^ {2}} = f ^ {2} (z ^ {2}), \quad z \in V, \end{array} \right. \tag {8.2.11}
$$

这里 $z^{1}=(z_{1},\cdots,z_{k})$ .

证明 设 $f^{2}(z) \neq f^{2}(z^{2})$ ，则存在 $1 \leqslant i \leqslant k$ 使得 $\frac{\partial f^2(z)}{\partial z_i^1} \neq 0$ . 那么

$$
\left[ f, \frac {\partial}{\partial z _ {i} ^ {1}} \right] = \left[ \begin{array}{l} \frac {\partial f ^ {1} (z)}{\partial z _ {i} ^ {1}} \\ \frac {\partial f ^ {2} (z)}{\partial z _ {i} ^ {1}} \end{array} \right] \not \in \nabla ,
$$

即得矛盾.

回到系统 (8.1.1). 设 $x_0$ 为 $\mathcal{F}_0$ 的正则点，即存在 $x_0$ 的邻域 $U$ 使得

$$\operatorname{rank} \left(\mathcal {F} _ {0} (x)\right) = k, \quad x \in U.$$

命题8.2.1 设 $x_0$ 为 $\mathcal{F}_0$ 的一个正则点，且 $\operatorname{rank}(\mathcal{F}_0(x_0)) = k$ ，则存在 $x_0$ 的一个局部坐标卡 $(V, z)$ ，使系统(8.1.1)能局部表示为

$$
\left\{ \begin{array}{l l} \dot {z} ^ {1} = f ^ {1} (z, u), \\ \dot {z} ^ {2} = f ^ {2} (z ^ {2}), & z \in V, \end{array} \right. \tag {8.2.12}
$$

这里 $F_{0}=\operatorname{span}\left\{\frac{\partial}{\partial z_{i}^{1}}, i=1,2,\cdots,k\right\}.$

证明 因为 $\mathcal{F}_0$ 是 Lie 代数，故作为一个分布它是对合的，并且显然 $\mathcal{F}_0$ 是 $F$ 不变的。由引理8.2.2，存在一个局部平整坐标，使系统变为

$$
\left\{ \begin{array}{l l} \dot {z} ^ {1} = f ^ {1} (z, u), \\ \dot {z} ^ {2} = f ^ {2} (z ^ {2}, u), \end{array} \right. \quad z \in V,
$$

并且 $\mathcal{F}_0 = \operatorname{span}\left\{\frac{\partial}{\partial z_i^1}\right\}$ . 现在我们只要证明 $f^2$ 与 $u$ 无关即可. 如果 $f^2$ 依赖于 $u$ , 则可找到两个不同的定常控制 $u_1$ 和 $u_2$ , 使得 $f^2(u_1) \neq f^2(u_2)$ . 那么 $f(u_1) - f(u_2) \notin \mathcal{F}_0$ , 这与 $\mathcal{F}_0$ 的定义矛盾.

将以上命题用于仿射非线性系统 (8.1.2)，则得到下述推论：

推论8.2.1 对系统(8.1.2)，设 $x_0$ 为 $\mathcal{F}_0$ 的一个正则点，且 $\operatorname{rank}(\mathcal{F}_0(x_0)) = k,$ 则存在 $x_0$ 的一个局部坐标卡 $(V,z)$ ，使系统(8.1.2)可局部表示为

$$
\left\{ \begin{array}{l} z ^ {1} = f ^ {1} (z) + \sum_ {i = 1} ^ {m} g _ {i} (z) u _ {i}, \\ z ^ {2} = f ^ {2} (z ^ {2}), \quad z \in V, \end{array} \right. \tag {8.2.13}
$$

这里 $F_{0}=\operatorname{span}\left\{\frac{\partial}{\partial z_{i}^{1}}, i=1,2,\cdots,k\right\}$ .

注8.2.2 如果用能控Lie代数 $\mathcal{F}$ 代替强能控Lie代数 $\mathcal{F}_0$ ，则可得到类似的分解.

下面讨论能观测余分布 $\mathcal{H}$ . 一个向量场 $X$ 称与 $\mathcal{H}$ 正交, 如果对任一 $\omega \in \mathcal{H}$ 均有 $\langle \omega, X \rangle = 0$ . 由此可定义分布 $\mathcal{H}^{\perp}$
