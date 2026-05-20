$$\lim _ {k \rightarrow \infty} \| \mathrm{i} \omega_ {k} \varphi_ {k} - A \varphi_ {k} \| = 0,$$

这表明 $\sup \left\{\| R(\mathrm{i}\omega;A)\|\mid \omega \in \mathbb{R}\right\} = \infty$ ，与 $T(t)$ 指数稳定相矛盾。证毕。

定理10.4.1的证明 (1)假定 $G \supset J$ 并且方程(10.4.5)是精确能控的．定义有界线性算子 $K_{0} \in \mathcal{L}(L^{2}(\Omega))$

$$
K _ {0} \varphi = \left\{ \begin{array}{l l} b (x) \varphi (x), & x \in G, \\ b _ {0} \varphi (x), & x \in \Omega \backslash G. \end{array} \right.
$$

于是 $K_{0}$ 是 $L^{2}(\Omega)$ 中有界正定对称算子，并且 $K_{0} \geqslant b_{0}I$ 。由于 $\mathcal{A}^{*} = -\mathcal{A}$ ，依据定理10.3.8，由 $\mathcal{A} - \mathcal{B}_{J}K_{0}\mathcal{B}_{J}^{*}$ 生成的 $C_{0}$ 压缩半群是指数稳定的。注意

$$
\mathcal {A} - \mathcal {B} _ {J} K _ {0} \mathcal {B} _ {J} ^ {*} = \left[ \begin{array}{c c} 0 & I \\ - A & - \delta_ {J} (\cdot) b \end{array} \right],
$$

从而如果我们记

$$
\mathcal {F} = \left[ \begin{array}{c c} 0 & 0 \\ 0 & - \delta_ {J ^ {c}} (\cdot) b \end{array} \right],
$$

其中 $J^{c} = \Omega \backslash J$ ，而 $\delta_{J^c}$ 为 $\Omega$ 上子集 $J^{c}$ 的特征函数，于是方程 (10.4.4) 可以写成

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} Y (t)}{\mathrm{d} t} = (\mathcal {A} - \mathcal {B} _ {J} K _ {0} \mathcal {B} _ {J} ^ {*}) Y (t) + \mathcal {F} Y (t), \\ Y (0) = Y _ {0}. \end{array} \right. \tag {10.4.6}
$$

容易验证 $\mathcal{F}$ 满足引理10.4.1的两个条件．因此方程(10.4.4)是指数稳定的.

(2) 现在假定 $J \sup b$ , 并且方程 (10.4.4) 是指数稳定的. 如果我们定义算子 $K \in \mathcal{L}(L^2(\Omega))$ : $K \varphi = b(x) \varphi(x), \forall \varphi \in L^2(\Omega)$ , 那么

$$\mathcal {A} + \mathcal {B} = \mathcal {A} - \mathcal {B} _ {J} K \mathcal {B} _ {J} ^ {*}.$$

显然 $K$ 是非负对称的，从而根据定理10.3.8, $(\mathcal{A},\mathcal{B}_J)$ 在某个区间 $[0,t_f]$ 上是精确能控的．证毕.

现在我们考虑 Hilbert 空间 H 中如下二阶系统：

$$\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} (t) + A x (t) = B _ {1} \frac {\mathrm{d} x (t)}{\mathrm{d} t} + B _ {2} x (t), \tag {10.4.7}$$

其中 $A$ 是 $H$ 中具有紧豫解式的正定自伴算子， $B_{1}, B_{2} \in \mathcal{L}(H)$ 是紧算子。在应用中，式(10.4.7)当 $B_{1} = B_{2} = 0$ 时表示一无阻尼振动系统。如果在能量空间 $\mathcal{H}$ 中定义线性算子 $\mathcal{B}$

$$
\boldsymbol {\mathcal {B}} = \left[ \begin{array}{c c} 0 & 0 \\ B _ {1} & B _ {2} \end{array} \right],
$$

则系统 (10.4.7) 可以写成 $\mathcal{H}$ 中线性系统

$$\frac {\mathrm{d} Y (t)}{\mathrm{d} t} = (\mathcal {A} + \mathcal {B}) Y (t), \tag {10.4.8}$$

其中 $Y(t) = [x(t), \dot{x}(t)]^{\mathrm{T}}$ . 显然 $\mathcal{A} + \mathcal{B}$ 生成 $\mathcal{H}$ 上一 $C_0$ 群 $S(t)$ . 我们有
