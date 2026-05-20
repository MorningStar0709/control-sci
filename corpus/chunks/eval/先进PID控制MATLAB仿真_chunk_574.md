# 14.4.1 移动机器人运动学模型

以轮式移动机器人为例，该机器人两个后轮较大，为驱动轮，两个后轮较小，为从动轮。左右两个后轮各由一个电动机来驱动，如果两个电动机的转速不同，则左右两个后轮会产生“差动”，从而可实现转弯。

如图 14-14 所示，移动机器人的状态由其两个驱动轮的轴中点 M 在坐标系的位置及航向角 $\theta$ 来表示，令 $P = [x \quad y \quad \theta]^{T}$ ， $q = [v \quad \omega]^{T}$ ，其中 $[x \quad y]$ 为移动机器人的位置， $\theta$ 为移动机器人前进方向与 x 轴的夹角，v 和 $\omega$ 分别为移动机器人的线速度和角速度，在运动学模型中它们是控制的输入信号。

移动机器人的运动学方程为

$$
\dot {\boldsymbol {p}} = \left( \begin{array}{c} \dot {x} \\ \dot {y} \\ \dot {\theta} \end{array} \right) = \left( \begin{array}{c c} \cos \theta & 0 \\ \sin \theta & 0 \\ 0 & 1 \end{array} \right) \boldsymbol {q} \tag {14.18}
$$

![](image/b29cb77396e73f79b1f15e70f210607ff442ef50cf0174c6768390623fae6471.jpg)

<details>
<summary>text_image</summary>

y
y_d
M
θ
θ(0)
y(0)
O
x(0)
x_d
x
</details>

图 14-14 移动机器人的运动

由该运动学方程可见，共有两个自由度，模型输出为3个变量，该模型为欠驱动系统，只能实现两个变量的主动跟踪，剩余的变量为随动或镇定状态。本控制为轨迹跟踪问题，即通过设计控制律 $q=\left[v\quad\omega\right]^{T}$ 实现移动机器人的位置 $[x\quad y]$ 的跟踪，并实现夹角 $\theta$ 的随动。

由式（14.18）得移动机器人运动学模型为

$$\dot {x} = v \cos (\theta)\dot {y} = v \sin (\theta) \tag {14.19}\dot {\theta} = \omega$$

采用双环控制方法，针对位置 $\left[x\quad y\right]$ 的跟踪作为外环，外环产生 $\theta_{d}$ ，然后通过内环实现 $\theta$ 快速跟踪 $\theta_{d}$ 。

![](image/e41dc15f75d73ed5b89bfef022273dbf75c4315f9b36b957ddad792145082e92.jpg)
