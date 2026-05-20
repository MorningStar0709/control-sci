# 2.3 跟踪微分器的一般形式

经典微分环节是利用惯性环节有延迟地跟踪输入信号的性质,按近似微分公式

$$\dot {v} (t) \approx \frac {v (t) - v (t - \tau)}{\tau}$$

来构造的．根据这个理解,我们给出了按近似微分公式

$$\dot {v} (t) \approx \frac {v (t - \tau_ {1}) - v (t - \tau_ {2})}{\tau_ {1} - \tau_ {2}}$$

来实现的用两个惯性环节并联构成的微分器方案——公式(2.2.12)，公式(2.2.15).

已指出二阶传递函数

$$W (s) = \frac {r ^ {2} s}{s ^ {2} + 2 r \xi s + r ^ {2}} \tag {2.3.1}$$

具有较好的微分功能. 这里有两个参数 $r, \xi$ . 这个传递函数代表的二阶线性系统的离散形式为

$$
\left\{ \begin{array}{l} x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h \left(- r ^ {2} \left(x _ {1} (k) - v _ {0} (k)\right) - 2 \xi r x _ {2} (k)\right) \end{array} \right. \tag {2.3.2}
$$

取 $\xi = 0.5, 1.0, 1.5, r = 1$ 时的阶跃响应如图 2.3.1 所示.

![](image/f1f4869156696f99e732001b32ef53007792cf66636a37aae5365204de1e1fc7.jpg)

<details>
<summary>line</summary>

| x | y (ξ=0.5) | y (ξ=1.0) |
| --- | --- | --- |
| 7 | 0 | 0 |
| 8 | 0.25 | 0.25 |
| 9 | 0.5 | 0.5 |
| 10 | 0.75 | 0.75 |
| 1 | 1 | 1 |
| 2 | 1.25 | 1.25 |
| 3 | 1.5 | 1.5 |
| 4 | 1.75 | 1.75 |
| 5 | 2 | 2 |
| 6 | 2.25 | 2.25 |
| 7 | 2.5 | 2.5 |
| 8 | 2.75 | 2.75 |
| 9 | 3 | 3 |
| 10 | 3.25 | 3.25 |
The chart displays a line graph with two distinct curves labeled by ξ values: ξ=0.5 and ξ=1.5. The x-axis ranges from 0 to 10, and the y-axis ranges from 0 to 2. The lines are symmetrically placed around the origin, indicating that as x increases, y increases proportionally for both ξ values. The chart is divided into two sections based on the same axes, but no explicit numerical data or trend lines are provided in the image.
</details>

图2.3.1

$\xi$ 作为阻尼因子， $\xi = 0.5$ 是缺阻尼，阶跃响应上升快，超调大，振荡多， $\xi = 1.5$ 是过阻尼，虽然无超调，但达到稳态值的时间过长，但是当 $\xi = 1.0$ 时是几乎无超调地一次进入稳态值（图2.3.1).取别的 $r$ 值也有同样的现象，因此传递函数

$$W (s) = \frac {r ^ {2}}{s ^ {2} + 2 r s + r ^ {2}} \tag {2.3.3}$$

的阶跃响应是二阶线性系统中无超调地一次达到设定值的系统，其中参数 $r$ 越大，越快地达到设定值，因此参数 $r$ 可以当作决定跟踪速度的速度因子。系统(2.3.3）对不同参数 $r = 1.0,5.0,20.0$ 时的仿真结果显示于图2.3.2。这里达到稳态值的时间几乎与参数 $r$ 成反比。可以利用这个性质来建立如下线性跟踪微分器

$$
\left\{ \begin{array}{l} x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h \left(- r ^ {2} \left(x _ {1} (k) - v _ {0} (k)\right) - 2 r x _ {2} (k)\right) \end{array} \right. \tag {2.3.4}
$$

![](image/12ef5fe7653888f2f89626f432e94acbed8c8a54f3eda954942eb6a82aadc58c.jpg)

<details>
<summary>line</summary>
