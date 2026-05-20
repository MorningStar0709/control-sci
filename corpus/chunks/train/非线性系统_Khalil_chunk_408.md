这样 $|x_{1}(0)|\leqslant \frac{c}{a_{1}}\Rightarrow |x_{1}(t)|\leqslant \frac{c}{a_{1}},\forall t\geqslant 0$

集合 $\Omega = \left\{|x_1| \leqslant \frac{c}{a_1}, |s| \leqslant c\right\}$

在满足 $\left|\frac{a_{1}x_{2}+h(x)}{g(x)}\right|\leqslant k_{1},\quad\forall x\in\Omega$

时为正不变集,如图14.2所示,且每条始于 $\Omega$ 的轨线都随t趋于无穷而趋于原点。通过选择足够大的c,可使平面上的任一紧集都成为 $\Omega$ 的子集,因此如果k任意大,则上述控制律可达到半全局稳定。

由于实际系统中开关器件及继电器的非理想性,使滑模控制常常出现抖动,图14.3所示为延迟引起抖动的示意图。图中在区域s>0的轨线,向滑动流形s=0运动,在点a首次到达流形。在理想滑模控制中,轨线由a点出发沿流形滑动。在实际情况下,在s符号变化时刻与控制切换时刻之间会存在一个延迟。在延迟期间,轨线越过流形进入到s<0的区域。当控制切换时,轨线又调转方向,再次向流形方向运动并越过流形。如此反复,产生了如图所示的“之”字形的运动(振荡),这就是抖动。抖动会导致控制精度的降低,功率电路的热消耗和机械运动部件的磨损,还可能激励未建模的高频动力学系统,因而降低系统性能,甚至会导致系统不稳定。

![](image/43371ebe927003fdb62175a8d177473a483639efe897b4e3a50b0236d16127ea.jpg)

<details>
<summary>text_image</summary>

s = 0
x₂
c
c/a₁
x₁
</details>

图 14.2 吸引区的估计

![](image/19a11c77557898c951c7c40432ef461e758633c2302e78e07b5b0a834a3bd27e.jpg)

<details>
<summary>text_image</summary>

滑动流形
s < 0
s > 0
a
</details>

图 14.3 控制切换中延迟造成的抖动

为了更好地理解抖动,我们对单摆方程的滑模控制进行仿真。单摆方程为

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - (g _ {0} / \ell) \sin (x _ {1} + \delta_ {1}) - (k _ {0} / m) x _ {2} + (1 / m \ell^ {2}) uu = - k \operatorname{sgn} (s) = - k \operatorname{sgn} \left(a _ {1} x _ {1} + x _ {2}\right)$$

控制目标是在 $\delta_{1}=\pi/2$ 处稳定单摆，其中 $x_{1}=\theta-\delta_{1},x_{2}=\dot{\theta}$ ，常数 $m,\ell,k_{0}$ 和 $g_{0}$ 分别为质量、长度、摩擦系数和重力加速度，取 $a_{1}=1,k=4$ 。增益 k=4 是根据

$$
\begin{array}{l} \left| \frac {a _ {1} x _ {2} + h (x)}{g} \right| = \left| \ell^ {2} (a _ {1} m - k _ {0}) x _ {2} - m g _ {0} \ell \cos (x _ {1}) \right| \\ \leqslant \ell^ {2} | a _ {1} m - k _ {0} | (2 \pi) + m g _ {0} \ell \leqslant 3. 6 8 \\ \end{array}
$$

选择的,上式中的边界在集合 $\{|x_{1}|\leqslant\pi,|x_{1}+x_{2}|\leqslant\pi\}$ 上,当 $0.05\leqslant m\leqslant0.2,0.9\leqslant\ell\leqslant1.1,0\leqslant k_{0}\leqslant0.05$ 时求得,采用m=0.1, $\ell=1,k_{0}=0.02$ 进行仿真。图14.4所示为理想滑模控制,而图14.5为非理想情况下的滑模控制,其中切换延迟是由未建模执行部件动力学特性产生的,其传递函数为 $1/(0.01s+1)^{2}$ 。

![](image/ad0b3d7493abca7071ee969aef9a19f745f39c372d8676ef5b766641d1fe6d38.jpg)

<details>
<summary>line</summary>

| 时间 | θ |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.2 |
| 4 | 1.5 |
| 6 | 1.55 |
| 8 | 1.55 |
</details>

![](image/baec2c3c763a2dbb13747abf4de2cbe7c2087abda31cfb7fc6ad92cb8ac2b15d.jpg)
