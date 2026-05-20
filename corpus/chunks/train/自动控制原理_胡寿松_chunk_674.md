由于选取非奇异变换阵 $P^{-1}$ 的列向量 $s_{1}, s_{2}, \cdots, s_{r}$ 及 $s_{r+1}, \cdots, s_{n}$ 的非唯一性，虽然系统可控性规范分解的形式不变，但诸系数阵不相同，故可控性规范分解不是唯一的。

④ 不可控系统的可控性规范分解将整个系统的特征值分解为可控因子与不可控因子两类。

由于

$$\det (s \boldsymbol {I} - \bar {\boldsymbol {A}}) = \det (s \boldsymbol {I} - \bar {\boldsymbol {A}} _ {1 1}) \cdot \det (s \boldsymbol {I} - \bar {\boldsymbol {A}} _ {2 2}) \tag {9-200}$$

故 $x_{c}$ 的稳定性完全由 $\overline{A}_{11}$ 的特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{r}$ 决定； $x_{c}$ 的稳定性完全由 $\overline{A}_{22}$ 的特征值 $\lambda_{r+1}, \cdots, \lambda_{n}$ 决定，而 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 都是 A 的特征值。 $\lambda_{1}, \cdots, \lambda_{r}$ 称为系统 (A, B, C) 的可控因子或可控振型， $\lambda_{r+1}, \cdots, \lambda_{n}$ 称为不可控因子或不可控振型。

例 9-19 已知系统 $(A,b,c)$ ，其中

$$
\mathbf {A} = \left[ \begin{array}{c c c} 1 & 2 & - 1 \\ 0 & 1 & 0 \\ 1 & - 4 & 3 \end{array} \right], \quad \mathbf {b} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {c} = \left[ \begin{array}{c c c} 1 & - 1 & 1 \end{array} \right]
$$

试按可控性分解为规范形式。

解 系统可控性矩阵为

$$
\boldsymbol {S} = \left[ \begin{array}{l l l} \boldsymbol {b} & \boldsymbol {A b} & \boldsymbol {A ^ {2}} \boldsymbol {b} \end{array} \right] = \left[ \begin{array}{c c c} 0 & - 1 & - 4 \\ 0 & 0 & 0 \\ 1 & 3 & 8 \end{array} \right]
\operatorname{rank} \mathbf {S} = 2 < n = 3
$$

故系统不可控。从可控性矩阵中选出两个线性无关的列向量 $[0\quad 0\quad 1]^{\mathrm{T}}$ 和 $[-1\quad 0\quad 3]^{\mathrm{T}}$ ，附加

任意列向量 $[0\quad 1\quad 0]^{\mathrm{T}}$ ，构成非奇异变换阵 $P^{-1}$

$$
\boldsymbol {P} ^ {- 1} = \left[ \begin{array}{c c c} 0 & - 1 & 0 \\ 0 & 0 & 1 \\ 1 & 3 & 0 \end{array} \right]
$$

计算矩阵 $\pmb{P}$ 和变换后的各矩阵

$$
\boldsymbol {P} = (\boldsymbol {P} ^ {- 1}) ^ {- 1} = \left[ \begin{array}{c c c} 3 & 0 & 1 \\ - 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right]

\boldsymbol {P} \boldsymbol {A} \boldsymbol {P} ^ {- 1} = \left[ \begin{array}{c c c} 0 & - 4 & 2 \\ 1 & 4 & - 2 \\ \hdashline 0 & 0 & 1 \end{array} \right], \quad \boldsymbol {P} \boldsymbol {b} = \left[ \begin{array}{c} 1 \\ 0 \\ \hdashline 0 \end{array} \right], \quad \boldsymbol {c} \boldsymbol {P} ^ {- 1} = \left[ \begin{array}{l l l} 1 & 2 & - 1 \end{array} \right]
$$

可控子系统动态方程为

$$
\dot {\boldsymbol {x}} _ {c} = \left[ \begin{array}{l l} 0 & - 4 \\ 1 & 4 \end{array} \right] \boldsymbol {x} _ {c} + \left[ \begin{array}{l} 2 \\ - 2 \end{array} \right] \boldsymbol {x} _ {c} + \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \boldsymbol {u}, \quad y _ {1} = [ 1, 2 ] \boldsymbol {x} _ {c}
$$

不可控子系统动态方程为
