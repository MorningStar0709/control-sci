# (1) 具有死区特性的非线性控制系统

设系统结构如图 8-28 所示, 系统初始状态为零, 输入 $r(t)=R \cdot 1(t)$ 。

根据图 8-28, 可列写系统的微分方程

$$
T \dot {c} (t) + \dot {c} (t) = K m (t)
m (t) = \left\{ \begin{array}{l l} k [ e (t) + \Delta ], & e (t) \leqslant - \Delta \\ 0, & | e (t) | <   \Delta \\ k [ e (t) - \Delta ], & e (t) \geqslant \Delta \end{array} \right. \tag {8-40}
e (t) = r (t) - c (t)
$$

![](image/09f8893ef93f292ef764bcab642a257d613c57d460005ec2e7e2550628c1b0a3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> +
    + --> e --> |k| Δ0
    Δ0 --> m --> K/(s(Ts+1)) --> c
    c --> -
    - --> +
    + --> -
    - --> -
    - --> -
```
</details>

图 8-28 具有死区特性的非线性系统

为便于分析,取 $e(t)$ , $\dot{e}(t)$ 作为状态变量,并按特性曲线分区域列写微分方程式

区域 I: $T\ddot{e} + \dot{e} + Kke = T\ddot{r} + \dot{r} - Kk\Delta$ ,

$$e \leqslant - \Delta$$

区域 II: $T\ddot{e} + \dot{e} = T\ddot{r} + \dot{r}$ ,

$$| e | < \Delta \tag {8-41}$$

区域 III: $T\ddot{e} + \dot{e} + Kke = T\ddot{r} + \dot{r} + Kk\Delta,$

$$e \geqslant \Delta$$

显然， $e = -\Delta$ 和 $e = \Delta$ 为死区特性的转折点，亦为相平面的开关线。代入 $r(t)$ 形式，因为 $\ddot{r} (t) = \dot{r} (t) = 0$ ，整理得

区域I： $T(e + \Delta)'' + (e + \Delta)' + Kk(e + \Delta) = 0,$

$$e \leqslant - \Delta$$

区域 II: $T\ddot{e} + \dot{e} = 0$ ,

$$| e | < \Delta \tag {8-42}$$

区域 III: $T(e - \Delta)'' + (e - \Delta)' + Kk(e - \Delta) = 0$

$$e \geqslant \Delta$$

若给定参数 T=1, Kk=1，根据线性系统相轨迹分析结果，可得奇点类型

区域 I: 奇点 $(-\Delta,0)$ 为稳定焦点, 相轨迹为向心螺旋线 $(\zeta=0.5)$ ;

区域 II：奇点为 $(x,0)$ ， $x\in(-\Delta,\Delta)$ ，相轨迹沿直线收敛；

区域 III: 奇点 $(\Delta,0)$ 为稳定焦点，相轨迹为向心螺旋线 $(\zeta=0.5)$ 。

由零初始条件 $c(0) = 0, \dot{c}(0) = 0$ 和 $r(t) = R \cdot 1(t)$ ，得 $e(0) = r(0) - c(0) = R, \dot{e}(0) = 0$ 。根据区域奇点类型及对应的运动形式,作相轨迹如图 8-29 实线所示。

由图 8-29 可知, 各区域的相轨迹运动形式由该区域的线性微分方程的奇点类型决定, 相轨迹在开关线上改变运动形式, 系统存在稳态误差, 而稳态误差的大小取决于系统参数, 亦与输入和初始条件有关。若用比例环节 k=1 代替死区特性, 即无死区影响时, 线性二阶系统的相轨迹如图 8-29 中虚线所示。由此亦可以比较死区特性对系统运动的影响。

![](image/fbeacaf3c8dca794def6faafdeac8112b1d1a333a162da212b4154a7ed86e11b.jpg)

<details>
<summary>text_image</summary>

I
II
ē
III
-Δ
0
Δ
R
e
</details>

图 8-29 具有死区特性的非线性系统相轨迹
