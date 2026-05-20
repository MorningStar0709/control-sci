$$\Omega_ {\varepsilon} = \left\{V _ {1} (\eta) \leqslant \frac {4 \| P _ {0} B _ {0} \| _ {2} ^ {2} \varepsilon^ {2} \| P _ {0} \| _ {2}}{\theta_ {1} ^ {2}}, | s | \leqslant \varepsilon \right\}$$

在 $\Omega_{\varepsilon}$ 内，系统

$$\dot {x} _ {0} = x _ {1}\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - \left(g _ {0} / \ell\right) \sin \left(x _ {1} + \delta_ {1}\right) - \left(k _ {0} / m\right) x _ {2} - \left(k / m \ell^ {2} \varepsilon\right) \left(a _ {0} x _ {0} + a _ {1} x _ {1} + x _ {2}\right)$$

在 $\bar{x}=[-(\varepsilon mg_{0}\ell/ka_{0})\sin\delta_{1},0,0]^{T}$ 处有唯一的平衡点。重复前面的稳定性分析，可以证明当 $\varepsilon$ 足够小时，平衡点 $\bar{x}$ 是渐近稳定的，且在 t 趋于无穷时， $\Omega_{\varepsilon}$ 内的每条轨线都收敛于 $\bar{x}$ ，因此 $\theta$ 收敛到期望的位置 $\delta_{1}$ 。图 14.11 给出了当 m=0.1, $\ell=1$ , $k_{0}=0.02$ , $\delta_{1}=\pi/2$ , $a_{0}=a_{1}=1$ , k=4，且 $\varepsilon=1$ 时的仿真结果。

![](image/60e5c30df7cd873071e228034a659f9e45914ce66ce26b1957d05daab4ce2ea4.jpg)

<details>
<summary>line</summary>

| 时间 | θ |
| --- | --- |
| 0 | 0.0 |
| 2 | 2.5 |
| 4 | 3.0 |
| 6 | 3.1 |
| 8 | 3.1 |
</details>

![](image/9c26e73a030d432619a5f90255e9d0b0de52a3727fd12f829e9ddbd0c95251e1.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 0 | 2.9 |
| 1 | 1.5 |
| 2 | 0.7 |
| 3 | 0.3 |
| 4 | 0.15 |
| 5 | 0.08 |
| 6 | 0.05 |
</details>

图 14.10 当 $\delta_{1}=\pi$ 时的连续滑模控制

![](image/89b2863fc177926319919f6a82ea4960193857db7b5793f17e0850786ab32aa4.jpg)

<details>
<summary>line</summary>

| 时间 | θ |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.0 |
| 2 | 1.8 |
| 3 | 1.9 |
| 4 | 1.7 |
| 5 | 1.5 |
| 6 | 1.5 |
| 7 | 1.5 |
| 8 | 1.5 |
| 9 | 1.5 |
| 10 | 1.5 |
| 11 | 1.5 |
| 12 | 1.5 |
| 13 | 1.5 |
| 14 | 1.5 |
| 15 | 1.5 |
</details>

![](image/0aaceacf55cf677466963958b6dd8d88a36197e242a6f31c06e4bd7e48fe88b5.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 0 | 1.5 |
| 2 | 0.5 |
| 4 | -0.3 |
| 6 | 0.0 |
| 8 | 0.0 |
</details>

图 14.11 当 $\delta_{1}=\pi/2$ 时, 具有积分作用的连续滑模控制
