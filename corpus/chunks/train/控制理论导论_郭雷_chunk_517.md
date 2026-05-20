# 习题 7.1

7.1.1 设

$$
\left\{ \begin{array}{l} \dot {x} _ {1} (t) = u (t), \\ \dot {x} _ {2} (t) = x _ {1} (t) + \frac {1}{2} u ^ {2} (t), \end{array} \right. \tag {7.1.83}
$$

其中 $x_{1}(0) = x_{10}, x_{2}(0) = x_{20}, u(t) \in \mathbb{R}$ , 性能指标为

$$J [ u ] = x _ {1} (1).$$

试求出上述系统的最优控制和最优轨线.

7.1.2 利用极大值原理证明：保守系统是能量守恒的，提示：力学中的Hamilton原理叙述为：一个保守系统从初始时刻 $t_0$ 开始到 $t_f (> t_0)$ 时刻结束的运动是使如下积分：

$$\int_ {t _ {0}} ^ {t _ {f}} l (x (t), \dot {x} (t)) \mathrm{d} t,$$

达到极小的运动，其中 $x \in \mathbb{R}^n$ 为系统的广义坐标， $\dot{x} = \frac{\mathrm{d}x}{\mathrm{d}t}$ 为广义速度， $l(x, \dot{x}) \stackrel{\mathrm{def}}{=} T(\dot{x}) - V(x)$ ， $T(\dot{x}) = \dot{x}^{\mathrm{T}} Q x$ 和 $V(x)$ 分别是系统的 Lagrange 函数，系统的动能和势能， $Q$ 为正定对称常阵。注意到，不同的广义速度 $\dot{x}(t)$ 对应于不同的运动，即可将 $\dot{x}$ 视为控制量，于是 $\dot{x} = u$ 可视为保守系统的状态方程。

7.1.3 证明引理 7.1.1.

7.1.4 大气层外质点A和质点B的最优交会问题可描述为状态方程

$$
\left\{ \begin{array}{l} \dot {x} = v, \\ \dot {v} - \frac {F (t)}{m} u, \\ \dot {m} = - \frac {1}{C} F (t), \end{array} \right.
$$

其中 $x \in \mathbb{R}^3, v \in \mathbb{R}^3$ 分别表示质点 A 和 B 的相对位置向量，相对速度向量， $F(t)$ 和 $u$ 为质点 A 的控制加速度大小和方向， $m$ 为质点 A 的质量， $C$ 为有效排气速度.

初始条件： $x(t_0) = x_0, v(t_0) = v_0, m(t_0) = m_0.$

控制约束：

$$
\left\{ \begin{array}{l} 0 \leqslant F (t) \leqslant \max F (t) \stackrel {\text { def }} {=} F, \\ u ^ {T} u = 1. \end{array} \right.
$$

终端条件： $x(t_{f}) = 0, v(t_{f}) = 0, m(t_{f})\geqslant m_{e}$ （质点A的有效载荷）.

性能指标:

$$J [ F (\cdot), u (\cdot) ] = \int_ {t _ {0}} ^ {t _ {f}} [ c _ {1} + F (t) ] \mathrm{d} t, \qquad c _ {1} > 0 \text {常数}.$$

试利用极大值原理讨论质点 A 和 B 的最优交会问题.
