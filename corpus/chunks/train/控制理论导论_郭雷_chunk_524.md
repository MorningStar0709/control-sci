$$\alpha^ {\mathrm{T}} \left[ b _ {j _ {0}}, A b _ {j _ {0}}, \dots , A ^ {(n - 1)} b _ {j _ {0}} \right] = 0,$$

即

$$\alpha^ {\mathrm{T}} b _ {j _ {0}} = 0, \quad \alpha^ {\mathrm{T}} A b _ {j _ {0}} = 0, \dots , \quad \alpha^ {\mathrm{T}} A ^ {(n - 1)} b _ {j _ {0}} = 0. \tag {7.2.22}$$

由此利用 Cayley-Hamilton 定理可得

$$\mathrm{e} ^ {A (t _ {f} - t)} = \sum_ {m = 0} ^ {n - 1} \beta_ {m} (t) A ^ {(m)}, \quad m = 0, 1, \dots , n - 1,$$

式中 $\beta_{m}(t)$ 是 $t$ 的标量解析函数。在上式两端分别左乘 $\alpha^{\mathrm{T}}$ 和右乘 $b_{j_0}$ ，并考虑到式(7.2.22)即得

$$\alpha^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} - t)} b _ {j _ {0}} = \sum_ {m = 0} ^ {n - 1} \beta_ {m} (t) \alpha^ {\mathrm{T}} A ^ {(m)} b _ {j _ {0}} = 0, \quad \forall t \in [ t _ {1}, t _ {2} ].$$

注意 $\psi_{\alpha}^{\mathrm{T}}(t) = \alpha^{\mathrm{T}}\mathrm{e}^{A(t_f - t)}$ 是共轭方程满足 $\psi^{\mathrm{T}}(t_f) = \alpha^{\mathrm{T}}\neq 0$ 的解，但 $\psi_{\alpha}^{\mathrm{T}}(t)b_{j_0} = \alpha^{\mathrm{T}}\mathrm{e}^{A(t_f - t)}b_{j_0} = 0,$ 这与正则快速系统的假设矛盾.

推论 7.2.1 线性定常系统 (7.2.18) 为奇异快速系统的充要条件是：至少有一个 $j_{1}, 1 \leqslant j_{1} \leqslant n,$ 使得相应的 $G_{j_{1}}$ 满足

$$\operatorname{rank} G _ {j _ {1}} = \operatorname{rank} \left[ b _ {j _ {1}}, A b _ {j _ {1}}, \dots , A ^ {(n - 1)} b _ {j _ {1}} \right] < n.$$

从定理7.2.3知，一个正则快速控制系统必定满足

$$\operatorname{rank} \left[ B A B \dots A ^ {(n - 1)} B \right] = n, \tag {7.2.23}$$

即一个正则快速控制系统一定是完全能控系统.
