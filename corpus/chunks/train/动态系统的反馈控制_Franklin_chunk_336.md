# 例6.10 开环不稳定系统的奈奎斯特图

第三个例子是定义在图 6.28 中的。利用奈奎斯特判据判断它的稳定性。

解答。这个系统当 K>1 时的根轨迹画在图 6.29 中。因为开环系统在右半平面有一个极点，所以它是不稳定的。开环伯德图如图 6.30 所示。注意 $\left|KG(j\omega)\right|$ 的表现行为与极

![](image/780844b32557130ae5df16a5f6e54f57aa16ad93fe9aa0dd02c9806c466497ec.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum --> K
    K --> Transfer[" transfer function s/(s/10 - 1) "]
    Transfer --> Y
    Y -->|-| Sum
```
</details>

图 6.28 例 6.10 的控制系统

点处于左半平面时的相同。然而， $\angle G(\mathrm{j}\omega)$ 增加 $90^{\circ}$ 而不是像通常那样在极点处减小。任何带有右半平面极点的系统都是不稳定的；因此通过实验的方法来确定它的频率响应是很困难的，这是因为对于正弦输入，系统从来不会达到一个稳态正弦响应。然而根据6.1节的规则来计算传递函数的幅值和相位是可行的。因为式(6.28)中的 $P$ 为 $+1$ ，所以右半平

面的极点影响了奈奎斯特包围判据。

![](image/96e5c515ec1835b15c45fb167bde8cb3382d4f73b5ffadd71504ed17ee89c68a.jpg)

<details>
<summary>text_image</summary>

Im(s)
4
2
-2
-2
-4
-8 -6 -4 2 4 6 8 10 Re(s)
</details>

图 6.29 $G(s)=(s+1)/s[(s/10-1)]$ 的根轨迹

![](image/64b23fb0cbbd850e414d5728224f60a171606b9443671529e20e0aac1700c25b.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 幅值, G | 幅值, dB |
| --- | --- | --- |
| 0.1 | 10 | 20 |
| 1 | 1 | 0 |
| 10 | 0.1 | -20 |
| 100 | 0.01 | -20 |
</details>

a)

![](image/662425055014ea1876ab7eb1cbdfc041f42e48b3e88b3170df370c3b57e54eb5.jpg)

<details>
<summary>line</summary>

| ω (rad/s) | 相位, ∠G |
| --- | --- |
| 0.1 | 90° |
| 1 | 140° |
| 10 | 220° |
| 100 | 270° |
</details>

b)   
图6.30 $G(s) = (s + 1) / s[(s / 10 - 1)]$ 的伯德图

像前几个例子那样，我们将图6.30所示的频率响应信息转化到图6.31a所示的奈奎斯特图中。和之前一样，图6.31b中 $C_1$ 绕过 $s = 0$ 的极点，这在图6.31a中的无穷远处产生了一个大圆弧。这个圆弧穿越负实轴，这是由于右半平面极点导致了 $180^{\circ}$ 的相位改变，如图6.31b所示。

![](image/ef355d8db347874c25ba01c8e50449ce2b3b4e28ee3727cfa965beea8fddf4f2.jpg)

<details>
<summary>text_image</summary>

C
ω>0
ω=±√10
B -1/Ks -1 Re[G(s)]
-1/K1 ω=+∞
ω<0
A
由ω≈0产生的
位于+∞处的圆弧
Im[G(s)]
</details>

a） $\mathrm{G}(\mathrm{s}) = (\mathrm{s} + 1) / [\mathrm{s}(\mathrm{s}/10 - 1)]$ 的奈奎斯特图 $^{-}$

![](image/fcbf1f94671526b7c0c8e1698869db2ab7428f5b80cd5e04eb3c948c6effb7b0.jpg)

<details>
<summary>text_image</summary>

Im(s)
C₁
C
~180°
B
A
Re(s)
</details>

b）闭合曲线 $C_{1}$   
图6.31 例6.10

实轴穿越出现在 $|G(s)| = 1$ 处，这是因为在伯德图中，当 $\angle G(s) = 180^{\circ}$ 时， $|G(s)| = 1$ ，这发生于 $\omega \approx 3\mathrm{rad / s}$ 处。
