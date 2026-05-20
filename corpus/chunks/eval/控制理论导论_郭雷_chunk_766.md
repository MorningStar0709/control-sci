# 强镇定

上面我们已经证明了，如果 $A$ 是Hibert空间 $H$ 中具有紧豫解式的斜自伴算子， $B$ 是从另一个Hilbert空间 $U$ 到 $H$ 的有界线性算子， $(A, B)$ 是完全近似能控的，那么由 $A - BB^{*}$ 生成的 $C_{0}$ 半群是强稳定的。现在我们仍然在Hilbert空间中来研究确保强能稳性的更一般的条件。

我们设 $T(t)$ 是Banach空间 $X$ 中的 $C_0$ 半群. 半群 $T(t)$ 的通过 $x \in X$ 的轨线 $\mathcal{O}_T(x)$ 定义为

$$\mathcal {O} _ {T} (x) = \left\{T (t) x \mid t \geqslant 0 \right\},$$

而 $\omega-$ 极限集 $\Omega_T(x)$ 定义为

$$\Omega_ {T} (x) = \big \{y \in X \mid \exists t _ {k} \uparrow \infty , \text {使得} \lim _ {k \to \infty} T (t _ {k}) x = y \big \}.$$

集合 $M \subset X$ 叫做相对 $C_0$ 半群 $T(t)$ 是不变的, 是指对于每一 $x \in M$ , 有 $\mathcal{O}_T(x) \subset M$ .

设 $V: X \to \mathbb{R}$ 是一连续函数，我们定义泛函

$$\dot {V} (x) = \varlimsup_ {t \rightarrow 0 ^ {+}} \frac {1}{t} [ V (T (t) x) - V (x) ], \quad x \in X.$$

$V: X \to \mathbb{R}$ 称为集合 $G \subset X$ 上的一 Lyapunov 泛函，是指 $\dot{V}(x)$ 在 $\overline{G}$ 上连续，并且 $\dot{V}(x) \leqslant 0, \forall x \in G$ . 进而我们记

$$E = \{x \in G | \dot {V} (x) = 0 \}.$$

在上述这些定义之下，我们叙述如下定理 (见文献 [10]):

定理 10.3.4 (LaSalle 不变原理) 设 $T(t)$ 是 X 上的 $C_{0}$ 半群，V 是 $G \subset X$ 上的 Lyapunov 泛函，M 是相对 $C_{0}$ 半群 $T(t)$ 的在 E 中的最大不变集。如果对于某个 $y \in X$ ，轨线 $\mathcal{O}_{T}(y)$ 是相对紧的，且包含在 G 中，则对于任意 $x \in X$ ，当 $t \to \infty$ 时 $T(t)x \to M$ ，即极限 $\lim_{t \to \infty} T(t)x$ 存在并且属于 M。

为了应用上述强稳定性判据，我们要找出一适当的泛函 $V$ ，并证明 $M = \{0\}$ . 现在我们在 Hilbert 空间 $H$ 中考虑如下线性控制系统

$$\dot {x} (t) = A x (t) + B u (t),$$

其中 $A$ 生成 $H$ 上 $C_0$ 半群 $T(t)$ , 而 $B \in \mathcal{L}(U, H)$ . 我们选择反馈控制 $u(t) = -B^* x(t)$ , 于是相应的闭环系统为

$$\dot {x} (t) = A x (t) - B B ^ {*} x (t).$$

我们的目的是找出使得由 $A - BB^{*}$ 生成的 $C_0$ 半群 $S(t)$ 是强稳定的一些条件.

定理 10.3.5 设 A 是 Hilbert 空间 H 中 $C_{0}$ 压缩半群 $T(t)$ 的生成算子， $B \in \mathcal{L}(H)$ . 设 $S(t)$ 是 $A - BB^{*}$ 生成的 $C_{0}$ 半群. 如果

(1) 对于某个 $y \in X$ , 轨线 $\mathcal{O}_{S^*}(y)$ 在 $X$ 的某个 (可能与 $y$ 有关的) 紧集中;

(2) $(A, B)$ 是完全近似能控的，

那么 $S(t)$ 是弱稳定的，从而 $(A, B)$ 是弱能稳的.

证明 记 $F = A - BB^{*}$ , 则 $F^{*} = A^{*} - BB^{*}$ , 并且 $\mathcal{D}(F^{*}) = \mathcal{D}(A^{*})$ . 我们知道, $F^{*}$ 是 $C_{0}$ 半群 $S^{*}(t)$ 的生成算子. 考虑 $H$ 上的泛函 $V(x) = \frac{1}{2} \| x \|_{H}^{2}$ . 由于 $\| T(t) \| \leqslant 1, \forall t \geqslant 0$ , 并且 $A$ 和 $A^{*}$ 是耗散的, 故 $\operatorname{Re}(x, A^{*}x) \leqslant 0, \forall x \in \mathcal{D}(A^{*})$ . 容易验证, $\forall x \in \mathcal{D}(A^{*}), t \geqslant 0$ , 有
