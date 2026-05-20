![](image/388b4193d4aef479422c0f2e8e374f325a56e2c794610213b63e050245fdb9d2.jpg)

<details>
<summary>line</summary>

| 实轴 | 虚轴 |
| --- | --- |
| -4 | 4 |
| 0 | 0 |
| -4 | -4 |
</details>

图5.5 规则2实轴上的部分根轨迹在奇数个零极点的左侧

$$s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n} + K \left(s ^ {m} + b _ {1} s ^ {m - 1} + \dots + b _ {m}\right) \tag {5.27}= (s - r _ {1}) (s - r _ {2}) \dots (s - r _ {n}) = 0$$

注意，根的和是 $s^{n - 1}$ 项系数的相反数，若 $m < n - 1$ ，则此和与 $K$ 无关，因此，如果 $L(s)$ 中极点个数至少比零点个数多2个，则有 $a_1 = -\sum r_i$ 。由此说明，如果 $m < n - 1$ ，则根的中心点不随 $K$ 变化而变化，且开环极点与闭环极点的和相等，都是 $-a_1$ ，可表示为

$$- \sum r _ {i} = - \sum p _ {i} \tag {5.28}$$

对于很大的 $K$ 值，可以发现 $m$ 个根 $r_i$ 接近零点 $z_i$ ， $n - m$ 个根接近渐近系统 $\frac{1}{(s - \alpha)^{n - m}}$ 的分支，其中渐近系统的极点的和为 $(n - m)\alpha$ 。综上所知，所有根之和等于趋向于无穷大的根之和加上趋向于 $L(s)$ 零点的根之和，即

$$- \sum r _ {i} = - (n - m) \alpha - \sum z _ {i} = - \sum p _ {i}$$

解出 $\alpha$ ，得

$$\alpha = \frac {\sum p _ {i} - \sum z _ {i}}{n - m} \tag {5.29}$$

注意，既然复数零极点总是以共轭复数对的形式出现的，所以在 $\sum p_i$ 和 $\sum z_i$ 中虚部之和总是为零。因此，式(5.29)只需要实部信息，由式(5.20)，可得

$$\alpha = \frac {- 4 - 4 + 0}{3 - 0} = - \frac {8}{3} = - 2. 6 7$$

在图 5.6 中， $\pm60^{\circ}$ 渐近线由虚线表示，该渐近线与虚轴相交于点 $\pm2.67j\times\sqrt{3}=\pm4.62j$ 。180°渐近线可由规则 2 在实轴上绘出。

规则 4 根轨迹中，单个极点出射角可表示为

$$\phi_ {\mathrm{dep}} = \sum \psi_ {i} - \sum_ {i \neq \mathrm{dep}} \phi_ {i} - 1 8 0 ^ {\circ} \tag {5.30}$$

其中： $\sum\phi_{i}$ 为其他极点到该极点所对应相角的和， $\sum\psi_{i}$ 为所有零点到该极点所对应相角的和。对于 q 重极点，出射角可表示为

$$q \phi_ {l, \mathrm{dep}} = \sum \psi_ {i} - \sum_ {i \neq l, \mathrm{dep}} \phi_ {i} - 1 8 0 ^ {\circ} - 3 6 0 ^ {\circ} (l - 1) \tag {5.31}$$

![](image/a3a9c5dcbc5cf3b07789f8b13f1ec7b5cb33b6b532de00c5e560bdd86e6157c9.jpg)

<details>
<summary>scatter</summary>

| 实轴 | 虚轴 |
| --- | --- |
| -4 | 4 |
| -4 | -4 |
| 0 | 0 |
</details>

图5.6 在 $a$ 处向外辐射的 $n - m$ 条渐近线

其中：l 是整数，取值为 1, 2, …, q。

注意，如果有 q 重极点，则根轨迹有起始于极点的 q 个分支。

同理，系统有 $q$ 重零点时，入射角表示为

$$q \psi_ {l, \text {arr}} = \sum \phi_ {i} - \sum_ {i \neq l, \text {arr}} \psi_ {i} + 1 8 0 ^ {\circ} + 3 6 0 ^ {\circ} (l - 1) \tag {5.32}$$

其中： $\sum\phi_{i}$ 为所有极点到该零点所对应相角的和； $\sum\psi_{i}$ 为其他零点到该零点所对应相角的和，并且 l 取值为 1, 2, …, q 根轨迹的 q 个分支终止于这些零点。
