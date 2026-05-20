$$J ^ {*} (x _ {0}, t _ {0}; t _ {f}) = \frac {1}{2} x _ {0} ^ {\mathrm{T}} P (t _ {0}; t _ {f}, 0) x _ {0}.$$

将式 (7.3.24) 中 $u(t)$ 限制在 $[t_0, t_f]$ 上时，则其相应性能指标值 $J[u; t_f]$ 满足

$$\frac {1}{2} x _ {0} ^ {\mathbf {T}} P (t _ {0}; t _ {f}, 0) x _ {0} \leqslant J [ u; t _ {f} ].$$

根据引理7.3.1, 在上式两端令 $t_f \to +\infty$ 得到

$$\frac {1}{2} x _ {0} ^ {\mathrm{T}} \bar {P} (t _ {0}) x _ {0} \leqslant J [ u; + \infty ]. \tag {7.3.26}$$

比较式 (7.3.25) 和式 (7.3.26) 得

$$J [ u _ {i} + \infty ] = \frac {1}{2} x _ {0} ^ {\mathrm{T}} \bar {P} (t _ {0}) x _ {0}.$$

任取 $x_0 \in \mathbb{R}^n$ ，设式 (7.3.1) 和式 (7.3.19) 的最优解为 $(u^*(t), x^*(t))$ ，则相应的最优指标值 $J^*(x_0, t_0; +\infty)$ 为

$$J ^ {*} (x _ {0}, t _ {0}; + \infty) = \frac {1}{2} \int_ {t _ {0}} ^ {+ \infty} \left(x ^ {* T} (t) Q (t) x ^ {*} (t) + u ^ {* T} (t) R (t) u ^ {*} (t)\right) d t. \tag {7.3.27}$$

显然有

$$J ^ {*} (x _ {0}, t _ {0}; + \infty) \leqslant J [ u; + \infty ] = \frac {1}{2} x _ {0} ^ {\mathrm{T}} \dot {P} (t _ {0}) x _ {0}.$$

另一方面，对任意固定的 $t_f$ 将 $(u^{*}(t), x^{*}(t))$ 限制在 $[t_0, t_f]$ 上时，依定理7.3.1有

$$\frac {1}{2} x _ {0} ^ {T} P (t _ {0}; t _ {f}, 0) x _ {0} \leqslant J [ u ^ {*} (\cdot); t _ {f} ].$$

在上式两端令 $t_f \to +\infty$ ，根据引理7.3.1和式(7.3.27)得

$$J ^ {*} (x _ {0}, t _ {0}; + \infty) = J [ u; + \infty ] = \frac {1}{2} x _ {0} ^ {\mathrm{T}} \bar {P} (t _ {0}) x _ {0}.$$

从而

$$u ^ {*} (t) = u (t), \quad \forall t \in [ t _ {0}, + \infty).$$

对于无穷时间区间上的线性定常二次最优控制，定理7.3.2的条件就是假设系统完全能控.

引理7.3.2 设 $[A, B]$ 完全能控， $Q \geqslant 0, R > 0$ ，则下列Riccati矩阵微分方程终值问题：

$$
\left\{ \begin{array}{l} - \dot {P} (t) = P (t) A + A ^ {\mathrm{T}} P (t) + Q - P (t) B R ^ {- 1} B ^ {\mathrm{T}} P (t), \\ P \left(t _ {f}\right) = 0, \quad t _ {f} > 0 \end{array} \right. \tag {7.3.28}
$$

的解矩阵 $P(t; t_f, 0)$ 当 $t_f \to +\infty$ 时的极限矩阵 $P$ 是半正定常值矩阵，且满足 Riccati 矩阵代数方程

$$P A + A ^ {\mathrm{T}} P + Q - P B R ^ {- 1} B ^ {\mathrm{T}} P = 0. \tag {7.3.29}$$

证明 事实上，由于 $P(t; t_f, 0)$ 是方程 (7.3.28) 中定常 Riccati 矩阵微分方程的解，故它对时间 $t$ 是平移不变的，即

$$P (t; t _ {f}, 0) = P (0; t _ {f} - t, 0).$$

![](image/952251a9944187c7b32b30979b1691d21402a2486b2cf4a3f5aacdff4fd0096f.jpg)

<details>
<summary>line</summary>

| t | P(t; t_f - t, 0) |
| --- | --- |
| t | P(0; t_f - t, 0) |
| t_f - t | P(t; t_f, 0) |
| t_f | P(t; t_f, 0) |
</details>

图7.3.2

在上式两端令 $t_f \to +\infty$ ，根据引理7.3.1得到

$$\lim _ {t _ {f} \to + \infty} P (t; t _ {f}, 0) = \bar {P} (t) = \lim _ {t _ {f} \to + \infty} P (0; t _ {f} - t, 0) = \bar {P} (0), \forall t \in [ 0, + \infty),$$

即 $\dot{P}(t) = \bar{P}(0) \stackrel{\mathrm{def}}{=} P$ . 再由 $P(t; t_f, 0) \geqslant 0$ , 知 $P \geqslant 0$ .

利用定理 7.3.2 和引理 7.3.2 即可得出.

定理7.3.3 对于完全能控的线性定常系统(7.3.1)，其无穷时间区间上的二次最优控制存在唯一，且其最优控制综合函数 $u(x)$ 为

$$u (x) = - R ^ {- 1} B ^ {\mathrm{T}} P x, \tag {7.3.30}$$

这里 $P$ 是Riccati矩阵代数方程(7.3.28)的半正定对称解矩阵.
