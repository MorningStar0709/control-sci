# 例 5.13 飞机的负根轨迹

绘制如下方程的负根轨迹：

$$1 + K \frac {s - 6}{s (s ^ {2} + 4 s + 1 3)} = 0 \tag {5.84}$$

解答。

规则 1 共有三条根轨迹分支和两条渐近线。

规则 2 实轴上的根轨迹是 s=6 的右侧部分和 s=0 的左侧部分。

规则 3 渐近线的角度是 $\phi_{l}=\frac{(l-1)360^{\circ}}{2}=0^{\circ}$ ， $180^{\circ}$ 渐近线的中心在 $\alpha=\frac{-2-2-(6)}{3-1}=-5$ 。

规则 4 始于极点 $s = -2 + j3$ 根轨迹的出射角为

$$
\begin{array}{l} \phi = \arctan \left(\frac {3}{- 8}\right) - \arctan \left(\frac {3}{- 2}\right) - 9 0 ^ {\circ} + 3 6 0 ^ {\circ} (l - 1) \\ \phi = 1 5 9. 4 ^ {\circ} - 1 2 3. 7 ^ {\circ} - 9 0 ^ {\circ} + 3 6 0 ^ {\circ} (l - 1) \\ \phi = - 5 4. 3 ^ {\circ} \\ \end{array}
$$

用 Matlab 绘制的根轨迹如图 5.39 所示，与绘制规则所得的结果一致。

![](image/20b93cff6713b895805ea0bedc547ea6a4d4787663f819f48e19b9f2d37a96d4.jpg)

<details>
<summary>scatter</summary>

| 实轴 | 虚轴 |
| --- | --- |
| -2 | 3 |
| 0 | 0 |
| 6 | 0 |
| 10 | 0 |
| -3 | -3 |
| 0 | -4 |
</details>

图 5.39 $L(s)=(s-6)/s(s^{2}+4s+13)$ 的负根轨迹
