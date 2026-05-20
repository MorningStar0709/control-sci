为 $n \times np$ 矩阵，由子列向量 $u(0), u(1), \cdots, u(n-1)$ 构成的控制列向量是 np 维的。式 (9-147) 含 n 个方程，但有 np 个待求的控制量。由于初态 $x(0)$ 可任意给定，根据解存在定理，矩阵 $S_{2}^{\prime}$ 的秩为 n 时，方程组才有解。于是多输入线性离散系统状态可控的充分必要条件是

$$\operatorname{rank} \mathbf {S} _ {2} ^ {\prime} = n \tag {9-149}$$

或 $\mathrm{rank}S_2' = \mathrm{rank}[G^n S_2'] = \mathrm{rank}[G^{n-1}H\cdots GH H] = n$ (9-150)

或 $\mathrm{rank}S_{2} = \mathrm{rank}[H\quad GH\quad \dots \quad G^{n - 1}H] = n$ (9-151)

式(9-149)～式(9-151)都是多输入线性离散系统的可控性判据，通常使用式(9-151)较为方便。应当指出：

1) 由于式(9-147)中方程个数少于未知量个数, 方程组的解便不唯一, 任意假定 $np - n$ 个控制量, 其余 $n$ 个控制量才能唯一确定。多输入线性离散系统控制序列的选择, 通常具有无穷多种方式。  
2) 由于 $S_{2}$ 的行数总小于列数，因而在列写 $S_{2}$ 时，只要所选取的列能判断出 $S_{2}$ 的秩为 $n$ ，便不必再将 $S_{2}$ 的其余列都列写出来。  
3）多输入线性定常离散系统由任意初态转移至原点一般可少于 $n$ 个采样周期。

例 9-17 设单输入线性定常离散系统状态方程为

$$
\boldsymbol {x} (k + 1) = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & - 2 \\ - 1 & 1 & 0 \end{array} \right] \boldsymbol {x} (k) + \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right] u (k)
$$

试判断其可控性；若初始状态 $x(0) = [2\quad 1\quad 0]^{\mathrm{T}}$ ，确定使 $\pmb {x}(3) = \pmb{0}$ 的控制序列 $u(0),u(1)$ $u(2)$ ；研究使 $\pmb {x}(2) = \pmb{0}$ 的可能性。

解 由题意知

$$
\boldsymbol {G} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 2 & - 2 \\ - 1 & 1 & 0 \end{array} \right], \quad \boldsymbol {h} = \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right]

\operatorname{rank} \mathbf {S} _ {1} = \operatorname{rank} [ \mathbf {h} \quad \mathbf {G h} \quad \mathbf {G} ^ {2} \mathbf {h} ] = \operatorname{rank} \left[ \begin{array}{c c c} 1 & 1 & 1 \\ 0 & - 2 & - 2 \\ 1 & - 1 & - 3 \end{array} \right] = 3 = n
$$

故系统可控。可按式(9-139)求出 $u(0), u(1), u(2)$ ，为了减少求逆阵的麻烦，现用递推法来求。令 $k = 0, 1, 2$ ，可得状态序列

$$
\boldsymbol {x} (1) = \boldsymbol {G x} (0) + \boldsymbol {h u} (0) = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 2 & - 2 \\ - 1 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} 2 \\ 1 \\ 0 \end{array} \right] + \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right] u (0) = \left[ \begin{array}{l} 2 \\ 2 \\ - 1 \end{array} \right] + \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right] u (0)

\boldsymbol {x} (2) = \boldsymbol {G x} (1) + \boldsymbol {h u} (1) = \left[ \begin{array}{l} 2 \\ 6 \\ 0 \end{array} \right] + \left[ \begin{array}{l} 1 \\ - 2 \\ - 1 \end{array} \right] u (0) + \left[ \begin{array}{l} 1 \\ 0 \\ 1 \end{array} \right] u (1)
