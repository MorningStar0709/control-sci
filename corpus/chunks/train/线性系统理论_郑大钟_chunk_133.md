$$
\overline {{{B}}} = P B = \left[ \begin{array}{c} p _ {1} ^ {T} B \\ \vdots \\ p _ {k} ^ {T} B \\ - \frac {}{p _ {k + 1} ^ {T} B} \\ \vdots \\ p _ {n} ^ {T} B \end{array} \right] = \left[ \begin{array}{l} \overline {{{B}}} _ {s} \\ 0 \end{array} \right] \tag {3.244}
$$

而 $\overline{C}$ 无特殊形式，为

$$\bar {C} = C P ^ {- 1} = \left[ C q _ {1}, \dots , C q _ {k} \mid C q _ {k + 1}, \dots , C q _ {n} \right]= \left[ \bar {C} _ {e}, \bar {C} _ {z} \right] \tag {3.245}$$

这样，就证明了规范表达式(3.239)。再之，有

$$
\begin{array}{l} k = \operatorname{rank} Q _ {o} = \operatorname{rank} \bar {Q} _ {o} = \operatorname{rank} [ \bar {B} | \bar {A} \bar {B} | \dots | \bar {A} ^ {* + 1} \bar {B} ] \\ = \operatorname{rank} \left[ \begin{array}{c c c c} \bar {B} _ {\epsilon} & \bar {A} _ {\epsilon} \bar {B} _ {\epsilon} & \dots & \bar {A} _ {\epsilon} ^ {* - 1} \bar {B} _ {\epsilon} \\ 0 & 0 & & 0 \end{array} \right] \\ \end{array}
= \operatorname{rank} \left[ \bar {B} _ {\bullet} \mid \bar {A} _ {c} \bar {B} _ {\bullet} \mid \dots \mid \bar {A} _ {c} ^ {n - 1} \bar {B} _ {\bullet} \right] \tag {3.246}
$$

而由凯莱-哈密顿定理又知，因 $\overline{A}_{c}$ 为 $k \times k$ 矩阵，故 $\overline{A}_{c}^{k}\overline{B}_{c}, \cdots, \overline{A}_{c}^{n-1}\overline{B}_{c}$ 均可表为 $\{\overline{B}_{c}, \overline{A}_{c}\overline{B}_{c}, \cdots, \overline{A}_{c}^{k-1}\overline{B}_{c}\}$ 的线性组合，从而由 (3.246) 可进而导出

$$\operatorname{rank} \left[ \bar {B} _ {c} \mid \bar {A} _ {c} \bar {B} _ {c} \mid \dots \mid \bar {A} _ {c} ^ {k - 1} \bar {B} _ {c} \right] = k \tag {3.247}$$

这表明 $(\overline{A}_c, \overline{B}_c)$ 为能控，即 $\overline{x}_c$ 为能控分状态。至此，就完成了证明。

例 给定线性定常系统

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \\ 0 & 1 \end{array} \right] \boldsymbol {u}
y = [ 1 \quad 0 \quad 1 ] x
$$

已知 $n = 3$ , $\operatorname{rank} B = 2$ , 故只需判断 $[B \mid AB]$ 是否为行满秩。现知

$$
\operatorname{rank} [ B \vdots A B ] = \operatorname{rank} \left[ \begin{array}{l l l l} 0 & 1 & 1 & 2 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 2 \end{array} \right] = 2 <   n = 3
$$

表明系统为不完全能控。进而，在 $Q_{\bullet}$ 中取线性无关的列 $\pmb{q}_{1} = [010]^{T}$ 和 $\pmb{q}_{2} = [101]^{T}$ ，再任取 $\pmb{q}_{3} = [100]^{T}$ ，使构成的矩阵

$$
P ^ {- 1} = Q = \left[ \begin{array}{c c c c} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right]
$$

为非奇异。而通过求逆，可定出

$$
P = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & - 1 \end{array} \right]
$$

于是，即可算得
