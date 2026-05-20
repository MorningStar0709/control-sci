依定义存在序列 $\{t_f^m\}$ 使得 $t_f^* = \lim_{m\to \infty}t_f^m$ 。令 $u^{m}(t)$ 是定义在区间 $[t_0,t_f^m]$ 上满足控制约束方程 (7.2.12) 的 $r$ 维向量值函数，且方程 (7.2.18) 相应于 $u^{m}(t)$ 的解 $x^{m}(t)$ 满足 $x^{m}(t_{0}) = x_{0}, x^{m}(t_{f}^{*}) = 0$ 。显然， $u^{m}(\cdot) \in \mathcal{U}_{[t_0,t_f^*]}$ ，并且

$$x _ {0} = - \int_ {t _ {0}} ^ {t _ {f} ^ {m}} \mathrm{e} ^ {A (t _ {0} - \tau)} B u ^ {m} (\tau) \mathrm{d} \tau . \tag {7.2.32}$$

记 $L_{[t_0,t_f^* ]}\stackrel {\mathrm{def}}{=}\{u(\cdot)\mid u(\cdot):\left[t_0,t_f^*\right]\to \mathbb{U}_r$ 可测}，这里 $\mathbb{U}_r$ 是 $r$ 维单位立方体，见(7.2.12).显然， $u^{m}\in L[t_{0},t_{f}^{*}],\forall m\geqslant 1.$ 于是存在 $\{u^{m}(\cdot)\}$ 的一个弱收敛子列，为简化记号，不妨设 $\{u^{m}(\cdot)\}$ 本身弱收敛于 $u^{*}(\cdot)\in L_{[t_{0},t_{f}]}$ 因此，特别地，我们有

$$\lim _ {m \rightarrow \infty} \int_ {t _ {0}} ^ {t _ {f} ^ {m}} \mathrm{e} ^ {A (t _ {0} - s)} B u ^ {m} (s) \mathrm{d} s = \int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mathrm{e} ^ {A (t _ {0} - s)} B u ^ {*} (s) \mathrm{d} s.$$

由此从式 (7.2.32) 得到

$$x _ {0} = - \int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mathrm{e} ^ {A (t _ {0} - s)} B u ^ {*} (s) \mathrm{d} s. \tag {7.2.33}$$

上式表明，如果记 $x^{*}(t)$ 是方程(7.2.18)相应于 $u^{*}(t)$ 的解，则有 $x^{*}(t_{f}^{*}) = 0$ 。下面证明

$$\left| u _ {j} ^ {*} (t) \right| \leqslant 1, \quad j = 1, 2, \dots , r, \quad \text { a.e. } \quad t \in [ 0, t ^ {*} ]. \tag {7.2.34}$$

事实上，由于 $u^m (\cdot)\in \mathcal{U}_{[t_0,t_f^* ]}$ ，所以对任意固定 $j_0,0\leqslant j_0\leqslant r$ ，皆有

$$\left| u _ {j _ {0}} ^ {m} (t) \right| \leqslant 1, \quad \forall t \in [ t _ {0}, t _ {f} ^ {*} ]. \tag {7.2.35}$$

记 $\mathcal{M} \stackrel{\mathrm{def}}{=} \{t \mid u_{j_0}^*(t) > 1, t \in [t_0, t_f^*]\}$ , 于是

$$u _ {j _ {0}} ^ {*} (t) > 1, \quad \forall t \in \mathcal {M}. \tag {7.2.36}$$

今定义函数 $v_{j_0}(t)$

$$
v _ {j _ {0}} (t) = \left\{ \begin{array}{l l} 1, & \text {当} t \in \mathcal {M} \text {时}, \\ 0, & \text {当} t \in [ t _ {0}, t _ {f} ^ {*} ] \backslash \mathcal {M} \text {时}. \end{array} \right.
$$

易知， $v_{j_0}(t)\in L_{[t_0,t_f^* ]}$ .从式(7.2.35）知

$$- 1 \leqslant u _ {j _ {0}} ^ {m} (t) \leqslant 1, \quad \forall t \in \mathcal {M}, \forall m \geqslant 1. \tag {7.2.37}$$

联合式 (7.2.36) 和式 (7.2.37) 可知

$$u _ {j _ {0}} ^ {*} (t) - u _ {j _ {0}} ^ {m} (t) \geqslant u _ {j _ {0}} ^ {*} (t) - 1 > 0, \quad \forall t \in \mathcal {M}, m \geqslant 1. \tag {7.2.38}$$

注意
