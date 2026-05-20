$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = w (x _ {1}, x _ {2}, t) + u \end{array} , | w (x _ {1}, x _ {2}, t) | <   r _ {2} \right.
$$

和

$$
\left\{ \begin{array}{l} x _ {1} = x _ {2} \\ \dot {x} _ {2} = w (t) + u \end{array} , | w (t) | <   r _ {2} \right.
$$

的控制问题不应该有什么本质上的区别.

我们在两个闭环系统

$$
\left\{ \begin{array}{l} \dot {x _ {1}} = x _ {2} \\ \dot {x _ {2}} = w (x _ {1}, x _ {2}, t) - r \text {sign} \left(x _ {1} + \frac {| x _ {2} | x _ {2}}{2 r}\right) \end{array} \right.
$$

和 $\left\{\begin{aligned}\dot{x}_{1}&=x_{2}\\ \dot{x}_{2}&=w(t)\end{aligned}\right.-r\mathrm{sign}\left(x_{1}+\frac{|x_{2}|x_{2}}{2r}\right)$

中取 $w(t) = \sin(t)$ 和 $w(x_{1}, x_{2}, t) = x_{1} + x_{2} + \sin(t)$ ，参数 r 取 5 时的仿真结果如图 3.3.4 所示.

![](image/0479176b069da2d390a3c728ba47ae0435a7a21efe3364d448f962a7a437407e.jpg)

<details>
<summary>line</summary>

| x | w |
| --- | --- |
| 0 | 0.8 |
| 5 | -1.0 |
| 10 | 0.8 |
| 15 | -1.0 |
| 20 | 0.8 |
</details>

![](image/5af9733ecfd5b236f7c381c7050096f601a99f85176e042f7c0db4baffb25585.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.0 |
| 5 | -0.8 |
| 10 | 0.8 |
| 15 | -0.8 |
| 20 | 1.0 |
</details>

图3.3.4

这里不管扰动是纯时变的还是依赖于状态变量的, 只要参数 r 足够大, 都能彻底抑制扰动. 但在这里系统状态进入稳态时有高频振荡, 这是由于在开关线两边状态反馈量在 ±r 之间不断切换的结果. 为了消除这种高频颤震, 容易想到的是把开关函数 sign(·) 改成线形饱和函数 sat(·, δ). 这里, sat(·, δ) 的定义为

$$
\operatorname{sat} (s, \delta) = \left\{ \begin{array}{l} \operatorname{sign} (s), | s | > \delta \\ \frac {s}{\delta}, | \delta | \leqslant \delta \end{array} \right. \tag {3.3.25}
$$

然而, 仿真图 3.3.5 所示那样, $x_{1}$ 进入稳态后仍然有高频振荡. 为了彻底避免这种高频振荡, 我们在第二章中给出了离散系统

$$
\left\{ \begin{array}{l} x _ {1} (t + h) = x _ {1} (t) + h x _ {2} (t) \\ x _ {2} (t + h) = x _ {2} (t) + h u \end{array} , | u | \leqslant r \right. \tag {3.3.26}
$$

![](image/7de425ad1998c8d96a553fd8c4861af379abe9da44a76e43f500c3e14027fef1.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1 |
| 5 | -1 |
| 10 | 1 |
| 15 | -1 |
| 20 | 1 |
</details>

![](image/eec4f454ceb24a231ad5589c1b3d63db7b9d3cc1c7ff52f74568193c2b7078c1.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.0 |
| 5 | -0.8 |
| 10 | 0.8 |
| 15 | -0.8 |
| 20 | 1.0 |
</details>

图3.3.5

的最速反馈函数 $f\mathrm{han}(x_{1},x_{2},r,h)$ :
