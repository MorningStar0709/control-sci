<details>
<summary>line</summary>

| 时间 | S |
| --- | --- |
| 0.00 | -1.5 |
| 0.05 | 0.0 |
| 0.20 | 0.0 |
</details>

图14.4 理想滑模控制

![](image/ab54ca8a2d7ad94dbaed9f394d4644b81073e2b2449fc7cb4fcfa412d27e4324.jpg)

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

![](image/f21a9fa1c4e6ebdfd2e93a166591e0dad98c22703925ccf9b7b46dfc134064e3.jpg)

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

图 14.5 对执行部件动力学特性未建模情形下的滑模控制

下面给出两种能减小或消除抖动的方法。一种方法是将控制分解为连续控制和切换控制两部分，以减小切换部分的幅度。设 $\hat{h}(x)$ 和 $\hat{g}(x)$ 分别为 $h(x)$ 和 $g(x)$ 的标称模型，取

$$u = - \frac {[ a _ {1} x _ {2} + \hat {h} (x) ]}{\hat {g} (x)} + v$$

得 $\dot{s} = a_{1}\left[1 - \frac{g(x)}{\hat{g}(x)}\right]x_{2} + h(x) - \frac{g(x)}{\hat{g}(x)}\hat{h} (x) + g(x)v\stackrel {\mathrm{def}}{=}\delta (x) + g(x)v$

如果扰动项 $\delta (x)$ 满足不等式 $\left|\frac{\delta(x)}{g(x)}\right| \leqslant \varrho (x)$

则可取 $v = -\beta (x)\operatorname {sgn}(s)$

其中 $\beta(x) \geqslant \varrho(x) + \beta_{0}$ 。由于 $\varrho$ 是扰动项的上界，因此它可能比整个函数的上界小，因而切换部分

的幅度较小。例如回到单摆方程，取 $m, \ell$ 和 $k_0$ 的标称值为 $\hat{m} = 0.125, \hat{\ell} = 1, \hat{k}_0 = 0.025$ ，则有

$$\left| \frac {\delta (x)}{g} \right| = \left| \left(a _ {1} m \ell^ {2} - a _ {1} \hat {m} \hat {\ell} ^ {2} - k _ {0} \ell^ {2} + \hat {k} _ {0} \hat {\ell} ^ {2}\right) x _ {2} - g _ {0} (m \ell - \hat {m} \hat {\ell}) \cos x _ {1} \right| \leqslant 1. 8 3$$

其边界值的计算如前所述,修正的滑模控制表示为

$$u = - 0. 1 x _ {2} + 1. 2 2 6 3 \cos x _ {1} - 2 \operatorname{sgn} (s)$$

从中可以看出切换项的幅值由4降为2,图14.6给出了存在未建模执行器件时修正控制的仿真结果,从图中可以看出抖动幅度明显减小。

![](image/92d19f6f68072d9f79d0d8fdb78850075bda617e45567236bd6703723ce24875.jpg)

<details>
<summary>line</summary>

| 时间 | θ |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.2 |
| 4 | 1.5 |
| 6 | 1.55 |
| 8 | 1.55 |
</details>

![](image/da86c886921ae994541552b84bbda44c5a5048fe2629cda6cd018b24e2dac763.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 2.0 | 1.0 |
| 2.05 | -0.5 |
| 2.1 | 2.5 |
| 2.15 | -0.5 |
| 2.2 | 2.5 |
| 2.25 | -0.5 |
| 2.3 | 2.5 |
| 2.35 | -0.5 |
| 2.4 | 2.5 |
</details>

图 14.6 具有未建模执行器件动力学因素的修正滑模控制

消除抖动的第二种办法是用一个陡峭的饱和函数代替符号函数,即控制律取为

$$u = - \beta (x) \text { sat } \left(\frac {s}{\varepsilon}\right)$$

其中 $\mathrm{sat}(\cdot)$ 是饱和函数，定义为
