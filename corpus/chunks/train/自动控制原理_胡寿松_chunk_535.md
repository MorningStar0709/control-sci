$$\frac {\dot {c} ^ {2}}{\dot {c} _ {0} ^ {2} + \omega_ {n} ^ {2} c _ {0} ^ {2}} + \frac {\omega_ {n} ^ {2} c ^ {2}}{\dot {c} _ {0} ^ {2} + \omega_ {n} ^ {2} c _ {0} ^ {2}} = 1 \tag {8-37}$$

显然，上式为相平面的椭圆方程。系统的相平面图为围绕坐标原点的一簇椭圆，如图8-21所示。椭圆的横轴和纵轴由初始条件给出。

系统的相平面图 ⑤ $-1 < \zeta < 0$ 。系统特征根为一对具有正实部的共轭复根，系统自由运动呈发散振荡形式。取 $\zeta = -0.5, \omega_n = 1$ 时，系统相轨迹如图8-22所示，为离心螺旋线，最终发散至无穷。

![](image/341cb646106fc2dff130eb6d1f8d5301fea28be65a9cb817edd3249aca353b38.jpg)

<details>
<summary>text_image</summary>

ċ
0
c
</details>

图 8-21 $\zeta=0$ 时线性二阶系统的相平面图

![](image/2df209f2b504afad08349760912aae86feb69070200c7e8546dd52ad4c0350f7.jpg)

<details>
<summary>scatter</summary>

| Point | c | y |
| --- | --- | --- |
| A | 0 | 0 |
| B | 10 | -10 |
</details>

图 8-22 $\zeta=-0.5,\omega_{n}=1$ 时线性二阶系统相平面图(MATLAB)

⑥ $\zeta \leqslant -1$ 。 $\zeta < -1$ 时系统特征根为两个正实根， $s_1 = |\zeta| \omega_n + \omega_n \sqrt{\zeta^2 - 1}$ ， $s_2 = |\zeta| \omega_n - \omega_n \sqrt{\zeta^2 - 1}$ 。系统自由运动呈非振荡发散，系统相平面图见图8-23。如图所示，存在两条特殊的等倾线 $\dot{c} = s_1 c$ 和 $\dot{c} = s_2 c$ 。当初始点落在这两条直线上，则相轨迹沿该直线趋于无穷；当初始点位于其余位置时，相轨迹发散至无穷远处，相轨迹曲线的形式与 $\zeta > 1$ 的情况相同，只是运动方向相反。

当 $\zeta = -1$ 时，系统特征根为两个相同的正实根，存在一条特殊的等倾线。系统相轨迹发散，相平面图如图8-24所示。

![](image/d373186b3db26d585fcf66eb45925f83f68b66e2ebca0fac854f6e9234b0c643.jpg)

<details>
<summary>line</summary>

| c | σ |
| --- | --- |
| -30 | -30 |
| -20 | -20 |
| 0 | 0 |
| 20 | 20 |
| 30 | 30 |
</details>

图 8-23 $\zeta<-1$ 时线性二阶系统相平面图(MATLAB)

![](image/4b9400b75bd914154a23b7eec2d2704c572a3e3164c421ef9375ce6edb509e42.jpg)

<details>
<summary>text_image</summary>

c
ẋ₀
0
x₀
c
</details>

图8-24 $\zeta = -1$ 时线性二阶系统的相平面图

应当指出,二阶系统的相轨迹可应用 MATLAB 软件包,运行相应的 M 文本,在相平面上精确绘制,并可方便地给出相应的时间响应曲线,便于对比分析。
