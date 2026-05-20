# 1.2.4 负阻振荡器

图 1.6 所示为一类重要电子振荡器的基本电路结构。假设电感和电容是线性时不变的无源元件，即 L > 0, C > 0。电阻是具有 v-i 特性为 $i = h(v)$ 的有源电路，如图 1.6 所示，函数

$h(\cdot)$ 满足条件

$$h (0) = 0, \quad h ^ {\prime} (0) < 0h (v) \to \infty \quad {\text {当}} v \to \infty , \quad h (i) \to - \infty \quad {\text {当}} v \to - \infty$$

其中 $h'(v)$ 是 $h(v)$ 对 v 的一阶导数。这样的 v-i 特性是可以实现的，例如图 1.7 所示的双隧道二极管电路，隧道二极管特性如图 1.2 所示。运用基尔霍夫电流定律可写出方程：

$$i _ {C} + i _ {L} + i = 0$$

即 $C\frac{dv}{dt} + \frac{1}{L}\int_{-\infty}^{t}v(s)ds + h(v) = 0$

对 t 求一次微分, 并两边同乘以 L, 得

$$C L \frac {d ^ {2} v}{d t ^ {2}} + v + L h ^ {\prime} (v) \frac {d v}{d t} = 0$$

上式可写成与非线性系统理论中一些大家熟知的公式相一致的形式,为此把时间变量 t 变换为 $\tau = t / \sqrt{CL}$ , v 对 t 的导数与对 $\tau$ 的导数有下述关系:

$$\frac {d v}{d \tau} = \sqrt {C L} \frac {d v}{d t}, \quad \frac {d ^ {2} v}{d \tau^ {2}} = C L \frac {d ^ {2} v}{d t ^ {2}}$$

把 v 对 $\tau$ 的导数记为 i，电路方程可写为

$$\ddot {v} + \varepsilon h ^ {\prime} (v) \dot {v} + v = 0$$

其中 $\varepsilon = \sqrt{L/C}$ ，该方程是李纳(Liénard)方程

$$\ddot {v} + f (v) \dot {v} + g (v) = 0 \tag {1.16}$$

的特例,当 $h(v) = -v + \frac{1}{3}v^{3}$

时,电路方程的形式为 $\ddot{v}-\varepsilon(1-v^{2})\dot{v}+v=0$ (1.17)

该方程称为范德波尔(Van der Pol)方程。Van der Pol用该方程研究真空管电路中的振荡，它是非线性振荡理论的基本例子。此方程有一个周期解，在唯一的平衡点 $v = \dot{v} = 0$ 吸引除零解以外的所有其他解。为写出电路的状态模型，取 $x_{1} = v, x_{2} = \dot{v}$ ，得

$$\dot {x} _ {1} = x _ {2} \tag {1.18}\dot {x} _ {2} = - x _ {1} - \varepsilon h ^ {\prime} (x _ {1}) x _ {2} \tag {1.19}$$

注意,选择电容两端的电压和流过电感的电流作为状态变量,即可获得另一个状态模型。状态变量记为 $z_{1}=i_{L}, z_{2}=v_{C}$ , 则状态模型由下式给出:

$$\frac {d z _ {1}}{d t} = \frac {1}{L} z _ {2}\frac {d z _ {2}}{d t} = - \frac {1}{C} [ z _ {1} + h (z _ {2}) ]$$

由于第一个状态模型是对时间变量 $\tau=t/\sqrt{CL}$ 的,我们写出对 $\tau$ 的模型

$$\dot {z} _ {1} = \frac {1}{\varepsilon} z _ {2} \tag {1.20}\dot {z} _ {2} = - \varepsilon [ z _ {1} + h (z _ {2}) ] \tag {1.21}$$

对 x 和 z 的状态模型看上去不一样,但它们是同一系统的等效表示。通过坐标变换

$$z = T (x)$$

这些模型就能相互获得,由此可看出它们是等效的。由于既有 x 又有 z 与电路物理变量的关系,因此不难找出映射 $T(\cdot)$ ,我们有

$$x _ {1} = v = z _ {2}x _ {2} = \frac {d v}{d \tau} = \sqrt {C L} \frac {d v}{d t} = \sqrt {\frac {L}{C}} [ - i _ {L} - h (v _ {C}) ] = \varepsilon [ - z _ {1} - h (z _ {2}) ]$$

这样 $z = T(x) = \left[ \begin{array}{c} - h(x_{1}) - (1 / \varepsilon)x_{2}\\ x_{1} \end{array} \right]$

其逆映射为 $x = T^{-1}(z) = \left[ \begin{array}{c}z_{2}\\ -\varepsilon z_{1} - \varepsilon h(z_{2}) \end{array} \right]$

![](image/32f24920440751d97c6747a16657d36fc5d85ee5c322db8e13d2eb3436e14078.jpg)

<details>
<summary>text_image</summary>

i
+
L
v
-
iC
iL
电阻元件
(a)
</details>

![](image/15d5ce5fcc4036689dc0d42b9796583d51410cc165d6fb13a46a213fe75e041d.jpg)

<details>
<summary>text_image</summary>

i = h(v)
(b)
</details>

图 1.6 (a) 基本振荡电路; (b) 典型的驱动点特性

![](image/16b7960e36fdbd36e3aeeb5db652f2c2caca2a3981de2522a8a3a3a5ede9afb8.jpg)

<details>
<summary>text_image</summary>

i
+
v
-
0.3 V
0.3 V
</details>

图 1.7 双隧道二极管负阻电路
