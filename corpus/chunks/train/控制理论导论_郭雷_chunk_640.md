$$L _ {\tilde {g} _ {j}} L _ {\tilde {f}} ^ {k} h _ {i} (x) = 0, \quad k \geqslant 0, j \neq i. \tag {8.5.12}$$

事实上，当 $k < \rho_{i} - 1$ 时，由相对阶的定义可知式(8.5.12)成立。当 $k = \rho_{i} - 1$ 时，它是式(8.5.11)的第一式。最后，当 $k \geqslant \rho_{i}$ 时，它是式(8.5.11)的第二式。

利用引理8.5.1, 很明显 $v^i$ 并不影响 $y_j$ , $j \neq i$ .

最后，我们必须证明 $v_{i}$ 能控制 $y_{i}$ .

利用引理 8.5.2, 选择 $z_{1}^{p+1}, \cdots, z_{\rho_{p}}^{p+1}$ ，使得 $\left\{z_{j}^{i} \mid i = 1, \cdots, p + 1, j = 1, \cdots, \rho_{i}\right\}$ 是线性无关的。于是 z 是一局部坐标，这里

$$z _ {j} ^ {i} = L _ {j} ^ {j} h _ {i}, \quad i = 1, \dots , p, j = 0, \dots , \rho_ {i} - 1,$$

且

$$\rho_ {1} + \dots + \rho_ {p + 1} = n.$$

显然在这个坐标架下，反馈系统可变为

$$
\left\{ \begin{array}{l} \left\{ \begin{array}{c c} \dot {z} _ {1} ^ {i} = z _ {2} ^ {i}, & \\ \vdots & \\ & i = 1, \dots , p, \\ \dot {z} _ {\rho_ {i} - 1} ^ {i} = z _ {\rho_ {i}} ^ {i}, & \\ \dot {z} _ {\rho_ {i}} ^ {i} = v _ {i}, & \end{array} \right. \\ \dot {z} _ {s} ^ {p + 1} = f _ {s} ^ {p + 1} (z) + \gamma_ {s} ^ {p + 1} (z) v, & s = 0, 1, \dots , \rho_ {p + 1}, \\ y _ {i} = z _ {1} ^ {i}, & i = 1, 2, \dots , i = 1, \dots , p. \end{array} \right. \tag {8.5.13}
$$

由此可见， $v_{i}$ 能控制 $y_{i}$ .

下面考虑非线性系统的正则型．首先，考虑单输入单输出的情况.

命题8.5.2 考虑单输入单输出系统

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + g (x) u, \quad x \in M, \\ y = h (x). \end{array} \right. \tag {8.5.14}
$$

如果相对阶 $\rho$ 在 $x_0 \in M$ 有定义，则存在 $x_0$ 的邻域 $U$ ，使得该系统能局部表示为

$$
\left\{ \begin{array}{l} \dot {z} _ {1} - z _ {2}, \\ \dot {z} _ {2} = z _ {3}, \\ \vdots \\ \dot {z} _ {\rho - 1} = z _ {\rho}, \\ \dot {z} _ {\rho} = a (\xi) + b (\xi) u, \\ \dot {w} = \varphi (\xi), \\ y = z _ {1}, \quad \xi \in U, \end{array} \right. \tag {8.5.15}
$$

这里 $\xi = (z, w)$ . 式 (8.5.15) 称为 Byrnes-Isidori 正则型.

证明 利用引理 8.5.2, 我们能构造 $\{z_i = L_f^{i-1}h \mid i = 1, \cdots, \rho\}$ , 它们是线性无关的. 对于 $z_1, \cdots, z_\rho$ , 可找到 $n - \rho$ 个函数 $w = \{w_1, \cdots, w_{n-\rho}\}$ , 使得 $\mathrm{d}w_i \in \{g\}^\perp$ , 且 $\xi = (z, w)$ 成为 $U$ 上的局部坐标. 在局部坐标 $\xi$ 下, 系统 (8.4.14) 变为正则型式 (8.5.15).

对多输入系统，设 $p = m$ ，即系统的输入输出相等，那么我们称以下式(8.5.16)为Byrnes-Isidori正则型：

$$
\left\{ \begin{array}{l} \dot {z} _ {1} ^ {i} = z _ {2} ^ {i}, \\ \dot {z} _ {2} ^ {i} = z _ {3} ^ {i}, \\ \vdots \\ \dot {z} _ {\rho_ {i} - 1} ^ {i} = z _ {\rho_ {i}} ^ {i}, \\ \dot {z} _ {\rho_ {i}} ^ {i} = a _ {i} (\xi) + b _ {i} (\xi) u _ {i}, \quad i = 1, \dots , m \\ \vdots \\ \dot {w} = \varphi (\xi), \\ y _ {i} = z _ {1} ^ {i}, \quad i = 1, \dots , m, \xi \in U, \end{array} \right. \tag {8.5.16}
$$

这里 $\xi=(z,w)$ .
