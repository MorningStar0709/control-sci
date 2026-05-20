$$
\left\{ \begin{array}{l} \dot {x} _ {1} = - x _ {2} - x _ {3} \\ \dot {x} _ {2} = x _ {1} + a x _ {2} \\ \dot {x} _ {3} = b + x _ {3} (x _ {1} - c) \\ y = x _ {1} \end{array} \right. \tag {4.6.12}
$$

式中， $a = 0.2, b = 0.2, c = 5.7, x_1(0) = -1, x_2(0) = -1,$ $x_{3}(0) = 0$ 时产生混沌（图4.6.4）

这里，

$$f _ {1} \left(x _ {1}, x _ {2}, x _ {3}\right) = - x _ {2} - x _ {3},\frac {\partial f _ {1}}{\partial x _ {1}} f _ {1} + \frac {\partial f _ {1}}{\partial x _ {2}} f _ {2} + \frac {\partial f _ {1}}{\partial x _ {3}} f _ {3} = - (x _ {1} + a x _ {2}) - (b + x _ {3} (x _ {1} - c))$$

![](image/cf82c608d53617b251b54c1f493434725afd9560b9990f66685acc2e530a2701.jpg)

<details>
<summary>surface_3d</summary>

| X | Y |
| --- | --- |
| -10 | 0 |
| -5 | 5 |
| 0 | 10 |
| 5 | 5 |
| 10 | 0 |
| 15 | 0 |
</details>

图 4.6.4

因此

$$
\begin{array}{l} g \left(x _ {1}, x _ {2}, x _ {3}\right) = - x _ {1} - a x _ {2} - x _ {1} x _ {3} - b + c x _ {3} = \\ - 0. 2 - x _ {1} - 0. 2 x _ {2} + 5. 7 x _ {3} - x _ {1} x _ {3} \\ \end{array}
$$

经过坐标变换

$$
\left\{ \begin{array}{l} y _ {1} = x _ {1} \\ y _ {2} = f _ {1} \left(x _ {1}, x _ {2}, x _ {3}\right) \\ y _ {3} = g \left(x _ {1}, x _ {2}, x _ {3}\right) \end{array} \right.

\left\{ \begin{array}{l} \dot {y} _ {1} = y _ {2} \\ \dot {y} _ {2} = y _ {3} \\ \dot {y} _ {3} = \frac {\partial g}{\partial x _ {1}} f _ {1} + \frac {\partial g}{\partial x _ {2}} f _ {2} + \frac {\partial g}{\partial x _ {1}} f _ {3} \\ y = y _ {1} \end{array} \right.
$$

其中

$$
\begin{array}{l} \frac {\partial g}{\partial x _ {1}} f _ {1} + \frac {\partial g}{\partial x _ {2}} f _ {2} + \frac {\partial g}{\partial x _ {1}} f _ {3} = (1. 1 4 + 0. 4 x _ {1} + 0. 9 4 x _ {2}) - \\ (3 1. 4 9 - 1 1. 4 x _ {1} + x _ {2} - x _ {1} ^ {2} + x _ {3}) x _ {3} \\ \end{array}
$$

用扩张状态观测器(4.6.4)，其参数仍取式(4.6.11)给出的值.所作的仿真结果中只显示扩展状态观测器的变量 $z_{1},z_{2}$ 分别跟踪系统(4.6.9)的状态 $y_{1},y_{2}$ 的情形(图4.6.5和图4.6.6).同样,图4.6.6和图4.6.5的上图是对应轨线的第一坐标的情形,而下图是第一坐标跟踪误差曲线.

![](image/cb407ee6315513e9ce3dabebe98f44abbb84bc089ee5d185fa982e686f8ea69f.jpg)

<details>
<summary>line</summary>

| x | y (x·10⁻³) |
| --- | --- |
| 0 | 0 |
| 10 | 5 |
| 20 | -5 |
| 30 | 10 |
| 40 | -10 |
| 50 | 15 |
| 60 | -15 |
| 70 | 20 |
| 80 | -20 |
| 90 | 25 |
| 100 | -25 |
</details>

图4.6.5  
![](image/e029825b7cac641e6575eda46fae52cb71b660b56561a1a9bc0bd18feabb279b.jpg)

<details>
<summary>line</summary>

| x | y1 | y2 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10 | -5 | 5 |
| 20 | 10 | 10 |
| 30 | -15 | 15 |
| 40 | 20 | 20 |
| 50 | -25 | 25 |
| 60 | 30 | 30 |
| 70 | -35 | 35 |
| 80 | 45 | 45 |
| 90 | -45 | 45 |
| 100 | 55 | 55 |
</details>

图4.6.6
