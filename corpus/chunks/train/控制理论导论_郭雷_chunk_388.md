$$
\begin{array}{l} \| \lambda R (\lambda ; A) T (t) - T (t) \| \leqslant \int_ {0} ^ {\delta} \lambda \mathrm{e} ^ {- \lambda s} \| T (t + s) - T (t) \| \mathrm{d} s \\ + \int_ {\delta} ^ {\infty} \lambda \mathrm{e} ^ {- \lambda s} \| T (t + s) - T (t) \| \mathrm{d} s \\ \leqslant \sup _ {0 \leqslant s \leqslant \delta} \| T (t + s) - T (t) \| \\ + (2 \lambda - \omega) M (\lambda - \omega) ^ {- 1} \mathrm{e} ^ {\omega (t + \delta) - \lambda \delta}. \\ \end{array}
$$

因此

$$\overline {{\lim _ {\lambda \to \infty}}} \| \lambda R (\lambda ; A) T (t) - T (t) \| \leqslant \sup _ {0 \leqslant s \leqslant \delta} \| T (t + s) - T (t) \|, \quad \delta > 0.$$

由于 $\delta > 0$ 的任意性，我们得到

$$\lim _ {\lambda \rightarrow \infty} \| \lambda R (\lambda ; A) T (t) - T (t) \| = 0, \quad \forall t > 0,$$

这表明 $T(t)$ 对于 $t > 0$ 是紧算子. 证毕.

Hilbert 空间 $H$ 上的 $C_0$ 半群 $T(t)$ 称为是自伴的, 是指它满足 $T(t)^* = T(t), \forall t \geqslant 0$ , 即 $T(t)$ 对于所有 $t \geqslant 0$ 是自伴的.

引理5.3.6 为了Hilbert空间 $H$ 上的 $C_0$ 半群 $T(t)$ 是自伴的，必须且只须 $T(t)$ 的生成算子是自伴的.

证明 留作练习.

定理5.3.16 设 $T(t)$ 是无穷维Hilbert空间 $H$ 上的 $C_0$ 紧自伴半群. 那么

(1) $T(t)$ 的生成算子 $A$ 有紧豫解式：  
(2) $A$ 有实纯点谱 $\sigma(A) = \{\lambda_k \mid k \geqslant 1\}$ , 并且 $\lambda_k \to -\infty (k \to \infty)$ , $A$ 的相应的直交规范本征元序列 $\{\varphi_k \mid k \geqslant 1\}$ 构成 $H$ 的直交规范基;  
(3) $\forall x \in H, T(t)x \in \mathcal{D}(A), \forall t > 0,$ 并且

$$T (t) x = \sum_ {k = 1} ^ {\infty} \mathrm{e} ^ {\lambda_ {k} t} \langle x, \varphi_ {k} \rangle \varphi_ {k}. \tag {5.3.35}$$

证明 (1) 是定理 5.3.15 的结果，而 (2) 是 (1) 的直接推论。为证 (3)，任取 $z \in H$ ，当 $k \geqslant 1$ 时，我们有

$$\frac {\mathrm{d}}{\mathrm{d} t} \langle z, T (t) \varphi_ {k} \rangle = \langle z, T (t) A \varphi_ {k} \rangle = \langle z, \lambda_ {k} T (t) \varphi_ {k} \rangle .$$

于是 $\langle z, T(t) \varphi_k \rangle = \langle z, \mathrm{e}^{\lambda_k t} \varphi_k \rangle, \forall t \geqslant 0, z \in H.$ 因此

$$T (t) \varphi_ {k} = \mathrm{e} ^ {\lambda_ {k} t} \varphi_ {k}, \quad \forall k \geqslant 1, t \geqslant 0.$$

这意味着 $\{\mathrm{e}^{\lambda_k t} \mid k \geqslant 1\}$ 和 $\{\varphi_k \mid k \geqslant 1\}$ 是 $T(t)$ 的本征值集和相应的本征元集. 因此根据紧白伴算子理论，式 (5.3.35) 成立.

最后，为证 $T(t)x\in \mathcal{D}(A),\forall t > 0,$ 我们仅需证明

$$\sum_ {k = 1} ^ {\infty} \lambda_ {k} ^ {2} \mathrm{e} ^ {2 \lambda_ {k} t} \langle x, \varphi_ {k} \rangle^ {2} < \infty , \quad t > 0.$$

但这是显然的，因为使得 $\lambda_{k} \geqslant 0$ 的这些 $k$ 的数目是有限的。证毕

现在对于 $\lambda \in \rho(A)$ , 记 $\lambda = \sigma + i\tau$ , 其中 $\sigma$ 和 $\tau$ 分别为 $\lambda$ 的实部和虚部.
