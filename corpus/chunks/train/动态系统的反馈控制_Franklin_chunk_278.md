# 例 5.11 超前补偿设计

为对象 $G(s)=1/[s(s+1)]$ 设计补偿控制器，要求超调不大于 20%，上升时间不超过 0.3s。

解答。根据第3章的内容，我们估计阻尼比 $\zeta \geqslant 0.5$ ，自然频率 $\omega_{\mathrm{n}} \approx \frac{1.8}{0.3} \mathrm{rad/s} \approx 6 \mathrm{rad/s}$ 可以满足设计要求。为了提供一些裕度，让 $\zeta \geqslant 0.5$ 和 $\omega_{\mathrm{n}} \geqslant 7 \mathrm{rad/s}$ ，根据图5.23中的根轨迹，我们首先尝试

$$D _ {\mathrm{c}} (s) = K \frac {s + 2}{s + 1 0}$$

图 5.24 表明，K=70 对应 $\zeta=0.56,\omega_{n}=7.7rad/s$ ，满足最初所估计的设计目标。K=70 时，对应的第三个极点位于 s=-2.4 处。由于这个极点与超前零点-2 非常接近，超调不会比二阶系统的情况增加很多。然而，图 5.25 显示系统的阶跃响应略微超过了要求值。通常，前向通道中的超前补偿会增大阶跃响应的超调，因为零点补偿具有微分作用，正如第 3 章所讨论的。上升时间指标已经满足，因为幅值从 0.1 上升到 0.9 的时间少于 0.3s。

![](image/96d53eda7cfecc9a46c32ac5947d0f0ff677376ee7e024e3ee648bea6edb682f.jpg)

<details>
<summary>line</summary>

| 实轴 | 虚轴 |
| --- | --- |
| -4 | 70 |
| -10 | 7 |
| -2 | 0 |
| 0 | 0 |
</details>

图 5.24 超前设计的根轨迹

我们希望通过调整补偿器来获得更好的阻尼比，从而减小暂态响应的超调。有效的方法就是利用 rltool，其语句如下。

$$
\begin{array}{l} s = t f \left(^ {\prime} s ^ {\prime}\right); \\ \operatorname{sysG} = 1 / \left(s ^ {*} (s + 1)\right); \\ \mathrm{sysD} = (s + 2) / (s + 1 0); \\ \operatorname{rltool} (\text {sysG}, \text {sysD}) \\ \end{array}
$$

通过进一步向左移动超前补偿的极点，向左拖动根轨迹并选择 K=91，我们得到

$$D _ {c} (s) = 9 1 \frac {(s + 2)}{(s + 1 3)}$$

这比之前的设计迭代具有更大的阻尼比。图 5.26 显示的根轨迹为 rltool 绘制的根轨迹以及 s 平面的区域的叠加图。由 rltool 得到的暂态响应如图 5.27 所示，该图说明已经达到了超调的设计要求(其实比设计要求还低一点)即 $M_{p}=17\%$ ，上升时间比之前的设计要差一些，但仍然满足0.3s的指标。

![](image/bd3dfe02226d7511ac904491e2548829cc26780855b771b5f83ef550387e4b77.jpg)

<details>
<summary>line</summary>

| 时间/s | 幅值 |
| --- | --- |
| 0.0 | 0.0 |
| 0.3 | 1.2 |
| 0.6 | 1.1 |
| 0.9 | 1.0 |
| 1.2 | 1.0 |
| 1.5 | 1.0 |
| 1.8 | 1.0 |
</details>

图5.25 例5.11的阶跃响应

![](image/bb69dc270e1115ec66c2d384fddbd8697af22afd011cc6279f2b71f25d7507f7.jpg)

<details>
<summary>radar</summary>
