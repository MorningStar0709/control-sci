定理10.4.2 设 $\mathcal{A}$ 和 $\mathcal{B}$ 如上，那么由 $\mathcal{A} + \mathcal{B}$ 生成的 $C_0$ 群 $S(t)$ 不是指数稳定的.

证明 设 $\{\lambda_n | n \geqslant 1\}$ 是 $\mathcal{A}$ 的本征值序列，而 $\{\varphi_n | n \geqslant 1\}$ 是 $\mathcal{A}$ 的相应的本征元序列，后者构成 $H$ 的直交规范基。显然 $\{\varphi_n | n \geqslant 1\}$ 也是 $V$ 中的直交基，从而 $\{[\varphi_n, 0]^{\mathrm{T}} | n \geqslant 1\}$ 和 $\{[0, \varphi_n]^{\mathrm{T}} | n \geqslant 1\}$ 是 $\mathcal{H}$ 中的直交基。

设 $V_{n}=H_{n}=\operatorname{span}\left\{\varphi_{1},\cdots,\varphi_{n}\right\}$ ，而 $P_{n}$ 是 H 到 $V_{n}\times H_{n}$ 的投影算子。由于 B 在 H 中是紧的，它可以用一列有穷秩算子 $B_{n}=P_{n}BP_{n}$ 按 $\mathcal{L}(\mathcal{H})$ 中范数任意逼近（见文献 [16]）。现在如果 $S(t)$ 是指数稳定的，则由 $A+B_{n}$ 生成的 H 中的 $C_{0}$ 半群当 $\|B-B_{n}\|_{\mathcal{L}(\mathcal{H})}$ 非常小但非零时是指数稳定的。但是，由于

$$\left\| S _ {n} (t) \left[ \varphi_ {m}, \mathrm{i} \sqrt {\lambda_ {m}} \varphi_ {m} \right] ^ {\mathrm{T}} \right\| _ {\mathcal {H}} = \left\| \left[ \varphi_ {m}, \mathrm{i} \sqrt {\lambda_ {m}} \varphi_ {m} \right] ^ {\mathrm{T}} \right\| _ {\mathcal {H}}, \quad t \in \mathbb {R}, 1 \leqslant n < m,$$

故 $S_{n}(t)$ 不可能指数稳定，从而 $S(t)$ 也不可能指数稳定。证毕.

下面几个定理在研究弹性振动这样的系统的指数镇定时是很有用的. 考虑 Hilbert 空间 $\mathcal{H}$ 中线性系统

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} Y (t)}{\mathrm{d} t} = \mathcal {A} Y (t) + \mathcal {B} Y (t), \\ Y (0) = Y _ {0} \in \mathcal {H}. \end{array} \right. \tag {10.4.9}
$$

假定 $\mathcal{A}$ 是斜自伴的，即 $\mathcal{A}^{*} = -\mathcal{A}$ ，并且 $\mathcal{A}$ 有紧豫解式。进而为方便起见假定 $\mathcal{N}(\mathcal{A}) = \{0\}$ 。于是 $\mathcal{A}$ 有本征值序列 $\{\mathrm{i}\omega_{n} \mid n \geqslant 1\} \subset \mathrm{i}\mathbb{R}$ ，并设 $\mathcal{A}$ 的相应的直交规范本征元序列为 $\{\varphi_{nj} \mid n \geqslant 1, 1 \leqslant j \leqslant r_{n}\}$ ，即满足 $\|\varphi_{nj}\| = 1$ ， $\langle \varphi_{nj}, \varphi_{mk} \rangle = \delta_{nm} \delta_{jk}$ ，以及

$$
\left\{ \begin{array}{l l} {\mathcal {A} \varphi_ {n j} = \mathrm{i} \omega_ {n} \varphi_ {n j},} & {\qquad n = 1, 2, \dots ,} \\ {\underset {n \to \infty} {\lim} | \omega_ {n} | = \infty ,} & \\ {0 <   | \omega_ {1} | \leqslant | \omega_ {2} | \leqslant \dots ,} & {\qquad \omega_ {n} \neq \omega_ {m} \text {若} n \neq m,} \end{array} \right.
$$

这里 $\tau_{n}$ 是相应于本征值 $\mathrm{i}\omega_{n}$ 的本征子空间的维数。假定 $\mathcal{A}$ 的谱满足如下间隙条件：

$$\inf \left\{\left| \omega_ {n} - \omega_ {m} \right| \mid m, n = 1, 2, \dots , m \neq n \right\} = \gamma > 0. \tag {10.4.10}$$
