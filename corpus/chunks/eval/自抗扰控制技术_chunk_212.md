![](image/6206e3f526138e39f7d3d8a1024a54db5674630954e0dcd51236a63b6ad1ab1f.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 10 | 2 |
| 20 | 2 |
| 30 | 2 |
| 40 | 2 |
| 50 | 2 |
| 60 | 2 |
| 70 | 2 |
| 80 | 2 |
| 90 | 2 |
| 100 | 2 |

Legend:
| Parameter | Value |
| --- | --- |
| h | 0.01, β = 100, β = 3000, β = 30000
r₀ | 0.5, r = 40, β = 10, β = 5 |
The chart displays a single continuous curve with parameters h, β, r, and r₀. The function f(x) is calculated as (a - a₁x - a₂x + y) * sign((x(1,t)).
</details>

图6.2.3

假定对象为“最小相位”系统，即 $q(s)$ 是稳定多项式，且确切知道。这时我们可以用如下方式解决这类系统的控制问题。首先用自抗扰控制器来决定虚拟控制量 $U(t)$ ，然后以 $U(t)$ 为输入，求解系统 $u = \frac{1}{q(s)} U$ 来决定实际控制量 $u(t)$ 。

设 $p(s) = s^3 + a_3s^2 + a_2s + a_1, q(s) = s^2 + 2s + 1$ ，设定值为 $v(t) = 2.0$ . 对这个系统设计的控制算法为

$$
\left\{ \begin{array}{l} f _ {s} = - r (r (r (v _ {1} - v (t)) + 3 v _ {2}) + 3 v _ {3}) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h v _ {3} \\ v _ {3} = v _ {3} + h f s \\ e = z _ {1} - y \\ z _ {1} = z _ {1} + h (z _ {2} - \beta_ {0 1} e) \\ z _ {2} = z _ {2} + h (z _ {3} - \beta_ {0 2} e) \\ z _ {3} = z _ {3} + h (z _ {4} - \beta_ {0 3} e + U) \\ z _ {4} = z _ {4} + h (- \beta_ {0 4} e) \\ \left\{ \begin{array}{l} e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2}, e _ {3} = v _ {3} - z _ {3} \\ U = \beta_ {1} e _ {1} + \beta_ {2} e _ {2} + \beta_ {3} e _ {3} - z _ {4} \end{array} \right. \end{array} \right. \tag {6.2.17}

\left\{ \begin{array}{l} \mathrm{fu} = - (U _ {1} - U) - 2 U _ {2} \\ U _ {1} = U _ {1} + h U _ {2} \\ U _ {2} = U _ {2} + h \mathrm{fu} \\ u = U _ {1} \end{array} \right. \tag {6.2.19}
$$

原对象运动轨迹的积分是按如下方式递推决定

$$
\left\{ \begin{array}{l} f = - a _ {1} x _ {1} - a _ {2} x _ {2} - a _ {3} x _ {3} + \gamma \operatorname{sign} (\sin (t / 1 0)) \\ x _ {1} = x _ {1} + h x _ {2} \\ x _ {2} = x _ {2} + h x _ {3} \\ x _ {3} = x _ {3} + h (f + u) \\ y = x _ {1} + 2 x _ {2} + x _ {3} \end{array} \right. \tag {6.2.20}
$$

对象参数取 $a_{1}=1.0, a_{2}=2.0, a_{3}=3.0$ ，扩张状态观测器的参数为

$$\beta_ {0 1} = 1 0 0. 0, \beta_ {0 2} = 3 0 0 0. 0, \beta_ {0 3} = 3 0 0 0 0. 0, \beta_ {0 4} = 2 0 0 0 0 0. 0$$

反馈增益取为

$$\beta_ {1} = 2. 0, \beta_ {2} = 5. 0, \beta_ {3} = 4. 0$$

时的仿真结果如图6.2.4所示.对象参数变成 $a_1 = -1.0, a_2 = -2.0, a_3 = -3.0$ ，即开环不稳定，而控制器参数保持不变时的仿真结果如图6.2.5所示.

![](image/db57c3f73472c9d37ccd65a27f441f2e9592b050695c763d264025fa9d505bf1.jpg)

<details>
<summary>line</summary>
