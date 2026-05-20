选取 a 和 K，使系统的上升时间约为 2s、超调不超过 25%。绘制关于 K 的根轨迹。

(c) 绘制未补偿被控对象的伯德图(幅值和相位图)。

(d) 绘制补偿设计的伯德图并估计相位裕度。设计状态反馈使得闭环极点与(b)问中设计的极点位置相同。

(e) 用测量值 x=y 为 x 和 $\dot{x}$ 设计一个估计器，并选择观测器增益 L，使得关于 $\widetilde{x}$ 的方程的特征根满足阻尼比 $\zeta=0.5$ 、自然频率 $\omega_{n}=8$ 。

(f) 绘制将估计器与控制律结合得到的系统框图，并标出 $\hat{x}$ 和 $\dot{x}$ 。绘制该闭环系统的伯德图并将得到的带宽和稳定裕度与 (b) 问中的设计进行比较。

7.53 如图 7.98 所示的柔性机械臂的简化控制模型，其中： $k/M=900rad/s^{2}$ ，y 为输出，物体的位置；u 为输入，弹簧末端的位置。

![](image/f46913d63d2da10bb559be4f924a400ea8377dbb55242b3c7c69a1705cba0a67.jpg)

<details>
<summary>text_image</summary>

u
k
M
y
</details>

图 7.98 习题 7.53 的简化机械手臂

(a) 写出状态空间形式的运动方程。

(b) 设计一个估计器，其根为 s = -100 ± 100j。

(c) 若仅 $\dot{y}$ 的测量值可得，系统的两个状

态变量是否均能被估计？

(d) 设计一个全状态反馈控制器使其根为 $s = -20 \pm 20j$ 。

(e) 为系统设计一个根为 $s = -200 \pm 200j$ 的控制律是否理？陈述你的理由。

(f) 写出补偿器方程，其中包含 y 的控制输入。为闭环系统绘制伯德图并给出该设计的增益和相位裕度。

7.54 两个级联水箱如图 7.99 所示，控制液体流动动态特性的线性化微分方程如下：

$$\dot {\delta h _ {1}} + \sigma \delta h _ {1} = \delta u\delta \dot {h} _ {2} + \sigma \delta h _ {2} = \sigma \delta h _ {1}$$

![](image/2aee37fcfb17460a4ca1c3c0770f4dd7de34d30fd8e36ef2b1c7fc872952a9e6.jpg)

<details>
<summary>text_image</summary>

u
h₁
h₂
</details>

图 7.99 习题 7.54 的耦合水箱

其中： $\delta h_{1}$ 为容器 1 中液体距标称液位深度的微分； $\delta h_{2}$ 为容器 2 中液体距标称液位深度的微分； $\delta u$ 为容器 1 中液体流入速度的微分（控制量）。

(a) 两个级联水箱的液位控制器：用如下形式的状态反馈

$$\delta u = - K _ {1} \delta h _ {1} - K _ {2} \delta h _ {2}$$

选择 $K_{1}$ 和 $K_{2}$ 的值，使得闭环特征根为 $s = -2\sigma(1 \pm j)$

(b) 两个级联水箱的液位估计器：假定仅容器2的液位微分（即 $y=\delta h_{2}$ 是可测的。用该测量值设计估计器，使其给出容器1和容器2液位微分的连续且平滑的观测值，估计器误差极点为 $-8\sigma(1\pm j)$ 。

(c) 两个级联水箱的估计器/控制器：绘制将(b)问中的估计器与(a)问中的控制器结合得到的闭环系统的框图(给出独立的积分器)。

(d) 用 Matlab 计算并绘制对 $\delta h_{1}$ 的初始偏移 y 的响应。绘图时假设 $\sigma=1$ 。

7.55 一船长 100m，以 10m/s 的常速度运动，其横向运动的描述如下：

$$
\left[ \begin{array}{c} \dot {\beta} \\ \dot {r} \\ \dot {\psi} \end{array} \right] = \left[ \begin{array}{c c c} - 0. 0 8 9 5 & - 0. 2 8 6 & 0 \\ - 0. 0 4 3 9 & - 0. 2 7 2 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} \beta \\ r \\ \psi \end{array} \right]

+ \left[ \begin{array}{c} 0. 0 1 4 5 \\ - 0. 0 1 2 2 \\ 0 \end{array} \right] \delta
$$

其中： $\beta$ 为侧滑角， $(^\circ)$ ； $\psi$ 为航向角， $(^\circ)$ ； $\delta$ 为舵角， $(^\circ)$ ；r 为偏航速度（见图 7.100）

![](image/0d9212b0472482de64f5f7e11b5fa99154f7571f14417c166e2ff031143127a4.jpg)

<details>
<summary>text_image</summary>

船的运动方向
β
ψ
δ
</details>

图 7.100 习题 7.55 中船的俯视图
