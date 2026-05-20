- 解标称状态方程的标称解 $x(t, \lambda_0)$ 。  
- 计算雅可比矩阵

$$A (t, \lambda_ {0}) = \left. \frac {\partial f (t , x , \lambda)}{\partial x} \right| _ {x = x (t, \lambda_ {0}), \lambda = \lambda_ {0}}, B (t, \lambda_ {0}) = \left. \frac {\partial f (t , x , \lambda)}{\partial \lambda} \right| _ {x = x (t, \lambda_ {0}), \lambda = \lambda_ {0}}$$

\- 解灵敏度方程(3.5)求 $S(t)$ 。

在上述步骤中,需要解非线性标称状态方程和线性时变灵敏度方程。除某些简单情况外,我们必须求这些方程的数值解。另一个计算 $S(t)$ 的方法是同时求标称解和灵敏度函数,可以对初始状态方程附加变分方程(3.4),然后设 $\lambda = \lambda_{0}$ ,获得 $(n + np)$ 阶增广方程

$$
\begin{array}{l} \dot {x} = f (t, x, \lambda_ {0}), \quad x \left(t _ {0}\right) = x _ {0} \\ \dot {S} = \left[ \frac {\partial f (t , x , \lambda)}{\partial x} \right] _ {\lambda = \lambda_ {0}} S + \left[ \frac {\partial f (t , x , \lambda)}{\partial \lambda} \right] _ {\lambda = \lambda_ {0}}, S (t _ {0}) = 0 \tag {3.7} \\ \end{array}
$$

这样就可用数值方法求解。注意,如果初始状态方程是自治的,也就是说, $f(t,x,\lambda)=f(x,\lambda)$ ,那么增广方程(3.7)也是自治的。后面的步骤将在下面的例题中说明。

例3.7 考虑锁相环模型

$$
\begin{array}{r c l r c l} \dot {x} _ {1} & = & x _ {2} & = & f _ {1} (x _ {1}, x _ {2}) \\ \dot {x} _ {2} & = & - c \sin x _ {1} - (a + b \cos x _ {1}) x _ {2} & = & f _ {2} (x _ {1}, x _ {2}) \end{array}
$$

并假设参数 $a, b$ 和 $c$ 的标称值为 $a_0 = 1, b_0 = 0, c_0 = 1$ ，则标称系统为

$$
\begin{array}{r c l} \dot {x} _ {1} & = & x _ {2} \\ \dot {x} _ {2} & = & - \sin x _ {1} - x _ {2} \end{array}
$$

雅可比矩阵 $[\partial f / \partial x]$ 和 $[\partial f / \partial \lambda]$ 由下式给出：

$$
\begin{array}{l} \frac {\partial f}{\partial x} = \left[ \begin{array}{c c} 0 & 1 \\ - c \cos x _ {1} + b x _ {2} \sin x _ {1} & - (a + b \cos x _ {1}) \end{array} \right] \\ \frac {\partial f}{\partial \lambda} = \left[ \begin{array}{l l l} \frac {\partial f}{\partial a} & \frac {\partial f}{\partial b} & \frac {\partial f}{\partial c} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ - x _ {2} & - x _ {2} \cos x _ {1} & - \sin x _ {1} \end{array} \right] \\ \end{array}
$$

计算标称参数 a=1, b=0, c=1 时的雅可比矩阵, 得

$$
\left. \frac {\partial f}{\partial x} \right| _ {\text {标称}} = \left[ \begin{array}{c c} 0 & 1 \\ - \cos x _ {1} & - 1 \end{array} \right]

\left. \frac {\partial f}{\partial \lambda} \right| _ {\text {标称}} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ - x _ {2} & - x _ {2} \cos x _ {1} & - \sin x _ {1} \end{array} \right]
$$
