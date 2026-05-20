# 例2.1 一个简单系统：巡航控制模型

（1）以速度为变量列写运动方程，如图2.1所示，汽车正向行驶，假定发动机的牵引力为u。对微分方程进行拉普拉斯变换，并找到输入u和输出v之间的传递函数。

（2）用 Matlab 找出输入在 t=0 时刻由 u=0 跳变到常值 u=500N 后，汽车的速度响应。假设汽车的质量 m 是 1000kg，黏性阻力系数 $b=50N \cdot s/m$ 。

![](image/8ef492d640820bcb71241f8273b18699a304d5ca3e4e8ff21713d63f1aaf6874.jpg)

<details>
<summary>text_image</summary>

MPH
u
</details>

图 2.1 巡航控制模型

解答。

（1）运动方程：为简单起见，我们假设车轮的旋转惯性可以忽略，阻碍汽车运动的摩擦与车速成正比例，比例关系数为 $b^{\ominus}$ 。为了便于建模，汽车受力图可近似为图2.2所示的，图中定义了坐标系，画出了所有作用在物体上的力（粗线），并且标出了加速度（虚线）。汽车的位置坐标x是距选定的参考位置的距离，方向向右为正。由于

![](image/25dc15371145f664a1a2a12493201d4c6cff94a7059ef7da892db4b57c0b6efd.jpg)

<details>
<summary>text_image</summary>

摩擦力bx
m
→ x
→ ẋ
</details>

图 2.2 巡航控制受力图

汽车相对于惯性参考系的位置可以测量，所以容易求得惯性加速度为对于 x 的二阶导数（即 $a=\ddot{x}$ ），利用方程(2.1)建立运动方程，摩擦力与物体运动的方向相反；因此，图中画出它的方向与正运动方向相反，在方程(2.1)中有一个反向作用力，结果得

$$u - b \dot {x} = m \ddot {x} \tag {2.2}$$

或

$$\ddot {x} + \frac {b}{m} \dot {x} = \frac {u}{m} \tag {2.3}$$

由于是汽车巡航控制，这里感兴趣的变量是速度 $v(=\dot{x})$ ，其运动方程可变为：

$$\dot {v} + \frac {b}{m} v = \frac {u}{m} \tag {2.4}$$

我们将在第3章详细介绍如何求解这样的方程；而实际上，假定解的形式为 $v = V_{\circ}\mathrm{e}^{st}$ ，输入形式为 $u = U_{\circ}\mathrm{e}^{st}$ ，那么 $\dot{v} = sV_{\circ}\mathrm{e}^{st}$ ，则微分方程可写为

$$\left(s + \frac {b}{m}\right) V _ {\mathrm{o}} \mathrm{e} ^ {s t} = \frac {1}{m} U _ {\mathrm{o}} \mathrm{e} ^ {s t} \tag {2.5}$$

消去 $\mathrm{e}^{st}$ ，整理得

$$\frac {V _ {\mathrm{o}}}{U _ {\mathrm{o}}} = \frac {\frac {1}{m}}{s + \frac {b}{m}} \tag {2.6}$$

通常使用大写字母来表示以强调这是解的变换，或者写成

$$\frac {V (s)}{U (s)} = \frac {\frac {1}{m}}{s + \frac {b}{m}} \tag {2.7}$$

其具体原因，详见第3章。此表达式是由微分方程(2.4)确定的，称为传递函数，在后续章节中会经常用到。实质上，我们注意到式(2.7)是把方程(2.4)中的d/dt用s取代。传递函数作为一个数学模型，将汽车速度与推进汽车的力联系起来，就是说，输入来自汽车的加速踏板。在后面的章节中，系统的传递函数将会被用来设计反馈控制器，例如，现代汽车中大量使用的巡航控制设备。

（2）时间响应：系统动态可以根据传递函数写成 Matlab 语句，如下所示的 Matlab 语句给出了式(2.7)的实现。Matlab 中的 step. 函数用于计算单位阶跃输入下的线性系统时间响应。因为系统是线性的，所以某阶跃输入的幅值乘以这种情况下的输出就可以得到任意幅度的阶跃响应。相当于，sys 可以与阶跃输入的幅值相乘。

Matlab 语句如下：

$$
\begin{array}{l l} \text {s = tf('s') ;} & \% \text {sets up the mode to define the} \\ & \text {transfer function} \\ \text {sys = (1 / 1000) / (s + 50 / 1000) ;} & \% \text {defines the transfer function from} \\ & \text {Eq. (2.7) with the numbers filled in} \\ \text {step(500*sys);} & \% \text {plots the step response for u = 500} \end{array}
$$

在 500N 的阶跃输入下，计算并绘制速度的时间响应曲线。阶跃响应如图 2.3 所示。

牛顿定律也可以用在多个质量体的系统中。这时，画出每一部分质量体的受力图相当重要，要求标明所受的外力以及一个物体作用在另一个物体上大小相等、方向相反的内部作用力。
