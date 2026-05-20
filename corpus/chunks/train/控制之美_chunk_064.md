# 3.3.1 一维相轨迹

首先讨论使用图形化分析一阶微分方程的方法。考虑一个一阶微分方程：

$$\frac {\mathrm{d} z (t)}{\mathrm{d} t} = z ^ {2} (t) - 1 \tag {3.3.1}$$

将其在相平面中绘制出来, 令横轴为状态变量 $z(t)$ , 纵轴为 $\frac{\mathrm{d}z(t)}{\mathrm{d}t}$ 。式(3.3.1)所表达的是一条抛物线, 如图3.3.1所示, 它与横坐标之间存在两个交点, 分别定义为 $z_{\mathrm{f1}}$ 和 $z_{\mathrm{f2}}$ 。当状态变量 $z(t)$ 位于这两个点时, $\left.\frac{\mathrm{d}z(t)}{\mathrm{d}t}\right|_{z(t)=z_{\mathrm{f1}}}=\left.\frac{\mathrm{d}z(t)}{\mathrm{d}t}\right|_{z(t)=z_{\mathrm{f2}}}=0$ , 说明此刻的 $z(t)$ 将不会随时间发生任何改变。因此, 这两个点被称为平衡点 (Equilibrium Point 或者 Fixed Point)。从动态系统的角度考虑, 当状态变量 $z(t)$ 位于平衡点时的动态系统会保持“静止”的状态。

一旦状态变量偏离平衡点之后,动态系统便会“动”起来,此时我们所关心的是系统能否回到静止的状态(平衡点)。首先看图3.3.1(a),假设状态变量 $z(t)$ 在t=0时位于平衡点 $z_{f1}$ 的左边,即 $z(0)=z_{11}$ 。根据图像显示,此时 $\left.\frac{\mathrm{d}z(t)}{\mathrm{d}t}\right|_{z(t)=z_{11}}>0$ ,这说明随着时间的增加,状态变量 $z(t)$ 也会增加。在图中, $z(t)$ 将沿着向右的轨迹移动。而在它移动的过程中, $\frac{\mathrm{d}z(t)}{\mathrm{d}t}$ 始终保持为正值,因此 $z(t)$ 就会一直增加并保持向右移动。直到 $z(t)=z_{\mathrm{f1}}$ 时才会停下来(此时 $\left.\frac{\mathrm{d}z(t)}{\mathrm{d}t}\right|_{z(t)=z_{\mathrm{f1}}}=0$ )。同理,如果t=0时 $z(0)$ 在 $z_{f1}$ 的右边,即 $z(0)=z_{1r}$ ,此时

![](image/372dc1587129f94279fcf51835a99b5341ed89f89f83f09fd7d7223ec8926e72.jpg)

<details>
<summary>text_image</summary>

dz(t)/dt|z(t)=z₁₁ >0
dz(t)/dt
dz(t)/dt=z²(t)-1
z₁₁ z₁₁ z₁₁ O
dz(t)/dt|z(t)=z₁₁ <0
</details>

(a) 初始位置在平衡点 $z_{f1}$ 附近

![](image/de8dae65de68f9e8f519c08291b34b3bb27bf02885978df3694c983bfc1d19ac.jpg)

<details>
<summary>line</summary>

| z(t) | dzt/dt |
| --- | --- |
| 0 | 0 |
| z21 | 0 |
| zf2 | 0.3 |
| z2r | 1.0 |
</details>

(b) 初始位置在平衡点 $z_{f2}$ 附近  
图 3.3.1 一维微分方程图形化分析

$\frac{\mathrm{d}z(t)}{\mathrm{d}t}\bigg|_{z(t)=z_{1r}}<0,z(t)$ 则会随着时间的增加而向左移动（随着时间的增加而减小），直到平衡点 $z_{f1}$ 为止。以上的分析说明，当系统的状态变量 $z(t)$ 小范围偏离平衡点 $z_{f1}$ 后，会自动回到平衡点 $z_{f1}$ 。因此， $z_{f1}$ 被称为稳定平衡点。

用同样的方法分析另一个平衡点 $z_{\mathrm{f2}}$ ，请读者根据图3.3.1(b)自行推导，可以发现，无论 $z(t)$ 的初始位置在 $z_{\mathrm{f2}}$ 的左边还是右边，它的变化趋势都将会是远离 $z_{\mathrm{f2}}$ 。因此， $z_{\mathrm{f2}}$ 被称为系统的不稳定平衡点。即状态变量偏离 $z_{\mathrm{f2}}$ 之后，就无法再自动地回到 $z_{\mathrm{f2}}$ 这个平衡点上。需要注意的是，根据图3.3.1，只有当初始位置 $z(0)$ 在 $z_{\mathrm{f2}}$ 左边，即 $z(0) < z_{\mathrm{f2}}$ 时，状态变量才可以回到平衡点 $z_{\mathrm{f1}}$ 。因此， $z_{\mathrm{f1}}$ 是一个局部(Local)稳定的平衡点。

使用此方法来分析如下非线性微分方程。

例 3.3.1 利用相平面与相轨迹分析 Logistic 人口繁殖模型, 它的微分方程为
