$$
\left[ \begin{array}{c c} I & 0 \\ K & I \end{array} \right]
$$

可得 $V^{\mathrm{T}}(-s)V(s)$ 的另一个最小实现

$$
\begin{array}{l} \{\mathcal {A} _ {2}, \mathcal {B} _ {2}, \mathcal {C} _ {2}, \mathcal {D} _ {2} \} = \\ \left\{\left[ \begin{array}{c c} F & 0 \\ 0 & - F ^ {\mathrm{T}} \end{array} \right], \left[ \begin{array}{c} G \\ K G + H ^ {\mathrm{T}} J \end{array} \right], \left[ \begin{array}{c c} J ^ {\mathrm{T}} H + G ^ {\mathrm{T}} K & - G ^ {\mathrm{T}} \end{array} \right], J ^ {\mathrm{T}} J \right\} \\ \end{array}
$$

又由于 $\{-A^{\mathrm{T}},C^{\mathrm{T}}, - B^{\mathrm{T}},D^{\mathrm{T}}\}$ 是 $U^{\mathrm{T}}(-s)$ 的最小实现，因此

$$
\left\{\mathcal {A} _ {3}, \mathcal {B} _ {3}, \mathcal {C} _ {3}, \mathcal {D} _ {3} \right\} = \left\{\left[ \begin{array}{c c} A & 0 \\ 0 & - A ^ {\mathrm{T}} \end{array} \right], \left[ \begin{array}{l} B \\ C ^ {\mathrm{T}} \end{array} \right], \left[ \begin{array}{c c} C & - B ^ {\mathrm{T}} \end{array} \right], D + D ^ {\mathrm{T}} \right\}
$$

是并联连接 $U(s) + U^{\mathrm{T}}(-s)$ 的一个实现。由于 $A$ 的特征值都在左半开平面，而 $-A^{\mathrm{T}}$ 的特征值在右半开平面，容易看出这是最小实现。这样，根据方程(C.39)可知 $\{\mathcal{A}_2,\mathcal{B}_2,\mathcal{C}_2,\mathcal{D}_2\}$ 和 $\{\mathcal{A}_3,\mathcal{B}_3,\mathcal{C}_3,\mathcal{D}_3\}$ 是同一传递函数等价的最小实现。因此，它们具有相同的维数，且存在一个非奇异矩阵 $T$ ，满足①

$$\mathcal {A} _ {2} = T \mathcal {A} _ {3} T ^ {- 1}, \mathcal {B} _ {2} = T \mathcal {B} _ {3}, \mathcal {C} _ {2} = \mathcal {C} _ {3} T ^ {- 1}, J ^ {\mathrm{T}} J = \mathcal {D} + \mathcal {D} ^ {\mathrm{T}}$$

矩阵 T 必须是一个分块对角矩阵,为了理解这一点,将 T 划分为

$$
T = \left[ \begin{array}{l l} T _ {1 1} & T _ {1 2} \\ T _ {2 1} & T _ {2 2} \end{array} \right]
$$

则矩阵 $T_{12}$ 满足方程

$$F T _ {1 2} + T _ {1 2} A ^ {\mathrm{T}} = 0$$

上式两边左乘 $\exp (Ft)$ ，右乘 $\exp (A^{\mathrm{T}}t)$ ，得到

$$0 = \exp (F t) [ F T _ {1 2} + T _ {1 2} A ^ {\mathrm{T}} ] \exp (A ^ {\mathrm{T}} t) = \frac {d}{d t} [ \exp (F t) T _ {1 2} \exp (A ^ {\mathrm{T}} t) ]$$

因此对于所有 $t \geqslant 0, \exp(Ft) T_{12} \exp(A^{\mathrm{T}} t)$ 是常数。特别地，由于 $\exp(0) = I$ ，当 $t$ 趋于无穷时，有

$$T _ {1 2} = \exp (F t) T _ {1 2} \exp (A ^ {\mathrm{T}} t) \rightarrow 0$$

因此 $T_{12}=0$ 。同样可以证明 $T_{21}=0$ 。由此可得矩阵 $T_{11}$ 是非奇异的，且

$$F = T _ {1 1} A T _ {1 1} ^ {- 1}, G = T _ {1 1} B, J ^ {\mathrm{T}} H + G ^ {\mathrm{T}} K = C T _ {1 1} ^ {- 1}$$

定义

$$P = T _ {1 1} ^ {\mathrm{T}} K T _ {1 1}, L = H T _ {1 1}, W = J$$

容易验证 P, L 和 W 满足方程

$$P A + A ^ {\mathrm{T}} P = - L ^ {\mathrm{T}} L, \quad P B = C ^ {\mathrm{T}} - L ^ {\mathrm{T}} W, \quad W ^ {\mathrm{T}} W = D + D ^ {\mathrm{T}}$$
