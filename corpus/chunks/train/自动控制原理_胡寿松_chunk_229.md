# 2. 附加开环零点的作用

在控制系统设计中,我们常用附加位置适当的开环零点的方法来改善系统性能。因此,研究

开环零点变化时的根轨迹变化,有很大的实际意义。

设系统开环传递函数为

$$G (s) H (s) = \frac {K ^ {*} (s - z _ {1})}{s (s ^ {2} + 2 s + 2)} \tag {4-35}$$

式中， $z_{1}$ 为附加的开环实数零点，其值可在 $s$ 左半平面内任意选择。当 $z_{1} \to \infty$ 时，表示有限零点 $z_{1}$ 不存在的情况。

令 $z_{1}$ 为不同数值，对应于式(4-35)的闭环系统根轨迹如图4-17所示。由图可见，当开环极点位置不变，而在系统中附加开环负实数零点时，可使系统根轨迹向 $s$ 左半平面方向弯曲，或者说，附加开环负实数零点，将使系统的根轨迹图发生趋向附加零点方向的变形，而且这种影响将随开环零点接近坐标原点的程度而加强。如果附加的开环零点不是负实数零点，而是具有负实部的共轭零点，那么它们的作用与负实数零点的作用完全相同。此外，根据图4-17，利用劳斯判据的方法不难证明，当 $z_{1} < -2$ 时，系统的根轨迹与虚轴存在交点；而当 $z_{1} \geqslant -2$ 时，系统的根轨迹与虚轴不存在交点。因此，在 $s$ 左半平面内的适当位置上附加开环零点，可以显著改善系统的稳定性。

![](image/a9ae066927b7996449980f2208894c3d6728ed721f9d5a75eeffcaa72c007720.jpg)

<details>
<summary>line</summary>

| Point Label | Real Axis | Imaginary Axis |
| --- | --- | --- |
| -1+j | -1 | -1 |
| -1-j | -1 | -1 |
| 60° | -1 | 0 |
| 60° | 0 | 60° |
</details>

(a) $z_{1}\rightarrow \infty$

![](image/ba96ba5d2ddf788f3b84b06349341a39568cffdc8baae3e87164f285f2d7d542.jpg)

<details>
<summary>line</summary>

| Point Label | Real Axis (°) | Imaginary Axis (°) |
| --- | --- | --- |
| -1+j | ~0 | ~1 |
| -1-j | ~0 | ~-1 |
| 90° | 90 | 1 |
</details>

(b) $z_{1} = -3$

![](image/ae4ef5a41561c43c2a68bdb8b175b238216cc14adbee2927dc71dc656155ffc2.jpg)

<details>
<summary>line</summary>

| Point Label | Real Axis Start | Real Axis End | Imaginary Axis Start | Imaginary Axis End |
| --- | --- | --- | --- | --- |
| -1+j | 0 | 0 | -1+j | -1-j |
| -1-j | 0 | 0 | -1-j | -1-j |
</details>

(c) $z_{1} = -2$

![](image/af3f5a08edb677dd3ca5b2718f9ef2a4c3efff064ccfacb17a37524da1f85b34.jpg)

<details>
<summary>geo</summary>

Pole Zero Map
| Real Axis | Imaginary Axis | Pole Zero Index |
| --- | --- | --- |
| -1+j | -1+j | -1 |
| -1-j | -1-j | -1 |
</details>

(d) $z_{1} = 0$   
图4-17 $z_{1}$ 为不同数值的根轨迹图
