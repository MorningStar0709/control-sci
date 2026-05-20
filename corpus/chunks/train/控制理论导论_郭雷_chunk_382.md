# $C_0$ 半群的扰动

设 $A$ 是Banach空间 $X$ 上某 $C_0$ 半群的生成算子， $B \in \mathcal{L}(X)$ 。现在的问题是 $A + B$ 是否仍然生成 $X$ 上的 $C_0$ 半群。这样的问题常常在线性系统的反馈控制中出现。

定理5.3.8 设 $A$ 是Banach空间 $X$ 上 $C_0$ 半群 $T(t)$ 的生成算子，满足 $\| T(t)\| \leqslant Me^{\omega t},\forall t\geqslant 0,$ 并且 $B\in \mathcal{L}(X)$ .那么 $A + B$ 是另一个 $C_0$ 半群 $S(t)$ 的生成算子，并且 $S(t)$ 由下列方程唯一确定：

$$S (t) x = T (t) x + \int_ {0} ^ {t} T (t - s) B S (s) x \mathrm{d} s, \quad t \geqslant 0, x \in X, \tag {5.3.25}$$

并满足

$$\| S (t) \| \leqslant M \mathrm{e} ^ {(\omega + \| B \| M) t}, \quad \forall t \geqslant 0. \tag {5.3.26}$$

证明 设 $\lambda \in \mathbb{C}$ 满足 $\operatorname{Re} \lambda > \omega + M \| B \|$ . 根据假定，

$$\| R (\lambda ; A) ^ {n} \| \leqslant M / (\operatorname{Re} \lambda - \omega) ^ {n}, \quad \forall n \geqslant 1.$$

于是 $\| BR(\lambda; A) \| \leqslant M \| B \| / (\operatorname{Re} \lambda - \omega) < 1$ ，从而 $\lambda \in \rho(A + B)$ ，并且

$$\| R (\lambda ; A + B) \| \leqslant \| R (\lambda ; A) \| \| (I - B R (\lambda ; A) ^ {- 1} \| \leqslant M / (\operatorname{Re} \lambda - \omega - M \| B \|).$$

利用归纳法可以证明，当 $\operatorname{Re} \lambda > \omega + M \| B \|$ 时

$$\| R (\lambda ; A + B) \| \leqslant M / (\operatorname{Re} \lambda - \omega - M \| B \|) ^ {n}, \quad \forall n \geqslant 1.$$

因此根据Hille-Yosida定理， $A + B$ 生成 $X$ 上某个 $C_0$ 半群 $S(t)$

今令 $V(s) = T(t - s)S(s), 0 \leqslant s \leqslant t$ . 于是对于任意固定的 $x \in \mathcal{D}(A) = \mathcal{D}(A + B), V(s)x$ 是 $s \in (0, t)$ 的可微函数，并且

$$\frac {\mathrm{d} V (s) x}{\mathrm{d} s} = T (t - s) B S (s) x, \quad 0 < s < t.$$

对上式从 0 到 t 积分，可见 $S(t)$ 确实是方程 (5.3.25) 的解。今证积分方程 (5.3.25) 有唯一解。事实上，如果 $U(t)$ 是方程 (5.3.25) 的另一个解，则

$$\| S (t) x - U (t) x \| \leqslant \int_ {0} ^ {t} M \| B \| \mathrm{e} ^ {\omega (t - s)} \| S (s) x - U (s) x \| \mathrm{d} s, \quad \forall t \geqslant 0.$$

根据 Gronwall 不等式 (见第 2 章), 上式蕴含 $S(t) = U(t), \forall t \geqslant 0$ . 证毕.
