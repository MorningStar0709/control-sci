$$\operatorname{ad} _ {g _ {i}} X \in (\Omega_ {k ^ {*}} \cap G ^ {\perp}) ^ {\perp} = \Omega_ {k ^ {*}} ^ {\perp} + G, \quad i = 0, 1, \dots , m.$$

由于 $X \in \Delta$ 是任选的，故有

$$[ g _ {i}, \Delta ] \subset \Delta + G, \quad i = 0, 1, \dots , m.$$

下面证明 $\Delta$ 是 $\ker(h)$ 中的最大弱 $(f, g)$ 不变分布。设 $D$ 是 $\ker(h)$ 中的另一个弱 $(f, g)$ 不变分布。不失一般性，我们设 $D$ 是对合的。令 $X \in D, \omega \in D^{\perp} \cap G^{\perp}$ 。利用式 (8.4.23)，有

$$\langle L _ {g _ {i}} \omega , X \rangle = 0.$$

因此，

$$L _ {g _ {i}} (D ^ {\perp} \cap G ^ {\perp}) \subset D ^ {\perp}, \quad i = 0, 1, \dots , m.$$

现证明由方程 (8.4.22) 定义的 $\Omega_{k}$ 满足

$$\Omega_ {k} \subset D ^ {\perp}, \qquad k = 0, 1, \dots . \tag {8.4.24}$$

为此用归纳法证. 由 $\Omega_0$ 和 $D$ 的定义, 显然对 $k = 0$ , 式 (8.4.24) 成立. 设式 (8.4.24) 对 $k$ 成立, 则

$$
\begin{array}{l} \Omega_ {k + 1} = \Omega_ {k} + L _ {f} (\Omega_ {k} \cap G ^ {\perp}) + \sum_ {i = 1} ^ {m} L _ {g _ {i}} (\Omega_ {k} \cap G ^ {\perp}) \\ \subset \Omega_ {k} + L _ {f} (D ^ {\perp} \cap G ^ {\perp}) + \sum_ {i = 1} ^ {m} L _ {g _ {i}} (D ^ {\perp} \cap G ^ {\perp}) \\ \subset D ^ {\perp}. \\ \end{array}
$$

于是

$$\Delta^ {\perp} = \Omega_ {k ^ {*}} \subset D ^ {\perp},$$

这说明

$$D \subset \Delta .$$

显然在上面的算法中，关键在于 $k^{*}$ 的存在性。设 $x_{0}$ 为 $\Omega_0, \Omega_1, \dots, \Omega_{n-1}$ 的一个正则点，则显然对这个余分布增列，或者存在一个 $k^{*}$ 使得 $\Omega_{k^{*}} = \Omega_{k^{*}+1}$ ，或者 $\operatorname{rank}(\Omega_{n-1}) = n$ 。无论那种情况都有

$$\Delta = \Omega_ {n - 1} ^ {\perp}. \tag {8.4.25}$$

换言之，总存在 $k^{*} \leqslant n - 1$ .

如果系统解析，不难看出存在 $M$ 的一个开稠集 $U$ 使得式 (8.4.25) 在 $U$ 上成立.

例8.4.2 考虑下列系统在零点的一个邻域内的解耦问题：

$$
\left\{ \begin{array}{l} \dot {x} = f (x) + g (x) u + p (x) w, \\ y = h (x) = x _ {1} - \mathrm{e} ^ {x _ {4}} + \frac {1}{2} (x _ {3} + 1) ^ {- 2}, \end{array} \right. \tag {8.4.26}
$$

这里 $f(x)$ 和 $g(x)$ 与例8.4.1中的式(8.4.15)相同，且干扰 $\pmb{w}$ 由下述通道进入系统：

$$p (x) = [ \mathrm{e} ^ {x _ {1}}, \mathrm{e} ^ {x _ {4}}, 0, 1 ] ^ {\mathrm{T}}.$$

我们首先计算 $\Omega_0$ .

$$\Omega_ {0} = \operatorname{span} \{\mathrm{d} h \} = \operatorname{span} \left\{\left(1, 0, - (x _ {3} + 1) ^ {- 3}, - \mathrm{e} ^ {x _ {4}}\right) \right\}.$$

显然 $\Omega_0\subset G^{\perp}$ ，故

$$
\begin{array}{l} \Omega_ {0} \cap G ^ {\perp} = \Omega_ {0}, \\ \Omega_ {1} = \Omega_ {0} + L _ {f} \Omega_ {0} + L _ {g} \Omega_ {0} \\ = \operatorname{span} \left\{\left[ 1, 0, - (x _ {3} + 1) ^ {- 3}, - \mathrm{e} ^ {x _ {4}} \right] ^ {\mathrm{T}}, \left[ - 1, 0, 0, \mathrm{e} ^ {x _ {4}} \right] \right\}. \\ \end{array}
$$

于是

$$\Omega_ {1} \cap G ^ {\perp} = \Omega_ {0}.$$

因此 $\Omega_2 = \Omega_1$ 。由定理8.4.3，有
