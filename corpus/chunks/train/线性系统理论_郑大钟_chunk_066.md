# 2.2 线性定常系统的运动分析

零输入响应 给定线性定常系统的自治方程, 即在 (2.2) 中取输入 $u = 0$ 所导出的

方程

$$\dot {x} = A x, x (0) = x _ {0}, t \geqslant 0 \tag {2.10}$$

其中， $x$ 为 $n$ 维状态向量， $A$ 为 $n\times n$ 常阵。再定义 $n\times n$ 的矩阵函数

$$e ^ {A t} \triangleq I + A t + \frac {1}{2 !} A ^ {2} t ^ {2} + \dots = \sum_ {k = 0} ^ {\infty} \frac {1}{k !} A ^ {k} t ^ {k} \tag {2.11}$$

并称其为矩阵指数函数。那么，对线性定常系统的零输入响应，可导出如下的结论。

结论1 由(2.10)所描述的线性定常系统的零输入响应的表达式为

$$\phi (t; 0, x _ {0}, 0) = e ^ {A t} x _ {0}, t \geqslant 0 \tag {2.12}$$

证 令方程(2.10)的解为系数向量待定的一个幂级数,即

$$x (t) = b _ {0} + b _ {1} t + b _ {2} t ^ {2} + \dots = \sum_ {k = 0} ^ {\infty} b _ {k} t ^ {k}, \quad t \geqslant 0 \tag {2.13}$$

则由其必须满足方程(2.10)，可导出

$$\boldsymbol {b} _ {1} + 2 \boldsymbol {b} _ {2} t + 3 \boldsymbol {b} _ {3} t ^ {2} + \dots = A \boldsymbol {b} _ {0} + A \boldsymbol {b} _ {1} t + A \boldsymbol {b} _ {2} t ^ {2} + \dots \tag {2.14}$$

从而，由比较上列等式两边 $t^{k}(k=0,1,\cdots)$ 的系数向量，可定出待定向量 $b_{1}, b_{2}, b_{3}, \cdots$ 为：

$$\boldsymbol {b} _ {1} = A \boldsymbol {b} _ {0}, \quad \boldsymbol {b} _ {2} = \frac {1}{2} A \boldsymbol {b} _ {1} = \frac {1}{2 !} A ^ {2} \boldsymbol {b} _ {0}, \quad \boldsymbol {b} _ {3} = \frac {1}{3} A \boldsymbol {b} _ {2} = \frac {1}{3 !} A ^ {3} \boldsymbol {b} _ {0},\dots , b _ {k} = \frac {1}{k} A b _ {k - 1} = \frac {1}{k !} A ^ {k} b _ {0}, \dots \tag {2.15}$$

将(2.15)代入(2.13)，可把解的表达式进而表为：

$$\boldsymbol {x} (t) = \left(I + A t + \frac {1}{2 !} A ^ {2} t ^ {2} + \frac {1}{3 !} A ^ {3} t ^ {3} + \dots\right) \boldsymbol {b} _ {0}, \quad t \geqslant 0 \tag {2.16}$$

令上式中 $t = 0$ ，并考虑到其应满足初始条件即 $\pmb{x}(0) = \pmb{x}_0$ ，又可定出

$$\boldsymbol {b} _ {0} = \boldsymbol {x} _ {0} \tag {2.17}$$

于是，将(2.17)代入(2.16)，并利用(2.11)，就可导出(2.12)。证明完成。

下面，对由（2.12）所给出的线性定常系统的零输入响应，作如下的几点解释：

① 如果将 $t$ 取为某个固定值，那么零输入响应 $\phi(t;0,x_0,0)$ 即为状态空间中由初始状态 $x_0$ 经线性变换阵 $e^{At}$ 所导出的一个变换点。因此，系统的自由运动就是由初始状态 $x_0$ 出发的，并由 $x_0$ 的各时刻的变换点所组成的一条轨线。

② 自由运动轨线的形态，也即零输入响应的形态，是由矩阵指数函数 $e^{At}$ 所唯一地决定的。 $e^{At}$ 包含了自由运动性质的全部信息。

③ 如果当 $t \to \infty$ 时自由运动轨线最终趋向于系统 (2.10) 的平衡状态 $x = 0$ (即状态空间的原点), 则称系统是渐近稳定的。由 (2.12) 可容易看出, 线性定常系统为渐近稳定的充分必要条件是

$$\lim _ {t \rightarrow \infty} e ^ {A t} = 0 \tag {2.18}$$

进一步，当且仅当矩阵 $A$ 的特征值均具有负实部，也即均位于左半开复平面时，式（2.18）成立。对于这一点，可说明如下：首先，考虑一种较为特殊的情况，设 $A$ 的 $n$ 个特征值 $\lambda_1, \lambda_2, \cdots, \lambda_n$ 为两两相异，则由（1.58）可导出：

$$
A = P \left[ \begin{array}{c c c} \lambda_ {1} & & \\ & \ddots & \\ & & \lambda_ {n} \end{array} \right] P ^ {- 1} \tag {2.19}
$$

其中 P 为常数矩阵。于是，由此就有
