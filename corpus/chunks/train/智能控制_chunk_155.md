$$
\begin{array}{l} (\mathbf {A} \times \mathbf {B}) ^ {\mathrm{T1}} = [ 0. 1 \quad 0. 5 \quad 0. 5 \quad 0. 1 \quad 1. 0 \quad 0. 6 \quad 0. 1 \quad 0. 1 \quad 0. 1 ] ^ {\mathrm{T}} \\ \boldsymbol {R} = (\boldsymbol {A} \times \boldsymbol {B}) ^ {\mathrm{T1}} \circ \boldsymbol {C} = [ 0. 1 0. 5 0. 5 0. 1 1. 0 0. 6 0. 1 0. 1 0. 1 ] ^ {\mathrm{T}} 。 \\ [ 0. 4 \quad 1 ] = \left[ \begin{array}{l l l l l l l l l} 0. 1 & 0. 4 & 0. 4 & 0. 1 & 0. 4 & 0. 4 & 0. 1 & 0. 1 & 0. 1 \\ 0. 1 & 0. 5 & 0. 5 & 0. 1 & 1 & 0. 6 & 0. 1 & 0. 1 & 0. 1 \end{array} \right] ^ {\mathrm{T}} \\ \end{array}
$$

当输入为 $A_{1}$ 和 $B_{1}$ 时, 有

$$
\boldsymbol {A} _ {1} \times \boldsymbol {B} _ {1} = \boldsymbol {A} _ {1} ^ {\mathrm{T}} \wedge \boldsymbol {B} _ {1} = \left[ \begin{array}{l} 1 \\ 0. 5 \\ 0. 1 \end{array} \right] \wedge [ 0. 1 0. 5 1 ] = \left[ \begin{array}{l l l} 0. 1 & 0. 5 & 1 \\ 0. 1 & 0. 5 & 0. 5 \\ 0. 1 & 0. 1 & 0. 1 \end{array} \right]
$$

将 $A_{1} \times B_{1}$ 矩阵扩展成如下行向量

$$\left(\boldsymbol {A} _ {1} \times \boldsymbol {B} _ {1}\right) ^ {\mathrm{T2}} = \left[ 0. 1 \quad 0. 5 \quad 1 \quad 0. 1 \quad 0. 5 \quad 0. 5 \quad 0. 1 \quad 0. 1 \quad 0. 1 \right]$$

最后得 $C_{1}$ 为

$$
\begin{array}{l} \boldsymbol {C} _ {1} = \left(\boldsymbol {A} _ {1} \times \boldsymbol {B} _ {1}\right) ^ {\mathrm{T2}} \circ \boldsymbol {R} = \left[ 0. 1 \quad 0. 5 \quad 1 \quad 0. 1 \quad 0. 5 \quad 0. 5 \quad 0. 1 \quad 0. 1 \quad 0. 1 \right] 。 \\ \left[ \begin{array}{l l l l l l l l l} 0. 1 & 0. 4 & 0. 4 & 0. 1 & 0. 4 & 0. 4 & 0. 1 & 0. 1 & 0. 1 \\ 0. 1 & 0. 5 & 0. 5 & 0. 1 & 1 & 0. 6 & 0. 1 & 0. 1 & 0. 1 \end{array} \right] ^ {\mathrm{T}} = \left[ \begin{array}{l l} 0. 4 & 0. 5 \end{array} \right] \\ \end{array}
$$

即 $C_{1}=\frac{0.4}{c_{1}}+\frac{0.5}{c_{2}}$ 。

采用 Matlab 实现上述过程的仿真,模糊推理仿真程序见附录程序 chap3\_5.m。
