![](image/ab3c7bfd0c574b270cb4abbafeab5c0e40d1df3450245e52d6c628ce767f4f44.jpg)

<details>
<summary>line</summary>

| k=5 | x₁ |
| --- | --- |
| 0 | 1.0 |
| 5 | 0.1 |
| 10 | 0.05 |
| 15 | 0.02 |
| 20 | 0.01 |
</details>

![](image/cf5956c2da872afeb9a5fb5df35e426005fe61aa0c31f6d56db63fbbf4590a4b.jpg)

<details>
<summary>line</summary>

| k | x₁ |
| --- | --- |
| 0 | 1.0 |
| 10 | 0.0 |
| 20 | 0.0 |
</details>

![](image/87cdee2eefef8e298623a84c4f9f8c9e4ff6d5f233f8b0baeab139ff9e8ef4be.jpg)

<details>
<summary>line</summary>

| k | Value |
| --- | --- |
| 0 | 1.0 |
| 10 | 0.1 |
| 20 | 0.0 |
</details>

图3.2.4

比较图3.2.3和图3.2.4中明显看出同样增益 $k$ 的反馈作用之下，线性反馈和非线性反馈抑制扰动的不同效果

下面比较线性和非线性 PD 反馈的一些几何性质.

线性 PD 反馈: $u = -\beta_{1}e_{1} - \beta_{2}e_{2}$ (3.2.32)

![](image/a88115cc41aa6ce37919dbabee4a40baa99e31224a2c6f377a6215dc906e23bf.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2.0 | 1.5 |
| -1.5 | 1.0 |
| -1.0 | 0.5 |
| -0.5 | 0.0 |
| 0.0 | -0.5 |
| 0.5 | -1.0 |
| 1.0 | -1.5 |
| 1.5 | -2.0 |
| 2.0 | -2.5 |
</details>

图3.2.5

这是以 $k = -\frac{\beta_{1}}{\beta_{2}}$ 为斜率过原点的直线 $L: e_{2} = -\frac{\beta_{1}}{\beta_{2}} e_{1}$ 作为分界线，右上方取 u < 0，左下方取 u > 0 的控制律（图 3.2.5）.

如果取 $u = -r \text{sign}(\beta_{1} e_{1} + \beta_{2} e_{2})$ ，那么这是以 $L: e_{2} = -\frac{\beta_{1}}{\beta_{2}} e_{1}$ 为滑动曲线的变结构控制.

非线性 PD 反馈: $u = -\beta_{1} | e_{1}|^{\alpha} \text{sign}(e_{1}) - \beta_{2} | e_{2}|^{2\alpha} \text{sign}(e_{2})$

(3.2.33)

这里如果记

$$x _ {1} = \left| e _ {1} \right| ^ {\alpha} \operatorname{sign} \left(e _ {1}\right), x _ {2} = \left| e _ {2} \right| ^ {\alpha} \operatorname{sign} \left(e _ {2}\right)$$

那么 $\mathrm{sign}(x_1) = \mathrm{sign}(e_1),\mathrm{sign}(x_2) = \mathrm{sign}(e_2)$ ，因此

$$u = - \beta_ {1} \left| e _ {1} \right| ^ {\alpha} \operatorname{sign} \left(e _ {1}\right) - \beta_ {2} \left| e _ {2} \right| ^ {2 \alpha} \operatorname{sign} \left(e _ {2}\right) = - \beta_ {1} x _ {1} - \beta_ {2} x _ {2} \left| x _ {2} \right| \tag {3.2.34}$$

这是以曲线(图 3.2.6)

$$V: e _ {2} = - \sqrt {\frac {\beta_ {1}}{\beta_ {2}}} | e _ {1} | ^ {0. 5} \operatorname{sign} (e _ {1}) \tag {3.2.35}$$

等价地以曲线 $V: x_{2} = -\sqrt{\frac{\beta_{1}}{\beta_{2}}} |x_{1}|^{0.5}\mathrm{sign}(x_{1})$ 为分界线，右上方取 $u < 0$ ，左下方取 $u > 0$ 的控制律.

![](image/8c1fe902d9de8344f6c6a37fe8a42b8f188eec1a17813993d8338fab125e90db.jpg)

<details>
<summary>line</summary>
