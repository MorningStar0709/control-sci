$$
v = - \beta (\cdot) \varphi (s / \varepsilon), \quad \varepsilon > 0, \quad \varphi (y) = \left\{ \begin{array}{l l} y / \| y \| _ {2}, & \| y \| _ {2} \geqslant 1 \\ y, & \| y \| _ {2} <   1 \end{array} \right.
$$

其中 $\beta$ 可能与 $(q, \dot{q}, q_{r}, \dot{q}_{r}, \ddot{q}_{r})$ 有关，证明应如何选择 $\beta$ 才能保证误差 e 全局一致毕竟有界，并估计最终边界与 $\varepsilon$ 的关系。

(d) 当 $\beta$ 取一个常数时, 证明该滑模控制器具有哪些性质?

14.54 两连杆机器人如图 14.23 所示, 可用方程(14.120)建立模型 $^{[171]}$ , 其中

$$
M = \left[ \begin{array}{c c} a _ {1} + 2 a _ {4} \cos q _ {2} & a _ {2} + a _ {4} \cos q _ {2} \\ a _ {2} + a _ {4} \cos q _ {2} & a _ {3} \end{array} \right], \quad C = a _ {4} \sin q _ {2} \left[ \begin{array}{c c} - \dot {q} _ {2} & - (\dot {q} _ {1} + \dot {q} _ {2}) \\ \dot {q} _ {1} & 0 \end{array} \right]

g = \left[ \begin{array}{c} b _ {1} \cos q _ {1} + b _ {2} \cos (q _ {1} + q _ {2}) \\ b _ {2} \cos (q _ {1} + q _ {2}) \end{array} \right]
$$

式中 $a_{1}$ 到 $a_{4}, b_{1}$ 和 $b_{2}$ 都是正常数，与质量、转动惯量、两个连杆的长度以及重力加速度有关。忽略阻尼并取 D=0，设各参数的标称值为

$$a _ {1} = 2 0 0. 0 1, a _ {2} = 2 3. 5, a _ {3} = 1 2 2. 5, a _ {4} = 2 5, b _ {1} = 7 8 4. 8, b _ {2} = 2 4 5. 2 5$$

为将臂从位置 $(q_{1} = 0,q_{2} = 0)$ 移动到 $(q_{1} = \pi /2,q_{2} = \pi /2)$ ，取参考轨线为

$$q _ {r 1} (t) = q _ {r 2} (t) = (\pi / 2) [ 1 - \exp (- 5 t) (1 + 5 t) ]$$

假设把控制输入限制为 $|u_{1}|\leqslant6000\ Nm,|u_{2}|\leqslant5000\ Nm$ 。在前两题中我们设计了四个滑模控制律，分别是

$$
\begin{array}{l} u = - \hat {M} \beta \operatorname{sat} (s / \varepsilon) \\ u = - \hat {M} \beta \operatorname{sat} (s / \varepsilon) + \hat {C} \dot {q} + \hat {g} + \hat {M} \ddot {q} _ {r} - \hat {M} \Lambda \dot {e} \\ u = - \beta \varphi (s / \varepsilon) \\ u = - \beta \varphi (s / \varepsilon) + \hat {C} (\dot {q} _ {r} - \Lambda e) + \hat {g} + \hat {M} \ddot {q} _ {r} - \hat {M} \Lambda \dot {e} \\ \end{array}
$$

为方便, $\beta$ 取常数。

(a) 通过仿真,选择各控制器的设计参数 $\Lambda,\beta$ 和 $\varepsilon$ ,在仿真中包含一个限幅器作为控制约束。

(b) 由未知负载引起的振动,使实际系统参数变为

$$a _ {1} = 2 5 9. 7, a _ {2} = 5 8. 1 9, a _ {3} = 1 5 7. 1 9, a _ {4} = 5 6. 2 5, b _ {1} = 1 0 3 0. 1, b _ {2} = 5 5 1. 8 1 2 5$$

比较此时四个控制器的性能。

(c) 假设只能测量角度 $q_{1}$ 和 $q_{2}$ ，设计一个高增益观测器以实现状态反馈控制器。通过仿真，比较其中一种控制律的状态反馈控制器和输出反馈控制器的性能。

14.55 重新考虑上题中的两连杆机器人，

(a) 根据例 14.16, 设计一个基于无源的控制器, 把角度 $(q_{1}, q_{2})$ 从 $(0,0)$ 调节到 $(\pi/2, \pi/2)$ 。运用仿真选择参数 $K_{p}$ 和 $K_{d}$ , 并与上题中的滑模控制器相比较。

(b) 假设只能测量角度 $q_{1}$ 和 $q_{2}$ ，设计一个高增益观测器实现状态反馈控制器。运用仿真，比较状态反馈控制器与输出反馈控制器的性能。

![](image/b7683b8f46dd795aa97d4a4cf9f8f85af752a8da76ffedfa3b8eabe8da7dbbe7.jpg)

<details>
<summary>text_image</summary>

负载
q₂
q₁
</details>

图 14.23 两连杆机器人
