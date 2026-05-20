$$x _ {n} (t, x _ {0}) = T ^ {\prime} (t) x _ {0} - \int_ {0} ^ {t} T (t - s) B R ^ {- 1} B ^ {*} P _ {n} (s) x _ {n} (s, x _ {0}) \mathrm{d} s, \tag {10.6.25}$$

那么

$$\lim _ {n \rightarrow \infty} x _ {n} (t, x _ {0}) = x (t, x _ {0}), \quad \forall t \in \mathbb {R} ^ {+}; \tag {10.6.26}$$

(3) 对于任意 $x_0 \in H$ , 有

$$\lim _ {n \rightarrow \infty} m \left(t _ {n}, x _ {0}\right) = \lim _ {n \rightarrow \infty} \left(P _ {n} (t) x _ {0}, x _ {0}\right) = \left(P x _ {0}, x _ {0}\right)= \lim _ {t \rightarrow \infty} \int_ {0} ^ {t} \left((Q + P B R ^ {- 1} B ^ {*} P) x (s, x _ {0}), x (s, x _ {0})\right) \mathrm{d} s, \tag {10.6.27}$$

这里为简单起见，记 $m(t,x_0)\stackrel {\mathrm{def}}{=}m(0,t,x_0);$

(4) 控制 $u(t) = -R^{-1}B^{*}Px(t,x_{0})$ 使得由式 (10.6.21) 定义的性能指标泛函 $J(\cdot ,x_0)$ 达到极小.

证明 (1) 是定理 5.3.8 的直接结果.

(2) 首先注意 $\| T(t) \| \leqslant \mu_1 e^{\omega t}$ , 并且 $\| BR^{-1} B^* \| \stackrel{\mathrm{def}}{=} \mu_6 < \infty$ . 于是利用式 (10.6.24) 和式 (10.6.25) 我们有

$$
\begin{array}{l} \left\| x _ {n} (t) - x (t) \right\| \leqslant \mu_ {1} \mu_ {6} \int_ {0} ^ {t} \mathrm{e} ^ {\omega (t - s)} \| P _ {n} (s) \| \| x _ {n} (s) - x (s) \| \mathrm{d} s \\ + \mu_ {1} \mu_ {6} \int_ {0} ^ {t} \mathrm{e} ^ {\omega (t - s)} \| (P _ {n} (s) - P) x (s) \| \mathrm{d} s. \tag {10.6.28} \\ \end{array}
$$

根据引理 10.6.3, 对于任意 $s \geqslant 0$ , $P_{n}(s)$ 强收敛于 $P$ , $\| P_n(s) \| \leqslant \| P \|$ , 并且根据已经证明的 (1), $x(s)$ 在 $\mathbb{R}^+$ 连续. 因此, 如果我们记

$$q _ {n} (t) = \mu_ {1} \mu_ {6} \int_ {0} ^ {t} \mathrm{e} ^ {\omega (t - s)} \| (P _ {n} (s) - P) x (s) \| d s,$$

则使用Lebesgue控制收敛定理可知，当 $n\to \infty$ 时 $q_{n}(t)\rightarrow 0,\forall t\in \mathbb{R}^{+}$ ，于是由Gronwall不等式可得

$$\left\| x _ {n} (t) - x (t) \right\| \leqslant q _ {n} (t) + \int_ {0} ^ {t} q _ {n} (s) \mathrm{e} ^ {\left(\mu_ {1} \mu_ {6} \| P \| + \omega\right) (t - s)} \mathrm{d} s.$$

然后再次使用控制收敛定理可知式 (10.6.26) 成立.

(3) 我们知道，关于性能指标 $J(\cdot; 0, t_n, x_0)$ 的最优控制是

$$u _ {n} (t) = - R ^ {- 1} B ^ {*} P _ {n} (t) x _ {n} (t).$$

因此

$$(Q x _ {n} (t), x _ {n} (t)) + (R u _ {n} (t), u _ {n} (t)) = ((Q + P _ {n} (t) B R ^ {- 1} B ^ {*} P _ {n} (t)) x _ {n} (t), x _ {n} (t)).$$

注意对于每一 $t \in \mathbb{R}^+$ , $P_n(t)$ 强收敛于 $P$ . 故不等式

$$\left\| P _ {n} (t) x _ {n} (t) - P x (t) \right\| \leqslant \| P \| \left\| x _ {n} (t) - x (t) \right\| + \left\| P _ {n} (t) - P\right) x (t) \|$$

表明 $P_{n}(t)x_{n}(t)$ 在 $\mathbb{R}^{+}$ 上点点收敛于 $Px(t)$ . 于是对于任意 $t \in \mathbb{R}^{+}$ ,
