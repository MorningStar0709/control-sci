# 2. 求解 TSP 问题的 Hopfield 网络设计

TSP 问题是在一个城市集合 $\{A_{c}, B_{c}, C_{c}, \cdots\}$ 中找出一个最短且经过每个城市各一次并回到起点的路径。为了将 TSP 问题映射为一个神经网络的动态过程，Hopfield 采取了换位矩阵的表示方法，用 $N \times N$ 矩阵表示商人访问 N 个城市。例如，有 4 个城市 $\{A_{c}, B_{c}, C_{c}, D_{c}\}$ ，访问路线是 $D_{c} \rightarrow A_{c} \rightarrow C_{c} \rightarrow B_{c} \rightarrow D_{c}$ ，则 Hopfield 网络输出所代表的有效解用表 8-2 来表示，其中“1”代表到达，“0”代表未到达。

表 8-2 4 个城市的访问路线

<table><tr><td>城市\次序</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td> $A_c$ </td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $B_c$ </td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $C_c$ </td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $D_c$ </td><td>1</td><td>0</td><td>0</td><td>0</td></tr></table>

表 8-2 构成了一个 $4 \times 4$ 的矩阵，该矩阵中，各行各列只有一个元素为 1，其余为 0，否则是一个无效的路径。采用 $V_{xi}$ 表示神经元 $(x, i)$ 的输出，相应的输入用 $U_{xi}$ 表示。如果城市 x 在 i 位置上被访问，则 $V_{xi} = 1$ ，否则 $V_{xi} = 0$ 。

针对 TSP 问题, Hopfield 定义了如下形式的能量函数 $^{[16]}$

$$
\begin{array}{l} E = \frac {A}{2} \sum_ {x = 1} ^ {N} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} V _ {x i} V _ {x j} + \frac {B}{2} \sum_ {i = 1} ^ {N} \sum_ {x = 1} ^ {N} \sum_ {y = x} ^ {N} V _ {x i} V _ {y i} + \\ \frac {C}{2} \left(\sum_ {x = 1} ^ {N} \sum_ {i = 1} ^ {N} V _ {x i} - N\right) ^ {2} + \frac {D}{2} \sum_ {x = 1} ^ {N} \sum_ {y = 1} ^ {N} \sum_ {i = 1} ^ {N} d _ {x y} V _ {x i} \left(V _ {y, i + 1} + V _ {y, i - 1}\right) \tag {8.21} \\ \end{array}
$$

式中，A, B, C, D 是权值， $d_{xy}$ 表示城市 x 到城市 y 之间的距离。

式(8.21)中，E 的前三项是问题的约束项，最后一项是优化目标项。E 的第一项保证矩阵 V 的每一行不多于一个 1 时 E 最小（即每个城市只去一次），E 的第二项保证矩阵 V 的每一列不多于一个 1 时 E 最小（即每次只访问一城市），E 的第三项保证矩阵 V 中 1 的个数恰好为 N 时 E 最小。

Hopfield 将能量函数的概念引入神经网络,开创了求解优化问题的新方法。但该方法在求解上存在局部极小、不稳定等问题。为此,文献[17]将 TSP 的能量函数定义为

$$E = \frac {A}{2} \sum_ {x = 1} ^ {N} \left(\sum_ {i = 1} ^ {N} V _ {x i} - 1\right) ^ {2} + \frac {A}{2} \sum_ {i = 1} ^ {N} \left(\sum_ {x = 1} ^ {N} V _ {x i} - 1\right) ^ {2} + \frac {D}{2} \sum_ {x = 1} ^ {N} \sum_ {y = 1} ^ {N} \sum_ {i = 1} ^ {N} V _ {x i} d _ {x y} V _ {y, i + 1} \tag {8.22}$$

针对 TSP 问题的 Hopfield 网络设计中, 由于 W 和 I 为固定值, 与时间无关, 则 $\Delta = 0$ , 可保证式 (8.20) 中的 $\frac{dE_{N}}{dt} \leqslant 0$ , 实现 $E_{N}$ 极小。由 Hopfield 网络原理 (式 (8.16) 和式 (8.18)) 可知, Hopfield 网络的动态方程存在如下关系

$$\frac {\mathrm{d} U _ {x i}}{\mathrm{d} t} = - \frac {\partial E _ {N}}{\partial V _ {x i}} (x, i = 1, 2, \dots , N - 1)= \sum_ {j = 1} ^ {n} \omega_ {i j} v _ {j} + I _ {i} (\text {取} C _ {i} = 1, R _ {i} \rightarrow \infty)$$

按上式求出 $U_{xi}$ ，便可实现 $E_{N}$ 极小。

按 E 设计能量函数 $E_{N}^{[16]}$ ，即取 E 为 $E_{N}$ ，则
