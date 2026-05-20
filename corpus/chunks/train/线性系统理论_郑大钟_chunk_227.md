(2) 通常, 如何确定函数观测器的维数 $m$ , 是一个比较复杂的问题。但是, 如果所设计的是一个 $Kx$ 的函数观测器, 其中 $K$ 为 $1 \times n$ 维常向量; 那么可取 $m = \nu - 1$ , 这里 $\nu$ 是 $\{A, C\}$ 的能观测性指数。当系统输出维数 $q$ 比较大时, 一般 $\nu - 1$ 远比 $n - q$ 要小得多, 也即函数观测器的维数可比降维状态观测器的维数要小得多。

这一点可这样地来证明：令 $\operatorname{rank} C = q$ ，并且引入非奇异阵 $P^T = [C^T, R^T]$ ，其中 $R$ 为任取的满足要求的 $(n - q) \times n$ 常阵，便可由通过变换 $\bar{x} = Px$ 而将(5.347)化成为：

$$
\left[ \begin{array}{l} \dot {\bar {x}} _ {1} \\ \dot {\bar {x}} _ {2} \end{array} \right] = \left[ \begin{array}{l l} \overline {{A}} _ {1 1} & \overline {{A}} _ {1 2} \\ \overline {{A}} _ {2 1} & \overline {{A}} _ {2 2} \end{array} \right] \left[ \begin{array}{l} \bar {x} _ {1} \\ \bar {x} _ {2} \end{array} \right] + \left[ \begin{array}{l} \overline {{B}} _ {1} \\ \overline {{B}} _ {2} \end{array} \right] u \triangleq \overline {{A}} \bar {x} + \bar {B} u \tag {5.354}

\mathbf {y} = \left[ I _ {q} \quad 0 \right] \left[ \begin{array}{l} \bar {x} _ {1} \\ \bar {x} _ {2} \end{array} \right] \triangleq \bar {C} \bar {x}
$$

目标是要使函数观测器（5.348）的标量输出 $w(t)$ 渐近地趋于 $Kx = KP^{-1}\bar{x} = \bar{K}\bar{x}$ ，其中 $\bar{K} = KP^{-1}$ 。进而，表 $T = [T_1, T_2]$ ，其中 $T_1$ 和 $T_2$ 分别为 $m \times q$ 和 $m \times (n - q)$ 矩阵。由此，并注意到 $\vec{C} = [I_q, 0]$ ，可把 $T\vec{A} - FT = G\vec{C}$ 表示为：

$$T _ {1} \overline {{{A}}} _ {1 1} + T _ {2} \overline {{{A}}} _ {2 1} - F T _ {1} = G \tag {5.355}T _ {1} \bar {A} _ {1 2} + T _ {2} \bar {A} _ {2 2} - F T _ {2} = 0 \tag {5.356}$$

再表 $\bar{K} = [\bar{K}_1, \bar{K}_2]$ ，其中 $\bar{K}_1$ 和 $\bar{K}_2$ 分别为 $1 \times q$ 和 $1 \times (n - q)$ 的向量，那么可把 $MT + N\bar{C} = \bar{K}$ 表示为：

$$M T _ {1} + N = \bar {K} _ {1} \tag {5.357}M T _ {2} = \bar {K} _ {2} \tag {5.358}$$

现将 $\pmb{F}$ 和 $M$ 取为

$$
F = \left[ \begin{array}{c c} 0 & \\ \vdots & I _ {m - 1} \\ 0 & \\ \hline - \alpha_ {0} & - \alpha_ {1} \dots - \alpha_ {m - 1} \end{array} \right] \tag {5.359}
M = [ 1 \quad 0 \dots 0 ] \tag {5.360}
$$

显然， $\{F,M\}$ 为能观，而 $\{a_{i},i=0,1,\cdots,m-1\}$ 可任意配置。同时，令

$$
T _ {1} = \left[ \begin{array}{c} t _ {1 1} \\ t _ {1 2} \\ \vdots \\ t _ {1 m} \end{array} \right], \quad T _ {2} = \left[ \begin{array}{c} t _ {2 1} \\ t _ {2 2} \\ \vdots \\ t _ {2 m} \end{array} \right] \tag {5.361}
$$

于是，由 $F$ 和 $M$ 的形式，可根据(5.358)和(5.356)进一步导出：
