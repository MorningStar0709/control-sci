$$
\begin{array}{l} \dot {x} _ {2} = x _ {2} + u \\ y = x _ {1} \\ \end{array}
$$

例13.2 考虑系统 $\dot{x}_{1} = x_{1}$

计算 $y$ 的导数，得

$$\dot {y} = \dot {x} _ {1} = x _ {1} = y$$

因而，对于所有 $n \geqslant 1, y^{(n)} = y = x_1$ 。在这种情况下，系统不具有符合上述定义的相对阶。

由于本例很简单,不难看出这是因为输出 $y(t)=x_{1}(t)=e^{t}x_{1}(0)$ 与输入 u 无关。

例 13.3 一个场控直流电动机, 若忽略轴阻尼, 其模型为状态方程(见习题 1.17):

$$
\begin{array}{l} \dot {x} _ {1} = - a x _ {1} + u \\ \dot {x} _ {2} = - b x _ {2} + k - c x _ {1} x _ {3} \\ \dot {x} _ {3} = \theta x _ {1} x _ {2} \\ \end{array}
$$

其中， $x_{1},x_{2}$ 和 $x_{3}$ 分别是场励磁电流、电枢电流和角速度，a,b,c,k 和 $\theta$ 是正常数。对于速度控制，选择输出为 $y=x_{3}$ ，则输出导数为

$$
\begin{array}{l} \dot {y} = \dot {x} _ {3} = \theta x _ {1} x _ {2} \\ \ddot {y} = \theta x _ {1} \dot {x} _ {2} + \theta \dot {x} _ {1} x _ {2} = (\cdot) + \theta x _ {2} u \\ \end{array}
$$

这里(·)中的各项为 $x$ 的函数。系统在区域 $D_0 = \{x \in R^3 | x_2 \neq 0\}$ 上的相对阶为2。

例 13.4 考虑一个线性系统, 其传递函数为

$$H (s) = \frac {b _ {m} s ^ {m} + b _ {m - 1} s ^ {m - 1} + \cdots + b _ {0}}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {0}}$$

其中 $m < n$ 且 $b_{m} \neq 0$ 。系统的状态模型可取为

$$\dot {x} = A x + B uy = C x$$

这里

$$
\begin{array}{r l} A & = \left[ \begin{array}{c c c c c c c c c} 0 & 1 & 0 & \dots & & & \dots & 0 \\ 0 & 0 & 1 & \dots & & & \dots & 0 \\ \vdots & & \ddots & & & & & \vdots \\ & & & \ddots & & & & \\ & & & & \ddots & & & \\ \vdots & & & & & \ddots & & 0 \\ 0 & & & & & & 0 & 1 \\ - a _ {0} & - a _ {1} & \dots & \dots & - a _ {m} & \dots & \dots & - a _ {n - 1} \end{array} \right] _ {n \times n}, B = \left[ \begin{array}{c} 0 \\ 0 \\ \vdots \\ \\ \vdots \\ 0 \\ 1 \end{array} \right] _ {n \times 1} \\ C & = \left[ \begin{array}{c c c c c c c c c} b _ {0} & b _ {1} & \dots & \dots & b _ {m} & 0 & \dots & 0 \end{array} \right] _ {1 \times n} \end{array}
$$

该线性状态模型是系统(13.7)\~(13.8)的特例,其中 $f(x)=Ax,g=B,h(x)=Cx$ 。为检验系统的相对阶,我们计算输出的导数。其一阶导数为

$$\dot {y} = C A x + C B u$$

如果 m=n-1，则 $CB=b_{n-1}\neq0$ ，系统的相对阶为 1；否则 CB=0，继续计算二阶导数 $y^{(2)}$ 。注意，CA 是一个行向量，由 C 的元素右移一次得到，而 $CA^{2}$ 由 C 的元素右移两次得到，依次类推，可知

$$C A ^ {i - 1} B = 0, \quad i = 1, 2, \dots , n - m - 1, \quad C A ^ {n - m - 1} B = b _ {m} \neq 0$$

这样， $u$ 首次出现在 $y^{(n - m)}$ 的方程中，即

$$y ^ {(n - m)} = C A ^ {n - m} x + C A ^ {n - m - 1} B u$$

系统的相对阶是 n-m，即 $H(s)$ 的分母多项式与分子多项式的次数之差 $^{①}$ 。

为了进一步研究可输入-输出线性化系统的控制和内部稳定问题,我们先讨论上例的线性系统。传递函数 $H(s)$ 可写为

$$H (s) = \frac {N (s)}{D (s)}$$

其中 $\deg D = n, \deg N = m < n$ 。 $\rho = n - m$ 。由欧几里得除法， $D(s)$ 可写为

$$D (s) = Q (s) N (s) + R (s)$$

其中 $Q(s)$ 和 $R(s)$ 分别为多项式的商和余数。由欧几里得除法法则可知

$$\deg Q = n - m = \rho , \quad \deg R < m$$

$Q(s)$ 的首项系数是 $1/b_{m}$ 。根据该 $D(s)$ 的表达式， $H(s)$ 可重写为
