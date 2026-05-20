# 3.4.2 模糊矩阵的运算与模糊关系

设有 n 阶模糊矩阵 A 和 $\boldsymbol{B}, \boldsymbol{A} = (a_{ij}), \boldsymbol{B} = (b_{ij})$ ，且 $i, j = 1, 2, \cdots, n$ ，则定义如下几种模糊矩阵的运算方式。

(1) 相等

若 $a_{ij} = b_{ij}$ ，则 A = B。

(2) 包含

若 $a_{ij} \leqslant b_{ij}$ , 则 $\mathbf{A} \subseteq \mathbf{B}$ 。

(3) 并运算

若 $c_{ij} = a_{ij} \vee b_{ij}$ ，则 $C = (c_{ij})$ 为 A 和 B 的并，记为 $C = A \cup B$ 。

(4) 交运算

若 $c_{ij}=a_{ij}\wedge b_{ij}$ ，则 $\boldsymbol{C}=(c_{ij})$ 为 A 和 B 的交，记为 $C=A\cap B$ 。

(5) 补运算

若 $c_{ij}=1-a_{ij}$ ，则 $\boldsymbol{C}=(c_{ij})$ 为 A 的补，记为 $C=\overline{A}$ 。

【例3.7】设 $\mathbf{A} = \begin{bmatrix} 0.7 & 0.1 \\ 0.3 & 0.9 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 0.4 & 0.9 \\ 0.2 & 0.1 \end{bmatrix}$ ，则

$$
\boldsymbol {A} \cup \boldsymbol {B} = \left[ \begin{array}{l l l} 0. 7 \vee 0. 4 & 0. 1 \vee 0. 9 \\ 0. 3 \vee 0. 2 & 0. 9 \vee 0. 1 \end{array} \right] = \left[ \begin{array}{l l} 0. 7 & 0. 9 \\ 0. 3 & 0. 9 \end{array} \right]

\mathbf {A} \cap \mathbf {B} = \left[ \begin{array}{l l l l l} 0. 7 & 0. 4 & 0. 1 & 0. 9 \\ 0. 3 & 0. 2 & 0. 9 & 0. 1 \end{array} \right] = \left[ \begin{array}{l l} 0. 4 & 0. 1 \\ 0. 2 & 0. 1 \end{array} \right]

\overline {{{\boldsymbol {A}}}} = \left[ \begin{array}{l l} 1 - 0. 7 & 1 - 0. 1 \\ 1 - 0. 3 & 1 - 0. 9 \end{array} \right] = \left[ \begin{array}{l l} 0. 3 & 0. 9 \\ 0. 7 & 0. 1 \end{array} \right]
$$

模糊关系的定义为: 设 X, Y 是两个非空集合, 则 $X \times Y$ 的一个模糊子集称为 X 到 Y 的一个模糊关系。
