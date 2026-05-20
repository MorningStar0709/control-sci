定理5.3.26 设 $A$ 是Hilbert空间 $H$ 的闭稠定线性算子，那么为了 $A$ 是 $C_0$ 等距群 $T(t)$ 生成算子，必须且只须 $\mathbf{i}A$ 是极大对称的，即 $\mathrm{i}A\subset (\mathrm{i}A)^*$ 或 $A\subset -A^{*}$ 并且 $\mathcal{R}(I\pm A) = H.$

证明 只需注意在 Hilbert 空间情形下， $F(x) = x, \forall x \in H.$ 另一方面， $\operatorname{Re}(Ax, x) = 0, \forall x \in \mathcal{D}(A)$ ，即 $(Ax, x) = (x, -Ax), \forall x \in H.$ 这意味着 $A \subset -A^{*}$ . 于是从定理 5.3.25 即得所要结论．证毕.

定理 5.3.27(Stone) 设 A 是 Hilbert 空间 H 中闭稠定线性算子，那么为了 A 是某 $C_{0}$ 西群 $T(t)$ 的生成算子，必须且只须 A 是斜自伴的，即 $A^{*} = -A$ .

证明 只需注意 $T^{*}(t)$ 也是一酉群，即 $T^{*}(t)T(t) = T(t)T^{*}(t) = I, \forall t \geqslant 0$ ，并且其生成算子是 $A^{*}$ . 于是根据定理5.3.26, $A \subset -A^{*}$ ，并且 $A^{*} \subset -A$ ，从而 $A^{*} = -A$ . 证毕

现在我们来刻画 $C_0$ 等距半群的谱结构。一般说来， $C_0$ 半群生成算子的谱可能是空的。然而，对于 $C_0$ 等距半群，其生成算子至少有一纯虚谱点。

我们首先叙述有关等距算子局部谱性质的一个引理。对于 $X$ 中的闭线性算子 $T$ ，子空间 $X_0 \subset X$ 称为相对 $T$ 是不变的，是指它满足 $T(X_0 \cap \mathcal{D}(T)) \subset X_0$ 。对于一有界线性算子 $T \in \mathcal{L}(X)$ ，子空间 $X_0 \subset X$ 称为相对 $T$ 是超不变的，是指 $X_0$ 相对所有与 $T$ 可交换的 $S \in \mathcal{L}(X)$ 是不变的。

引理5.3.13 设 $T$ 是Banach空间 $X$ 中可逆的等距线性算子，则对于任意 $\lambda_0\in \sigma (T)$ 和任意 $\delta_0 > 0,$ 必存在相对 $T$ 超不变的非零子空间 $X_0$ ，使得

$$\sigma (T | x _ {0}) \subset \sigma (T) \cap \left\{\lambda \in \mathbb {C} \mid | \lambda - \lambda_ {0} | \leqslant \delta_ {0} \right\}. \tag {5.3.64}$$

证明 注意 $\sigma(T) \subset \mathbb{C}_1 \stackrel{\mathrm{def}}{=} \left\{ \lambda \in \mathbb{C} \mid |\lambda| = 1 \right\}$ . 设 $0 < \delta < \min\{1, \delta_0\}$ , 并记 $J_0 = \mathbb{C}_1 \cap \left\{ \lambda \in \mathbb{C} \mid |\lambda - \lambda_0| \leqslant \delta \right\}$ . 定义

$X_0 = \{x \in X \mid (\lambda I - T)^{-1} x \text{ 可以解析开拓到整个 } J_0^c = \mathbb{C} \setminus J_0\}$ .

今证 $X_0$ 是相对 $T$ 超不变的非平凡子空间，从而根据 $X_0$ 的定义，式 (5.3.64) 成立.

显然 $X_0$ 是线性子空间，并且如果 $S \in \mathcal{L}(X)$ 满足 $TS = ST$ ，则 $S(\lambda I - T)^{-1} = (\lambda I - T)^{-1}S, \forall \lambda \in \rho(T)$ ，从而 $SX_0 \subset X_0$ ，即 $X_0$ 相对 $T$ 是超不变的。现在我们证明 $X_0$ 是闭的。

设 $z_{1}$ 和 $z_{2}$ 是弧线 $J_{0}$ 的两个端点. 设 $\mathbb{C}_2 = \{\nu \in \mathbb{C} \mid |\nu| = 2\}$ , 并如图5.3.2所示, 定义

$$\Gamma_ {k} = \left\{\lambda z _ {k} \mid 0 \leqslant \lambda \leqslant 2 \right\}, \quad k = 1, 2,\Gamma_ {4} = \left\{2 z \mid z \in J _ {0} \right\}, \quad \Gamma_ {3} = \mathbb {C} _ {2} \backslash \Gamma_ {4},$$

设 $G_{1}$ 和 $G_{2}$ 为分别由 $(\Gamma_1, \Gamma_2, \Gamma_3)$ 和 $(\Gamma_1, \Gamma_2, \Gamma_4)$ 所包围的两个开扇形.
