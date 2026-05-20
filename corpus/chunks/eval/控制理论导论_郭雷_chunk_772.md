# 弱镇定

下面讨论 Hilbert 空间 $H$ 中 $C_0$ 半群的弱镇定问题。首先我们叙述两个有关 $C_0$ 压缩半群的分解定理。

设 $H$ 是 Hilbert 空间. 我们说子空间 $V \subset H$ 约化有界线性算子 $B \in \mathcal{L}(H)$ , 亦称 $V$ 是 $B$ 的约化子空间, 是指

$$B V \subset V \quad {\text { 和 }} \quad B ^ {*} V \subset V.$$

一有界线性算子 $B \in \mathcal{L}(H)$ 称为酉算子，是指它满足

$$B ^ {*} B = B B ^ {*} = I,$$

$B$ 称为是完全非酉算子，是指如果 $V$ 是 $B$ 的一非零约化子空间，则 $B$ 在 $V$ 上的限制不可能是酉算子.

定理10.3.10 设 $T(t)$ 是Hilbert空间 $H$ 上一 $C_0$ 压缩半群， $A$ 为其生成算子。那么 $H$ 可以分解成直交和 $H = H_u \oplus H_v$ ，其中 $H_u$ 和 $H_v$ 是 $T(t)$ 的约化子空间，使得

(1) $T(t)$ 在 $H_{u}$ 上的限制 $T_{u}(t) = T(t)|_{H_{u}}$ 是一酉群；  
(2) $T(t)$ 在 $H_{v}$ 上的限制 $T_{v}(t) = T(t)|_{H_{v}}$ 是一完全非酉半群；  
(3) 这种分解是唯一的，并且

$$H _ {u} = \left\{x \in H \mid \| T (t) x \| = \| T ^ {*} (t) x \| = \| x \|, \forall t \geqslant 0 \right\}.$$

此外，

$$H _ {u} = \overline {{{\mathcal {D} (A) \cap H _ {u}}}}.$$

证明 记 $J(t) = I - T(t)T^{*}(t), J_{*}(t) = I - T^{*}(t)T(t)$ ，则 $\| T(t)x\| = \| T^{*}(t)x\| = \| x\|$ 等价于

$$(J (t) x, x) = (J _ {*} (t) x, x) = 0. \tag {10.3.16}$$

由于 $T(t)$ 是压缩的，故 $J(t)$ 和 $J_{*}(t)$ 都是自伴非负定算子．因此，(10.3.16) $\Longleftrightarrow x\in \mathcal{N}(J(t))\cap \mathcal{N}(J_{*}(t)).$ 令

$$H _ {u} = \bigcap_ {t > 0} \left[ \mathcal {N} (J (t)) \cap \mathcal {N} (J _ {*} (t)) \right] \quad {\text {和}} \quad H _ {v} = H _ {u} ^ {\perp}.$$

显然 $H_{u}$ 是闭的，并且 $T_{u}(t) = T(t)|_{H_{u}}$ 可以延拓为一酉群。今证在 $H_{v}$ 上， $T_{v}(t)$ 是一完全非酉半群。事实上，不然的话，存在一非零子空间 $V \subset H_{v}$ 约化 $T_{v}(t)$ 为一酉群。但容易验证 $T(t)$ 在 $H_{u} \oplus V$ 上的限制也是一酉群，则与 $H_{u}$ 的定义矛盾。

从 $H_{u}$ 的定义容易看出，

$$T (t) H _ {u} \subset H _ {u} \quad {\text { 和 }} \quad T ^ {*} (t) H _ {u} \subset H _ {u} \qquad \forall t \geqslant 0.$$

最后我们证明 $H_{u} = \overline{\mathcal{D}(A)\cap H_{u}}$ 事实上，由于 $H_{u}$ 是闭的，我们只需证明 $H_{u}\subset \overline{\mathcal{D}(A)\cap H_{u}}$ 对于任意 $x\in H_u$ 和 $\lambda \in \mathbb{R},\lambda >\omega (A)$ ，我们有

$$R (\lambda ; A) x = \int_ {0} ^ {\infty} \mathrm{e} ^ {\lambda t} T (t) x \mathrm{d} t.$$

于是，从 $T(t)x\in H_u,\forall t\geqslant 0,$ 可得 $R(\lambda ;A)x\in \mathcal{D}(A)\cap H_u$ ，但我们知道当 $\lambda \to \infty$ 时 $\lambda R(\lambda ;A)x\to x,$ 从而 $x\in \overline{\mathcal{D}(A)\cap H_u}$ .证毕.

定理10.3.11 设 $T(t)$ 是 $H$ 上一 $C_0$ 压缩半群. 令

$$W = \left\{x \in H \mid T (t) x \rightarrow 0 (t \rightarrow \infty) \right\},$$

则 (1) $W$ 约化 $T(t), \forall t \geqslant 0$ ;

(2) $T(t)$ 在 $W^{\perp}$ 上约化为一酉群，即 $W^{\perp} \subset H_{u}$ ;

(3) $W = \{x\in H\mid T^{*}(t)x\to 0(t\to \infty)\} .$

证明 (1) 首先注意 $W$ 是 $H$ 的闭子空间. 对于任意 $x \in W$ 和任意 $s \geqslant 0$ , 当 $t \to \infty$ 时,
