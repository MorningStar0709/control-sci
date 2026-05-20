# 习题 11.7

11.7.1 用状态反馈把以下系统变成一致稳定的：

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c} 2 & 0 & \cdot & \cdot \\ \cdot & 1 & \cdot & \cdot \\ \cdot & 0 & 3 & 0 \\ \cdot & \cdot & \cdot & 3 \end{array} \right], \quad \boldsymbol {B} = [ 0 \cdot \cdot \cdot ].
$$

11.7.2 已知系统

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 3 & \cdot \\ 0 & 4 \end{array} \right], \quad \boldsymbol {B} = [ 5 0 ], \quad \boldsymbol {C} = \left[ \begin{array}{l} 0 \\ 5 \end{array} \right].
$$

证明 $G(k)=BA^{k-1}C=5+4(k-1), k=1,2,\cdots$ 于是 $(A,B,C)$ 是 $\{G(k)\}_{k=1}^{\infty}$ 的一个实现。进而证明这个实现是结构能达能观测的，但不是最小实现。

11.7.3 设式 (11.7.3) 中各阵如下:

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 2 & \cdot \\ 0 & 6 \end{array} \right], \quad \boldsymbol {B} = [ 0 \cdot ], \quad \boldsymbol {C} = \left[ \begin{array}{l} 0 \\ \cdot \end{array} \right], \boldsymbol {S} = [ \cdot 0 ].
$$

试问如何取状态反馈 K，使得系统 DDP 能解，且 $A \oplus KB$ 为 d 阶 $\lambda$ 周期阵.
