在一些复杂的非线性控制系统中,有可能出现两个或两个以上的极限环,图 8-26 是有两个极限环的例子,里面的一个是不稳定的极限环;外边的一个是稳定的极限环,这时非线性系统的工作状态,不仅取决于初始条件,也取决于扰动的方向和大小。应该指出,只有稳定的极限环才能在实验中观察到,不稳定或半稳定的极限环是无法在实验中观察到的。

例 8-2 已知非线性系统的微分方程为

$$\ddot {x} + 0. 5 \dot {x} + 2 x + x ^ {2} = 0 \tag {8-39}$$

试求系统的奇点，并绘制系统的相平面图。

解 系统相轨迹微分方程为

$$\frac {\mathrm{d} \dot {x}}{\mathrm{d} x} = \frac {- (0 . 5 \dot {x} + 2 x + x ^ {2})}{\dot {x}}$$

令 $\frac{\mathrm{d}\dot{x}}{\mathrm{d}x} = \frac{0}{0}$ ，则求得系统的两个奇点

$$
\left\{ \begin{array}{l} x _ {1} = 0 \\ \dot {x} _ {1} = 0 \end{array} , \right. \quad \left\{ \begin{array}{l} x _ {2} = - 2 \\ \dot {x} _ {2} = 0 \end{array} \right.
$$

为确定奇点类型,需计算各奇点处的一阶偏导数及增量线性化方程。

![](image/1f937d5b29b4cd5847ab4eb9f622e4f61e1d12c6cd84d15eba824a6b42662319.jpg)

<details>
<summary>text_image</summary>

稳定极限环
不稳定极限环
</details>

图8-26 双极限环

奇点(0,0)处

$$
\left. \frac {\partial f (x , \dot {x})}{\partial x} \right| _ {\substack {x = 0 \\ \dot {x} = 0}} = - 2, \quad \left. \frac {\partial f (x , \dot {x})}{\partial \dot {x}} \right| _ {\substack {x = 0 \\ \dot {x} = 0}} = - 0.5
\Delta \ddot {x} + 0. 5 \Delta \dot {x} + 2 \Delta x = 0
$$

特征根为 $s_{1,2}=-0.25\pm j1.39$ ，故奇点 $(0,0)$ 为稳定焦点。

奇点 $(-2,0)$ 处

$$
\left. \frac {\partial f (x , \dot {x})}{\partial x} \right| _ {\substack {x = - 2 \\ \dot {x} = 0}} = 2, \quad \left. \frac {\partial f (x , \dot {x})}{\partial \dot {x}} \right| _ {\substack {x = - 2 \\ \dot {x} = 0}} = - 0.5
\Delta \ddot {x} + 0. 5 \Delta \dot {x} - 2 \Delta x = 0
$$

特征根为 $s_{1}=1.19, s_{2}=-1.69$ ，故奇点 $(-2,0)$ 为鞍点。

根据奇点的位置和奇点类型,应用 MATLAB 方法,可以获得系统的相平面图,如图 8-27 所示。图中相交于鞍点 $(-2,0)$ 的两条相轨迹为奇线,将相平面划分为两个区域,相平面图中阴影线内区域为系统的稳定区域,阴影线外区域为系统的不稳定区域。凡初始条件位于阴影线内区域时,系统的运动均收敛至原点;凡初始条件位于阴影线外区域时,系统的运动发散至无穷大。该例说明,非线性系统的运动及其稳定性与初始条件有关。

![](image/1510bb73e01bf36ba3eabf6987f65a0fb392d0d06264b609231daf4fce8ca741.jpg)

<details>
<summary>other</summary>

| x | y |
| --- | --- |
| -8 | -10 |
| -6 | -8 |
| -4 | -6 |
| -2 | -4 |
| 0 | -2 |
| 2 | 0 |
| 4 | 2 |
| 6 | 4 |
| 8 | 6 |
</details>

图 8-27 例 8-2 系统相平面图 (MATLAB)
