![](image/5d883990e9c8b2252ffdf5c498ac5b5504e8e32f4605b88047f3b5207cf550ab.jpg)

<details>
<summary>line</summary>

| 时间/s | 温度/K (r) | 温度/K (y) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10 | ~5 | ~5 |
| 20 | ~15 | ~15 |
| 30 | ~25 | ~25 |
| 40 | ~25 | ~25 |
| 50 | ~25 | ~25 |
| 60 | ~25 | ~25 |
| 70 | ~25 | ~25 |
| 80 | ~0 | ~0 |
| 90 | ~0 | ~0 |
| 100 | ~0 | ~0 |
</details>

a）温度跟踪呼应

![](image/61dac0c546a14e81bb26174d77f9e5c05b6231cf4096e70796415a91ffe07424.jpg)

<details>
<summary>line</summary>

| 时间/s | 灯管电压 |
| --- | --- |
| 0 | 0 |
| 20 | 4 |
| 30 | 3 |
| 70 | -20 |
| 80 | -1 |
| 90 | 0 |
| 100 | 0 |
</details>

b）温度跟踪呼应  
图 10.67 PI 控制器的线性闭环 RTP 响应

步骤 6 评估/修正被控对象。在执行器及传感器选择时已经讨论过。

步骤 7 尝试最优设计。我们使用包含积分控制的误差空间法和第 7 章介绍的线性二次高斯(Gauss)法进行设计。误差系统为

$$
\left[ \begin{array}{l} \dot {e} \\ \dot {\xi} \end{array} \right] = \left[ \begin{array}{l l} 0 & C \\ 0 & A \end{array} \right] \left[ \begin{array}{l} e \\ \xi \end{array} \right] + \left[ \begin{array}{l} D \\ B \end{array} \right] \mu \tag {10.44}
$$

其中：

$$
\mathbf {A} _ {\mathrm{s}} = \left[ \begin{array}{l l} 0 & \mathbf {C} \\ \mathbf {0} & \mathbf {A} \end{array} \right], \quad \mathbf {B} _ {\mathrm{s}} = \left[ \begin{array}{l} D \\ \mathbf {B} \end{array} \right]
$$

$e=y-r,\ \xi=\dot{T}$ 并且 $\mu=\dot{u}$ 。对状态反馈的设计，利用第7章的LQR公式得

$$\mathcal {J} = \int_ {0} ^ {+ \infty} \left\{\boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {z} + \rho \mu^ {2} \right\} \mathrm{d} t$$

其中： $z=\left[e\quad\xi^{T}\right]^{T}$ 。注意，J的选择是为了处理轨迹误差e、控制信号u和3个温度的差值。因此，性能指数应该为以下形式：

$$1 0 \{(\dot {T} _ {1} - \dot {T} _ {2}) ^ {2} + (\dot {T} _ {1} - \dot {T} _ {3}) ^ {2} + (\dot {T} _ {2} - \dot {T} _ {3}) ^ {2} \}$$

这样就可以减小温度的不均匀性。因子10作为误差状态与对象状态之间相对加权值，由反复实验来确定。状态矩阵及控制加权矩阵 $Q$ 和 $R$ 分别为

$$
Q = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 2 0 & - 1 0 & - 1 0 \\ 0 & - 1 0 & 2 0 & - 1 0 \\ 0 & - 1 0 & - 1 0 & 2 0 \end{array} \right], \quad R = \rho = 1
$$

利用下面的 Matlab 命令来设计反馈增益：

$$[ K ] = \mathrm{lqr} (\mathrm{As}, \mathrm{Bs}, \mathrm{Q}, \mathrm{R})$$

由 Matlab 计算的反馈增益矩阵为

$$\boldsymbol {K} = \left[ K _ {1}: \boldsymbol {K} _ {0} \right]$$

其中：

$$K _ {1} = 1, \quad K _ {0} = [ 0. 1 2 2 1 \quad 2. 0 7 8 8 \quad - 0. 2 1 4 0 ]$$

由此得出的内部模型控制器的形式为：

$$\dot {x} _ {\mathrm{c}} = B _ {\mathrm{c}} eu = C _ {\mathrm{c}} x _ {\mathrm{c}} - K _ {0} T \tag {10.45}$$

其中： $x_{c}$ 表示控制器状态，且

$$B _ {\mathrm{c}} = - K _ {1} = - 1, \quad C _ {\mathrm{c}} = 1$$

由 Matlab 得到状态反馈闭环极点为 $-0.5574 \pm 0.4584j$ ; -0.1442 和 -0.0877。全阶估计器设计时选定过程和传感器噪声强度作为估计器设计的调节器：
