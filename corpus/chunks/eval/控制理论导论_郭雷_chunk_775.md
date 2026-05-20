由此不难看出当 $t \to \infty$ 时 $T^{*}(t)x \rightharpoonup 0$ . 另一方面, 由于 $T^{*}(t)$ 是压缩的, 我们可以利用定理10.3.11中(3)证明当 $t \to \infty$ 时 $T(t)x \rightharpoonup 0$ , 由此得到 $x \in W$ . 于是 $C^{\perp}(A,B) \subset W$ .

(2) 充分性. 假定 $C^{\perp}(A, B) \subset W$ . 取反馈算子 $K = -B^{*}$ . $A - BB^{*}$ 生成某个 $C_{0}$ 压缩半群 $S(t)$ . 应用定理 10.3.10 于 $S(t)$ , 我们可以把 $H$ 分解成两个彼此直交的子空间 $H_{u}^{s}$ 和 $H_{v}^{s}$ , 这里 $H_{u}^{s}$ 约化 $S(t)$ 为一酉群, $H_{v}^{s}$ 约化 $S(t)$ 为一完全非酉半群. 于是从推论 10.3.4 可知, 对于任意 $x \in H_{v}^{s}$ , 当 $t \to \infty$ 时 $S(t)x \to 0$ . 剩下只需证明 $S(t)$ 在 $H_{u}^{s}$ 上是弱稳定的. 对于任意 $x \in H_{u}^{s} \cap \mathcal{D}(A)$ 和 $t \geqslant 0$ , 我们有

$$\frac {\mathrm{d}}{\mathrm{d} t} \| S ^ {*} (t) x \| ^ {2} = ((A ^ {*} - B B ^ {*}) S ^ {*} (t) x, S ^ {*} (t) x) + (S ^ {*} (t) x, (A ^ {*} - B B ^ {*}) S ^ {*} (t) x) = 0.$$

由于 $A^{*}$ 和 $-BB^{*}$ 是耗散的，上述方程意味着 $B^{*}S^{*}(t)x = 0, \forall t \geqslant 0$ . 因此从引理10.3.3可知 $B^{*}T^{*}(t)x = 0, \forall t \geqslant 0$ 或等价地， $x \in C^{\perp}(A, B)$ . 于是

$$x \in \mathcal {D} (A) \cap H _ {u} ^ {s} \Longrightarrow x \in C ^ {\perp} (A, B) \subset W. \tag {10.3.22}$$

这样从式 (10.3.21) 得到

$$S ^ {*} (t) x = T ^ {*} (t) x, \quad \forall x \in \mathcal {D} (A) \cap H _ {u} ^ {s}, \forall t \geqslant 0.$$

但是 $x \in W$ , 故当 $t \geqslant 0$ 时 $T^{*}(t)x \rightharpoonup 0$ . 因此当 $t \geqslant 0$ 时 $S^{*}(t)x \rightharpoonup 0$ , 并且根据定理10.3.11, 当 $t \geqslant 0$ 时 $S(t)x \rightharpoonup 0$ . 至此我们证明了, 对于所有的 $x \in \mathcal{D}(A) \cap H_{u}^{s}$ , 当 $t \geqslant 0$ 时 $S(t) \rightharpoonup 0$ . 由于 $\mathcal{D}(A) \cap H_{u}^{s}$ 在 $H_{u}^{s}$ 中是稠密的, 并且 $\| S(t) \| \leqslant 1$ , 容易验证对于所有的 $x \in H_{u}^{s}$ , 当 $t \to \infty$ 时 $S(t)x \rightharpoonup 0$ . 证毕.

推论 10.3.5 设 A 生成 Hilbert 空间 H 上 $C_{0}$ 压缩半群。如果 A 有紧豫解式，或者 A 是自伴的，则定理 10.3.12 的条件对于 $(A, B)$ 的强能稳性是必要且充分的，并且由 $A - BB^{*}$ 生成的 $C_{0}$ 半群是强稳定的。

证明 必要性是显然的，而充分性则是定理10.1.2的直接结果.

推论 10.3.6 设 A 生成 Hilbert 空间中一 $C_{0}$ 紧压缩半群。那么定理 10.3.12 的条件对于 $(A, B)$ 的指数能稳性是充要的，并且由 $A - BB^{*}$ 生成 $C_{0}$ 半群是指数稳定的。
