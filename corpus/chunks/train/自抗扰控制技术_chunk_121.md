$$\frac {\partial T}{\partial x _ {1}} = \frac {s}{\sqrt {r} \sqrt {\frac {x _ {2} ^ {2}}{2 r} + s x _ {1}}}, \frac {\partial T}{\partial x _ {2}} = \frac {s}{r} + \frac {x _ {2}}{r} \frac {1}{\sqrt {r} \sqrt {\frac {x _ {2} ^ {2}}{2 r} + s x _ {1}}}$$

因此就有

$$\frac {\mathrm{d} T (x _ {1} , x _ {2})}{\mathrm{d} t} = \frac {\partial T}{\partial x _ {1}} x _ {2} - \frac {\partial T}{\partial x _ {2}} r s = - 1 \tag {3.5.16}$$

于是由于

$$T (x _ {1} (t), x _ {2} (t)) = - t + T (x _ {1} (0), x _ {2} (0)) \tag {3.5.17}$$

所有轨线都以有限时间到达原点. 这是对系统(3.4.1)作不连续的, 非光滑的状态反馈(3.5.4)带来的特殊效果. 正定函数 $T(x_{1}, x_{2})$ 的等值线和不连续系统(3.5.15)的运动轨线分布图如图3.5.2所示, 而其三维曲面图如图3.5.3所示.

以上讨论的是闭环系统

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = - r \mathrm{sign} \left(x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r}\right) \end{array} \right. \tag {3.5.18}
$$

![](image/42460ea892eb6df9163a9f8ea2772e97e261b5150c3e9b33b48e42df491a9c6f.jpg)

<details>
<summary>text_image</summary>

Mathematical diagram showing a coordinate plane with curved and straight lines intersecting at points (-1.5, 0), (0, 0), and (1.5, -1.5)
</details>

图3.5.2  
![](image/b729e7d5bef7aa3fd53f4fd2c6b760bd60e2f973ce62132504053981a6b2be74.jpg)

<details>
<summary>surface_3d</summary>

| X | Y | Z |
| --- | --- | --- |
| -4 | 5 | 2 |
| -2 | 3 | 1 |
| 0 | 1 | 0 |
| 2 | 0 | -1 |
| 4 | -1 | -2 |
</details>

图3.5.3

的相平面轨线的有关性质.

下面用同样的方式讨论闭环系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} \text {sign} \left(x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r}\right), r _ {1} > r \end{array} \right. \tag {3.5.19}
$$

的轨线分布和过渡时间函数. 这里决定开关线的参数 r 和决定加速度的最大值的参数 $r_{1}$ 应该满足 $r_{1} > r$ .

此系统花 t 时间到达原点的轨线的初始点是用倒退积分系统 (3.5.2) 来决定. 系统 (3.5.2) 的倒退方程为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = - u \end{array} \right.
$$

在这里加速度取 $u = +r_{1}$ 和 $u = -r_{1}$ 的分界线是

$$x _ {1} + \frac {x _ {2} \mid x _ {2} \mid}{2 r} = 0$$

这个曲线是在原点对顶的两个半抛物线(图3.5.4). 这个曲线实际上是系统(3.5.2)的进入原点的最速轨线, 上半部分为 u = -r 的最速轨线, 而下半部分为 $u = +r$ 的最速轨线, 它们是可以用如下方式确定.

![](image/41a6296a1b548c8975398f62bc7d437e8588868595d79c89e883384d2e02e56f.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2.0 | 2.0 |
| -1.5 | 1.5 |
| -1.0 | 1.0 |
| -0.5 | 0.5 |
| 0.0 | 0.0 |
| 0.5 | -0.5 |
| 1.0 | -1.0 |
| 1.5 | -1.5 |
| 2.0 | -2.0 |
</details>

图3.5.4

1. 先取 $u = +r$ ，从原点出发积分到 $\tau$ 时刻倒退方程

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \dot {x} _ {2} = - r \end{array} \right.
$$

得
