# 7.5节习题

7.21 考虑如下描述的被控对象：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ 7 & - 4 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] \boldsymbol {u}

y = \left[ \begin{array}{l l} 1 & 3 \end{array} \right] x
$$

(a) 画出该被控对象的框图，其每个状态变量对应一个积分器。

(b) 用矩阵代数求出传递函数。

(c) 若反馈如下，求出闭环特征方程：

(i) $u = -\left[K_{1} \quad K_{2}\right]x;$

(ii) $u=-Ky$ 。

7.22 对于系统：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 6 & - 5 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u
$$

设计一个满足如下性能指标的状态反馈控制器。

(a) 闭环极点的阻尼系数为 $\zeta=0.707$ 。

(b) 阶跃响应的峰值时间小于 3.14s。

用 Matlab 验证设计结果。

7.23 (a)为下面的系统设计一个状态反馈控制器，使其满足：闭环阶跃响应的超调低于 $25\%$ ，且 $1\%$ 的调整时间低于

0.115s。

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 1 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \boldsymbol {u}
$$

(b) 用 Matlab 的 step 命令验证你的设计符合指标要求。如果不符合，相应地更改反馈增益。

7.24 考虑系统

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} - 1 & - 2 & - 2 \\ 0 & - 1 & 1 \\ 1 & 0 & - 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 2 \\ 0 \\ 1 \end{array} \right] u
$$

(a) 为该系统设计一个状态反馈控制器，使得闭环阶跃响应的超调低于 5%，且 1% 的调整时间小于 4.6s。

(b) 用 Matlab 中的 step() 函数验证你的设计满足指标要求。如果不符合，相应地更改反馈增益。

7.25 考虑如图 7.87 所示系统。

![](image/be994b59ebeaa78e1268aa5b5ac24da7bcb63b266292fefad8b492e4a0c8efb2.jpg)  
图 7.87 习题 7.25 的系统

(a) 写出描述该系统的一组能控标准形方程，形如：

$$\dot {x} = A x + B u \text {和} y = C x$$

(b) 设计如下形式的控制律

$$
u = - \left[ \begin{array}{l l} K _ {1} & K _ {2} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right]
$$

使闭环极点配置到 $s = -2 \pm 2j$ 。

7.26 输出可控性。在很多情况下，控制工程师更感兴趣的是控制输出 y 而不是状态 x。如果在任意时刻，用适当的控制信号 $u \times$ 均能在有限的时间内将输出从零转移到任意期望的输出 $y \times$ ，则称系统是输出可控的。推导使连续系统 $(A, B, C)$ 是输出可控的充分必要条件。状态可控性与输出可控性有关系吗？若有，关系是什么？

7.27 考虑如下系统

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{r r r r} 0 & 4 & 0 & 0 \\ - 1 & - 4 & 0 & 0 \\ 5 & 7 & 1 & 1 5 \\ 0 & 0 & 3 & - 3 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \\ 0 \end{array} \right] u
$$

(a) 求出该系统的特征根(提示: 注意 A 的三角分块结构)。  
(b) 找出该系统的可控与不可控模态。  
(c) 为每一个不可控模态找出一个矢量 v，满足

$$\boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {B} = 0, \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {A} = \lambda \boldsymbol {v} ^ {\mathrm{T}}$$

(d) 证明存在无穷个反馈增益 K 使得系统的极点重新配置在 -5、-3、-2 和 -2 上。  
(e) 找出唯一矩阵 K，获得这些极点位置，且能防止系统不可控部分的初始状态影响可控部分。
