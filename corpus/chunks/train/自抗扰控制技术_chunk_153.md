# 4.4 其他形式的扩张状态观测器

上面讨论的是固定形式的如下扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, \delta), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, \delta) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe} + b u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {\mathrm{t}}\right) \end{array} \right. \tag {4.4.1}
$$

实际上，这里的函数 $\operatorname{fal}(e,\alpha,\delta)$ 可以取别的形式，如线性函数 $\operatorname{fal}(e,1.0,\delta)=e$ ，也可以取别的非线性函数形式，如 $\operatorname{fal}(e,0.0,\delta)=\operatorname{sat}(e,\delta)$ 。从大的方面分类就是线性和非线性两大类。

在线性情况下扩张状态观测器的方程变成

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} e + b u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} e\right) \end{array} \right. \tag {4.4.2}
$$

其输入到输出 $z_{1}, z_{2}, z_{3}$ 之间的传递关系分别为

$$z _ {1} = w _ {1} (s) y = \frac {\beta_ {0 1} s ^ {2} + \beta_ {0 2} s + \beta_ {0 3}}{s ^ {3} + \beta_ {0 1} s ^ {2} + \beta_ {0 2} s + \beta_ {0 3}} yz _ {2} = w _ {2} (s) y = \frac {\beta_ {0 2} s ^ {2} + \beta_ {0 3} s}{s ^ {3} + \beta_ {0 1} s ^ {2} + \beta_ {0 2} s + \beta_ {0 3}} y \tag {4.4.3}z _ {3} = w _ {3} (s) y = \frac {\beta_ {0 3} s ^ {2}}{s ^ {3} + \beta_ {0 1} s ^ {2} + \beta_ {0 2} s + \beta_ {0 3}} y$$

在“总和扰动”的变化范围不太大的情况下，用算法(4.4.2)进行估计的效果也不错.但要保证一定的估计精度，需要取比较大的增益，即系数 $\beta_{01},\beta_{02},\beta_{03}$ 就要取得大一些，这就是所谓的“高增益状态观测器”形式.

例 对三阶对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = \gamma \operatorname{sign} (\sin (t / 2)) \\ y = x _ {1} \end{array} \right. \tag {4.4.4}
$$

用线性扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} e\right) \\ z _ {3} = z _ {3} + h \left(z _ {4} - \beta_ {0 3} e + b u\right) \\ z _ {4} = z _ {4} + h (- \beta_ {0 4} e) \end{array} \right. \tag {4.4.5}
$$

进行估计的仿真结果如图 4.4.1 所示.

![](image/7772fdf3905da1a4b122aac05e9f1185c2d8954b9ff5a42f621fbb63c5050a01.jpg)

<details>
<summary>line</summary>
