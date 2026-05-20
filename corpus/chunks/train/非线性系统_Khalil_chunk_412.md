<details>
<summary>line</summary>

| 时间 | θ |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.0 |
| 4 | 1.5 |
| 6 | 1.5 |
| 8 | 1.5 |
</details>

![](image/7cac519cc8196d2b02ea2f830f3b4457176ebde43f3f2609ee0291878424f41c.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 0 | -3.0 |
| 1 | 0.5 |
| 2 | 1.0 |
| 3 | 1.0 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
</details>

![](image/01f98cf6aed93e116e9e7994d74a8441538cce8c5692d918a017405d2af47636.jpg)

<details>
<summary>line</summary>

| 时间 | θ |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.2 |
| 4 | 1.4 |
| 6 | 1.5 |
| 8 | 1.5 |
</details>

![](image/966019c095d8fff2012f6b95e2e94d2974ec8a9751a6c2e084e8b65566a2161a.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 2.0 | -2.0 |
| 2.05 | 3.5 |
| 2.1 | -2.0 |
| 2.15 | 3.5 |
| 2.2 | -2.0 |
| 2.25 | 3.5 |
| 2.3 | -2.0 |
| 2.35 | 3.5 |
| 2.4 | -2.0 |
</details>

图 14.9 具有未建模执行部件动力学因素的连续滑模控制

如果 $\delta_{1}$ 为0或 $\pi$ （开环平衡点）之外的任意角度，那么系统将在原点以外的一个平衡点稳定。这会导致一个稳态误差，它早先是用 $(\varepsilon mg_0\ell /ka_1)\sin \delta_1$ 进行逼近的。通过积分作用仍可以使稳态误差为0。设 $x_0 = \int x_1$ ，则增广系统（augmented system）为

$$\dot {x} _ {0} = x _ {1}\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - \left(g _ {0} / \ell\right) \sin \left(x _ {1} + \delta_ {1}\right) - \left(k _ {0} / m\right) x _ {2} + \left(1 / m \ell^ {2}\right) u$$

取 $s = a_0x_0 + a_1x_1 + x_2$ ，其中矩阵

$$
A _ {0} = \left[ \begin{array}{c c} 0 & 1 \\ - a _ {0} & - a _ {1} \end{array} \right]
$$

为赫尔维茨矩阵。在感兴趣的区域里,如果

$$m \ell^ {2} \left| a _ {0} x _ {1} + a _ {1} x _ {2} - (g _ {0} / \ell) \sin (x _ {1} + \delta_ {1}) - (k _ {0} / m) x _ {2} \right| \leqslant k _ {1}$$

则可取连续滑模控制为 $u = -k\mathrm{sat}\left(\frac{s}{\varepsilon}\right),\quad k > k_{1}$

上式可保证 s 在有限时间内到达边界层 $\{|s| \leqslant \varepsilon\}$ ，这是由于

$$s \dot {s} \leqslant - (k - k _ {1}) | s |, \quad | s | \geqslant \varepsilon$$

在边界层内,系统可表示为

$$
\dot {\eta} = A _ {0} \eta + B _ {0} s, \text {其中} \eta = \left[ \begin{array}{l} {{x _ {0}}} \\ {{x _ {1}}} \end{array} \right], B _ {0} = \left[ \begin{array}{l} {{0}} \\ {{1}} \end{array} \right]
$$

取 $V_{1} = \eta^{\mathrm{T}}P_{0}\eta$ ，这里 $P_0$ 为李雅普诺夫方程 $P_0A_0 + A_0P_0 = -I$ 的解，可以验证

$$\dot {V} _ {1} = - \eta^ {\mathrm{T}} \eta + 2 \eta^ {\mathrm{T}} P _ {0} B _ {0} s \leqslant - (1 - \theta_ {1}) \| \eta \| _ {2} ^ {2}, \forall \| \eta \| _ {2} \geqslant 2 \| P _ {0} B _ {0} \| _ {2} \varepsilon / \theta_ {1}$$

其中 $0 < \theta_{1} < 1$ 。因此所有轨线在有限时间内到达集合
