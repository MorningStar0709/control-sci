![](image/b65a0b2cfc8c93f75bc037f869b45e90001fe19230d6b9ff043e50090b669151.jpg)

<details>
<summary>heatmap</summary>

| X\Y | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| -1 | -0.5 | -0.5 | -0.5 | -0.5 | -0.5 | -0.5 | -0.5 | -0.5 |
| -2 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| -3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| 1 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| 2 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| 3 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
The image displays a grayscale heatmap with contour lines indicating local minima or gradients in the underlying data space. No explicit numerical values are labeled on the chart.
</details>

(a)

![](image/df84815d5314f7141a6fc2d92efa21d0b07cdbbcda45e001a697f568f44d0668.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 10 | 52 |
| 20 | 48 |
| 30 | 38 |
| 40 | 28 |
| 50 | 20 |
| 60 | 12 |
</details>

(b)   
图2.4.4

把函数 $u = \mathrm{fhan}(x_1, x_2, r, h)$ 代到系统(2.4.4)中，得

$$
\left\{ \begin{array}{l} \mathrm{fh} = \mathrm{fhan} (x _ {1} (k), x _ {2} (k), r, h) \\ x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h \mathrm{fh} \end{array} \right. \tag {2.4.7}
$$

从非零初值出发,按这个差分方程递推,就能以有限步到达原点并停止不动.

现在用 $x_{1}(k) - v(k)$ 代替方程中的 $x_{1}(k)$ ，就得离散化的跟踪微分器

$$
\left\{ \begin{array}{l} \mathrm{fh} = \mathrm{fhan} (x _ {1} (k) - v (k), x _ {2} (k), r, h) \\ x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h \mathrm{fh} \end{array} \right. \tag {2.4.8}
$$

我们把这个跟踪微分器称做快速离散系统(2.4.7)派生的最速离散跟踪微分器.

图 2.4.5(a) 和图 2.4.5(b) 分别是 v = 1, r = 0.1，而步长分别取 h = 0.1, h = 0.001 时的系统 (2.4.8) 的阶跃响应曲线和放大了的速度曲线.

![](image/34665901a8638080b464c0a7a5efe72dcf0f81b539aee716ba61237c7e4fc82d.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | -0.5 |
| 5 | 0.5 |
| 10 | 1 |
| 15 | 1 |
| 20 | 1.5 |
</details>

![](image/fb497c0f48cedd822a45d0e0071ac10d66f837a31ea403d209cff86e7c8e3733.jpg)

<details>
<summary>line</summary>

| x | y (×10⁻³) |
| --- | --- |
| 6 | 4 |
| 7 | -2 |
| 8 | -4 |
</details>

![](image/6cdc4fea359719804bf1d1f5aba9706025fd39ae4467891f6bf1c5304218e76c.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 5 | 0.5 |
| 10 | 1 |
| 15 | 1.5 |
| 20 | 1.5 |
</details>

![](image/020011e0a7141c104c12e140607688378345abd2d7842ab611111fff598bf015.jpg)

<details>
<summary>bar</summary>

| x | y (×10⁻³) |
| --- | --- |
| 6 | -2 |
| 7 | 0 |
| 8 | 2 |
| 9 | 4 |
| 10 | 6 |
</details>
