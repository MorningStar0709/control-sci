$$
\left\{ \begin{array}{l} f _ {1} \left(x _ {1}, x _ {2}, x _ {3}\right) = \sigma \left(x _ {2} - x _ {1}\right) = 1 0 x _ {2} - 1 0 x _ {1} \\ f _ {2} \left(x _ {1}, x _ {2}, x _ {3}\right) = \rho x _ {1} - x _ {2} - x _ {1} x _ {3} = 2 8 x _ {1} - x _ {2} - x _ {1} x _ {3} \\ f _ {3} \left(x _ {1}, x _ {2}, x _ {3}\right) = - b x _ {3} - x _ {1} x _ {2} = - \frac {8}{3} x _ {3} - x _ {1} x _ {2} \end{array} \right. \tag {4.6.7}
$$

于是

$$\frac {\partial f _ {1}}{\partial x _ {1}} f _ {1} + \frac {\partial f _ {1}}{\partial x _ {2}} f _ {2} + \frac {\partial f _ {1}}{\partial x _ {3}} f _ {3} = - \sigma (\sigma (x _ {2} - x _ {1})) + \sigma (\rho x _ {1} - x _ {2} - x _ {1} x _ {3}) =\sigma \left[ (\sigma + \rho) x _ {1} - (\sigma + 1) x _ {2} - x _ {1} x _ {3} \right] =3 8 0 x _ {1} - 1 1 0 x _ {2} - 1 0 x _ {1} x _ {3}$$

记

$$g (x _ {1}, x _ {2}, x _ {3}) = 3 8 0 x _ {1} - 1 1 0 x _ {2} - 1 0 x _ {1} x _ {3} \tag {4.6.8}$$

则经过坐标变换(此变换是可逆的)

$$
\left\{ \begin{array}{l} y _ {1} = x _ {1} \\ y _ {2} = f _ {1} (x _ {1}, x _ {2}, x _ {3}) \\ y _ {3} = g (x _ {1}, x _ {2}, x _ {3}) \end{array} \right. \tag {4.6.9}
$$

得

$$
\left\{ \begin{array}{l} \dot {y} _ {1} = y _ {2} \\ \dot {y} _ {2} = y _ {3} \\ \dot {y} _ {3} = \frac {\partial g}{\partial x _ {1}} f _ {1} + \frac {\partial g}{\partial x _ {2}} f _ {2} + \frac {\partial g}{\partial x _ {3}} f _ {3} \\ y = y _ {1} \end{array} \right. \tag {4.6.10}
$$

式中： $\frac{\partial g}{\partial x_{1}}f_{1}+\frac{\partial g}{\partial x_{2}}f_{2}+\frac{\partial g}{\partial x_{3}}f_{3}=-6880x_{1}+3910x_{2}+236.67x_{1}x_{3}-100x_{2}x_{3}+10x_{1}^{2}x_{2}.$

对此系统用扩张状态观测器(4.6.4)进行估计. 取扩张状态观测器参数

$$h = 0. 0 0 1, \beta_ {0 1} = 1 0 0 0, \beta_ {0 2} = 3 0 0 0 0, \beta_ {0 3} = 8 0 0 0 0 0 \tag {4.6.11}$$

所作的仿真结果如图 4.6.2、图 4.6.3 所示.

图 4.6.2 和图 4.6.3 分别表示扩张状态观测器 (4.6.4) 的状态 $z_{1}, z_{2}$ 分别跟踪系统 (4.6.9) 的状态 $y_{1}, y_{2}$ 的情形. 每个图的下半部是上半部图的跟踪误差. 跟踪的相对误差只有千分之几的程度, $y_{i}$ 和 $z_{i}$ 几乎是“同步”的.

![](image/f68ee49803556a24c1b297178596b21070d609b2a0494ce4e02ce370d1a6949e.jpg)

<details>
<summary>line</summary>

| Time | Value |
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

图4.6.2  
![](image/237ab55e8bee46cb8053e6dcc28968b475ae01bb14506788d01495d1db106101.jpg)

<details>
<summary>line</summary>

| x | y1 | y2 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 10 | 0 | 0 |
| 20 | 0 | 0 |
| 30 | 0 | 0 |
| 40 | 0 | 0 |
| 50 | 0 | 0 |
| 60 | 0 | 0 |
| 70 | 0 | 0 |
| 80 | 0 | 0 |
| 90 | 0 | 0 |
| 100 | 0 | 0 |
</details>

图4.6.3

2. 针对 Rossler 系统
