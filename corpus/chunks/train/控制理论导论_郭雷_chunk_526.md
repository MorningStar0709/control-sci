$$\int_ {t _ {0}} ^ {t _ {f} ^ {*}} \mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - s)} B u ^ {*} (s) \mathrm{d} s = \int_ {t _ {0}} ^ {t _ {f}} \mu^ {\mathrm{T}} \mathrm{e} ^ {A (t _ {f} ^ {*} - s)} B \tilde {u} ^ {*} (s) \mathrm{d} s,$$

导致矛盾，从而定理7.2.4得证.

定理 7.2.5(开关次数定理) 假定线性定常系统 (7.2.18) 是正则的， $u^{*}(t)=\left[u_{1}^{*}(t),u_{2}^{*}(t),\cdots,u_{r}^{*}(t)\right]^{\mathrm{T}}$ 为快速控制函数。如果系统矩阵 A 的特征值 $\lambda_{1},\cdots,\lambda_{n}$ 皆为实数，则 $u^{*}(t)$ 的开关次数为 $N\leqslant n-1$ ，即

$$N = \max \left\{N _ {j} \mid j = 1, 2, \dots , r \right\} \leqslant n - 1.$$

这里 $N_{j}$ 为 $u_{j}^{*}(t)$ 的零点个数.

证明 依定理7.2.4, $u^{*}(t)$ 在 $[t_0, t_f^*]$ 上除有限多个时刻外唯一确定，且有

$$u ^ {*} (t) = \operatorname{sign} \left[ B ^ {\mathrm{T}} \mathrm{e} ^ {A ^ {\mathrm{T}} (t _ {j} - t)} \mu \right], \quad \mu \neq 0.$$

记

$$\mathrm{e} ^ {A ^ {\mathrm{T}} \left(t _ {f} ^ {*} - t\right)} \mu = \left[ \psi_ {1} (t), \psi_ {2} (t), \dots , \psi_ {n} (t) \right] ^ {\mathrm{T}},q _ {j} (t) = \sum_ {i = 1} ^ {n} b _ {i j} \psi_ {i} (t), \tag {7.2.29}$$

这里 $b_{j}=[b_{1j},b_{2j},\cdots,b_{nj}]^{T}, B=[b_{1},b_{2},\cdots,b_{r}]$ 。令 $\lambda_{1},\lambda_{2},\cdots,\lambda_{m}$ 为 A 的 $m(\leqslant n)$ 个不同特征值，其重数分别为 $k_{1},k_{2},\cdots,k_{m}$ ，从而有 $\sum_{l=1}^{m}k_{l}=n$ 。根据线性常微分方程理论，有

$$\psi_ {i} (t) = \sum_ {l = 1} ^ {m} f _ {i l} (t) \mathrm{e} ^ {\lambda_ {l} (t _ {f} ^ {*} - t)}, \quad i = 1, 2, \dots , n,$$

其中 $f_{il}(t)$ 是 $t$ 的多项式，其次数 $\deg (f_{il}(t))$ 满足

$$\deg (f _ {i l} (t)) \leqslant k _ {l} - 1, \quad i = 1, 2, \dots , n, l = 1, \dots , m. \tag {7.2.30}$$

将 $\psi_{i}(t)$ 代入 $q_{j}(t)$ 得

$$q _ {j} (t) = \sum_ {l = 1} ^ {m} \psi_ {j l} (t) \mathrm{e} ^ {\lambda_ {l} \left(t _ {f} ^ {*} - t\right)}, \quad j = 1, 2, \dots , r, \tag {7.2.31}$$

其中 $\psi_{jl}(t) = \sum_{i=1}^{n} b_{ij} f_{il}(t)$ 是 $t$ 的多项式. 易知有

$$\deg (\psi_ {j l} (t)) \leqslant k _ {l} - 1, \quad l = 1, 2, \dots , m, j = 1, 2, \dots , r.$$

注意到 $u_{j}^{*}(t)$ 的开关次数由 $q_{j}(t)$ 的零点个数确定，所以为证明定理，只须证明式(7.2.31)中 $q_{j}(t)$ 的零点个数不超过 $(n - 1)$ .

应用下列命题 7.2.1 的结论于式 (7.2.31) 中的多项式 $q_{j}(t)$ 即知， $q_{j}(t)$ 的零点个数不超过 $(m-1)+(k_{l}-1)+\cdots+(k_{m}-1)=(m-1)-m+k_{l}+\cdots+k_{m}=n-1$ .

命题 7.2.1 设 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$ 为彼此不同的实数， $g_{1}(t), g_{2}(t), \cdots, g_{m}(t)$ 分别是 t 的 $r_{1}, r_{2}, \cdots, r_{m}$ 次多项式．那么函数

$$g (t) = \sum_ {l = 1} ^ {m} g _ {l} (t) \mathrm{e} ^ {\lambda_ {l} t}$$

的零点个数小于或等于 $(m - 1) + \sum_{l = 1}^{m}r_l.$

命题7.2.1的证明可见文献[2].
