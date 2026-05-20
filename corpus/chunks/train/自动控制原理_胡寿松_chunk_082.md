# 4. 典型元部件的传递函数

自动控制系统是由各种元部件相互连接组成的，它们一般是机械的、电子的、液压的、光学的或其他类型的装置。为建立控制系统的数学模型，必须首先了解各种元部件的数学模型及其特性。

电位器 电位器是一种把线位移或角位移变换为电压量的装置。在控制系统中，单个电位器用作为信号变换装置，如图2-10(a)所示；一对电位器可组成误差检测器，如图2-10(b)所示。

![](image/43f1f4d0d11366b7af4d3a906cd3d995e38dd24292d6dd81309280299f75bf6c.jpg)

<details>
<summary>text_image</summary>

E
½θmax
θ
½θmax
u(t)
</details>

(a)

![](image/38da97786ea2580221b5f2fcf27676c214adb4275e554b701dee452d690efeef.jpg)

<details>
<summary>text_image</summary>

θ₁
E
K₁θ₁
K₁θ₂
u(t)
</details>

(b)

![](image/4c11c2be6fa8d4fd0e68de2844ef60f6de17a4197af028b1f6f082eb6ba1edda.jpg)

<details>
<summary>line</summary>

| πθ(t) | n(t) |
| --- | --- |
| -π | -π |
| 0 | 0 |
| πθ(t) | E/2 |
</details>

(c)

![](image/303685ae51d3685a9a61b6d1456240497d1c28a8af2c85a31b0d7d7cdf912056.jpg)  
(d)   
图 2-10 电位器及其特性

空载时,单个电位器的电刷角位移 $\theta(t)$ 与输出电压 $u(t)$ 的关系曲线如图 2-10(c) 所示。图中阶梯形状是由绕线线径产生的误差,理论分析时可用直线近似。由图可得输出电压为

$$u (t) = K _ {1} \theta (t) \tag {2-43}$$

式中， $K_{1}=E/\theta_{max}$ ，是电刷单位角位移对应的输出电压，称电位器传递系数，其中E是电位器电源电压， $\theta_{max}$ 是电位器最大工作角。对式(2-43)求拉氏变换，并令 $U(s)=\mathcal{L}[u(t)]$ ， $\Theta(s)=\mathcal{L}[\theta(t)]$ ，可求得电位器传递函数为

$$G (s) = \frac {U (s)}{\Theta (s)} = K _ {1} \tag {2-44}$$

式(2-44)表明,电位器的传递函数是一个常值,它取决于电源电压 E 和电位器最大工作角度 $\theta_{max}$ 。电位器可用图 2-10(d) 的方框图表示。

用一对相同的电位器组成误差检测器时,其输出电压为

$$
\begin{array}{l} u (t) = u _ {1} (t) - u _ {2} (t) \\ = K _ {1} \left[ \theta_ {1} (t) - \theta_ {2} (t) \right] = K _ {1} \Delta \theta (t) \\ \end{array}
$$

式中， $K_{1}$ 是单个电位器的传递系数； $\Delta \theta (t) = \theta_1(t) - \theta_2(t)$ 是两个电位器电刷角位移之差，称为误差角。因此，以误差角为输入量时，误差检测器的传递函数与单个电位器传递函数相同，即为

$$G (s) = \frac {U (s)}{\Delta \Theta (s)} = K _ {1} \tag {2-45}$$

![](image/014cb23a4e2c20a93fb877f44b10f0b04f12129459cd1d939afa78c1207c9079.jpg)

<details>
<summary>text_image</summary>

E
Rp
θ
Rp'
u(t)
Rt
</details>

图 2-11 负载效应示意图

在使用电位器时要注意负载效应。所谓负载效应是指在电位器输出端接有负载时所产生的影响。图2-11表示电位器输出端接有负载电阻 $R_{l}$ 时的电路图，设电位器电阻是 $R_{p}$ ，可求得电位器输出电压为

$$u (t) = \frac {E}{\frac {R _ {p}}{R _ {p}} + \frac {R _ {p}}{R _ {l}} \left(1 - \frac {R _ {p}}{R _ {p}}\right)} = \frac {E \theta (t)}{\theta_ {\max} \left[ 1 + \frac {R _ {p}}{R _ {l}} \frac {\theta (t)}{\theta_ {\max}} \left(1 - \frac {\theta (t)}{\theta_ {\max}}\right) \right]}$$
