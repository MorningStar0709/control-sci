$$
\begin{array}{l} \left. \frac {\partial k}{\partial x} \right| _ {*} = \left[ \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x _ {1}}, \dots , \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x _ {n}} \right], \\ \left. \frac {\partial^ {2} k}{\partial x ^ {2}} \right| _ {*} = \left[ \frac {\partial^ {2} k \left(x ^ {*} \left(t _ {f}\right)\right)}{\partial x _ {i} \partial x _ {j}} \right], \\ \left. \frac {\partial H}{\partial x} \right| _ {*} = \left[ \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial x _ {1}}, \dots , \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial x _ {n}} \right], \\ \left. \frac {\partial H}{\partial u} \right| _ {*} = \left[ \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u _ {1}}, \dots , \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u _ {r}} \right], \\ \left. \frac {\partial^ {2} H}{\partial x ^ {2}} \right| _ {*} = \left[ \frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial x _ {i} \partial x _ {j}} \right], \\ \left. \frac {\partial^ {2} H}{\partial u ^ {2}} \right| _ {*} = \left[ \frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u _ {k} \partial u _ {l}} \right], \\ \left. \frac {\partial^ {2} H}{\partial x \partial u} \right| _ {*} = \left[ \frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial x _ {i} \partial u _ {k}} \right], \\ \left. \frac {\partial^ {2} H}{\partial u \partial x} \right| _ {*} = \left[ \frac {\partial^ {2} H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u _ {k} \partial x _ {i}} \right]. \\ \end{array}
$$

引理7.1.1 令 $\xi(t)$ 是定义在 $[t_0, t_f]$ 上的分段连续 $r$ 维向量值函数。假设对定义在 $[t_0, t_f]$ 上的任一分段连续的 $r$ 维向量值函数 $\eta(t)$ 皆成立

$$\int_ {t _ {0}} ^ {t _ {f}} \xi^ {\mathrm{T}} (t) \eta (t) \mathrm{d} t = 0,$$

则必有 $\xi(t) = 0, \forall t \in [t_0, t_f]$ .

证明留作练习.

注意到 $J_{1}[u]$ 在 $u^{*}(t)$ 处达到极小，即 $J_{1}[\varepsilon]$ 在 $\varepsilon = 0$ 时达到极小，于是有

$$\left. \frac {\mathrm{d} J _ {1} (\varepsilon)}{\mathrm{d} \varepsilon} \right| _ {\varepsilon = 0} = 0.$$

由式 (7.1.13) 知

$$0 = \left(\frac {\partial k}{\partial x} \right| _ {*} + \psi^ {T} (t _ {f}) \cdot \delta x (t _ {f}) - \int_ {t _ {0}} ^ {t _ {f}} \left(\dot {\psi} ^ {T} (t) + \frac {\partial H}{\partial x} \right| _ {*}\cdot \delta x (t) \mathrm{d} t - \int_ {t _ {0}} ^ {t _ {f}} \left. \frac {\partial H}{\partial u} \right| _ {*} \cdot \delta u (t) \mathrm{d} t. \tag {7.1.15}$$

依关于 $f, k$ 和 $u^{*}(t)$ 的假设，以 $\psi$ 为未知量的线性时变非齐次向量方程
