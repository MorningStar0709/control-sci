![](image/b766ec1a6968af4c72e062fc9acae4b044c755671a9898cbac5522fbe605803a.jpg)

<details>
<summary>text_image</summary>

参考经度
轨道上的期望位置
u
x
y
z
</details>

图 7.95 习题 7.45 的同步卫星轨道图

7.46 如图 7.96 所示的单摆运动的线性化方程为

$$\ddot {\theta} + \omega^ {2} \theta = u$$

![](image/2cb76f6eb8a3a001013ec2513bb12c592d65c8b6bf129b1f092e03c81da40a7b.jpg)

<details>
<summary>text_image</summary>

Diagram of a pendulum with labeled angle θ and fixed support
</details>

图7.96 习题7.46的单摆图

(a) 写出状态空间形式的运动方程。

(b) 给定 $\theta$ 的测量值，设计一个估计（观测）器重构单摆的状态。假定 $\omega = 5 \, rad/s$ ，估计器极点选在 $s = -10 \pm 10 \, j$ 处。

(c) 写出从测量值 $\theta$ 到观测值 $\theta$ 之间的估计

器传递函数。

(d) 设计一个控制器(即确定状态反馈增益 K)，使闭环特征方程的根在 $s = -4 \pm 4j$ 处。

7.47 由某惯性导航仪的误差分析得出下面这组标准化的状态方程：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & - 1 & 0 \\ 1 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] u
$$

其中： $x_{1}$ 为东向速度误差； $x_{2}$ 为平台绕北轴的倾斜度； $x_{3}$ 为陀螺北向偏移；u 为陀螺偏移的变化率。

设计一个降阶估计器，取 $y=x_{1}$ 作为测量值，并使估计器的误差极点为 -0.1 和 -0.1。确保给出所有相关的估计器方程。
