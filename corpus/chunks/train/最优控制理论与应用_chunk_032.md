# 2.2 有约束条件的函数极值问题

前面讨论函数的极值问题时,向量 X 的各个分量可独立地选择,相互间无约束。本节将讨论 X 的各分量满足一定约束条件的情况。

设具有 $n$ 个变量的多元函数为

$$f (\textbf {X}) = f (x _ {1}, x _ {2}, \dots , x _ {n})$$

X 的各分量满足下面的 m 个等式约束方程：

$$g _ {j} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) = 0 \quad j = 1, 2, \dots , m (m < n) \tag {2-13}$$

若能从 m 个约束方程中解出 m 个 X 的分量, 即将它们用其他 n-m 个 X 的分量表示, 那么 X 中只剩下 n-m 个独立变量, 于是问题可化为求 n-m 个变量的多元函数的无约束极值问题。这就是所谓的“消去法”。由于从 m 个方程(一般是非线性方程) 求出 m 个分量常常是困难的, 故经常采用“拉格朗日乘子法”。为此, 对 m 个约束方程, 引入 m 个拉格朗日乘子 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$ , 并作出一个辅助函数——拉格朗日函数

$$
\begin{array}{l} L \left(x _ {1}, x _ {2}, \dots , x _ {n}; \lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {m}\right) \\ = f \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) + \sum_ {j = 1} ^ {m} \lambda_ {j} g _ {j} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \tag {2-14} \\ \end{array}
$$

若令

$$\boldsymbol {\lambda} = \left[ \lambda_ {1}, \lambda_ {2}, \dots , \lambda_ {m} \right] ^ {\mathrm{T}} \quad \boldsymbol {G} = \left[ g _ {1}, g _ {2}, \dots , g _ {m} \right] ^ {\mathrm{T}}$$

则式 $(2-14)$ 可用向量形式表示为

$$L (\boldsymbol {X}, \boldsymbol {\lambda}) = f (\boldsymbol {X}) + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {G} (\boldsymbol {X}) \tag {2-15}$$

于是 $f(X)$ 的条件极值问题就化为 $L(X, \lambda)$ 的无条件极值问题。函数 $L$ 有极值的必要条件为

$$
\begin{array}{l} \frac {\partial L}{\partial x _ {i}} = \frac {\partial f}{\partial x _ {i}} + \sum_ {j = 1} ^ {m} \lambda_ {j} \frac {\partial g _ {j}}{\partial x _ {i}} = 0 \quad i = 1, 2, \dots , n \\ \frac {\partial L}{\partial \lambda_ {j}} = g _ {j} \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) = 0 \quad j = 1, 2, \dots , m \\ \end{array}
$$

例2-3 求从原点 $(0,0,0)$ 至平面

$$g \left(x _ {1}, x _ {2}, x _ {3}\right) = a x _ {1} + b x _ {2} + c x _ {3} + d = 0$$

的最短距离。

解 原点至空间任何一点 $(x_{1}, x_{2}, x_{3})$ 的距离的平方为

$$f (x _ {1}, x _ {2}, x _ {3}) = x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2}$$

要使 $f(x_{1},x_{2},x_{3})$ 极小，而点 $(x_{1},x_{2},x_{3})$ 必须在 $g(x_{1},x_{2},x_{3}) = 0$ 所规定的平面上。这是一个条件极值问题。作拉格朗日函数

$$
\begin{array}{l} L \left(x _ {1}, x _ {2}, x _ {3}\right) = f \left(x _ {1}, x _ {2}, x _ {3}\right) + \lambda g \left(x _ {1}, x _ {2}, x _ {3}\right) \\ = x _ {1} ^ {2} + x _ {2} ^ {2} + x _ {3} ^ {2} + \lambda \left(a x _ {1} + b x _ {2} + c x _ {3} + d\right) \\ \end{array}
$$

极值的必要条件为

$$\frac {\partial L}{\partial x _ {1}} = 2 x _ {1} + a \lambda = 0\frac {\partial L}{\partial x _ {2}} = 2 x _ {2} + b \lambda = 0\frac {\partial L}{\partial x _ {3}} = 2 x _ {3} + c \lambda = 0\frac {\partial L}{\partial \lambda} = a x _ {1} + b x _ {2} + c x _ {3} + d = 0$$
