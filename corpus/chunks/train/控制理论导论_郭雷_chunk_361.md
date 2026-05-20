$$(A f) (t) = \int_ {0} ^ {1} K (t, s) f (s) \mathrm{d} s, \quad \forall f \in C [ 0, 1 ],$$

其中核函数 $K(t,s)$ 在 $[0,1]\times [0,1]$ 上连续. 试证 $A$ 是有界的.

5.1.11 $A$ 仍由上题给出，但 $A: L^2(0,1) \to L^2(0,1)$ ，而 $K(t,s)$ 是 $L^2((0,1) \times (0,1))$ 中的函数。试问 $A$ 有界吗？

5.1.12 设 $M$ 和 $N$ 是 Banach 空间 $X$ 的两个闭子空间，且任意 $x \in X$ 可唯一地分解成 $x = y + z$ ，其中 $y \in M, z \in N$ 。试证存在与 $x$ 无关的常数 $c > 0$ ，使得 $\|y\| \leqslant c \|x\|$ ， $\|z\| \leqslant c \|x\|$ 。

5.1.13 设 $M$ 是自反严格凸Banach空间 $X$ 中的闭凸集. 求证对于任意 $y \in X$ , 存在唯一元 $z = z(y) \in M$ , 使得

$$\| y - x \| = \inf \left\{\| y - x \| \mid x \in M \right\}.$$

注：这里一线性空间 $X$ 中的集合 $M$ 叫做凸的，是指它满足

$$x, y \in M \longrightarrow \lambda x + (1 - \lambda) y \in M, \quad \forall \lambda \in [ 0, 1 ];$$

而Banach空间 $X$ 叫做严格凸的，是指它的单位球面是严格凸的，即

$$x, y \in X, x \neq y, \| x \| = \| y \| = 1 \Longrightarrow \| \lambda x + (1 - \lambda) y \| < 1, \forall \lambda \in (0, 1).$$

5.1.14 一个线性赋范空间 $X$ 叫做一致凸的，是指对于任意 $\varepsilon, 0 < \varepsilon \leqslant 2$ ，存在常数 $\delta(\varepsilon) > 0$ 使得

$$x, y \in X, \| x \| < 1, \| y \| < 1, \| x - y \| \geqslant \varepsilon \Longrightarrow \| x + y \| \leqslant 2 (1 - \delta (\varepsilon)).$$

试证每个 Hilbert 空间均是一致凸的.

5.1.15 设 $X$ 是自反 Banach 空间，那么 $X$ 是局部序列紧的，即 $X$ 中任意强有界序列必含有一弱收敛的子序列。读者试就 $X$ 为 Hilbert 空间情形给出证明。

5.1.16 设 $A$ 是 Hilbert 空间 $H$ 中对称算子 (可能无界), 并且 $\lambda = \mu + \tau i$ , 其中 $\mu, \tau \in \mathbb{R}$ , 试证

$$\left\| (\lambda I - A) ^ {- 1} x \right\| \geqslant | \tau | \| x \|, \quad \forall x \in \mathcal {D} (A).$$
