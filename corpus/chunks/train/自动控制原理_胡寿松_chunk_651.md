# (1) 线性离散系统的可控性和可达性

设线性时变离散时间系统的状态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G} (k) \boldsymbol {x} (k) + \boldsymbol {H} (k) \boldsymbol {u} (k), \quad k \in T _ {k} \tag {9-135}$$

其中 $T_{k}$ 为离散时间定义区间。如果对初始时刻 $l \in T_{k}$ 和状态空间中的所有非零状态 $\pmb{x}(l)$ ，都存在时刻 $m \in T_{k}, m > l$ ，和对应的控制 $\pmb{u}(k)$ ，使得 $\pmb{x}(m) = \mathbf{0}$ ，则称系统在时刻 $l$ 为完全可控。对应地，如果对初始时刻 $l \in T_{k}$ 和初始状态 $\pmb{x}(l) = \mathbf{0}$ ，存在时刻 $m \in T_{k}, m > l$ ，和相应的控制 $\pmb{u}(k)$ ，使 $\pmb{x}(m)$ 可为状态空间中的任意非零点，则称系统在时刻 $l$ 为完全可达。

对于离散时间系统,不管是时变的还是定常的,其可控性和可达性只有在一定条件下才是等价的。业已证明,其等价的条件分别为

1) 线性离散时间系统(9-135)的可控性和可达性为等价的充分必要条件是, 系统矩阵 $\mathbf{G}(k)$ 对所有 $k \in [l, m-1]$ 为非奇异。

2) 线性定常离散时间系统

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {H u} (k); \quad k = 0, 1, 2, \dots \tag {9-136}$$

的可控性和可达性等价的充分必要条件是系统矩阵 G 为非奇异。

3）如果线性离散时间系统(9-135)或(9-136)是相应连续时间系统的时间离散化模型，则其可控性和可达性必是等价的。

线性定常离散系统的可控性判据 设单输入线性定常离散系统的状态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {h u} (k) \tag {9-137}$$

式中，x 为 n 维状态向量；u 为标量输入；G 为 $n \times n$ 非奇异矩阵。状态方程(9-137)的解为

$$\boldsymbol {x} (k) = \boldsymbol {G} ^ {k} \boldsymbol {x} (0) + \sum_ {i = 0} ^ {k - 1} \boldsymbol {G} ^ {k - 1 - i} \boldsymbol {h u} (i) \tag {9-138}$$

根据可控性定义, 假定 k = n 时, $x(n) = 0$ , 将式(9-138)两端左乘 $G^{-n}$ , 则有

$$
\begin{array}{l} \boldsymbol {x} (0) = - \sum_ {i = 0} ^ {n - 1} \boldsymbol {G} ^ {- 1 - i} \boldsymbol {h u} (i) \\ = - \left[ G ^ {- 1} h u (0) + G ^ {- 2} h u (1) + \dots + G ^ {- n} h u (n - 1) \right] \\ = - \left[ \begin{array}{l l l l} \mathbf {G} ^ {- 1} \mathbf {h} & \mathbf {G} ^ {- 2} \mathbf {h} & \dots & \mathbf {G} ^ {- n} \mathbf {h} \end{array} \right] \left[ \begin{array}{c} u (0) \\ u (1) \\ \vdots \\ u (n - 1) \end{array} \right] \tag {9-139} \\ \end{array}
$$

记 $S_{1}^{\prime}=\left[G^{-1}h\quad G^{-2}h\quad\cdots\quad G^{-n}h\right]$ (9-140)

称 $S_{1}^{\prime}$ 为 $n\times n$ 可控性矩阵。式(9-139)是一个非奇异线性方程组，含n个方程，有n个未知数 $u(0)$ ， $u(1),\cdots,u(n-1)$ 。由线性方程组解的存在定理可知，当矩阵 $S_{1}^{\prime}$ 的秩与增广矩阵 $[S_{1}^{\prime}:x(0)]$ 的秩相等时，方程组有解且为唯一解，否则无解。在 $x(0)$ 为任意的情况下，使方程组有解的充分必要条件是矩阵 $S_{1}^{\prime}$ 满秩，即

$$\operatorname{rank} \mathbf {S} _ {1} ^ {\prime} = n \tag {9-141}$$

或矩阵 $S_{1}^{\prime}$ 的行列式不为零

$$\det \mathbf {S} _ {1} ^ {\prime} \neq 0 \tag {9-142}$$

或矩阵 $S_{1}^{\prime}$ 是非奇异的。

由于满秩矩阵与另一满秩矩阵 $G^{n}$ 相乘其秩不变，故
