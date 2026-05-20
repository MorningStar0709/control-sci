$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e _ {1} \\ \dot {z} _ {2} = z _ {3} - \beta_ {0 2} | e _ {1} | ^ {\frac {1}{2}} \text {sign} (e _ {1}) \\ \vdots \\ z _ {n - 1} = z _ {n} - \beta_ {0 n - 1} | e _ {1} | ^ {\frac {1}{2 ^ {n - 2}}} \text {sign} (e _ {1}) \\ \dot {z} _ {n} = - \beta_ {n} | e _ {1} | ^ {\frac {1}{2 ^ {n - 1}}} \text {sign} (e _ {1}) + b u \end{array} \right. \tag {4.1.24}
$$

例如，对三阶对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = f (x _ {1}, x _ {2}, t) + b u \\ y = x _ {1} \end{array} \right. \tag {4.1.25}
$$

可以建立如下状态观测器

$$
\left\{ \begin{array}{l l} e = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} g _ {1} (e) \\ \dot {z} _ {2} = z _ {3} - \beta_ {0 2} g _ {2} (e) \\ \dot {z} _ {3} = - \beta_ {0 3} g _ {3} (e) + b u \end{array} \text {或} \quad \left\{ \begin{array}{l l} e = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e \\ \dot {z} _ {3} = z _ {3} - \beta_ {0 2} \mathrm{fal} \left(e, \frac {1}{2}, \delta\right) \\ \dot {z} _ {3} = - \beta_ {0 3} \mathrm{fal} \left(e, \frac {1}{4}, \delta\right) + b u \end{array} \right. \right. \tag {4.1.26}
$$

例 3 用状态观测器(4.1.26) 对三阶对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = \operatorname{sign} \left(\sin \left(\frac {t}{2}\right)\right) \\ y = x _ {1} \end{array} \right. \tag {4.1.27}
$$

进行状态估计的仿真结果如图 4.1.4 所示.

在状态观测器中取了如下参数：

![](image/a50bbd90fa7c98895976a752d164752dac21e2419b291b55159c166252ab8ff1.jpg)

<details>
<summary>line</summary>

| x | y1 | y2 | y3 |
| --- | --- | --- | --- |
| 0 | 0 | -5 | -5 |
| 5 | -50 | -10 | -10 |
| 10 | -100 | -15 | -15 |
| 15 | -150 | -20 | -20 |
| 20 | -200 | -25 | -25 |
| 25 | -250 | -30 | -30 |
| 30 | -300 | -35 | -35 |
| 35 | -350 | -40 | -40 |
| 40 | -400 | -45 | -45 |
</details>

图4.1.4

$$h = 0. 0 1, \delta = 0. 0 5, \beta_ {0 1} = 1 0 0, \beta_ {0 2} = 3 0 0, \beta_ {0 3} = 1 0 0 0$$

系统的状态变量 $x_{1}, x_{2}, x_{3}$ 和其估计值 $z_{1}, z_{2}, z_{3}$ 之间的差别几乎看不出来.
