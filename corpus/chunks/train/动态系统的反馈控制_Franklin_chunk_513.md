# 7.7节习题

7.34 考虑系统：

$$
\boldsymbol {A} = \left[ \begin{array}{c c} - 2 & 1 \\ 1 & 0 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right], \quad \boldsymbol {C} = \left[ \begin{array}{l l} 1 & 2 \end{array} \right]
$$

假定采用的反馈形式为 $u = -Kx + r$ ，其中 r 为参考输入信号。

(a) 证明(A, C)是可观测的。

(b) 证明存在一个 K，使得 $(A - BK, C)$ 是不可观测的

(c) 计算一个形如 $K=\left[1\ K_{2}\right]$ 的 K，使 (b) 问中的系统是不可观测的。即找出一个 $K_{2}$ ，使得闭环系统不可观测。

(d) 比较开环传递函数与(c)问中的闭环传递函数。不可观测性是由什么引起的？

7.35 考虑具有如下传递函数的系统：

$$G (s) = \frac {9}{s ^ {2} - 9}$$

(a) 求该系统的能观标准形矩阵 $(A_{0}, B_{0}, C_{0})$ 。

(b) $(A_{0}, B_{0})$ 是可控的吗？

(c) 计算 K，使得闭环极点配置到 $s = -3 \pm 3j$ 。

(d)(c)问中的闭环系统是可观测的吗?

(e) 设计一个全阶估计器，使得估计器误差极点在 $s = -12 \pm 12j$ 上。

(f) 假设将系统改为有一个零点的形式：

$$G _ {1} (s) = \frac {9 (s + 1)}{s ^ {2} - 9}$$

证明：若 $u = -Kx + r$ ，则存在一个反馈增益 K，使得闭环系统是不可观测的[再为 $G_{1}(s)$ 设计一种能观标准形实现]。

![](image/98008d41003df455df296b2770c6b8bba12d2554cf419d5e4d3588ed1fdfd998.jpg)

<details>
<summary>text_image</summary>

iL
L
C
+
vc
-
R
R
u
y
-
</details>

图 7.90 习题 7.37 的电路

7.36 说明线性系统可控性、可观测性和稳定性之间有何关系？

7.37 考虑如图 7.90 所示的电路图。

(a) 写出该电路的内部(状态)方程。输入 $u(t)$ 为电流，输出 y 为电压。令 $x_{1}=i_{L}$ 和 $x_{2}=v_{C}$ 。

(b) 为保证系统是可控的，R、L、C 应满足什么条件？

(c) 为保证系统是可观测的，R、L、C 应满足什么条件？

7.38 某反馈系统的框图如图 7.91 所示，系统状态为

$$
x = \left[ \begin{array}{c} x _ {\mathrm{p}} \\ x _ {\mathrm{f}} \end{array} \right]
$$

矩阵的维数如下：

$$\boldsymbol {A} = n \times n, \quad \boldsymbol {L} = n \times 1\boldsymbol {B} = n \times 1, \quad x = 2 n \times 1C = 1 \times n, \quad r = 1 \times 1\boldsymbol {K} = 1 \times n, \quad y = 1 \times 1$$

(a) 写出该系统的状态方程。

(b) 令 $x = Tz$ ，其中：

$$
\boldsymbol {T} = \left[ \begin{array}{c c} \boldsymbol {I} & \boldsymbol {0} \\ \boldsymbol {I} & \boldsymbol {I} \end{array} \right]
$$

证明系统是不可控的。

(c) 求出该系统从 r 到 y 的传递函数。

7.39 本题旨在使你增进对可控性和可观测性的理解。考虑如图 7.92 所示的电路，输入电压电源为 $u(t)$ ，输出电流为 $y(t)$ 。

(a) 用电容电压和电感电流为状态变量，写出该系统的状态方程和输出方程。

(b) 求出使得系统不可控， $R_{1}$ 、 $R_{2}$ 、C 和 L应该满足的条件。找出一族相似的条件使得系统不可观测。

![](image/222acc22aefa65620cb46de8a9385ad05bfed079fabf60c58259524393d5cf06.jpg)

<details>
<summary>flowchart</summary>
