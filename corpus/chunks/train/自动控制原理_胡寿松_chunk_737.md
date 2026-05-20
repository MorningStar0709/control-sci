9-37 设磁悬浮试验系统如图 9-49 所示。在该系统上方装有一个电磁铁，产生电磁吸力 F，以便将铁球悬浮于空中。系统的下方装有一个间隙测量传感器，以测量铁球的悬浮间隙。由于没有引入反馈，该磁悬浮试验系统不能稳定工作。

假定电磁铁电感为 $L = 0.508\mathrm{H}$ ，电阻为 $R = 23.2\Omega$ ，电流为 $i_1 = I_0 + i$ ，其中 $I_0 = 1.06\mathrm{A}$ 是系统的标称工作电流。再假定铁球的质量为 $m = 1.75\mathrm{kg}$ ，铁球悬浮间隙 $\mu_{g} = X_0 + x$ ，其中 $X_0 = 4.36\mathrm{mm}$ 为标称磁悬浮间隙。若电磁吸力满足如下条件：

$$F = k (i / \mu_ {g}) ^ {2}$$

式中 $k = 2.9 \times 10^{-4} \mathrm{~kg} \cdot \mathrm{m}^2 / \mathrm{A}^2$ 。选择 $x_{1} = x, x_{2} = \frac{\mathrm{d} x}{\mathrm{d} t}, x_{3} = i$ 为状态变量，试利用 $F$ 的泰勒展开式，列写磁悬浮试验系统的线性化状态空间表达式。

![](image/6dffcaa9f75c4fd28698554e4604a7ee0a74185f37f0291d1fdfad42308c82c1.jpg)

<details>
<summary>text_image</summary>

多臂机器人
空间结构体
操纵器
</details>

(a)   
![](image/9a0dd6cfcd38594ecdd2284ee9504dea3646084493231e7fac5a19bd8b922878.jpg)

<details>
<summary>text_image</summary>

驱动电机
k
θ₁
u
θ₂
J
负载
I, M
(b)
</details>

图 9-48 遥操作系统

![](image/00205c1b1601057f9f8cff53f6f0674dfb5785e663984191fade65c8debad007.jpg)

<details>
<summary>text_image</summary>

电磁铁
i₁
</details>

![](image/2819e743c965fb91cb5922ece8a884ec11add8d0d641e4fc71e7fbec34225e8c.jpg)

<details>
<summary>text_image</summary>

铁球
x
m
力F
mg
间隙传感器
</details>

图 9-49 磁悬浮系统

9-38 在大功率高性能的摩托车中，常采用图 9-50 所示的弹簧-质量-阻尼器系统作为减震器。

若已知减震器的基本参数取为质量 $m = 1\mathrm{kg}$ ，摩擦系数 $f = 9\mathrm{kg}\cdot \mathrm{m}\cdot \mathrm{s}$ ，弹簧系数 $k = 20\mathrm{kg / m},u(t)$ 为力输入， $y(t)$ 为位移输出。要求完成：

(1) 选择状态变量为 $x_{1}=y, y_{2}=\dot{y}$ ，列写系统的动态方程；  
(2) 计算系统的特征根及状态转移矩阵 $\Phi(t)$ ;  
(3) 若初始条件 $y(0)=1, \dot{y}(0)=2$ ，在 $0 \leqslant t \leqslant 2$ 范围内，绘出系统零输入响应 $y(t)$ 及 $\dot{y}(t)$ ;  
(4) 重新设计 f 和 k 的合适值, 使系统特征根为 $s_{1}=s_{2}=-10$ , 以减轻震动对车手的影响。

9-39 设汽车悬架控制系统如图 9-51 所示, 其中 $X_{1}(s), X_{2}(s)$ 和 $X_{3}(s)$ 为状态变量, $K_{1}, K_{2}$ 和 $K_{3}$ 为状态反馈系数, 已知 $K_{1} = 1$ 。试确定 $K_{2}$ 和 $K_{3}$ 的合适取值, 使闭环系统的三个特征根位于 $s = -3$ 和 $s = -6$ 之间。另外，还要求确定前置增益 $K_{p}$ 值，使系统对阶跃输入的稳态误差为零。

![](image/49b70065b3c1cabdcb575616dd8d97ca2364f971045840d789ce404cb9c03c5a.jpg)

<details>
<summary>text_image</summary>

摩擦
系数
f
k
m
y(t)
u(t)
</details>

图 9-50 弹簧-质量-阻尼器系统

9-40 在图 9-52(a) 所示的新型游船上, 采用了浮桥和稳定器来减少波浪对游船摇摆的影响, 游船摇摆控制系统如图 9-52(b) 所示。图中, $X_{1}, X_{2}$ 和 $X_{3}$ 为状态变量, $K_{2}$ 和 $K_{3}$ 为状态反馈增益。试确定 $K_{2}$ 和 $K_{3}$ 的合适取值, 使闭环特征根为 $s_{1,2} = -2 \pm j2, s_{3} = -15$ , 并画出系统在单位阶跃扰动作用下的响应曲线。
