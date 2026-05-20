再据凯莱-哈密顿定理知， $A^{n}, A^{n+1}, \cdots$ 均可表为 I, A, $A^{2}, \cdots, A^{n-1}$ 的线性组合，由此可将上式进一步写成为：

$$\alpha^ {T} A ^ {i} B = 0, \quad i = 0, 1, 2, \dots \tag {3.26}$$

从而，可得到对任意 $t_1 > 0$ 有

$$\pm a ^ {T} \frac {A ^ {i} t ^ {i}}{i !} B = 0, \forall i \in [ 0, t _ {1} ], i = 0, 1, 2, \dots \tag {3.27}$$

或

$$
\begin{array}{l} 0 = a ^ {T} \left[ I - A t + \frac {1}{2 !} A ^ {2} t ^ {2} - \frac {1}{3 !} A ^ {3} t ^ {3} + \dots \right] B \\ = \alpha^ {T} e ^ {- A t} B, \quad \forall t \in [ 0, t _ {1} ] \tag {3.28} \\ \end{array}
$$

利用(3.28)，即有

$$0 = \alpha^ {T} \int_ {0} ^ {t _ {1}} e ^ {- A t} B B ^ {T} e ^ {- A ^ {T} t} d t \alpha = \alpha^ {T} W [ 0, t _ {1} ] \alpha \tag {3.29}$$

表明格拉姆矩阵 $W[0, t_1]$ 为奇异，即系统为不完全能控。这是和已知条件相矛盾的，所以反设不能成立。于是，有 $\operatorname{rank} Q_e = n$ ，必要性得证。至此，证明完成。

例 1 考虑上节中给出的例 1, 其状态方程为:

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 4 & 0 \\ 0 & - 5 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] u, n = 2
$$

通过计算可得

$$
Q _ {t} = [ B: A B ] = \left[ \begin{array}{c c} 1 & 4 \\ 2 & - 1 0 \end{array} \right]
$$

容易断定， $\operatorname{rank}Q_{c}=2$ 。因此，系统为完全能控。

例2 考虑上节中给出的例3即图 $3.2(a)$ 所示的电路，不难导出其状态方程为：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - \frac {1}{R C} & 0 \\ 0 & - \frac {1}{R C} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} \frac {1}{R C} \\ \frac {1}{R C} \end{array} \right] u, n = 2
$$

其中 $R$ 和 $C$ 可为任意值。于是，通过计算可得

$$
Q _ {e} = [ B \mid A B ] = \left[ \begin{array}{l l} \frac {1}{R C} & - \frac {1}{(R C) ^ {2}} \\ \frac {1}{R C} & - \frac {1}{(R C) ^ {2}} \end{array} \right]
$$

显见 $\operatorname{rank} Q_{\epsilon} = 1 < 2$ ，因此系统为不完全能控。

例3 给定线性定常系统的状态方程为:

$$
\dot {x} = \left[ \begin{array}{c c c} - 1 & - 4 & - 2 \\ 0 & 6 & - 1 \\ 1 & 7 & - 1 \end{array} \right] x + \left[ \begin{array}{l} 2 \\ 0 \\ 1 \end{array} \right] u, n = 3
$$

通过计算可得

$$
Q _ {e} = [ B \mid A B \mid A ^ {2} B ] = \left[ \begin{array}{c c c} 2 & - 4 & 6 \\ 0 & - 1 & - 7 \\ 1 & 1 & - 1 2 \end{array} \right]
$$

由于 $\operatorname{det} Q_{\epsilon} \neq 0$ ，表明 $\operatorname{rank} Q_{\epsilon} = 3$ 。因此，可知系统为完全能控。

结论 3 [PBH 秩判据 $^{1)}$ ] 线性定常系统 (3.7) 为完全能控的充分必要条件是, 对矩阵 A 的所有特征值 $\lambda_{i}(i=1,2,\cdots,n)$ ，均成立

$$\operatorname{rank} \left[ \lambda_ {i} I - A, B \right] = n, i = 1, 2, \dots , n \tag {3.30}$$

或等价地表为

$$\operatorname{rank} [ s I - A, B ] = n, \forall s \in \mathcal {C} \tag {3.31}$$

也即 $(sI-A)$ 和B是左互质的。

证 必要性：系统完全能控，欲证（3.30）成立。
