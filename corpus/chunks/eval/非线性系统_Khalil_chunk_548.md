则对于所有 $\mathcal{X} \in \Omega_c$ ，但 $\mathcal{X} \notin \{V(\mathcal{X}) \leqslant c_0(\varepsilon)\}$ ，有与式 (C.100) 相似的不等式。由此可得集合 $\{V(\mathcal{X}) \leqslant c_0(\varepsilon)\} \times \Sigma$ 是正不变集，且 $\Omega_c \times \Sigma$ 内的每条轨线在有限时间内到达 $\{V(\mathcal{X}) \leqslant c_0(\varepsilon)\} \times \Sigma$ ，也就是说，给定式 (C.101)，存在一个有限时间 $\tilde{T} = \tilde{T}(\mu)$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_4$ ，有

$$\| \mathcal {X} (t) \| \leqslant \mu / 2, \quad \forall t \geqslant \tilde {T} \tag {C.102}$$

取 $\varepsilon_{2}^{*} = \varepsilon_{2}^{*}(\mu) = \min\{\varepsilon_{3}, \varepsilon_{4}\}$ 及 $T_{2} = T_{2}(\mu) = \max\{\tilde{T}, \tilde{T}\}$ ，则根据式(C.99)，式(C.102)， $\hat{x} = x - D(\varepsilon)\eta$ 及 $\|D(\varepsilon)\| = 1$ ，可得式(14.114)。

为了证明式(14.115)，把区间 $[0, \infty)$ 分成三个区间 $[0, T(\varepsilon)]$ ， $[T(\varepsilon), T_3]$ 和 $[T_3, \infty)$ ，分别在每个子区间上证明式(14.115)。根据式(14.114)给出的 $\mathcal{X}(t)$ 的毕竟有界性，和系统(C.96)的原点的渐近稳定性，可推出存在一个与 $\varepsilon$ 无关的有限时间 $T_3 \geqslant T(\varepsilon)$ ，使得对于每

个 $0 < \varepsilon \leqslant \varepsilon_{2}^{*}$ , 有

$$\left\| \mathcal {X} (t) - \mathcal {X} _ {r} (t) \right\| \leqslant \mu , \quad \forall t \geqslant T _ {3} \tag {C.103}$$

由式(C.97)可知,在区间 $[0,T(\varepsilon)]$ 上,有

$$\| \mathcal {X} (t) - \mathcal {X} (0) \| \leqslant k _ {1} t$$

同样可以证明在同一个区间上,有

$$\| \mathcal {X} _ {r} (t) - \mathcal {X} (0) \| \leqslant k _ {1} t$$

因此,有 $\|\mathcal{X}(t)-\mathcal{X}_{r}(t)\|\leqslant2k_{1}T(\varepsilon),\quad\forall t\in[0,T(\varepsilon)]$

由于当 $\varepsilon$ 趋于零时， $T(\varepsilon)$ 趋于零，因此存在 $0 < \varepsilon_5 \leqslant \varepsilon_2^*$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_5$ ，有

$$\| \mathcal {X} (t) - \mathcal {X} _ {r} (t) \| \leqslant \mu , \quad \forall t \in [ 0, T (\varepsilon) ] \tag {C.104}$$

在区间 $[T(\varepsilon), T_3]$ 上，解 $\mathcal{X}(t)$ 满足

$$\dot {\mathcal {X}} = F (\mathcal {X}, D (\varepsilon) \eta (t)), \quad \| \mathcal {X} (T (\varepsilon)) - \mathcal {X} _ {r} (T (\varepsilon)) \| \leqslant \delta_ {1} (\varepsilon)$$

其中 $D(\varepsilon)\eta$ 是 $O(\varepsilon)$ ，并且当 $\varepsilon$ 趋于零时， $\delta_1(\varepsilon)$ 趋于零。这样由定理3.5可得，存在 $0 < \varepsilon_6 \leqslant \varepsilon_2^*$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_6$ ，有
