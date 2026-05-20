其中 $b = C\rho (\varepsilon)\left[\frac{1}{\beta} +\frac{\gamma - \alpha}{\alpha(\beta - \gamma)}\right]$

选择足够小的 $\varepsilon$ 可保证 b<1 。因此 $P\eta$ 是 S 上的压缩映射。于是由压缩映射定理可知，映射 $P\eta$ 在 S 上有一个不动点。

现在假设 $\| g(y,0)\| \leqslant k\| y\|^p$ ，函数 $G(y,0)$ 满足同一边界。考虑闭子集

$$Y = \{\eta \in S | \| \eta (y) \| \leqslant c _ {4} \| y \| ^ {p} \}$$

其中 $c_{4}$ 是一个待选的正常数。为了完成引理的证明，需证明 $P\eta$ 的不动点在 $Y$ 内，也就是证明能够选择 $c_{4}$ ，使 $P\eta$ 把 $Y$ 映射到其自身。利用式(C.63)给出的 $G$ 的估计值，有

$$\| G (y, \eta (y)) \| \leqslant \| G (y, 0) \| + \| G (y, \eta (y)) - G (y, 0) \| \leqslant k \| y \| ^ {p} + \rho (\varepsilon) \| \eta (y) \|$$

由于在集合 $Y$ 内有 $\| \eta (y)\| \leqslant c_4\| y\|^p$ ，所以

$$\| G (y, \eta (y)) \| \leqslant [ k + c _ {4} \rho (\varepsilon) ] \| y \| ^ {p}$$

把该估计值用于式(C.61)，得

$$\| (P \eta) (y) \| \leqslant \int_ {- \infty} ^ {0} C \exp (\beta s) [ k + c _ {4} \rho (\varepsilon) ] \| \pi (s; y, \eta) \| ^ {p} d s$$

因为 $\pi (t;0,\eta) = 0$ ， $\| \pi_{y}(t;y,\eta)\| \leqslant M(\alpha)\exp (-\gamma t)$ ，与引理3.1的证明一样，可以证明当 $t\leqslant 0$ 时，有 $\| \pi (t;y,\eta)\| \leqslant M(\alpha)\exp (-\gamma t)\| y\|$

因而 $\| (P\eta)(y)\| \leqslant \frac{C[k + c_4\rho(\varepsilon)]M^p(\alpha)}{\beta - p\gamma}\| y\|^p \stackrel {\mathrm{def}}{=} c_5\| y\|^p$

只要 $\varepsilon$ 和 $\alpha$ 足够小, $\beta - p\gamma > 0$ 。选择足够大的 $c_{4}$ ，以及足够小的 $\varepsilon$ ，有 $c_{5} < c_{4}$ 。因此， $P\eta$ 把 Y 映射到其自身，引理证明完毕。

证明定理 8.1 根据引理 C.6, 当取 $A = A_{1}, B = A_{2}, f = g_{1}$ 和 $g = g_{2}$ 时, 即可证明定理 8.1。☐

证明定理8.3 定义 $\mu(y) = h(y) - \phi(y)$ ，利用 $\mathcal{N}(h(y)) = 0$ 和 $\mathcal{N}(\phi(y)) = O(\|y\|^p)$ ，其中 $\mathcal{N}(h(y))$ 由式(8.11)定义，可以证明 $\mu(y)$ 满足偏微分方程

$$\frac {\partial \mu}{\partial y} (y) [ A _ {1} y + N (y, \mu (y)) ] - A _ {2} \mu (y) - Q (y, \mu (y)) = 0 \tag {C.66}$$

其中 $N(y,z) = g_{1}(y,\phi (y) + z)$

$$
\begin{array}{l} Q (y, z) = g _ {2} (y, \phi (y) + z) - g _ {2} (y, \phi (y)) + \mathcal {N} (\phi (y)) \\ - \frac {\partial \phi}{\partial y} (y) [ g _ {1} (y, \phi (y) + z) - g _ {1} (y, \phi (y)) ] \\ \end{array}
$$

满足方程(C.66)的函数 $\mu(y)$ 是当 $A = A_{1}, B = A_{2}, f = N$ 和 $g = Q$ 时, 形如方程(C.54)\~方程(C.55)的中心流形, 此时还有

$$Q (y, 0) = \mathcal {N} (\phi (y)) = O (\| y \| ^ {p})$$

因此,根据引理 C.6,存在一个连续可微函数 $\mu(y)=O(\|y\|^{p})$ , 满足方程(C.66)。因此有 $h(y)-\phi(y)=O(\|y\|^{p})$ 。简化后的系统为

$$
\begin{array}{l} \dot {y} = A _ {1} y + g _ {1} (y, h (y)) \\ = A _ {1} y + g _ {1} (y, \phi (y)) + g _ {1} (y, h (y)) - g _ {1} (y, \phi (y)) \\ \end{array}
$$

由于 $g_{1}$ 是二次连续可微的，且其一阶偏导数在原点为零，因此在原点的邻域内有

$$\left\| \frac {\partial g _ {1}}{\partial z} (y, z) \right\| \leqslant k _ {1} \| y \| + k _ {2} \| z \|$$

根据均值定理, 得 $g_{1i}(y, h(y)) - g_{1i}(y, \phi(y)) = \frac{\partial g_{1i}}{\partial z}(y, \zeta(y))[h(y) - \phi(y)]$

其中当 $\| y\| < 1$ 时，有 $\| \zeta (y)\| \leqslant \| \mu (y)\| +\| \phi (y)\| \leqslant k_3\| y\| ^p\leqslant k_3\| y\|$

因此有 $\| g_1(y,h(y)) - g_1(y,\phi (y))\| \leqslant k_4\| y\| \| \mu (y)\| = O(\| y\|^{p + 1})$

证毕。
