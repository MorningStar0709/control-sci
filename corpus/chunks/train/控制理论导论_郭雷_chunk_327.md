$$\mathrm{d} \xi_ {t} ^ {\mathrm{T}} C _ {t} \xi_ {t} = [ \xi_ {t} ^ {\mathrm{T}} \dot {C} _ {t} \xi_ {t} + \xi_ {t} ^ {\mathrm{T}} (C _ {t} + C _ {t} ^ {\mathrm{T}}) a _ {t} + \operatorname{tr} C _ {t} B _ {t} B _ {t} ^ {\mathrm{T}} ] \mathrm{d} t + \xi_ {t} ^ {\mathrm{T}} C _ {t} B _ {t} \mathrm{d} w _ {t} + \xi_ {t} ^ {\mathrm{T}} C _ {t} ^ {\mathrm{T}} B _ {t} \mathrm{d} w _ {t}, \tag {4.3.21}$$

设 $(C_T, B_T)$ 为定义在 $[0, T]$ 上连续函数 $x$ 的可测空间， $\mathcal{B}_t = \sigma[x : x_s, s \leqslant t]$ ， $0 \leqslant t \leqslant T$ .

设 $a_{t}(x), b_{t}(x)$ 对任一 $t \in [0, T]$ 为 $\mathcal{B}_{t}$ 可测，且 $x \in \mathcal{B}_{T}$ . 如果对任意 $t \in [0, T]$

$$\xi_ {t} = \eta + \int_ {0} ^ {t} a _ {s} (\xi) \mathrm{d} s + \int_ {0} ^ {t} b _ {s} (\xi) \mathrm{d} w _ {s},$$

$\eta$ 对 $\mathcal{F}_0$ 可测， $(\xi_t, \mathcal{F}_t)$ 为适应过程， $\|a_t(\xi)\|^{\frac{1}{2}} \in \mathcal{P}_T, b_t(\xi) \in \mathcal{P}_T$ ，那么 $(\xi_t, \mathcal{F}_t)$ 称为随机微分方程

$$\mathrm{d} \xi_ {t} = a _ {t} (\xi) \mathrm{d} t + b _ {t} (\xi) \mathrm{d} w _ {t} \tag {4.3.22}$$

的强解.

如果在基本概率空间 $(\Omega, \mathcal{F}, P)$ 中可找到非降 $\sigma$ -代数族 $\mathcal{F}_t$ ，和 $\mathcal{F}_t$ 适应的过程 $\xi_t$ 及和 $\mathcal{F}_t$ 适应的 Wicner 过程 $(w_t, \mathcal{F}_t)$ ，使 $a_t(\xi), b_t(\xi)$ 都是和 $\mathcal{F}_t$ 适应的过程，使 $\|a_t(\xi)\|^{\frac{1}{2}} \in \mathcal{P}_T, b_t(\xi) \in \mathcal{P}_T, \xi_0$ 的分布为事先给定的分布 $\mu$ ，并且

$$\xi_ {t} = \xi_ {0} + \int_ {0} ^ {T} a _ {s} (\xi) \mathrm{d} s + \int_ {0} ^ {t} b _ {s} (\xi) \mathrm{d} w _ {s},$$

那么称 $(\xi_t, w_t, \mathcal{F}_t)$ 为对随机微分方程 (4.3.22) 具有初始分布 $\mu$ 的弱解.

定理 4.3.4 (弱解存在性) 如果 $a_{s}(x)$ 和 $b_{s}(x)$ 有界，并且固定 x 后，它们是 s 的连续函数，那么对任意初始分布 $\mu$ (作为 $\xi_{0}$ 的分布)，方程 (4.3.22) 存在弱解.

定理4.3.5 设 $a_{t}(x), b_{t}(x)$ 满足Lipschitz条件：对连续函数 $x, y$

$$\left\| a _ {t} (x) - a _ {t} (y) \right\| ^ {2} + \left\| b _ {t} (x) - b _ {t} (y) \right\| ^ {2} \leqslant L _ {1} \int_ {0} ^ {T} \left\| x _ {s} - y _ {s} \right\| ^ {2} \mathrm{d} K _ {s} + L _ {2} \left\| x _ {t} - y _ {t} \right\| ^ {2},\left\| a _ {t} (x) \right\| ^ {2} + \left\| b _ {t} (x) \right\| ^ {2} \leqslant L _ {1} \int_ {0} ^ {t} (1 + \| x \| ^ {2}) \mathrm{d} K _ {s} + L _ {2} (1 + \| x _ {t} \| ^ {2}),$$

这里 $L_{1}, L_{2}$ 为常数， $K_{s}$ 为有界非降右连续函数， $0 \leqslant K_{s} \leqslant 1$ .

设初值 $\xi_0$ 对 $\mathcal{F}_0$ 可测，那么方程(4.3.22)存在以 $\xi_0$ 为初值的唯一强解.

例4.3.8 考虑线性随机微分方程

$$\mathrm{d} \xi_ {t} = A _ {t} \xi_ {t} \mathrm{d} t + b _ {t} \mathrm{d} t + D _ {t} \mathrm{d} w _ {t}, \tag {4.3.23}$$
