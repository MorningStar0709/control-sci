由于 $W^{\perp}$ 约化 $T(t)$ , 故 $T(t)y_{2} \in W^{\perp}, (x, T(t)y_{2}) = 0$ . 但是 $y_{1} \in W$ , 故 $T(t)y_{1} \to 0$ ( $t \to \infty$ ). 因此我们证明了 $T^{*}(t)x \to 0$ ( $t \to \infty$ ). 交换 $T(t)$ 和 $T^{*}(t)$ 的位置, 可以证明 $T^{*}(t)x \to 0 \Longrightarrow T(t)x \to 0$ . 证毕.

推论10.3.4 设 $T(t)$ 是Hilbert空间 $H$ 中的 $C_0$ 压宿半群. 那么 $H$ 可以分解成三个彼此直交的子空间 $H_{\nu}, W_{u}$ 和 $W^{\perp}$ 之和, 这些子空间都约化 $T(t)$ 和 $T^{*}(t)$ , 使得 $W_{u} \oplus W^{\perp} = H_{u}, W_{u} \oplus H_{v} = W$ . 此外,

(1) 在 $H_{v}$ 上， $T(t)$ 是完全非酉的，并且是弱稳定的；  
(2) 在 $W_{u}$ 上， $T(t)$ 是酉群，并且是弱稳定的；  
(3) 在 $W^{\perp}$ 上， $T(t)$ 是酉群，并且 $\forall x \in W^{\perp}, T(t)x \neq 0, T^{*}(t)x \neq 0.$

证明可直接从定理 10.3.10, 10.3.11 推出，留作练习.

对于 Hilbert 空间 H 中的 $C_{0}$ 压宿半群 $T(t)$ ，集合

$$W = \{x \in H \mid T (t) x \rightarrow 0 (t \rightarrow \infty) \}$$

叫做弱稳定的子空间， $W^{\perp}$ 叫做弱不稳定的子空间，而 $W$ 和 $W^{\perp}$ 中的元则分别叫做弱稳定或弱不稳定的状态.

现在我们讨论线性控制系统

$$\dot {x} (t) = A x (t) + B u (t)$$

的弱镇定问题，其中 $A$ 是Hilbert空间 $H$ 中 $C_0$ 半群 $T(t)$ 的生成算子。在10.2节中我们定义了近似能控子空间

$$C (A, B) = \overline {{\bigcup_ {t \geqslant 0} \mathcal {R} (G (t))}},$$

其中 $G(t)$ 由式 (10.2.3) 定义. 显然,

$$C ^ {\perp} (A, B) \stackrel {{\mathrm{def}}} {{=}} (C (A, B)) ^ {\perp} = \bigcap_ {t \geqslant 0} \mathcal {N} (B ^ {*} T ^ {*} (t)).$$

$C^{\perp}(A,B)$ 叫做近似不能控子空间.

引理10.3.3 设 $T(t)$ 是 $H$ 中 $C_0$ 半群，其生成算子为 $A$ ，并设 $B \in \mathcal{L}(U, H)$ . 设 $K \in \mathcal{L}(H, U)$ ，而 $S(t)$ 是 $A + BK$ 生成的 $C_0$ 半群. 那么 $C(A, B) = C(A + BK, B)$ .

证明 这是定理 10.2.7 的直接结果.

为方便起见，我们列出有关 $T(t)$ 和 $S(t)$ 的如下两个恒等式：

$$S ^ {*} (t) x = T ^ {*} (t) x + \int_ {0} ^ {t} T ^ {*} (t - s) K ^ {*} B ^ {*} S ^ {*} (s) x d s, \tag {10.3.20}T ^ {*} (t) x = S ^ {*} (t) x - \int_ {0} ^ {t} S ^ {*} (t - s) K ^ {*} B ^ {*} T ^ {*} (s) x \mathrm{d} s. \tag {10.3.21}$$

定理10.3.12 设 $A$ 生成Hilbert空间 $H$ 中 $C_0$ 压宿半群, 而 $B \in \mathcal{L}(U, H)$ . 那么 $(A, B)$ 弱能稳当且仅当 $T(t)$ 的所有弱不稳定状态都是近似能控的, 并且 $K = -B^*$ 是一合适的弱镇定反馈增益算子.

证明 注意该定理可以表示成： $(A,B)$ 弱能稳 $\Longleftrightarrow W^{\perp} \subset C(A,B) \Longleftrightarrow C^{\perp}(A,B) \subset W$ ，这里 W 表示 $T(t)$ 的弱稳定子空间.

(1) 必要性. 假定 $(A, B)$ 是弱能稳的, 则存在 $K \in \mathcal{L}(H, U)$ 使得由 $A + BK$ 生成的 $C_0$ 半群 $S(t)$ 是弱稳定的. 于是对于 $x \in C^{\perp}(A, B)$ , 我们有 $B^{*}T^{*}(t)x = 0$ , $\forall t \geqslant 0$ . 从式 (10.3.21) 可知, 对于任意 $y \in H$ , 有

$$(T ^ {*} (t) x, y) = (S ^ {*} (t) x, y) = (x, S (t) y) \rightarrow 0 \quad (t \rightarrow \infty),$$
