# 有穷时间区间上的调节问题

现在我们考虑线性控制系统

$$
\begin{array}{l} x (t) \stackrel {\text { def }} {=} x (t; u, x _ {0}) = T (t - t _ {0}) x _ {0} \\ + \int_ {t _ {0}} ^ {t} T (t - s) B u (s) \mathrm{d} s, \quad 0 \leqslant t _ {0} \leqslant t \leqslant t _ {1} <   \infty , \tag {10.6.9} \\ \end{array}
$$

这里以及下面， $H$ 和 $U$ 表示实Hilbert空间， $B\in \mathcal{L}(U,H),x_0\in H,$ 而 $T(t)$ 是由 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．假定控制 $u(\cdot)\in L^2 (t_0,t_1;U)$ ，于是 $x(t)$ 在 $[t_0,t_1]$ 上是强连续的．根据 $C_0$ 半群理论，存在两个常数 $\mu_{1}\geqslant 1$ 和 $\omega \in \mathbb{R}$ 使得

$$\| T (t) \| \leqslant \mu_ {1} \mathrm{e} ^ {\omega t}. \quad \forall t \geqslant 0.$$

我们取与系统 (10.6.9) 相关的性能泛函 $J$ 为

$$J (u; t _ {0}, t _ {1}, x _ {0}) = \left. (G x (t _ {1}), x (t _ {1}))\right) _ {H} + \int_ {t _ {0}} ^ {t _ {1}} \left[ (Q x (s), x (s)) _ {H} + (R u (s), u (s)) _ {U} \right] d s, \tag {10.6.10}$$

其中 $G$ 和 $Q$ 是 $H$ 中的有界非负对称算子， $R$ 为 $U$ 中有界正定对称算子。于是存在正常数 $\mu_2, \mu_3, \mu_4$ 使得

$$\mu_ {2} \| u \| ^ {2} \leqslant (R u, u) _ {U} \leqslant \mu_ {3} \| u \| ^ {2}, \quad \forall u \in U,0 \leqslant (Q x, x) \leqslant \mu_ {4} \| x \| ^ {2}, \quad \forall x \in H.$$

所谓调节问题就是寻找一控制 $u^0 \in L^2(t_0, t_1; U)$ 使得

$$J (u ^ {0}; t _ {0}, t _ {1}, x _ {0}) = \inf _ {u \in L ^ {2} (t _ {0}, t _ {1}; U)} J (u; t _ {0}, t _ {1}, x _ {0}) \stackrel {\text { def }} {=} m (t _ {0}, t _ {1}, x _ {0}).$$

这样的控制 $u^0 \in L^2(t_0, t_1; U)$ 叫做关于性能指标 $J$ 的最优控制，而 (10.6.9) 的对应于 $u^0$ 的解 $x^0(t)$ 则叫做相应的最优轨线.

引理 10.6.1 在上述假设和记号下，我们有

(1) 当 $u \equiv 0$ 时， $J(0; t_0, t_1, x_0)$ 满足估计

$$J (0; t _ {0}, t _ {1}, x _ {0}) \leqslant \frac {\mu_ {1} ^ {2} \mu_ {4}}{2 \omega} \left(\mathrm{e} ^ {2 \omega t _ {1}} - \mathrm{e} ^ {2 \omega t _ {0}}\right) \| x _ {0} \| ^ {2} + \| G \| \mu_ {1} ^ {2} \mathrm{e} ^ {2 \omega (t _ {1} - t _ {0})} \| x _ {0} \| ^ {2}; \tag {10.6.11}$$

(2) 如果 $t_1 - t_0 \leqslant t_1' - t_0'$ , 则 $m(t_0, t_1, x_0) \leqslant m(t_0', t_1', x_0), \forall x_0 \in H$ , 并且等号仅当 $t_1 - t_0 = t_1' - t_0'$ 时成立;

(3) 设 $u^0$ 使 $J(\cdot; t_0, t_1, x_0)$ 达到极小，则对于任意 $t \in [t_0, t_1)$ , $u^0|_{[t, t_1]}$ 使 $J(\cdot; t, t_1, x(t; u^0, x_0))$ 达到极小.

证明 (1) 和 (2) 是显然的. 为证 (3), 只需注意从方程 (10.6.9), (10.6.10) 可得

$$J (u ^ {0}; t _ {0}, t _ {1}, x _ {0}) = J _ {1} (u ^ {0}; t _ {0}, t, x _ {0}) + J (u ^ {0}; t, t _ {1}, x (t; u ^ {0}, x _ {0})),$$

其中

$$J _ {1} (u; t _ {0}, t, x _ {0}) = \int_ {t _ {0}} ^ {t} \left[ (Q x (s), x (s)) _ {H} + (R u (s), u (s)) _ {U} \right] d s,$$

而 $x(t)$ 由式 (10.6.9) 给出．如果存在 $u^{1} \in L^{2}(t, t_{1}; U)$ 使得

$$J (u ^ {1}; t, t _ {1}, x (t; u ^ {0}, x _ {0})) < J (u ^ {0}; t, t _ {1}, x (t; u ^ {0}, x _ {0})),$$

则
