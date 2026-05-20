$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, 0. 0 1) \\ z _ {1} = z _ {1} + h (z _ {2} - 1 0 0 e) \\ z _ {2} = z _ {2} - h 2 0 0 \mathrm{fe} \end{array} \right. \tag {4.1.21}
$$

用这个递推公式,取采样周期 h = 0.01 来进行状态估计的结果如图4.1.2所示. 图4.1.2中原系统的状态和状态观测器给出的估计值几乎完全重合,看不出其差别.

例 2 对系统

$$
\left\{ \begin{array}{l l} x _ {1} = x _ {2}, & x _ {1} (0) = 0. 3 \\ x _ {2} = - x _ {1} - 0. 2 5 x _ {2} \left(1. 5 - x _ {1} ^ {2}\right) + \sin \left(\frac {t}{2}\right), & x _ {2} (0) = 0 \\ y = x _ {1} \end{array} \right. \tag {4.1.22}
$$

![](image/9690be0d079af0952c74d3211d51588f0fc22d838ce83e544dfc818780877326.jpg)

<details>
<summary>line</summary>

| x | y = x₁, z₁ |
| --- | --- |
| 0 | 0 |
| 5 | 0.5 |
| 10 | 0.8 |
| 15 | 2.5 |
| 20 | 0 |
</details>

![](image/9c28742bf24496180bc5ee3d5ef9971797d5fab6b485d140fb2a49c90d507a99.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 5 | -0.5 |
| 10 | 0.5 |
| 15 | 2.0 |
| 20 | 0.0 |
</details>

图4.1.2

就用上面给出的状态观测器(4.1.12)进行估计的仿真结果如图4.1.3(最右图为相平面图)，同样估计的很好.

![](image/4db3c951184cb9ada8f2d56b7a8568b857f72bc8225d494c228a95811a118a5c.jpg)

<details>
<summary>line</summary>

| x | y=x₁,z₁ |
| --- | --- |
| 0 | 0.5 |
| 5 | -1.5 |
| 10 | 0.5 |
| 15 | -1.5 |
| 20 | 0.0 |
</details>

![](image/5dc232c9993b9b1f1cc4fc8975298d3a4d3696a844e7d98e3246a0dd2f2ccfac.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.3 |
| 5 | -0.8 |
| 10 | 1.2 |
| 15 | -0.6 |
| 20 | 0.4 |
</details>

![](image/a689d3a60af171aca01fa0899b7db0db29abd68f0259e4ab0dc5c5b7fadb3ae2.jpg)

<details>
<summary>contour</summary>

| x | y |
| --- | --- |
| -1.5 | 0.0 |
| -1.0 | 0.5 |
| -0.5 | 1.0 |
| 0.0 | 1.5 |
| 0.5 | 1.0 |
| 1.0 | 0.5 |
| 1.5 | 0.0 |
</details>

图4.1.3

从这两个例子看,状态观测器(4.1.12)对一定范围的对象来说是完全通用的.这是因为状态观测器(4.1.12)的设计是与对象中的函数无关,而其估计效率之高是由于采用了合适的非光滑函数.

这种形式的非线性状态观测器是可以推广到任意阶系统上.如对系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \vdots \\ \dot {x} _ {n - 1} = x _ {n} \\ \dot {x} _ {n} = f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) + b u \\ y = x _ {1} \end{array} \right. \tag {4.1.23}
$$

可以建立如下状态观测器
