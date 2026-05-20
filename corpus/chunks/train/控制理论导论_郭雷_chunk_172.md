用 $A_{1}x_{1}, B_{1}x_{2}, C_{1}x_{3}$ 分别乘式 (2.4.30) 中各个方程的两端并相加，得到

$$\frac {\mathrm{d}}{\mathrm{d} t} \big (A _ {1} x _ {1} ^ {2} + B _ {1} x _ {2} ^ {2} + C _ {1} x _ {3} ^ {2} \big) = 2 \big (k _ {1} A _ {1} x _ {1} ^ {2} + k _ {2} B _ {1} x _ {2} ^ {2} + k _ {3} C _ {1} x _ {3} ^ {2} \big).$$

现任意取 $k_{1} < 0, k_{2} < 0, k_{3} < 0$ ，并记

$$k = \min \left\{k _ {1}, k _ {2}, k _ {3} \right\}.$$

有

$$\frac {\mathrm{d}}{\mathrm{d} t} \left(A _ {1} x _ {1} ^ {2} + B _ {1} x _ {2} ^ {2} + C _ {1} x _ {3} ^ {2}\right) \leqslant 2 k \left(A _ {1} x _ {1} ^ {2} + B _ {1} x _ {2} ^ {2} + C _ {1} x _ {3} ^ {2}\right). \tag {2.4.31}$$

显然，标量函数

$$W (x _ {1}, x _ {2}, x _ {3}) = A _ {1} x _ {1} ^ {2} + B _ {1} x _ {2} ^ {2} + C _ {1} x _ {3} ^ {2}$$

是定义在整个 $\mathbb{R}^3$ 上的正定函数。不等式 (2.4.31) 表示 $W(x_1, x_2, x_3)$ 沿微分方程 (2.4.30) 对时间 $t$ 的全导数 $\dot{W}(x_1, x_2, x_3) \big|_{(2.4.30)}$ 是 $(x_1, x_2, x_3)$ 的负定函数。于是根据定理 2.4.8，微分方程 (2.4.30) 的零解 $x_1 = x_2 = x_3 = 0$ 是渐近稳定的。因此任意给定一组负数 $k_1, k_2, k_3$ ，当飞行器受到某初始干扰（无论它多大）时，只要根据式 (2.4.29) 来给出控制力矩，那么经过无穷长时间以后，飞行器总能恢复到指定的姿态（零态）。当然这在工程上是不可能的。其实只要恢复到指定姿态附近即可。这个时间将不是无穷，而是有穷时间。同时为了使恢复到指定姿态的某个给定邻域的时间尽可能快，可以通过调整常数 $k_1, k_2, k_3$ 来达到。

下面给出线性定常微分方程的 Lyapunov 函数. 对于线性定常向量微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x, \tag {2.4.32}$$

从定理2.4.1知道，根据方阵 $\pmb{A}$ 的特征值能够判别它的零平衡解的稳定性。下面将具体构造出微分方程(2.4.32)的Lyapunov函数。

定理2.4.15 对于线性定常向量微分方程(2.4.32)，如果它的系数矩阵 $\pmb{A}$ 的特征值皆具有负实部，那么存在正定二次型 $W(x)$ ，它沿方程(2.4.32)对时间 $t$ 的全导数为负定二次型.

证明 由假设可知，由下式确定的 $n \times n$ 矩阵

$$\boldsymbol {P} \stackrel {\text { def }} {=} \int_ {0} ^ {+ \infty} \mathrm{e} ^ {\boldsymbol {A} ^ {\mathrm{T}} t} \mathrm{e} ^ {\boldsymbol {A} t} \mathrm{d} t \tag {2.4.33}$$

有意义，并且是正定对称的．令 $W(x)=\frac{1}{2}x^{T}Px,x\in\mathbb{R}^{n}$

现设 $x(t)$ 为微分方程 (2.4.32) 的任一非零解。于是有

$$\dot {\boldsymbol {W}} (\boldsymbol {x} (t)) \mid_ {(2. 4. 3 2)} = \dot {\boldsymbol {x}} (t) ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} (t) + \boldsymbol {x} (t) ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {x}} (t). \tag {2.4.34}$$

将方程 (2.4.32) 及 $P$ 的表示式代入式 (2.4.34) 中不难得到

$$\dot {\boldsymbol {W}} (\boldsymbol {x} (t)) \mid_ {(2. 4. 3 2)} = \boldsymbol {x} (t) ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {A} \boldsymbol {P}) \boldsymbol {x} (t) = - \boldsymbol {x} (t) ^ {\mathrm{T}} \boldsymbol {x} (t).$$

因此 $\dot{W} (x(t))\mid_{(2.4.32)}$ 是负定二次型.

定理2.4.16 对于任意给定的 $n \times n$ 正定对称常值矩阵 $Q$ , 线性矩阵代数方程
