$$\tilde {V} \geqslant - (g _ {0} / 2 \ell) y _ {1} ^ {2} + (k a _ {1} / 2 m \ell^ {2} \varepsilon) y _ {1} ^ {2} + (1 / 2) y _ {2} ^ {2}$$

是正定的,其导数为 $\dot{\tilde{V}} = -\left(\frac{k_{0}}{m} + \frac{k}{m\ell^{2}\varepsilon}\right)y_{2}^{2}$

根据不变原理可以证明平衡点 $(\bar{x}_{1},0)$ 是渐近稳定的，并且吸引 $\Omega_{\varepsilon}$ 内的每条轨线。

![](image/27fb53423b2ec88b5cb927ca252325ac1a9b4022f5363bea9bcc524fe7fc289a.jpg)

<details>
<summary>text_image</summary>

sgn(y)
1
y
-1
</details>

![](image/f7885c800a666741916e077f4547fdf2b63c40b3fe14ec3cb05db819f213ed97.jpg)

<details>
<summary>line</summary>

| y | sat(y/ε) |
| --- | --- |
| ε | -1 |
| 0 | 0 |
| ε | 1 |
</details>

图 14.7 符号非线性函数及其饱和函数逼近

为了提高精度,应选择尽可能小的 $\varepsilon$ ,但是当有时间延迟或未建模的快速动力学因素时, $\varepsilon$ 太小会引发抖动。图 14.8 所示为当 $\varepsilon$ 取两个不同值时,用于单摆方程的连续滑模控制器性能,图 14.9 所示为有未建模的执行部件 $1/(0.01s+1)^{2}$ 时控制器的性能。从中可以得出重要的观察结果,即在理想情况下减小 $\varepsilon$ 可提高精度,但在有延迟时由于抖动却不会有同样的效果。

一个无须将 $\varepsilon$ 取得太小就可以稳定原点的特例出现在 $h(0)=0$ 时, 此时在边界层内系统表示为

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = h (x) - \left[ \frac {g (x) k}{\varepsilon} \right] \left(a _ {1} x _ {1} + x _ {2}\right)$$

在原点处有一个平衡点。我们需要选择足够小的 $\varepsilon$ ，以稳定原点，并使 $\Omega_{\varepsilon}$ 为吸引区内的一个子集。对单摆方程，取 $\delta_1 = \pi$ ，重复前面的稳定性分析后可确定，当 $k / \varepsilon > mg_0 \ell / a_1$ 时达到了控制目标。当 $\ell \leqslant 1.1, m \leqslant 0.2, k = 4, a_1 = 1$ 时，只要 $\varepsilon < 1.8534$ 即可。图14.10所示为当 $\varepsilon = 1$ 时的仿真结果。

![](image/a457411a87e4f2a1a31c58ded4fda453b802da3dc81bd51576088325c8deb9d9.jpg)

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

![](image/b145b42bc6755f7b4e22e53bda388ac9729600c019863b74cc6713be923573e2.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 0.8 |
| 1.5 | 0.9 |
| 2.0 | 0.95 |
| 2.5 | 1.0 |
</details>

![](image/f50c17a20f74a1b49540ded06a8c566dacc34c1b062a9d36f355d2af0e8ef67a.jpg)

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

![](image/0c619b8d180dc25297baa8842241a45fd76f33472109640db1290da7a1462e5c.jpg)

<details>
<summary>line</summary>

| 时间 | u |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 0.8 |
| 1.5 | 0.9 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
</details>

图 14.8 连续滑模控制

![](image/2fc815fdb7679e229f21a0ffff27463f5bcf1bff2222b447375152c98269e556.jpg)
