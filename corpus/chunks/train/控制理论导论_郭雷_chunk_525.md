# 线性定常系统快速控制的唯一性和存在性

定理7.2.3表明，线性定常正则快速系统的快速控制函数在任意有限时间区间上，除有限多个时刻外是完全确定的，而且是Bang-Bang型的。进而我们有：

定理 7.2.4(快速控制唯一性定理) 假定线性定常系统 (7.2.18) 是正则的，则其快速控制函数是唯一的（指除在其定义的时间区间上至多除有限多个时刻外是唯一确定的）.

证明 设 $u^{*}(t)$ 和 $\tilde{u}^{*}(t)$ 是线性定常系统 (7.2.18) 的两个不同快速控制函数。显然它们都把 $t_0$ 时刻初态 $x_0$ 在相同时刻 $t_f^*$ 内控制到原点，即 $x(t_f^*) = 0$ ，相应于 $u^{*}(t)$ 和 $\tilde{u}^{*}(t)$ 的快速轨线 $x^{*}(t)$ 和 $\tilde{x}^{*}(t)$ 分别为

$$x ^ {*} (t) = \mathrm{e} ^ {A (t - t _ {0})} \left(x _ {0} + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {A (t _ {0} - s)} B u ^ {*} (s) \mathrm{d} s\right), \tag {7.2.24}\tilde {x} ^ {*} (t) = \mathrm{e} ^ {A (t - t _ {0})} \left(x _ {0} + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {A (t _ {0} - s)} B \tilde {u} ^ {*} (s) \mathrm{d} s\right), \tag {7.2.25}$$

注意到 $x^{*}(t_{f}^{*}) = \tilde{x}^{*}(t_{f}^{*}) = 0$ ，由式(7.2.24)和式(7.2.25)得到

$$\int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mathrm{e} ^ {A (t _ {0} - s)} B u ^ {*} (s) \mathrm{d} s = \int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mathrm{e} ^ {A (t _ {0} - s)} B \tilde {u} ^ {*} (s) \mathrm{d} s. \tag {7.2.26}$$

由于方程 (7.2.18) 的正则性，其快速控制函数 $u^{*}(t), \tilde{u}^{*}(t)$ 能表示为

$$u ^ {*} (t) = \operatorname{sign} \left[ B ^ {\mathrm{T}} \mathrm{e} ^ {A ^ {\mathrm{T}} \left(t _ {f} ^ {*} - t\right)} \mu \right], \quad \mu \neq 0,\tilde {u} ^ {*} (t) = \operatorname{sign} \left[ B ^ {\mathrm{T}} \mathrm{e} ^ {A ^ {\mathrm{T}} \left(t _ {f} ^ {*} - t\right)} \tilde {\mu} \right], \quad \tilde {\mu} \neq 0.$$

$u^{*}(t)$ 和 $\tilde{u}^{*}(t)$ 在 $[t_0, t_f^*]$ 上除各自的开关时刻（有限多个）外，皆完全确定，所以 $\mu \neq \bar{\mu}$ . 因为否则将有 $u^{*}(t) = \bar{u}^{*}(t)$ . 根据极大值原理，在 $[t_0, t_f^*]$ 上至多除有限多个时刻外，处处成立

$$\mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - t)} B u ^ {*} (t) \geqslant \mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - t)} B \tilde {u} ^ {*} (t). \tag {7.2.27}$$

依假设 $u^{*}(t)$ 和 $\tilde{u}^{*}(t)$ 不同，所以至少存在一个长度不为零的区间 $[t_1, t_2] \subset [t_0, t_f^*]$ ，使得在此区间上 $u^{*}(t) \neq \tilde{u}^{*}(t)$ ，即

$$\mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - t)} B u ^ {*} (t) > \mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - t)} B \bar {u} ^ {*} (t), \quad \forall t \in [ t _ {1}, t _ {2} ]. \tag {7.2.28}$$

由式 (7.2.27) 和式 (7.2.28) 可得

$$\int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mu^ {\mathrm{T}} \mathrm{e} ^ {A ^ {\mathrm{T}} (t _ {f} - s)} B u ^ {*} (s) \mathrm{d} s > \int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - s)} B \bar {u} ^ {*} (s) \mathrm{d} s.$$

另一方面，在等式(7.2.26)两端左乘 $\mu^{\mathrm{T}}\mathrm{e}^{A(t_f^* -t_0)}$ 后得到
